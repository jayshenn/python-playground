"""
分块拷贝大文件

对应文档: 05-file-operations.md § 5.8.3
"""

import os

SOURCE_FILE = 'large_source.bin'
DEST_FILE = 'large_dest.bin'

def setup_file():
    """创建一个稍大的文件"""
    print("Creating large file...")
    with open(SOURCE_FILE, 'wb') as f:
        # 写入 5MB 数据
        f.write(os.urandom(5 * 1024 * 1024))
    print("Large file created.")

def copy_large_file(source, destination, chunk_size=1024*1024):
    """
    分块拷贝大文件
    
    参数:
        source: 源文件路径
        destination: 目标文件路径
        chunk_size: 每次读取的字节数（默认 1MB）
    """
    print(f"Copying {source} to {destination} with chunk size {chunk_size}...")
    
    try:
        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break
                    dst.write(chunk)
                    print(".", end='', flush=True) # 进度指示
        
        print("\nCopy successful.")
        
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == '__main__':
    setup_file()
    try:
        # 使用较小的 chunk_size 以便演示多次读取
        copy_large_file(SOURCE_FILE, DEST_FILE, chunk_size=512*1024) 
    finally:
        if os.path.exists(SOURCE_FILE):
            os.remove(SOURCE_FILE)
        if os.path.exists(DEST_FILE):
            os.remove(DEST_FILE)
