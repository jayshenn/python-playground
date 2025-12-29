"""
逻辑运算符

对应文档: 01-python-basics.md § 1.6.4
"""

# 用于组合多个条件判断。

# and（与）：所有条件都为 True 时返回 True
print(f"True and True: {True and True}")    # True
print(f"True and False: {True and False}")   # False

# or（或）：至少一个条件为 True 时返回 True
print(f"True or False: {True or False}")    # True
print(f"False or False: {False or False}")   # False

# not（非）：取反
print(f"not True: {not True}")   # False
print(f"not False: {not False}")  # True

# 实际应用
age = 25
is_student = True
if age >= 18 and is_student:
    print("成年学生")

# 短路运算
x = 0
y = 10
# x == 0，不会执行 y / x，因此不会报错
result = x != 0 and y / x
print(f"Short-circuit result: {result}")
