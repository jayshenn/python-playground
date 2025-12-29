"""
比较运算符

对应文档: 01-python-basics.md § 1.6.3
"""

# 用于比较两个值，返回布尔值。

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # 等于: False
print(f"a != b: {a != b}")  # 不等于: True
print(f"a > b: {a > b}")   # 大于: True
print(f"a < b: {a < b}")   # 小于: False
print(f"a >= b: {a >= b}")  # 大于等于: True
print(f"a <= b: {a <= b}")  # 小于等于: False

# 链式比较
x = 5
print(f"x = {x}")
print(f"1 < x < 10: {1 < x < 10}")  # True
print(f"0 <= x <= 100: {0 <= x <= 100}")  # True
