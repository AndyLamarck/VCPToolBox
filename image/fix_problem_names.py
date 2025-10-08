#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复问题图片名：
1. 以"的"开头的文件名
2. "表情包_数字"格式的文件名
使用 GLM-4.5V API 重新标注
"""

import os
import base64
import json
import re
from pathlib import Path
from typing import Optional, List
import requests
import time
from PIL import Image
import io

# GLM-4 API 配置
API_KEY = "7fa002791a5440e7a94d6d3d8bc07708.jTVy4NbLL9S7Mgav"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 目标文件夹
IMAGE_DIR = Path(r"D:\vcp\VCPToolBox-main\image\通用表情包")

def encode_image_to_base64(image_path: Path) -> Optional[str]:
    """将图片编码为 base64 字符串"""
    try:
        img = Image.open(image_path)

        # 如果是 GIF，提取第一帧
        if image_path.suffix.lower() == '.gif':
            img.seek(0)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

        # 转换为 JPEG 格式
        buffer = io.BytesIO()
        img.convert('RGB').save(buffer, format='JPEG', quality=95)
        image_data = buffer.getvalue()

        base64_str = base64.b64encode(image_data).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_str}"
    except Exception as e:
        print(f"❌ 编码图片失败: {e}")
        return None


def call_glm4_vision(image_base64: str) -> Optional[str]:
    """调用 GLM-4.5V API 识别图片"""
    prompt = """用5-8个字描述这张表情包。
要求：角色+动作+情绪，直接输出，不解释。
例如：猫咪摊手无奈、少女害羞捂脸"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "glm-4.5v",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_base64}}
                ]
            }
        ],
        "temperature": 0.5,
        "max_tokens": 200
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if 'choices' in result and len(result['choices']) > 0:
            message = result['choices'][0]['message']
            description = message.get('content', '').strip()
            description = description.replace('<|begin_of_box|>', '').replace('<|end_of_box|>', '').strip()

            # 如果 content 为空或包含思考过程，从 reasoning_content 提取
            if not description or len(description) > 50 or any(kw in description for kw in ['需要描述', '角色是', '动作是', '情绪是', '不过', '或者', '那这里', '再看', '检查', '符合', '这样', '比如', '可能', '示例']):
                reasoning = message.get('reasoning_content', '')
                if reasoning:
                    # 尝试提取引号中的内容
                    quotes = re.findall(r'["""]([^"""]{4,15})["""]', reasoning)
                    if quotes:
                        for q in reversed(quotes):
                            if not any(kw in q for kw in ['角色', '动作', '情绪', '不过', '或者', '可能', '应该', '这样', '比如']):
                                description = q
                                break
                        if not description or len(description) > 15:
                            description = quotes[-1]

                    # 如果还是没有合适的，尝试提取简洁短语
                    if not description or len(description) > 15:
                        lines = reasoning.split('\n')
                        for line in reversed(lines):
                            matches = re.findall(r'([^\s"""，。]{5,15})', line)
                            for match in reversed(matches):
                                if not any(kw in match for kw in ['角色', '动作', '情绪', '不过', '或者', '可能', '应该', '这样', '比如', '需要', '用户', '首先', '所以', '但', '再', '检查', '符合', '格式']):
                                    description = match
                                    break
                            if description and 5 <= len(description) <= 15:
                                break

            if description:
                # 最终清理
                description = re.sub(r'[？?。！!，,、；;：:"""'']', '', description).strip()
                # 再次检查长度，如果还是太长就截取
                if len(description) > 15:
                    description = description[:15]
                return description

        return None

    except Exception as e:
        print(f"❌ API 调用失败: {e}")
        return None


def get_problem_files(limit: int = 5) -> List[Path]:
    """获取需要处理的问题文件"""
    problem_files = []

    for file_path in sorted(IMAGE_DIR.glob("*.*")):
        if file_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
            continue

        filename = file_path.name
        # 检查是否是问题文件名
        if filename.startswith('的') or filename.startswith('表情包_'):
            problem_files.append(file_path)
            if len(problem_files) >= limit:
                break

    return problem_files


def sanitize_filename(text: str, max_length: int = 15) -> str:
    """清理文本，使其适合作为文件名"""
    text = re.sub(r'[<>:"/\\|?*\n\r\t]', '', text)
    text = re.sub(r'\s+', '_', text.strip())
    text = re.sub(r'[。,、;:!?《》【】()（）\[\]""''…—·]', '', text)
    if len(text) > max_length:
        text = text[:max_length]
    return text


def process_batch(batch_size: int = 5):
    """处理一批问题图片"""
    files = get_problem_files(limit=batch_size)

    if not files:
        print("✅ 没有需要处理的问题图片了！")
        return 0

    print(f"📸 找到 {len(files)} 张问题图片，开始处理...\n")

    success_count = 0

    for idx, file_path in enumerate(files, 1):
        print(f"[{idx}/{len(files)}] 📸 处理: {file_path.name}")

        # 编码图片
        image_base64 = encode_image_to_base64(file_path)
        if not image_base64:
            print("❌ 编码失败\n")
            continue

        # 调用 API
        description = call_glm4_vision(image_base64)
        if not description:
            print("❌ 识别失败\n")
            continue

        print(f"✨ 识别结果: {description}")

        # 生成新文件名
        clean_name = sanitize_filename(description)
        new_name = f"{clean_name}{file_path.suffix}"
        new_path = file_path.parent / new_name

        # 处理文件名冲突
        counter = 1
        while new_path.exists() and new_path != file_path:
            new_name = f"{clean_name}_{counter}{file_path.suffix}"
            new_path = file_path.parent / new_name
            counter += 1

        # 重命名
        try:
            file_path.rename(new_path)
            print(f"✅ 重命名成功: {new_name}\n")
            success_count += 1
        except Exception as e:
            print(f"❌ 重命名失败: {e}\n")

        # API 限频延迟
        time.sleep(0.5)

    print(f"📊 本批处理完成！成功 {success_count}/{len(files)}\n")
    return len(files)


if __name__ == "__main__":
    print("🔧 开始修复问题图片名称...\n")

    total_processed = 0
    batch_num = 1

    while True:
        print(f"========== 第 {batch_num} 批 ==========\n")
        processed = process_batch(batch_size=5)

        if processed == 0:
            break

        total_processed += processed
        batch_num += 1

        # 检查是否还有剩余
        remaining = get_problem_files(limit=1)
        if not remaining:
            break

        print(f"⏸️ 等待 2 秒后处理下一批...\n")
        time.sleep(2)

    print(f"🎉 全部完成！共处理 {total_processed} 张图片")
