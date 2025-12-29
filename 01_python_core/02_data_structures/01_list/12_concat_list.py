"""
拼接列表

对应文档: 03-data-structures.md § 3.2.12
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List1: {list1}, List2: {list2}")

# 方法1: 使用 + 运算符（创建新列表）
result = list1 + list2
print(f"Using + operator: {result}")

# 方法2: 使用 extend()（原地修改）
list1_copy = list1.copy()
list1_copy.extend(list2)
print(f"Using extend(): {list1_copy}")

# 方法3: 使用 += 运算符（原地修改）
list1_copy = list1.copy()
list1_copy += list2
print(f"Using += operator: {list1_copy}")

# 方法4: 使用 * 运算符拆包
result = [*list1, *list2]
print(f"Using unpacking (*): {result}")

# 拼接多个列表
list3 = [7, 8, 9]
result = list1 + list2 + list3
print(f"Concatenating multiple lists: {result}")

# 使用列表推导式flatten列表
lists = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in lists for item in sublist]
print(f"Flattened list: {flattened}")
