"""
八进制转换成十进制

对应文档: 01-python-basics.md § 1.3.5
"""

# 八进制转十进制：将每一位上的数字乘以 8 的相应次幂，然后求和。
# 例如：52 (八进制) = 5×8¹ + 2×8⁰ = 40 + 2 = 42 (十进制)

# 使用内置函数转换
octal_str = "52"
decimal_value = int(octal_str, 8)

print(f"Octal string: {octal_str}")
print(f"int('{octal_str}', 8) = {decimal_value}")  # 输出: 42
