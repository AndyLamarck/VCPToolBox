#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终清理：手动修正所有不合格的文件名
"""

import re
from pathlib import Path

IMAGE_DIR = Path(r"D:\vcp\VCPToolBox-main\image\通用表情包")

# 手动修正映射表
MANUAL_FIXES = {
    # 直接删除前缀
    r"^那组合起来就是\"": "",
    r"^那组合起来就是": "",
    r"^那组合起来\"": "",
    r"^那组合起来": "",
    r"^那": "",
    r"^可以叫\"": "",
    r"^可以简化为\"": "",
    r"^可以": "",
    r"^看图片里她的": "",
    r"^看图片里的": "",
    r"^看画面里的": "",
    r"^看结构": "",
    r"^看她的不是有点": "有点",
    r"^看动漫风格的人物动作": "动漫人物",
    r"^看": "",
    r"^根据常见表情包风格": "表情",
    r"^根据": "",
    r"^和动漫风格": "动漫风格",
    r"^是兽耳少女": "兽耳少女",
    r"^是香蕉张开": "香蕉张开",
    r"^是": "",
    r"^子是\"": "",
    r"^少女的眼睛很大": "少女瞪眼",
    r"^少女有白发": "白发少女",
    r"^\"可以简化为\"金发少女\"": "金发少女",
    r"^\"少女捂脸心动\"": "少女捂脸心动",
    r"^\"": "",
    r"\"$": "",
}

def clean_bad_names():
    """清理所有不合格的文件名"""
    # 查找不合格文件
    bad_prefixes = ['那', '可以', '看', '根据', '是', '和', '子是', '少女的', '"', '\"']
    problem_files = []

    for file_path in IMAGE_DIR.glob("*.*"):
        if file_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
            continue

        filename = file_path.stem
        if any(filename.startswith(prefix) for prefix in bad_prefixes):
            problem_files.append(file_path)

    if not problem_files:
        print("✅ 没有需要修正的文件！")
        return

    print(f"📝 找到 {len(problem_files)} 个需要修正的文件\n")

    success = 0
    for file_path in problem_files:
        old_name = file_path.name
        new_stem = file_path.stem

        # 应用修正规则
        for pattern, replacement in MANUAL_FIXES.items():
            new_stem = re.sub(pattern, replacement, new_stem)

        # 清理多余的引号和符号
        new_stem = new_stem.replace('"', '').replace('"', '').replace('"', '')
        new_stem = new_stem.replace('(', '').replace(')', '').replace('（', '').replace('）', '')
        new_stem = new_stem.strip()

        # 如果清理后为空或太短，用默认名
        if len(new_stem) < 3:
            new_stem = f"表情_{hash(old_name) % 1000:03d}"

        new_name = f"{new_stem}{file_path.suffix}"
        new_path = file_path.parent / new_name

        # 处理冲突
        counter = 1
        while new_path.exists() and new_path != file_path:
            new_name = f"{new_stem}_{counter}{file_path.suffix}"
            new_path = file_path.parent / new_name
            counter += 1

        if new_path != file_path:
            try:
                file_path.rename(new_path)
                print(f"✅ {old_name}\n   → {new_name}\n")
                success += 1
            except Exception as e:
                print(f"❌ 失败: {old_name}: {e}\n")

    print(f"\n📊 完成！成功修正 {success} 个文件")

if __name__ == "__main__":
    clean_bad_names()
