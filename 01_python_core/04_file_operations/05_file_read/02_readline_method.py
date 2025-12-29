"""
readline() 方法

对应文档: 05-file-operations.md § 5.6.2
"""

import os

FILENAME = 'test_readline.txt'

def setup_file():
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Line 1\n')
        f.write('Line 2\n')
        f.write('Line 3')  # 最后一行没有换行符

def demo_readline():
    """演示 readline() 读取单行"""
    print("\n--- readline() ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        line1 = f.readline()
        print(f"1st line: {repr(line1)}")  # 使用 repr 显示 \n
        
        line2 = f.readline()
        print(f"2nd line: {repr(line2)}")
        
        line3 = f.readline()
        print(f"3rd line: {repr(line3)}")
        
        line4 = f.readline()
        print(f"4th line (EOF): {repr(line4)}")  # 空字符串表示文件结束

def demo_readline_loop():
    """演示循环读取所有行"""
    print("\n--- readline() loop ---")
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(f"Read: {line.strip()}")

if __name__ == '__main__':
    setup_file()
    try:
        demo_readline()
        demo_readline_loop()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
