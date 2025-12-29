"""
批量拷贝文件

对应文档: 05-file-operations.md § 5.8.6
"""

import os
import shutil
import glob

SOURCE_DIR = 'batch_source'
DEST_DIR = 'batch_dest'

def setup():
    if not os.path.exists(SOURCE_DIR):
        os.mkdir(SOURCE_DIR)
    
    # 创建一些文件
    for i in range(5):
        with open(os.path.join(SOURCE_DIR, f'file_{i}.txt'), 'w') as f:
            f.write(f'Content {i}')
            
    # 创建一些干扰文件
    with open(os.path.join(SOURCE_DIR, 'image.jpg'), 'w') as f:
        f.write('fake image')

def cleanup():
    if os.path.exists(SOURCE_DIR):
        shutil.rmtree(SOURCE_DIR)
    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)

def batch_copy_files(source_dir, dest_dir, pattern='*.txt'):
    """
    批量拷贝指定类型的文件
    """
    print(f"\nBatch copying '{pattern}' from {source_dir} to {dest_dir}...")
    
    # 确保目标目录存在
    os.makedirs(dest_dir, exist_ok=True)
    
    # 查找匹配文件
    search_pattern = os.path.join(source_dir, pattern)
    files = glob.glob(search_pattern)
    
    count = 0
    for src_file in files:
        filename = os.path.basename(src_file)
        dst_file = os.path.join(dest_dir, filename)
        
        try:
            shutil.copy2(src_file, dst_file)
            print(f"Copied: {filename}")
            count += 1
        except Exception as e:
            print(f"Failed to copy {filename}: {e}")
            
    print(f"Total copied: {count}")

if __name__ == '__main__':
    setup()
    try:
        batch_copy_files(SOURCE_DIR, DEST_DIR, '*.txt')
        
        # 验证
        print("\nFiles in destination:")
        print(os.listdir(DEST_DIR))
    finally:
        cleanup()
