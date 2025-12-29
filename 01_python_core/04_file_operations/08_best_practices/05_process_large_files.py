"""
最佳实践：逐行处理大文件

对应文档: 05-file-operations.md § 5.9.5
"""

import os

FILENAME = 'practice_large.txt'

def setup_large_file():
    """模拟大文件"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(f"Line {i}: data...\n")

def bad_practice():
    """反例：一次性读取所有行"""
    print("\n--- Bad Practice (readlines) ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        # 如果文件很大，readlines() 会消耗大量内存
        lines = f.readlines()
        print(f"Read {len(lines)} lines into memory.")

def good_practice():
    """正例：逐行迭代"""
    print("\n--- Good Practice (Iterate) ---")
    
    count = 0
    with open(FILENAME, 'r', encoding='utf-8') as f:
        # 文件对象是可迭代的，每次只读取一行到内存
        for line in f:
            count += 1
            # process(line)
            
    print(f"Processed {count} lines efficiently.")

if __name__ == '__main__':
    setup_large_file()
    try:
        bad_practice()
        good_practice()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
