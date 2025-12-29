"""
基本文本文件拷贝

对应文档: 05-file-operations.md § 5.8.1
"""

import os

SOURCE_FILE = 'source_text.txt'
DEST_FILE = 'dest_text.txt'

def setup_file():
    with open(SOURCE_FILE, 'w', encoding='utf-8') as f:
        f.write('This is the content of the source file.\n')
        f.write('Here is another line.\n')

def copy_text_file(source, destination):
    """
    拷贝文本文件
    """
    print(f"Copying {source} to {destination}...")
    
    try:
        with open(source, 'r', encoding='utf-8') as src:
            content = src.read()
            
        with open(destination, 'w', encoding='utf-8') as dst:
            dst.write(content)
            
        print("Copy successful.")
        
        # 验证
        with open(destination, 'r', encoding='utf-8') as f:
            print("Destination content:")
            print(f.read().strip())
            
    except FileNotFoundError:
        print(f"Error: {source} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    setup_file()
    try:
        copy_text_file(SOURCE_FILE, DEST_FILE)
    finally:
        if os.path.exists(SOURCE_FILE):
            os.remove(SOURCE_FILE)
        if os.path.exists(DEST_FILE):
            os.remove(DEST_FILE)
