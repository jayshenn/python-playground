"""
参数的描述

对应文档: 04-functions.md § 4.5.1
"""

# 参数是函数的输入，分为形式参数（形参）和实际参数（实参）。

def greet(name):  # name 是形参 (formal parameter)
    return f"Hello, {name}!"

# "Alice" 是实参 (actual argument)
message = greet("Alice")
print(message)
