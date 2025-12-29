"""
关闭文件

对应文档: 05-file-operations.md § 5.4.3
"""

import os

# 创建一个测试文件
TEST_FILE = 'test_close.txt'
with open(TEST_FILE, 'w', encoding='utf-8') as f:
    f.write('Test content for closing file.')


def manual_close():
    """方法 1：手动关闭文件"""
    print("\n--- Manual Close ---")
    
    file = open(TEST_FILE, 'r', encoding='utf-8')
    try:
        content = file.read()
        print(f"Read content: {content}")
    finally:
        # 无论是否发生异常，都确保文件被关闭
        file.close()
        print("File closed manually.")
    
    print(f"Is file closed? {file.closed}")


def with_statement():
    """方法 2：使用 with 语句（推荐）"""
    print("\n--- With Statement ---")
    
    # with 语句会在代码块执行完毕后自动调用 close()
    with open(TEST_FILE, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"Read content: {content}")
        # 在 with 块内部，文件是打开的
        print(f"Inside with block, closed? {file.closed}")
    
    # 离开 with 块后，文件自动关闭
    print("Exited with block.")
    print(f"Is file closed? {file.closed}")


def multiple_files():
    """打开多个文件"""
    print("\n--- Multiple Files with 'with' ---")
    
    # 可以同时打开多个文件
    # 这里模拟复制：从 TEST_FILE 读取，写入到 'test_copy.txt'
    copy_file = 'test_copy.txt'
    
    with open(TEST_FILE, 'r', encoding='utf-8') as src, \
         open(copy_file, 'w', encoding='utf-8') as dst:
        dst.write(src.read())
        print(f"Copied from {TEST_FILE} to {copy_file}")
    
    # 验证并清理
    if os.path.exists(copy_file):
        os.remove(copy_file)
        print("Copy file removed.")


if __name__ == '__main__':
    try:
        manual_close()
        with_statement()
        multiple_files()
    finally:
        # 清理测试文件
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
            print("Test file removed.")
