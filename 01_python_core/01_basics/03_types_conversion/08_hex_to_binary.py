"""
十六进制转换成二进制

对应文档: 01-python-basics.md § 1.3.8
"""

# 十六进制转二进制：每个十六进制位对应 4 个二进制位。

# 使用内置函数
hex_str = "FF"
decimal = int(hex_str, 16)
binary_str = bin(decimal)

print(f"Hex string: {hex_str}")
print(f"Decimal: {decimal}")
print(f"Binary string: {binary_str}")  # 输出: 0b11111111
