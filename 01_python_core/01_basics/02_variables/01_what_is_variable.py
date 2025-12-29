"""
什么是变量

对应文档: 01-python-basics.md § 1.2.1
"""

# 变量是用于存储数据的容器。在 Python 中，变量不需要提前声明类型，可以直接赋值使用。
# 变量就像一个标签，指向内存中的某个值

name = "Alice"
age = 25
height = 1.68

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
