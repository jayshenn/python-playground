"""
文件编码的最佳实践

对应文档: 05-file-operations.md § 5.3.5
"""

# 1. 始终显式指定编码
try:
    with open('file_enc.txt', 'w', encoding='utf-8') as f:
        f.write('你好')
    print("Wrote file with utf-8")
except IOError as e:
    print(f"Error writing: {e}")

# 2. 读取时使用相同的编码
try:
    with open('file_enc.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Read file: {content}")
except IOError as e:
    print(f"Error reading: {e}")

# 3. 处理未知编码的文件
def detect_encoding(file_path):
    """尝试不同编码读取文件（简单示例）"""
    encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except (UnicodeDecodeError, LookupError):
            continue
        except IOError:
            return None
    return None

detected = detect_encoding('file_enc.txt')
print(f"Detected encoding: {detected}")

# 清理
import os
try:
    os.remove('file_enc.txt')
except OSError:
    pass
