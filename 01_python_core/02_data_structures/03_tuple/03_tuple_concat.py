"""
元组相加

对应文档: 03-data-structures.md § 3.4.3
"""

# 使用 + 运算符（创建新元组）
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(f"Concatenated (+): {result}")

# 使用 * 运算符（重复）
tuple1 = (1, 2, 3)
result = tuple1 * 3
print(f"Repeated (*): {result}")

# 拼接多个元组
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5, 6)
result = tuple1 + tuple2 + tuple3
print(f"Multiple concatenation: {result}")

# 注意：元组是不可变的，不能使用 append、extend 等方法
# 如果需要修改，只能创建新元组
