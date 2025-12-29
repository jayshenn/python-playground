"""
最佳实践：显式指定编码

对应文档: 05-file-operations.md § 5.9.2
"""

import os
import locale

FILENAME = 'practice_encoding.txt'

def bad_practice():
    """反例：不指定编码（依赖系统默认）"""
    print("\n--- Bad Practice ---")
    print(f"System default encoding: {locale.getpreferredencoding()}")
    
    # 在某些系统（如 Windows）默认可能是 GBK 或 cp1252
    # 这会导致跨平台问题
    with open(FILENAME, 'w') as f:
        f.write('你好，世界')
        print(f"File opened with default encoding: {f.encoding}")

def good_practice():
    """正例：显式指定 encoding='utf-8'"""
    print("\n--- Good Practice ---")
    
    # 始终明确指定 utf-8，确保跨平台一致性
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('你好，世界')
        print(f"File opened with explicit encoding: {f.encoding}")

if __name__ == '__main__':
    bad_practice()
    good_practice()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
