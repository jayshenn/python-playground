"""
十进制转换成十六进制

对应文档: 01-python-basics.md § 1.3.6
"""

# 十进制转十六进制：使用"除16取余法"，类似于转二进制。

# 使用内置函数
decimal = 255
hex_str = hex(decimal)

print(f"Decimal: {decimal}")
print(f"hex({decimal}) = {hex_str}")  # 输出: 0xff
print(f"Hex string: {hex_str[2:]}")  # 去掉 0x 前缀，输出: ff
