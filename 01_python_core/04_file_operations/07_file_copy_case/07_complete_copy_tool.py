"""
完整的文件拷贝工具

对应文档: 05-file-operations.md § 5.8.7
"""

import os
import shutil
from pathlib import Path

def advanced_copy(source, destination, overwrite=False, preserve_metadata=True):
    """
    高级文件拷贝工具

    参数:
        source: 源文件或目录路径
        destination: 目标路径
        overwrite: 是否覆盖已存在的文件
        preserve_metadata: 是否保留元数据（修改时间等）

    返回:
        成功返回 True，失败返回 False
    """
    source_path = Path(source)
    dest_path = Path(destination)

    print(f"\nTask: Copy '{source}' -> '{destination}'")

    # 1. 检查源是否存在
    if not source_path.exists():
        print(f"Error: Source '{source}' does not exist.")
        return False

    # 2. 检查目标是否已存在
    if dest_path.exists():
        if not overwrite:
            print(f"Error: Destination '{destination}' already exists.")
            print("Tip: Use overwrite=True to force copy.")
            return False
        else:
            print("Warning: Destination exists, will overwrite.")
            # 如果目标是目录，且源也是目录，shutil.copytree 默认会报错（除非 dirs_exist_ok=True，Python 3.8+）
            # 这里为了通用性，如果 overwrite=True 且目标是目录，先删除
            if dest_path.is_dir() and source_path.is_dir():
                shutil.rmtree(dest_path)
            # 如果目标是文件，copy2 会直接覆盖

    try:
        # 3. 如果是文件
        if source_path.is_file():
            # 确保目标目录存在
            if not dest_path.parent.exists():
                dest_path.parent.mkdir(parents=True)
                
            if preserve_metadata:
                shutil.copy2(source_path, dest_path)
            else:
                shutil.copy(source_path, dest_path)

            size = source_path.stat().st_size
            print(f"Success: File copied. ({size} bytes)")

        # 4. 如果是目录
        elif source_path.is_dir():
            # copytree 递归拷贝
            # dirs_exist_ok=True 允许目标目录存在 (Python 3.8+)
            shutil.copytree(source_path, dest_path, dirs_exist_ok=overwrite)
            
            # 统计文件数
            file_count = sum(1 for _ in dest_path.rglob('*') if _.is_file())
            print(f"Success: Directory copied. ({file_count} files)")

        return True

    except PermissionError:
        print(f"Error: Permission denied.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# --- 测试代码 ---

TEST_SRC = 'tool_src'
TEST_DST = 'tool_dst'

def setup():
    if not os.path.exists(TEST_SRC):
        os.mkdir(TEST_SRC)
        with open(os.path.join(TEST_SRC, 'file1.txt'), 'w') as f:
            f.write('content1')
        with open(os.path.join(TEST_SRC, 'file2.txt'), 'w') as f:
            f.write('content2')

def cleanup():
    if os.path.exists(TEST_SRC):
        shutil.rmtree(TEST_SRC)
    if os.path.exists(TEST_DST):
        shutil.rmtree(TEST_DST)

if __name__ == '__main__':
    setup()
    try:
        # 1. 正常拷贝目录
        advanced_copy(TEST_SRC, TEST_DST)
        
        # 2. 尝试覆盖（如果不开启 overwrite 应失败）
        advanced_copy(TEST_SRC, TEST_DST, overwrite=False)
        
        # 3. 强制覆盖
        advanced_copy(TEST_SRC, TEST_DST, overwrite=True)
        
        # 4. 拷贝单个文件
        src_file = os.path.join(TEST_SRC, 'file1.txt')
        dst_file = os.path.join(TEST_DST, 'file1_copy.txt')
        advanced_copy(src_file, dst_file)
        
    finally:
        cleanup()
