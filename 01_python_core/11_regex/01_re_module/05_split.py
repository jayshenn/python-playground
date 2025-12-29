"""
split

对应文档: 13-regular-expressions.md § 13.2.5
"""

import re

# re.split() 根据匹配项分割字符串

def main():
    # 包含多种分隔符的字符串
    text = "apple,banana;orange lemon"
    
    # 匹配 , 或 ; 或 空格
    fruits = re.split(r"[,; ]", text)
    
    print(f"分割后的列表: {fruits}")

if __name__ == '__main__':
    main()
