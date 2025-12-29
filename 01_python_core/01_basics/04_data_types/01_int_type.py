"""
int 整数型

对应文档: 01-python-basics.md § 1.4.1
"""

# 整数类型用于表示没有小数部分的数字。Python 3 中的整数没有大小限制。

# 整数
age = 25
negative = -10
big_number = 123456789012345678901234567890

print(f"Age: {age}, Type: {type(age)}")
print(f"Negative: {negative}")
print(f"Big Number: {big_number}")

# 不同进制的整数
binary = 0b1010  # 二进制
octal = 0o12  # 八进制
hexadecimal = 0xA  # 十六进制

print(f"Binary 0b1010: {binary}")
print(f"Octal 0o12: {octal}")
print(f"Hexadecimal 0xA: {hexadecimal}")
