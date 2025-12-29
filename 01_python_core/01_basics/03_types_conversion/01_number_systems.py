"""
进制

对应文档: 01-python-basics.md § 1.3.1
"""

# 计算机中常用的进制系统：
# - 二进制（Binary）：基数为 2，使用 0 和 1
# - 八进制（Octal）：基数为 8，使用 0-7
# - 十进制（Decimal）：基数为 10，使用 0-9
# - 十六进制（Hexadecimal）：基数为 16，使用 0-9 和 A-F

# 在 Python 中，不同进制的整数在打印时默认显示为十进制
binary_num = 0b1010
octal_num = 0o12
hex_num = 0xA

print(f"二进制 0b1010: {binary_num}")
print(f"八进制 0o12: {octal_num}")
print(f"十六进制 0xA: {hex_num}")
