"""
带进度显示的文件拷贝

对应文档: 05-file-operations.md § 5.8.4
"""

import os
import time

SOURCE_FILE = 'progress_source.bin'
DEST_FILE = 'progress_dest.bin'

def setup_file():
    print("Creating file for progress demo...")
    with open(SOURCE_FILE, 'wb') as f:
        # 10 MB
        f.write(os.urandom(10 * 1024 * 1024))

def copy_file_with_progress(source, destination, chunk_size=1024*1024):
    """
    带进度显示的文件拷贝
    """
    try:
        file_size = os.path.getsize(source)
        copied_size = 0
        
        print(f"Copying {source} ({file_size} bytes)...")

        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break

                    dst.write(chunk)
                    copied_size += len(chunk)
                    
                    # 模拟慢速拷贝以便观察进度
                    # time.sleep(0.1) 

                    # 计算进度
                    progress = (copied_size / file_size) * 100
                    print(f"\rProgress: {progress:5.1f}% [{copied_size}/{file_size}]", end='')

        print(f"\nCopy complete: {destination}")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == '__main__':
    setup_file()
    try:
        # chunk size 512KB
        copy_file_with_progress(SOURCE_FILE, DEST_FILE, chunk_size=512*1024)
    finally:
        if os.path.exists(SOURCE_FILE):
            os.remove(SOURCE_FILE)
        if os.path.exists(DEST_FILE):
            os.remove(DEST_FILE)
