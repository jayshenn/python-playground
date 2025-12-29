"""
按内容分类

对应文档: 05-file-operations.md § 5.2.1
"""

# 1. 文本文件（Text File）
# 文本文件以字符形式存储数据，人类可读。
# 常见文本文件：.txt, .py, .md, .json, .csv, .xml, .html

# 文本文件示例
try:
    with open('text_example.txt', 'w', encoding='utf-8') as f:
        f.write('Hello, World!\n')
        f.write('这是一个文本文件')
    print("Created text_example.txt")
except IOError as e:
    print(f"Error creating text file: {e}")

# 2. 二进制文件（Binary File）
# 二进制文件以字节形式存储数据，通常不可直接阅读。
# 常见二进制文件：.jpg, .png, .mp3, .mp4, .zip, .exe

# 二进制文件示例：写入一些字节
try:
    with open('binary_example.bin', 'wb') as f:
        f.write(b'\x00\x01\x02\x03\x04')
    print("Created binary_example.bin")
except IOError as e:
    print(f"Error creating binary file: {e}")

# 清理生成的文件
import os
try:
    os.remove('text_example.txt')
    os.remove('binary_example.bin')
    print("Cleaned up created files")
except OSError as e:
    print(f"Error cleaning up: {e}")
