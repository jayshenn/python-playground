"""
write() 方法

对应文档: 05-file-operations.md § 5.5.1
"""

import os

FILENAME = 'test_write.txt'

def demo_basic_write():
    """演示基本的 write() 使用"""
    print("\n--- Basic write() ---")
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        # write() 写入字符串
        # 注意：write() 不会自动添加换行符，需要手动添加 \n
        f.write('Line 1\n')
        f.write('Line 2\n')
        
        # write() 返回写入的字符数
        count = f.write('Hello World')
        print(f"Wrote {count} characters")
        f.write('\n')

    # 验证内容
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print("File content:")
        print(f.read())

def demo_no_newline():
    """演示不加换行符的效果"""
    print("\n--- No newline ---")
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Hello')
        f.write('World') # 紧接着 'Hello' 写入
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print(f"Content: {f.read()}") # HelloWorld

if __name__ == '__main__':
    try:
        demo_basic_write()
        demo_no_newline()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
