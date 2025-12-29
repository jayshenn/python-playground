"""
迭代文件对象（推荐方式）

对应文档: 05-file-operations.md § 5.6.4
"""

import os

FILENAME = 'test_iterate.txt'

def setup_file():
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for i in range(5):
            f.write(f"Line {i+1}\n")

def demo_iterate_file():
    """演示直接迭代文件对象"""
    print("\n--- Iterate File Object ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        # 文件对象本身就是可迭代的
        # 这种方式内存效率最高，逐行读取
        for line in f:
            print(f"Read: {line.strip()}")

def demo_enumerate_file():
    """演示使用 enumerate 获取行号"""
    print("\n--- Enumerate File ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")

if __name__ == '__main__':
    setup_file()
    try:
        demo_iterate_file()
        demo_enumerate_file()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
