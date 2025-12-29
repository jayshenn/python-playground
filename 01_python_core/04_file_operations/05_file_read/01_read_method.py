"""
read() 方法

对应文档: 05-file-operations.md § 5.6.1
"""

import os

FILENAME = 'test_read.txt'

def setup_file():
    """创建测试文件"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Hello World\n')
        f.write('This is Python\n')
        f.write('File Operations')

def demo_read_all():
    """演示读取所有内容"""
    print("\n--- read() all ---")
    with open(FILENAME, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"Content:\n{content}")

def demo_read_size():
    """演示读取指定数量字符"""
    print("\n--- read(size) ---")
    with open(FILENAME, 'r', encoding='utf-8') as f:
        part1 = f.read(5)  # 读取前5个字符
        print(f"First 5 chars: '{part1}'")
        
        part2 = f.read(6)  # 继续读取6个字符
        print(f"Next 6 chars: '{part2}'")

def demo_read_chunks():
    """演示分块读取（适合大文件）"""
    print("\n--- Read in chunks ---")
    chunk_size = 8
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            print(f"Chunk: '{chunk}'")

if __name__ == '__main__':
    setup_file()
    try:
        demo_read_all()
        demo_read_size()
        demo_read_chunks()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
