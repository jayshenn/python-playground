"""
行长

对应文档: 01-python-basics.md § 1.7.2
"""

# 每行代码不应该超过 79 个字符（PEP 8 规范）。

# 过长的行应该折行
long_string = (
    "这是一个很长的字符串，"
    "为了保持代码的可读性，"
    "我们将它分成多行"
)

print(long_string)

# 函数调用可以这样折行
def some_function(arg1, arg2, arg3):
    print(f"Args: {arg1}, {arg2}, {arg3}")

some_function(
    "argument1",
    "argument2",
    "argument3"
)

# 列表、字典等也可以折行
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
print(my_list)
