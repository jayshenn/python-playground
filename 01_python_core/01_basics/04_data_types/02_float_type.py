"""
float 浮点型

对应文档: 01-python-basics.md § 1.4.2
"""

# 浮点型用于表示带有小数部分的数字。

# 浮点数
pi = 3.14159
height = 1.75
temperature = -5.5

print(f"Pi: {pi}, Type: {type(pi)}")
print(f"Height: {height}")
print(f"Temperature: {temperature}")

# 科学计数法
large = 1.5e10  # 1.5 × 10^10
small = 2.5e-5  # 2.5 × 10^-5

print(f"Large (1.5e10): {large}")
print(f"Small (2.5e-5): {small:.6f}")

# 浮点数精度问题
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")  # 0.30000000000000004
