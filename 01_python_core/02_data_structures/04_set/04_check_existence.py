"""
检查某值是否在集合中存在

对应文档: 03-data-structures.md § 3.5.4
"""

fruits = {"苹果", "香蕉", "橙子"}
print(f"Fruits: {fruits}")

# 使用 in / not in
print(f"'苹果' in fruits: {'苹果' in fruits}")
print(f"'西瓜' in fruits: {'西瓜' in fruits}")

# 结合条件判断
if "香蕉" in fruits:
    print("香蕉在集合中")

# 检查子集
set1 = {1, 2, 3}
set2 = {1, 2}
print(f"Set1: {set1}, Set2: {set2}")
print(f"set2.issubset(set1): {set2.issubset(set1)}")
print(f"set1.issuperset(set2): {set1.issuperset(set2)}")

# 检查是否有交集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set1: {set1}, Set2: {set2}")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")  # False（有交集）

set3 = {6, 7, 8}
print(f"Set3: {set3}")
print(f"set1.isdisjoint(set3): {set1.isdisjoint(set3)}")  # True（无交集）
