"""
使用 shutil 模块拷贝

对应文档: 05-file-operations.md § 5.8.5
"""

import shutil
import os
import time

SOURCE_FILE = 'shutil_source.txt'
DEST_FILE = 'shutil_dest.txt'

def setup_file():
    with open(SOURCE_FILE, 'w') as f:
        f.write('Content for shutil copy.')

def demo_shutil_copy():
    """演示 shutil 拷贝"""
    print("\n--- shutil.copy() ---")
    
    # shutil.copy(src, dst)
    # 拷贝文件数据和权限模式
    shutil.copy(SOURCE_FILE, DEST_FILE)
    print(f"Copied to {DEST_FILE}")
    
    # 验证
    if os.path.exists(DEST_FILE):
        os.remove(DEST_FILE)

def demo_shutil_copy2():
    """演示 shutil.copy2()"""
    print("\n--- shutil.copy2() ---")
    
    # shutil.copy2(src, dst)
    # 拷贝文件数据、权限模式以及元数据（如创建时间、修改时间）
    shutil.copy2(SOURCE_FILE, DEST_FILE)
    
    src_stat = os.stat(SOURCE_FILE)
    dst_stat = os.stat(DEST_FILE)
    
    print(f"Source mtime: {src_stat.st_mtime}")
    print(f"Dest mtime:   {dst_stat.st_mtime}")
    print(f"Metadata preserved: {abs(src_stat.st_mtime - dst_stat.st_mtime) < 1}")

    if os.path.exists(DEST_FILE):
        os.remove(DEST_FILE)

if __name__ == '__main__':
    setup_file()
    try:
        demo_shutil_copy()
        demo_shutil_copy2()
    finally:
        if os.path.exists(SOURCE_FILE):
            os.remove(SOURCE_FILE)
