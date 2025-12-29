"""
集合运算

对应文档: 03-data-structures.md § 3.5.8
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set1: {set1}")
print(f"Set2: {set2}")

# 并集（所有元素）
print(f"Union (|): {set1 | set2}")
print(f"Union (method): {set1.union(set2)}")

# 交集（共同元素）
print(f"Intersection (&): {set1 & set2}")
print(f"Intersection (method): {set1.intersection(set2)}")

# 差集（在 set1 但不在 set2 中）
print(f"Difference (-): {set1 - set2}")
print(f"Difference (method): {set1.difference(set2)}")

# 对称差集（不同时在两个集合中）
print(f"Symmetric Difference (^): {set1 ^ set2}")
print(f"Symmetric Difference (method): {set1.symmetric_difference(set2)}")

# 实际应用：去重
list_data = [1, 2, 3, 2, 1, 4, 5, 4]
unique = list(set(list_data))
print(f"Unique elements from list: {unique}")

# 找出两个列表的共同元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements between lists: {common}")

# 找出只在第一个列表中的元素
only_in_list1 = list(set(list1) - set(list2))
print(f"Elements only in list1: {only_in_list1}")
