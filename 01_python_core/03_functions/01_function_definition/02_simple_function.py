"""
定义一个简单的函数

对应文档: 04-functions.md § 4.2.2
"""

# 无参数、无返回值
def say_hello():
    print("Hello, World!")

print("Calling say_hello:")
say_hello()

# 有参数、无返回值
def greet(name):
    print(f"Hello, {name}!")

print("\nCalling greet:")
greet("Alice")

# 有参数、有返回值
def add(a, b):
    return a + b

print("\nCalling add:")
result = add(3, 5)
print(f"3 + 5 = {result}")

# 无参数、有返回值
def get_pi():
    return 3.14159

print("\nCalling get_pi:")
pi = get_pi()
print(f"Pi is {pi}")
