"""
形参和实参

对应文档: 04-functions.md § 4.5.2
"""

# 形参：定义时的参数
def add(a, b):  # a, b 是形参
    return a + b

# 实参：调用时的参数
result = add(3, 5)  # 3, 5 是实参
print(f"Result: {result}")

# 形参只在函数内部有效
def multiply(x, y):
    return x * y

# print(x)  # NameError: x 未定义（x 只在函数内有效）

# 实参可以是任何表达式
num1 = 10
num2 = 20
print(f"Variables as args: {add(num1, num2)}")  # 变量作为实参
print(f"Expressions as args: {add(2 + 3, 4 * 5)}")  # 表达式作为实参
