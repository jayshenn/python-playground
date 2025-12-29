"""
解包传参

对应文档: 04-functions.md § 4.5.5
"""

# 使用 * 和 ** 可以解包序列和字典作为参数。

# 解包列表/元组
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(f"Unpacking list: {add(*numbers)}")  # 等价于 add(1, 2, 3)

# 解包字典
def greet(name, age):
    return f"{name} is {age} years old"

person = {"name": "Alice", "age": 25}
print(f"Unpacking dict: {greet(**person)}")

# 混合使用
def func(a, b, c, d):
    return a + b + c + d

args = [1, 2]
kwargs = {"c": 3, "d": 4}
print(f"Mixed unpacking: {func(*args, **kwargs)}")
