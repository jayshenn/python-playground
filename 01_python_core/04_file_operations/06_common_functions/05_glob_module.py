"""
glob 模块

对应文档: 05-file-operations.md § 5.7.5
"""

import glob
import os
import shutil

TEST_DIR = 'test_glob'

def setup():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)
        os.mkdir(os.path.join(TEST_DIR, 'sub'))
    
    # 创建不同扩展名的文件
    files = ['a.txt', 'b.py', 'c.jpg', 'd.txt']
    for f in files:
        with open(os.path.join(TEST_DIR, f), 'w') as file:
            file.write('content')
            
    # 子目录文件
    with open(os.path.join(TEST_DIR, 'sub', 'e.py'), 'w') as file:
        file.write('content')

def cleanup():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

def demo_glob():
    print("\n--- glob.glob() ---")
    
    # 查找所有 .txt 文件
    pattern_txt = os.path.join(TEST_DIR, '*.txt')
    txt_files = glob.glob(pattern_txt)
    print(f"*.txt files: {txt_files}")
    
    # 查找所有文件
    pattern_all = os.path.join(TEST_DIR, '*')
    all_files = glob.glob(pattern_all)
    print(f"All files in {TEST_DIR}: {all_files}")

def demo_recursive():
    print("\n--- Recursive glob ---")
    
    # 递归查找所有 .py 文件 (Python 3.5+)
    # 需要设置 recursive=True 并使用 **
    pattern = os.path.join(TEST_DIR, '**/*.py')
    py_files = glob.glob(pattern, recursive=True)
    print(f"Recursive **/*.py: {py_files}")

def demo_iglob():
    print("\n--- glob.iglob() ---")
    
    # iglob 返回迭代器，适合大量文件
    pattern = os.path.join(TEST_DIR, '*.txt')
    iterator = glob.iglob(pattern)
    
    print("Iterating over .txt files:")
    for f in iterator:
        print(f" - {f}")

if __name__ == '__main__':
    setup()
    try:
        demo_glob()
        demo_recursive()
        demo_iglob()
    finally:
        cleanup()
