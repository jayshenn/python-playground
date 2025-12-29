"""
最佳实践：使用 pathlib 处理路径

对应文档: 05-file-operations.md § 5.9.4
"""

from pathlib import Path

def good_practice_pathlib():
    print("\n--- Using pathlib ---")
    
    # 构建路径 (跨平台安全)
    file_path = Path('practice_pathlib.txt')
    
    # 写入
    # pathlib 提供了便捷的 write_text 方法
    file_path.write_text('Content via pathlib', encoding='utf-8')
    print(f"Written to {file_path}")
    
    # 检查存在
    if file_path.exists():
        # 读取
        content = file_path.read_text(encoding='utf-8')
        print(f"Read: {content}")
        
        # 删除
        file_path.unlink()
        print("File deleted.")

if __name__ == '__main__':
    good_practice_pathlib()
