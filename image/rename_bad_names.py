#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修正不合格的表情包文件名
将包含描述性词汇的文件名改为简洁的描述
"""

import os
import re
from pathlib import Path

# 目标文件夹
IMAGE_DIR = Path(r"D:\vcp\VCPToolBox-main\image\通用表情包")

# 需要修正的文件名映射表
RENAME_MAP = {
    # 包含"角色是"、"动作是"、"情绪是"等描述性词汇的
    r".*角色是.*动作是.*情绪.*": "根据内容重命名",
    r".*或者.*": "提取关键词",
    r".*那这里.*": "提取关键词",
    r".*再看.*": "提取关键词",
    r".*示例.*": "提取关键词",
    r".*检查.*": "提取关键词",
    r".*符合.*": "提取关键词",
    r".*最终.*": "提取关键词",
    r".*不过.*": "提取关键词",
    r".*可能.*": "提取关键词",
    r".*这样.*": "提取关键词",
    r".*比如.*": "提取关键词",
}

def extract_keywords(filename):
    """从复杂文件名中提取关键词"""
    # 移除扩展名
    name_without_ext = Path(filename).stem

    # 尝试从引号中提取
    quote_match = re.search(r'["""]([^"""]{4,15})["""]', name_without_ext)
    if quote_match:
        return quote_match.group(1)

    # 查找包含角色、动作、情绪的关键词
    # 提取"XX少女XX害羞"这样的模式
    pattern_match = re.search(r'([\u4e00-\u9fa5]{2,4}(?:少女|女孩|女生|角色|猫耳|兔耳|兽耳|猫娘)[\u4e00-\u9fa5]{2,6}(?:害羞|开心|无奈|惊讶|困惑|愤怒|悲伤|得意|委屈|疑惑))', name_without_ext)
    if pattern_match:
        return pattern_match.group(1)

    # 简单提取中文字符（5-15字）
    chinese_chars = re.findall(r'[\u4e00-\u9fa5]+', name_without_ext)
    for chars in chinese_chars:
        if 5 <= len(chars) <= 15 and not any(kw in chars for kw in ['角色', '动作', '情绪', '或者', '那这', '再看', '示例', '检查', '符合', '最终', '不过', '可能', '这样', '比如']):
            return chars

    # 如果都没找到，返回前15个中文字符
    all_chinese = ''.join(chinese_chars)
    if all_chinese:
        return all_chinese[:15]

    return None


def clean_filename(filename):
    """清理文件名，返回简洁的新名字"""
    name_without_ext = Path(filename).stem
    ext = Path(filename).suffix

    # 移除常见的分析性词汇
    bad_keywords = [
        '角色是', '动作是', '情绪是', '或者', '那这里', '再看', '示例',
        '检查', '符合', '最终', '不过', '可能', '这样', '比如', '观察',
        '要简', '确定', '文字是', '表情是', '结合', '旁边', '元素', '眼睛',
        '5-15', '字数', '格式', '应该', '更准确', '简洁', '更简', '看图',
        '能更', '希望', '通用', '"', '"', '(', ')', '（', '）', '_', '不对',
        '因为', '所以', '然后', '首先', '其实', '哦', '吧', '呢', '啊'
    ]

    # 先尝试提取关键词
    keywords = extract_keywords(filename)
    if keywords:
        # 清理提取到的关键词
        for kw in bad_keywords:
            keywords = keywords.replace(kw, '')
        keywords = re.sub(r'["""\'\'\(\)（）\[\]【】]', '', keywords).strip()
        if 3 <= len(keywords) <= 15:
            return f"{keywords}{ext}"

    # 如果提取失败，尝试其他方法
    # 分割并提取有意义的部分
    parts = re.split(r'[，。、；：！？]', name_without_ext)
    for part in parts:
        part = part.strip()
        # 移除分析性词汇
        for kw in bad_keywords:
            part = part.replace(kw, '')
        part = part.strip()
        # 如果是合适长度的纯中文
        if 4 <= len(part) <= 15 and re.match(r'^[\u4e00-\u9fa5]+$', part):
            return f"{part}{ext}"

    # 实在没办法就用"表情包"加数字
    return f"表情包_{hash(filename) % 10000}{ext}"


def main():
    """主函数：批量重命名"""
    print("🔍 扫描需要重命名的文件...")

    # 查找所有需要重命名的文件
    files_to_rename = []

    for file_path in IMAGE_DIR.glob("*.*"):
        if file_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
            continue

        filename = file_path.name
        # 检查是否包含不良关键词
        bad_keywords = [
            '角色', '动作', '情绪', '或者', '那这里', '再看', '示例',
            '检查', '符合', '最终', '不过', '可能', '这样', '比如',
            '观察', '要简', '确定', '文字是', '表情是', '结合', '旁边',
            '元素', '5-15', '字数', '格式', '更准确', '简洁', '"', '"'
        ]

        if any(kw in filename for kw in bad_keywords):
            files_to_rename.append(file_path)

    print(f"📝 找到 {len(files_to_rename)} 个需要重命名的文件\n")

    if not files_to_rename:
        print("✅ 没有需要重命名的文件！")
        return

    # 执行重命名
    success_count = 0
    fail_count = 0

    for file_path in files_to_rename:
        old_name = file_path.name
        new_name = clean_filename(old_name)
        new_path = file_path.parent / new_name

        # 处理重名冲突
        counter = 1
        while new_path.exists() and new_path != file_path:
            name_part = Path(new_name).stem
            ext_part = Path(new_name).suffix
            new_name = f"{name_part}_{counter}{ext_part}"
            new_path = file_path.parent / new_name
            counter += 1

        try:
            if new_path != file_path:
                file_path.rename(new_path)
                print(f"✅ {old_name}\n   → {new_name}\n")
                success_count += 1
            else:
                print(f"⏭️ 跳过 {old_name} (无需重命名)\n")
        except Exception as e:
            print(f"❌ 重命名失败 {old_name}: {e}\n")
            fail_count += 1

    print(f"\n📊 处理完成！")
    print(f"✅ 成功: {success_count}")
    print(f"❌ 失败: {fail_count}")


if __name__ == "__main__":
    main()
