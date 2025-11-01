#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
表情包自动打标和重命名工具
使用 GLM-4 Vision API 识别表情包内容并生成中文描述
"""

import os
import base64
import json
import re
from pathlib import Path
from typing import Optional
import requests
import time

# GLM-4 API 配置
API_KEY = "7fa002791a5440e7a94d6d3d8bc07708.jTVy4NbLL9S7Mgav"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 目标文件夹
IMAGE_DIR = Path(r"D:\vcp\VCPToolBox-main\image\通用表情包")

# 支持的图片格式
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}


def encode_image_to_base64(image_path: Path) -> Optional[str]:
    """将图片编码为 base64 字符串"""
    try:
        from PIL import Image
        import io

        # 打开图片
        img = Image.open(image_path)

        # 如果是 GIF，提取第一帧
        if image_path.suffix.lower() == '.gif':
            img.seek(0)  # 定位到第一帧
            # 转换为 RGB（去除透明通道）
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

        # 转换为 JPEG 格式（API 支持更好）
        buffer = io.BytesIO()
        img.convert('RGB').save(buffer, format='JPEG', quality=95)
        image_data = buffer.getvalue()

        base64_str = base64.b64encode(image_data).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_str}"
    except Exception as e:
        print(f"❌ 编码图片失败 {image_path.name}: {e}")
        return None


def call_glm4_vision(image_base64: str, prompt: str = None) -> Optional[str]:
    """调用 GLM-4 Vision API 识别图片内容"""
    if prompt is None:
        prompt = """描述这张表情包，要求：
- 5-15个字
- 格式：角色+动作+情绪
- 适合做文件名
- 直接输出，不解释

示例：猫咪摊手无奈、熊猫开心鼓掌"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "glm-4.5v",  # 使用 GLM-4.5V 多模态视觉模型
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_base64
                        }
                    }
                ]
            }
        ],
        "temperature": 0.5,  # 降低温度，让输出更稳定
        "max_tokens": 200    # 增加token限制，防止被截断
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if 'choices' in result and len(result['choices']) > 0:
            message = result['choices'][0]['message']
            import re

            # 优先从 content 获取
            description = message.get('content', '').strip()
            # 清理特殊标记
            description = description.replace('<|begin_of_box|>', '').replace('<|end_of_box|>', '').strip()

            # 如果 content 为空或包含思考过程，从 reasoning_content 提取
            if not description or len(description) > 50 or any(kw in description for kw in ['需要描述', '角色是', '动作是', '情绪是', '不过', '或者', '那这里', '再看', '再确认', '再调整', '检查', '符合', '这样', '比如', '可能', '示例']):
                reasoning = message.get('reasoning_content', '')
                if reasoning:
                    # 尝试提取引号中的内容
                    quotes = re.findall(r'["""]([^"""]{4,15})["""]', reasoning)
                    if quotes:
                        # 优先选择不包含分析性词汇的引号内容
                        for q in reversed(quotes):
                            if not any(kw in q for kw in ['角色', '动作', '情绪', '不过', '或者', '可能', '应该', '这样', '比如']):
                                description = q
                                break
                        if not description or len(description) > 15:
                            description = quotes[-1]

                    # 如果还是没有合适的，尝试提取简洁短语
                    if not description or len(description) > 15:
                        # 从 reasoning 中提取最后一个符合格式的短语
                        lines = reasoning.split('\n')
                        for line in reversed(lines):
                            # 查找符合"角色+动作+情绪"格式的短语（5-15字）
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
            else:
                print(f"⚠️ 无法从 API 返回中提取描述")
                return None
        else:
            print(f"⚠️ API 返回格式异常: {result}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ API 调用失败: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"HTTP 状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text}")
        return None
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        return None


