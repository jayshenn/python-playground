"""
文件打开模式

对应文档: 05-file-operations.md § 5.4.2
"""

import os


def demo_read_mode():
    """演示 'r' 只读模式"""
    print("\n--- Demo: 'r' mode ---")
    # 先创建一个文件
    with open('mode_r.txt', 'w', encoding='utf-8') as f:
        f.write('Content for read mode.')
    
    # 以只读模式打开
    try:
        with open('mode_r.txt', 'r', encoding='utf-8') as f:
            print(f"Read: {f.read()}")
            # f.write('Try to write')  # 这会报错：io.UnsupportedOperation: not writable
    except IOError as e:
        print(f"Error: {e}")
    finally:
        os.remove('mode_r.txt')


def demo_write_mode():
    """演示 'w' 写入模式（覆盖）"""
    print("\n--- Demo: 'w' mode ---")
    # 创建文件并写入初始内容
    with open('mode_w.txt', 'w', encoding='utf-8') as f:
        f.write('Initial content.')
    
    # 再次以 'w' 模式打开，会覆盖原有内容
    with open('mode_w.txt', 'w', encoding='utf-8') as f:
        f.write('Overwritten content.')
    
    # 验证内容
    with open('mode_w.txt', 'r', encoding='utf-8') as f:
        print(f"Content after overwrite: {f.read()}")
    
    os.remove('mode_w.txt')


def demo_append_mode():
    """演示 'a' 追加模式"""
    print("\n--- Demo: 'a' mode ---")
    with open('mode_a.txt', 'w', encoding='utf-8') as f:
        f.write('Line 1\n')
    
    # 以追加模式打开
    with open('mode_a.txt', 'a', encoding='utf-8') as f:
        f.write('Line 2 (Appended)\n')
    
    with open('mode_a.txt', 'r', encoding='utf-8') as f:
        print(f"Content after append:\n{f.read().strip()}")
    
    os.remove('mode_a.txt')


def demo_read_plus_mode():
    """演示 'r+' 读写模式"""
    print("\n--- Demo: 'r+' mode ---")
    with open('mode_rp.txt', 'w', encoding='utf-8') as f:
        f.write('Hello World')
    
    # 'r+' 模式：指针在开头
    with open('mode_rp.txt', 'r+', encoding='utf-8') as f:
        content = f.read(5)  # 读取前5个字符 'Hello'
        print(f"Read first 5 chars: {content}")
        f.write(' Python')   # 接着当前指针位置写入
    
    with open('mode_rp.txt', 'r', encoding='utf-8') as f:
        print(f"Final content: {f.read()}")  # Hello Pythonld (World 被部分覆盖)
    
    os.remove('mode_rp.txt')


def demo_binary_mode():
    """演示二进制模式 'rb' 和 'wb'"""
    print("\n--- Demo: 'rb' & 'wb' mode ---")
    data = b'\x00\x01\x02\x03'
    
    # 二进制写入
    with open('binary.bin', 'wb') as f:
        f.write(data)
    
    # 二进制读取
    with open('binary.bin', 'rb') as f:
        read_data = f.read()
        print(f"Read binary data: {read_data}")
        print(f"Data matches: {data == read_data}")
    
    os.remove('binary.bin')


if __name__ == '__main__':
    # 演示各种模式
    demo_read_mode()
    demo_write_mode()
    demo_append_mode()
    demo_read_plus_mode()
    demo_binary_mode()
