"""
身份运算符

对应文档: 01-python-basics.md § 1.6.7
"""

# 用于比较两个对象的内存地址是否相同。
# is：两个对象是否相同（内存地址相同）
# is not：两个对象是否不同

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"c = {c}, id(c) = {id(c)}")

print(f"a == b: {a == b}")   # True（值相等）
print(f"a is b: {a is b}")   # False（不是同一个对象）
print(f"a is c: {a is c}")   # True（是同一个对象）

# 特殊情况：小整数和短字符串会被缓存
x = 10
y = 10
print(f"x = {x}, y = {y}")
print(f"x is y: {x is y}")  # True

# 与 None 比较时，应该使用 is
value = None
if value is None:
    print("value 是 None")
