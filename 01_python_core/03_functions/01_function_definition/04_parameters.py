"""
参数

对应文档: 04-functions.md § 4.2.4
"""

# 参数是函数接收的输入值。

# 单个参数
def square(x):
    return x ** 2

print(f"square(5): {square(5)}")

# 多个参数
def add(a, b):
    return a + b

print(f"add(3, 5): {add(3, 5)}")

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(f"greet('Alice'): {greet('Alice')}")
print(f"greet('Bob', 'Hi'): {greet('Bob', 'Hi')}")

# 可变数量参数
def sum_all(*numbers):
    return sum(numbers)

print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")
