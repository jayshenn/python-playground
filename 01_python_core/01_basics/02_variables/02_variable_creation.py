"""
变量的创建

对应文档: 01-python-basics.md § 1.2.2
"""

# 创建变量：使用赋值运算符 = 即可
x = 10  # 整数
y = 3.14  # 浮点数
name = "Bob"  # 字符串
is_valid = True  # 布尔值

print(f"x: {x}, y: {y}, name: {name}, is_valid: {is_valid}")

# 多重赋值
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

x = y = z = 0
print(f"x: {x}, y: {y}, z: {z}")
