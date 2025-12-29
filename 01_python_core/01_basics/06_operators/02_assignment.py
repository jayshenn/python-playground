"""
赋值运算符

对应文档: 01-python-basics.md § 1.6.2
"""

# 用于给变量赋值。

# 简单赋值
x = 10
print(f"x = {x}")

# 复合赋值
x += 5   # x = x + 5
print(f"x += 5 -> {x}")

x -= 3   # x = x - 3
print(f"x -= 3 -> {x}")

x *= 2   # x = x * 2
print(f"x *= 2 -> {x}")

x /= 4   # x = x / 4
print(f"x /= 4 -> {x}")

x //= 2  # x = x // 2
print(f"x //= 2 -> {x}")

x %= 3   # x = x % 3
print(f"x %= 3 -> {x}")

x **= 2  # x = x ** 2
print(f"x **= 2 -> {x}")

# 多重赋值
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 交换变量
print(f"Before swap: a={a}, x={x}")
a, x = x, a
print(f"After swap: a={a}, x={x}")
