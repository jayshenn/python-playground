"""
findall

对应文档: 13-regular-expressions.md § 13.2.3
"""

import re

# re.findall() 以列表形式返回所有匹配项

def main():
    text = "苹果价格是 10 元，香蕉价格是 5 元，西瓜价格是 20 元"
    
    # 查找所有数字
    prices = re.findall(r"\d+", text)
    
    print(f"提取出的价格列表: {prices}")

if __name__ == '__main__':
    main()
