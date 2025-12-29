"""
文件指针操作

对应文档: 05-file-operations.md § 5.6.6
"""

import os

FILENAME = 'test_pointer.txt'

def setup_file():
    with open(FILENAME, 'wb') as f:
        # 写入 ASCII 字符以便于字节计算
        f.write(b'Hello World Python')

def demo_pointer_ops():
    """演示 tell() 和 seek()"""
    print("\n--- File Pointer Operations ---")
    
    with open(FILENAME, 'rb') as f:
        # 1. 初始位置
        print(f"Initial position: {f.tell()}")
        
        # 2. 读取 5 个字节
        data = f.read(5)
        print(f"Read(5): {data}")
        print(f"Current position: {f.tell()}")
        
        # 3. seek(offset, whence)
        # whence: 0=start, 1=current, 2=end
        
        # 移动到开头
        f.seek(0, 0)
        print(f"Seek(0, 0) -> Start: {f.tell()}")
        print(f"Read(5): {f.read(5)}")
        
        # 从当前位置向前移动 1 字节 (Hello -> ello)
        # 这里的 seek 1 是相对当前位置 (5)
        f.seek(1, 1) 
        print(f"Seek(1, 1) -> Current+1: {f.tell()}")
        print(f"Read(5): {f.read(5)}") # 'World'
        
        # 移动到倒数第 6 个字节
        f.seek(-6, 2)
        print(f"Seek(-6, 2) -> End-6: {f.tell()}")
        print(f"Read(6): {f.read(6)}") # 'Python'

if __name__ == '__main__':
    setup_file()
    try:
        demo_pointer_ops()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
