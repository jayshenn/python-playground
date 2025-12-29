"""
读取方法对比

对应文档: 05-file-operations.md § 5.6.5
"""

import os
import time

FILENAME = 'test_comparison.txt'

def setup_file():
    """创建一个稍微大一点的文件"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(f"This is line {i} with some content to increase size.\n")

def compare_methods():
    print("\n--- Comparison ---")
    
    # 1. read() - 读取所有内容
    start = time.perf_counter()
    with open(FILENAME, 'r', encoding='utf-8') as f:
        content = f.read()
    end = time.perf_counter()
    print(f"read(): {len(content)} chars, Time: {end - start:.6f}s")
    
    # 2. readlines() - 读取所有行到列表
    start = time.perf_counter()
    with open(FILENAME, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    end = time.perf_counter()
    print(f"readlines(): {len(lines)} lines, Time: {end - start:.6f}s")
    
    # 3. Iterate - 逐行迭代
    start = time.perf_counter()
    line_count = 0
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
    end = time.perf_counter()
    print(f"Iterate: {line_count} lines, Time: {end - start:.6f}s")

def summary():
    print("\n--- Summary ---")
    print("1. read():       适合小文件，一次性读取全部内容。")
    print("2. readlines():  适合中等文件，需要列表操作时使用。")
    print("3. Iterate:      适合大文件，内存效率最高（推荐）。")

if __name__ == '__main__':
    setup_file()
    try:
        compare_methods()
        summary()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
