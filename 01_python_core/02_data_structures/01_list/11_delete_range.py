"""
删除列表中指定位置范围元素或者全部删除

对应文档: 03-data-structures.md § 3.2.11
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")

# 删除指定范围（使用切片 + del）
del numbers[2:5]  # 删除索引 2-4 的元素
print(f"After del numbers[2:5]: {numbers}")

# 使用切片赋值为空列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = []
print(f"After numbers[2:5] = []: {numbers}")

# 删除从开头到指定位置
numbers = [1, 2, 3, 4, 5]
del numbers[:2]
print(f"After del numbers[:2]: {numbers}")

# 删除从指定位置到末尾
numbers = [1, 2, 3, 4, 5]
del numbers[2:]
print(f"After del numbers[2:]: {numbers}")

# 清空整个列表
numbers.clear()  # 方法1
print(f"After clear(): {numbers}")

numbers = [1, 2, 3, 4, 5]
del numbers[:]  # 方法2
print(f"After del numbers[:]: {numbers}")

numbers = [1, 2, 3, 4, 5]
numbers = []  # 方法3（创建新列表）
print(f"After numbers = []: {numbers}")
