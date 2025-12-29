"""
readlines() 方法

对应文档: 05-file-operations.md § 5.6.3
"""

import os

FILENAME = 'test_readlines.txt'

def setup_file():
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Apple\n')
        f.write('Banana\n')
        f.write('Cherry\n')

def demo_readlines():
    """演示 readlines()"""
    print("\n--- readlines() ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        # readlines() 一次性读取所有行并返回列表
        lines = f.readlines()
        print(f"Type: {type(lines)}")
        print(f"Content: {lines}")

    # 处理列表
    print("\nProcessing lines:")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

def demo_readlines_hint():
    """演示 readlines(hint) 参数"""
    print("\n--- readlines(hint) ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        # hint 参数控制读取的字节数（大约）
        # 如果读取的字节数超过 hint，则停止读取后续行
        lines = f.readlines(10) 
        print(f"Lines with hint=10: {lines}")

if __name__ == '__main__':
    setup_file()
    try:
        demo_readlines()
        demo_readlines_hint()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
