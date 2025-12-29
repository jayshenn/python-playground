"""
writelines() 方法

对应文档: 05-file-operations.md § 5.5.2
"""

import os

FILENAME = 'test_writelines.txt'

def demo_writelines():
    """演示 writelines()"""
    print("\n--- writelines() ---")
    
    # 准备一个字符串列表
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        # writelines 接受一个字符串序列（列表、元组等）
        f.writelines(lines)
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print("Content:")
        print(f.read())

def demo_writelines_no_newline():
    """演示 writelines() 不会自动换行"""
    print("\n--- writelines() without newlines ---")
    
    lines = ['Apple', 'Banana', 'Cherry']
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print(f"Content: {f.read()}") # AppleBananaCherry

def demo_generator_input():
    """演示 writelines() 接受生成器"""
    print("\n--- writelines() with generator ---")
    
    # 使用生成器表达式添加换行符
    lines = ['Apple', 'Banana', 'Cherry']
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.writelines(line + '\n' for line in lines)
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print("Content:")
        print(f.read())

if __name__ == '__main__':
    try:
        demo_writelines()
        demo_writelines_no_newline()
        demo_generator_input()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
