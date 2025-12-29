"""
search

对应文档: 13-regular-expressions.md § 13.2.1
"""

import re

# re.search() 扫描整个字符串并返回第一个成功的匹配对象

def main():
    text = "Python is the best language in the world"
    
    # 查找单词 best
    result = re.search(r"best", text)
    
    if result:
        print(f"匹配成功: {result.group()}")
        print(f"匹配位置: {result.span()}")
    else:
        print("未找到匹配项")

if __name__ == '__main__':
    main()
