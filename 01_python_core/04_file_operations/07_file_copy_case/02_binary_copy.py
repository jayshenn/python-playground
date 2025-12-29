"""
二进制文件拷贝

对应文档: 05-file-operations.md § 5.8.2
"""

import os

SOURCE_FILE = 'source_img.bin' # 模拟二进制文件
DEST_FILE = 'dest_img.bin'

def setup_file():
    # 创建一个模拟的二进制文件
    data = bytes(range(256)) # 0-255 字节
    with open(SOURCE_FILE, 'wb') as f:
        f.write(data)

def copy_binary_file(source, destination):
    """
    拷贝二进制文件
    """
    print(f"Copying binary file {source} to {destination}...")
    
    try:
        # 使用 'rb' 和 'wb' 模式
        with open(source, 'rb') as src:
            data = src.read()
            
        with open(destination, 'wb') as dst:
            dst.write(data)
            
        print("Copy successful.")
        
        # 验证大小
        src_size = os.path.getsize(source)
        dst_size = os.path.getsize(destination)
        print(f"Source size: {src_size}, Dest size: {dst_size}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    setup_file()
    try:
        copy_binary_file(SOURCE_FILE, DEST_FILE)
    finally:
        if os.path.exists(SOURCE_FILE):
            os.remove(SOURCE_FILE)
        if os.path.exists(DEST_FILE):
            os.remove(DEST_FILE)
