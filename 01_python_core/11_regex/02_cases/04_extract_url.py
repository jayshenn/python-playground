"""
从检索中获取网址

对应文档: 13-regular-expressions.md § 13.8.4
"""

import re

def main():
    text = "访问官网: https://www.python.org 或者搜索 http://www.google.com 获取更多信息"
    
    # 匹配 http 或 https 开头的网址
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
    
    urls = re.findall(pattern, text)
    
    print("提取到的网址:")
    for url in urls:
        print(f" -> {url}")

if __name__ == '__main__':
    main()
