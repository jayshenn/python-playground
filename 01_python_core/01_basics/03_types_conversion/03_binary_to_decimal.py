"""
二进制转换成十进制

对应文档: 01-python-basics.md § 1.3.3
"""

# 二进制转十进制：将每一位上的数字乘以 2 的相应次幂，然后求和。
# 例如：1010 (二进制) = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = 10 (十进制)

# 使用内置函数转换
binary_str = "1010"
decimal_value = int(binary_str, 2)
print(f"int('{binary_str}', 2) = {decimal_value}")  # 输出: 10

# 手动计算
result = 1 * 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0
print(f"Manual calculation: {result}")  # 输出: 10
