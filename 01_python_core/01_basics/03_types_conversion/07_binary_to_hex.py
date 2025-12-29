"""
二进制转换成十六进制

对应文档: 01-python-basics.md § 1.3.7
"""

# 二进制转十六进制：可以先转为十进制，再转为十六进制。或者将二进制数每 4 位分组，直接转换。

# 方法1：通过十进制中转
binary_str = "11111111"
decimal = int(binary_str, 2)
hex_str = hex(decimal)
print(f"Binary '{binary_str}' -> Decimal {decimal} -> Hex {hex_str}")  # 输出: 0xff

# 方法2：直接使用格式化
binary_value = 0b11111111
print(f"Formatted hex: {binary_value:x}")  # 输出: ff
