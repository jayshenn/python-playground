"""
match

对应文档: 13-regular-expressions.md § 13.2.2
"""

import re

# re.match() 仅从字符串的起始位置开始匹配

def main():
    text = "Hello World"
    
    # 1. 匹配开头
    res1 = re.match(r"Hello", text)
    print(f"匹配 'Hello' 结果: {res1.group() if res1 else 'None'}")
    
    # 2. 匹配中间位置 (由于不是开头，match 会失败)
    res2 = re.match(r"World", text)
    print(f"匹配 'World' 结果: {res2}")

if __name__ == '__main__':
    main()
