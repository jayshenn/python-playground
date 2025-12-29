"""
文件对象方法

对应文档: 05-file-operations.md § 5.7.1
"""

import os

FILENAME = 'test_methods.txt'

def demo_file_attributes():
    """演示文件对象属性"""
    print("\n--- File Object Attributes ---")
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        print(f"Name: {f.name}")
        print(f"Mode: {f.mode}")
        print(f"Encoding: {f.encoding}")
        print(f"Closed (inside): {f.closed}")
        
    print(f"Closed (outside): {f.closed}")

def demo_common_methods():
    """演示常用方法"""
    print("\n--- Common Methods ---")
    
    with open(FILENAME, 'w+', encoding='utf-8') as f:
        # write
        f.write('Hello\n')
        f.flush() # 刷新缓冲区
        
        # tell & seek
        print(f"Position: {f.tell()}")
        f.seek(0)
        
        # read
        print(f"Read: {f.read().strip()}")
        
        # truncate
        f.seek(0)
        f.truncate(2) # 截断文件为 2 字节
        
        f.seek(0)
        print(f"After truncate(2): {f.read()}")

    if os.path.exists(FILENAME):
        os.remove(FILENAME)

if __name__ == '__main__':
    demo_file_attributes()
    demo_common_methods()
