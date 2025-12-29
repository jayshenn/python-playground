"""
pathlib 模块（推荐）

对应文档: 05-file-operations.md § 5.7.4
"""

from pathlib import Path
import shutil

TEST_DIR = Path('test_pathlib')

def demo_path_basics():
    """基础路径操作"""
    print("\n--- Path Basics ---")
    
    # 当前路径
    p = Path('.')
    print(f"Current: {p.resolve()}")
    
    # 路径拼接
    sub_path = p / 'folder' / 'file.txt'
    print(f"Joined: {sub_path}")
    
    # 属性
    print(f"Name: {sub_path.name}")
    print(f"Stem: {sub_path.stem}")
    print(f"Suffix: {sub_path.suffix}")
    print(f"Parent: {sub_path.parent}")

def demo_file_ops():
    """文件读写与操作"""
    print("\n--- File Operations ---")
    
    if not TEST_DIR.exists():
        TEST_DIR.mkdir()
    
    file_path = TEST_DIR / 'hello.txt'
    
    # 写入文本
    file_path.write_text('Hello Pathlib!', encoding='utf-8')
    print(f"Wrote to {file_path}")
    
    # 读取文本
    content = file_path.read_text(encoding='utf-8')
    print(f"Read content: {content}")
    
    # 重命名
    new_path = TEST_DIR / 'renamed.txt'
    file_path.rename(new_path)
    print(f"Renamed to {new_path}")
    
    # 检查
    print(f"Exists? {new_path.exists()}")
    print(f"Is file? {new_path.is_file()}")
    
    # 删除
    new_path.unlink()
    print("File deleted")

def demo_glob():
    """遍历文件"""
    print("\n--- Glob ---")
    
    # 创建一些文件
    (TEST_DIR / 'a.txt').touch()
    (TEST_DIR / 'b.py').touch()
    (TEST_DIR / 'sub').mkdir(exist_ok=True)
    (TEST_DIR / 'sub' / 'c.txt').touch()
    
    print("*.txt files:")
    for f in TEST_DIR.glob('*.txt'):
        print(f" - {f.name}")
        
    print("Recursive *.txt files:")
    for f in TEST_DIR.rglob('*.txt'):
        print(f" - {f}")

    # 清理
    shutil.rmtree(TEST_DIR)

if __name__ == '__main__':
    demo_path_basics()
    demo_file_ops()
    demo_glob()
