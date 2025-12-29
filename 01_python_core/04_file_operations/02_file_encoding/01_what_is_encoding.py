"""
什么是编码

对应文档: 05-file-operations.md § 5.3.1
"""

# 编码是将字符转换为字节序列的过程。
# 计算机只能处理二进制数据，所以需要将字符编码为字节。

# 编码过程：
# 字符 → (编码) → 字节 → 存储到文件
# 文件 → (解码) → 字节 → 字符

char = 'A'
print(f"Character: {char}")
print(f"Code point: {ord(char)}")
print(f"Binary: {bin(ord(char))}")
