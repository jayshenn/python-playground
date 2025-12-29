"""
缓冲和刷新

对应文档: 05-file-operations.md § 5.5.5
"""

import os
import time

FILENAME = 'test_buffer.txt'

def demo_default_buffering():
    """演示默认缓冲"""
    print("\n--- Default Buffering ---")
    
    # 写入数据，但不关闭文件，观察文件大小
    f = open(FILENAME, 'w', encoding='utf-8')
    f.write('Hello World ' * 100) # 写入一些数据到缓冲区
    
    # 此时数据可能还在内存缓冲区，未写入磁盘
    # 检查文件大小（可能为0，取决于操作系统和实现）
    size = os.path.getsize(FILENAME)
    print(f"File size before close/flush: {size} bytes")
    
    f.close() # 关闭时会自动刷新缓冲区
    
    size_after = os.path.getsize(FILENAME)
    print(f"File size after close: {size_after} bytes")
    
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

def demo_manual_flush():
    """演示手动刷新 flush()"""
    print("\n--- Manual Flush ---")
    
    f = open(FILENAME, 'w', encoding='utf-8')
    f.write('Important Data')
    
    print(f"Size before flush: {os.path.getsize(FILENAME)} bytes")
    
    f.flush() # 强制写入磁盘
    print(f"Size after flush: {os.path.getsize(FILENAME)} bytes")
    
    f.close()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

def demo_unbuffered_binary():
    """演示无缓冲（仅二进制模式支持）"""
    print("\n--- Unbuffered Binary (buffering=0) ---")
    
    # buffering=0 表示无缓冲，必须是二进制模式
    f = open(FILENAME, 'wb', buffering=0)
    
    f.write(b'a')
    print(f"Size after writing 1 byte: {os.path.getsize(FILENAME)} bytes")
    
    f.write(b'b')
    print(f"Size after writing 2nd byte: {os.path.getsize(FILENAME)} bytes")
    
    f.close()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

def demo_line_buffering():
    """演示行缓冲（buffering=1, 仅文本模式）"""
    print("\n--- Line Buffering (buffering=1) ---")
    
    f = open(FILENAME, 'w', encoding='utf-8', buffering=1)
    
    f.write('Hello')
    print(f"Size after 'Hello': {os.path.getsize(FILENAME)} bytes")
    
    f.write('\n') # 遇到换行符，刷新缓冲区
    print(f"Size after '\\n': {os.path.getsize(FILENAME)} bytes")
    
    f.close()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

if __name__ == '__main__':
    demo_default_buffering()
    demo_manual_flush()
    demo_unbuffered_binary()
    demo_line_buffering()
