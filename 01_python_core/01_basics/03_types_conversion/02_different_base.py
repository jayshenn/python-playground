"""
不同进制表示数字

对应文档: 01-python-basics.md § 1.3.2
"""

# 在 Python 中，可以使用不同的前缀来表示不同进制的数字。

# 十进制
decimal = 42
print(f"Decimal: {decimal}")

# 二进制（0b 或 0B 前缀）
binary = 0b101010
print(f"Binary (0b101010): {binary}")  # 输出: 42

# 八进制（0o 或 0O 前缀）
octal = 0o52
print(f"Octal (0o52): {octal}")  # 输出: 42

# 十六进制（0x 或 0X 前缀）
hexadecimal = 0x2A
print(f"Hexadecimal (0x2A): {hexadecimal}")  # 输出: 42
