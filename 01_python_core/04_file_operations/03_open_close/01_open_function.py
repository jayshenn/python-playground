"""
使用 open() 函数打开文件

对应文档: 05-file-operations.md § 5.4.1
"""

# 基本语法：file_object = open(file_path, mode, encoding=None)

# 参数说明：
# - file_path：文件路径（字符串）
# - mode：打开模式（字符串）
# - encoding：编码格式（文本模式下使用）

# 创建一个测试文件
with open('test_open.txt', 'w', encoding='utf-8') as f:
    f.write('Test content')

# 使用 open() 打开
try:
    file = open('test_open.txt', 'r', encoding='utf-8')
    print(f"File opened: {file}")
    content = file.read()
    print(f"Content: {content}")
    file.close()
    print("File closed")
except IOError as e:
    print(f"Error: {e}")

# 清理
import os
try:
    os.remove('test_open.txt')
except OSError:
    pass
