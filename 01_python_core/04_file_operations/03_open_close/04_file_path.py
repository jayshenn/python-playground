"""
文件路径

对应文档: 05-file-operations.md § 5.4.4
"""

import os
from pathlib import Path

def demo_relative_path():
    """演示相对路径"""
    print("\n--- Relative Path ---")
    
    # 相对路径是相对于当前工作目录 (CWD)
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    
    # 在当前目录下创建文件
    filename = 'relative_test.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Hello from relative path')
    
    print(f"Created file: {filename}")
    
    # 读取
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"Read: {f.read()}")
        os.remove(filename)

def demo_absolute_path():
    """演示绝对路径"""
    print("\n--- Absolute Path ---")
    
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    print(f"Current script path: {current_file}")
    
    # 获取所在的目录
    base_dir = os.path.dirname(current_file)
    print(f"Base directory: {base_dir}")
    
    # 拼接绝对路径
    file_path = os.path.join(base_dir, 'absolute_test.txt')
    print(f"Target file path: {file_path}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('Hello from absolute path')
    
    # 清理
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File removed.")

def demo_pathlib():
    """演示 pathlib (推荐)"""
    print("\n--- pathlib (Recommended) ---")
    
    # 获取当前脚本所在目录
    base_dir = Path(__file__).parent
    print(f"Base directory (pathlib): {base_dir}")
    
    # 拼接路径
    file_path = base_dir / 'pathlib_test.txt'
    print(f"Target path: {file_path}")
    
    # 写入
    # pathlib 的 write_text/read_text 是快捷方法，自动处理打开和关闭
    file_path.write_text('Hello from pathlib', encoding='utf-8')
    
    # 检查存在
    if file_path.exists():
        print(f"File exists: {file_path.exists()}")
        print(f"Content: {file_path.read_text(encoding='utf-8')}")
        
        # 删除
        file_path.unlink()
        print("File unlinked.")

if __name__ == '__main__':
    demo_relative_path()
    demo_absolute_path()
    demo_pathlib()
