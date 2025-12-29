"""
逗号(,)编码

对应文档: 01-python-basics.md § 1.7.6
"""

# 在使用逗号时，应该注意格式。通常逗号后面加一个空格。

# 函数参数
def example(a, b, c):
    pass

# 列表、元组等
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)

# 多行时，最后一项可以加逗号（推荐）
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing',  # 最后一项也加逗号，方便以后添加新项
}

# 函数调用
def some_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

arg1 = "a"
arg2 = "b"
arg3 = "c"

result = some_function(
    arg1,
    arg2,
    arg3,  # 最后一项也可以加逗号
)
