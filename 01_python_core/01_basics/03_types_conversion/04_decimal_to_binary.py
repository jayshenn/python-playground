"""
十进制转换成二进制

对应文档: 01-python-basics.md § 1.3.4
"""

# 十进制转二进制：使用"除2取余法"，将十进制数不断除以 2，取余数，直到商为 0。

# 使用内置函数
decimal = 10
binary_str = bin(decimal)

print(f"Decimal: {decimal}")
print(f"bin({decimal}) = {binary_str}")  # 输出: 0b1010
print(f"Binary string: {binary_str[2:]}")  # 去掉 0b 前缀，输出: 1010
