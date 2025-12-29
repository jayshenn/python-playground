"""
匹配电话号码

对应文档: 13-regular-expressions.md § 13.8.1
"""

import re

# 中国大陆手机号规律：1 开头，第二位通常是 3-9，总共 11 位数字

def check_phone(phone):
    pattern = r"^1[3-9]\d{9}$"
    if re.match(pattern, phone):
        return True
    return False

if __name__ == '__main__':
    phones = ["13812345678", "12345678901", "19988887777", "138-1234-5678"]
    for p in phones:
        print(f"{p} 是否为合法手机号: {check_phone(p)}")
