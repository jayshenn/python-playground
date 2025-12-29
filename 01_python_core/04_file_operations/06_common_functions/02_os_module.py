"""
os 模块常用操作

对应文档: 05-file-operations.md § 5.7.2
"""

import os
import time

TEST_DIR = 'test_os_dir'
TEST_FILE = 'test_os_file.txt'

def demo_file_ops():
    """文件操作"""
    print("\n--- os File Operations ---")
    
    # 准备文件
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)
    
    file_path = os.path.join(TEST_DIR, TEST_FILE)
    with open(file_path, 'w') as f:
        f.write('test content')
    
    print(f"Created: {file_path}")
    
    # 检查存在
    print(f"Exists: {os.path.exists(file_path)}")
    print(f"Is file: {os.path.isfile(file_path)}")
    
    # 获取信息
    print(f"Size: {os.path.getsize(file_path)} bytes")
    print(f"Created Time: {time.ctime(os.path.getctime(file_path))}")
    print(f"Modified Time: {time.ctime(os.path.getmtime(file_path))}")
    
    # 重命名
    new_path = os.path.join(TEST_DIR, 'renamed.txt')
    os.rename(file_path, new_path)
    print(f"Renamed to: {new_path}")
    
    # 删除文件
    os.remove(new_path)
    print("File removed.")

def demo_dir_ops():
    """目录操作"""
    print("\n--- os Directory Operations ---")
    
    cwd = os.getcwd()
    print(f"CWD: {cwd}")
    
    # 列出文件
    print(f"List dir '{TEST_DIR}': {os.listdir(TEST_DIR)}")
    
    # 删除目录
    os.rmdir(TEST_DIR) # 必须是空目录
    print(f"Removed dir: {TEST_DIR}")
    
    # 多级目录
    multi_dir = 'a/b/c'
    os.makedirs(multi_dir, exist_ok=True)
    print(f"Created makedirs: {multi_dir}")
    
    # 删除多级目录 (os.removedirs 只能删除空目录链，通常用 shutil.rmtree)
    # 这里为了演示简单，逐层删除
    os.rmdir('a/b/c')
    os.rmdir('a/b')
    os.rmdir('a')
    print("Removed multi dirs.")

def demo_path_ops():
    """路径操作"""
    print("\n--- os.path Operations ---")
    
    path = '/path/to/some/file.txt'
    
    print(f"Path: {path}")
    print(f"Dirname: {os.path.dirname(path)}")
    print(f"Basename: {os.path.basename(path)}")
    print(f"Split: {os.path.split(path)}")
    print(f"Splitext: {os.path.splitext(path)}")
    print(f"Join: {os.path.join('folder', 'file.txt')}")
    print(f"Abs: {os.path.abspath('.')}")

if __name__ == '__main__':
    demo_file_ops()
    demo_dir_ops()
    demo_path_ops()
