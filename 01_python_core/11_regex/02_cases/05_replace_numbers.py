"""
替换文本中的所有数字为对应的词

对应文档: 13-regular-expressions.md § 13.8.5
"""

import re

# 将数字转换为描述词
num_map = {
    '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍'
}

def replace_func(match):
    val = match.group()
    return num_map.get(val, val)

def main():
    text = "我有 1 个苹果，2 个梨，5 个西瓜"
    
    # re.sub 的第二个参数可以是一个函数
    new_text = re.sub(r"\d", replace_func, text)
    
    print(f"原句: {text}")
    print(f"替换后: {new_text}")

if __name__ == '__main__':
    main()
