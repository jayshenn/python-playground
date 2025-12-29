"""
shutil 模块常用操作

对应文档: 05-file-operations.md § 5.7.3
"""

import shutil
import os

TEST_DIR = 'test_shutil'

def setup():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)
    
    with open(os.path.join(TEST_DIR, 'source.txt'), 'w') as f:
        f.write('Source content')

def cleanup():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR) # 递归删除

def demo_copy_move():
    """演示复制和移动"""
    print("\n--- Copy & Move ---")
    
    src = os.path.join(TEST_DIR, 'source.txt')
    dst = os.path.join(TEST_DIR, 'dest.txt')
    
    # 复制文件
    shutil.copy(src, dst)
    print(f"Copied {src} to {dst}")
    
    # 移动文件
    moved = os.path.join(TEST_DIR, 'moved.txt')
    shutil.move(dst, moved)
    print(f"Moved {dst} to {moved}")

def demo_archive():
    """演示归档（压缩）"""
    print("\n--- Archive ---")
    
    # 创建压缩包
    base_name = os.path.join(TEST_DIR, 'archive')
    root_dir = TEST_DIR
    
    # 将 root_dir 压缩为 zip
    archive_path = shutil.make_archive(base_name, 'zip', root_dir)
    print(f"Created archive: {archive_path}")

def demo_disk_usage():
    """演示磁盘使用情况"""
    print("\n--- Disk Usage ---")
    
    # 获取当前目录所在磁盘的使用情况
    total, used, free = shutil.disk_usage('.')
    
    gb = 2**30
    print(f"Total: {total / gb:.2f} GB")
    print(f"Used:  {used / gb:.2f} GB")
    print(f"Free:  {free / gb:.2f} GB")

if __name__ == '__main__':
    setup()
    try:
        demo_copy_move()
        demo_archive()
        demo_disk_usage()
    finally:
        cleanup()
