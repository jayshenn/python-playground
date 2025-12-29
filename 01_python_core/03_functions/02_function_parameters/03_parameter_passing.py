"""
函数的参数传递

对应文档: 04-functions.md § 4.5.3
"""

# Python 中参数传递是传递对象引用（类似于"传引用"）。

# 不可变对象（整数、字符串、元组）：类似"传值"
def modify_number(x):
    x = 100  # 修改局部变量，不影响外部
    print(f"Inside function (number): {x}")

num = 10
print(f"Before function (number): {num}")
modify_number(num)
print(f"After function (number): {num}")  # 10（未改变）

# 可变对象（列表、字典、集合）：类似"传引用"
def modify_list(lst):
    lst.append(4)  # 修改列表内容，影响外部
    print(f"Inside function (list): {lst}")

numbers = [1, 2, 3]
print(f"\nBefore function (list): {numbers}")
modify_list(numbers)
print(f"After function (list): {numbers}")  # [1, 2, 3, 4]（已改变）

# 重新赋值不影响外部
def reassign_list(lst):
    lst = [100, 200]  # 重新赋值，不影响外部
    print(f"Inside function (reassign): {lst}")

numbers2 = [1, 2, 3]
print(f"\nBefore function (reassign): {numbers2}")
reassign_list(numbers2)
print(f"After function (reassign): {numbers2}")  # [1, 2, 3]（未改变）