def sanitize_filename(text: str, max_length: int = 50) -> str:
    """清理文本，使其适合作为文件名"""
    # 移除或替换不适合文件名的字符
    text = re.sub(r'[<>:"/\\|?*\n\r\t]', '', text)
    # 移除多余的空格
    text = re.sub(r'\s+', '_', text.strip())
    # 移除标点符号（保留中文）
    text = re.sub(r'[。,、;:!?《》【】()（）\[\]""''…—·]', '', text)
    # 限制长度
    if len(text) > max_length:
        text = text[:max_length]
    return text


def process_single_image(image_path: Path, dry_run: bool = False) -> bool:
    """处理单张图片：识别并重命名"""
    print(f"\n📸 处理: {image_path.name}")

    # 编码图片
    image_base64 = encode_image_to_base64(image_path)
    if not image_base64:
        return False

    # 调用 API 识别
    description = call_glm4_vision(image_base64)
    if not description:
        return False

    print(f"✨ 识别结果: {description}")

    # 生成新文件名
    clean_name = sanitize_filename(description)
    new_name = f"{clean_name}{image_path.suffix}"
    new_path = image_path.parent / new_name

    # 处理文件名冲突
    counter = 1
    while new_path.exists() and new_path != image_path:
        new_name = f"{clean_name}_{counter}{image_path.suffix}"
        new_path = image_path.parent / new_name
        counter += 1

    # 重命名
    if dry_run:
        print(f"🔍 [预览] {image_path.name} -> {new_name}")
    else:
        try:
            image_path.rename(new_path)
            print(f"✅ 重命名成功: {new_name}")
        except Exception as e:
            print(f"❌ 重命名失败: {e}")
            return False

    return True


def process_all_images(image_dir: Path, dry_run: bool = False, limit: int = None):
    """批量处理所有图片"""
    # 获取所有支持格式的图片
    image_files = []
    for ext in SUPPORTED_FORMATS:
        image_files.extend(image_dir.glob(f"*{ext}"))
        image_files.extend(image_dir.glob(f"*{ext.upper()}"))

    image_files = sorted(set(image_files))

    if limit:
        image_files = image_files[:limit]

    print(f"\n🎯 找到 {len(image_files)} 张图片")
    if dry_run:
        print("⚠️ 运行在预览模式，不会实际重命名文件\n")

    success_count = 0
    fail_count = 0

    for idx, image_path in enumerate(image_files, 1):
        try:
            print(f"\n[{idx}/{len(image_files)}] ", end="")
            if process_single_image(image_path, dry_run):
                success_count += 1
            else:
                fail_count += 1

            # API 调用限频，稍作延迟
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n\n⚠️ 用户中断操作")
            break
        except Exception as e:
            print(f"\n❌ 处理出错: {e}")
            fail_count += 1
            continue

    print(f"\n\n📊 处理完成！")
    print(f"✅ 成功: {success_count}")
    print(f"❌ 失败: {fail_count}")


def test_api():
    """测试 API 连接和图片识别功能"""
    print("🔧 测试 GLM-4 Vision API 连接...\n")

    # 找一张测试图片
    test_images = list(IMAGE_DIR.glob("*.jpg"))[:1]
    if not test_images:
        test_images = list(IMAGE_DIR.glob("*.png"))[:1]

    if not test_images:
        print("❌ 未找到测试图片")
        return False

    test_image = test_images[0]
    print(f"📸 使用测试图片: {test_image.name}\n")

    image_base64 = encode_image_to_base64(test_image)
    if not image_base64:
        return False

    description = call_glm4_vision(image_base64)
    if description:
        print(f"\n✅ API 测试成功！")
        print(f"✨ 识别结果: {description}")
        return True
    else:
        print(f"\n❌ API 测试失败")
        return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="表情包自动打标和重命名工具")
    parser.add_argument("--test", action="store_true", help="测试 API 连接")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际重命名")
    parser.add_argument("--limit", type=int, help="限制处理的图片数量")

    args = parser.parse_args()

    if args.test:
        test_api()
    else:
        process_all_images(IMAGE_DIR, dry_run=args.dry_run, limit=args.limit)
