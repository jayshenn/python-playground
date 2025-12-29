"""
算术运算符

对应文档: 01-python-basics.md § 1.6.1
"""

# 用于执行基本的数学运算。

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # 加法: 13
print(f"a - b = {a - b}")   # 减法: 7
print(f"a * b = {a * b}")   # 乘法: 30
print(f"a / b = {a / b}")   # 除法: 3.3333...
print(f"a // b = {a // b}")  # 整除: 3
print(f"a % b = {a % b}")   # 取余: 1
print(f"a ** b = {a ** b}")  # 幂运算: 1000

# 复合赋值运算符
x = 10
print(f"Initial x: {x}")
x += 5   # 等价于 x = x + 5
print(f"x += 5 -> {x}")
x -= 3   # 等价于 x = x - 3
print(f"x -= 3 -> {x}")
x *= 2   # 等价于 x = x * 2
print(f"x *= 2 -> {x}")
x /= 4   # 等价于 x = x / 4
print(f"x /= 4 -> {x}")
