"""
写入模式对比

对应文档: 05-file-operations.md § 5.5.4
"""

import os

FILENAME = 'test_mode.txt'

def demo_write_mode():
    """演示 'w' 模式：覆盖写入"""
    print("\n--- 'w' Mode (Overwrite) ---")
    
    # 第一次写入
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('First Write\n')
    
    # 验证
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print(f"After first write: {f.read().strip()}")
    
    # 第二次写入（覆盖）
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Second Write (Overwritten)\n')
    
    # 验证
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print(f"After second write: {f.read().strip()}")

def demo_append_mode():
    """演示 'a' 模式：追加写入"""
    print("\n--- 'a' Mode (Append) ---")
    
    # 确保文件以 'First Write' 开始
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('First Write\n')
    
    # 追加写入
    with open(FILENAME, 'a', encoding='utf-8') as f:
        f.write('Appended Content\n')
    
    # 验证
    with open(FILENAME, 'r', encoding='utf-8') as f:
        print(f"Content:\n{f.read().strip()}")

def demo_exclusive_creation():
    """演示 'x' 模式：独占创建"""
    print("\n--- 'x' Mode (Exclusive Creation) ---")
    
    # 确保文件存在
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Existing File')
        
    try:
        # 尝试用 'x' 模式打开已存在的文件 -> 报错
        with open(FILENAME, 'x', encoding='utf-8') as f:
            f.write('Should fail')
    except FileExistsError:
        print(f"Success: Caught FileExistsError because '{FILENAME}' exists.")
        
    # 删除文件后重试
    os.remove(FILENAME)
    
    try:
        with open(FILENAME, 'x', encoding='utf-8') as f:
            f.write('Created with x mode')
        print(f"Success: Created '{FILENAME}' with 'x' mode.")
    except FileExistsError:
        print("Error: Should not happen.")

if __name__ == '__main__':
    try:
        demo_write_mode()
        demo_append_mode()
        demo_exclusive_creation()
    finally:
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
