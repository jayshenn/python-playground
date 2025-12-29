"""
从 python-2.56 中提取 2 和 56 的数字

对应文档: 13-regular-expressions.md § 13.8.3
"""

import re

def main():
    text = "python-2.56"
    
    # 提取所有连续的数字
    nums = re.findall(r"\d+", text)
    
    print(f"原文本: {text}")
    print(f"提取结果: {nums}") # ['2', '56']

if __name__ == '__main__':
    main()
