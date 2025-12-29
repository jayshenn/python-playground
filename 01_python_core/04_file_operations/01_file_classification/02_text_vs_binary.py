"""
文本文件与二进制文件的区别

对应文档: 05-file-operations.md § 5.2.2
"""

# 对比示例

# 文本模式 ('w')
# 需要指定编码，写入字符串
try:
    with open('text_mode.txt', 'w', encoding='utf-8') as f:
        f.write('Hello')  # 写入字符串
    print("Created text_mode.txt")
except IOError as e:
    print(f"Error in text mode: {e}")

# 二进制模式 ('wb')
# 不需要指定编码，写入字节 (bytes)
try:
    with open('binary_mode.bin', 'wb') as f:
        f.write(b('Hello', encoding='utf-8'))  # 写入字节（注意 b 前缀或 encode）
        # 或者直接写 b'Hello' 如果是 ASCII
    print("Created binary_mode.bin")
except IOError as e:
    print(f"Error in binary mode: {e}")

# 清理
import os
try:
    if os.path.exists('text_mode.txt'):
        os.remove('text_mode.txt')
    if os.path.exists('binary_mode.bin'):
        os.remove('binary_mode.bin')
    print("Cleaned up files")
except OSError as e:
    print(f"Error cleaning up: {e}")
