"""
获取集合长度

对应文档: 03-data-structures.md § 3.5.5
"""

fruits = {"苹果", "香蕉", "橙子", "葡萄"}

# len(): 获取集合长度
print(f"Length of fruits: {len(fruits)}")

# 空集合
empty = set()
print(f"Length of empty set: {len(empty)}")

# 集合自动去重
numbers = {1, 2, 3, 2, 1}
print(f"Original numbers with duplicates: {{1, 2, 3, 2, 1}}")
print(f"Actual set: {numbers}")
print(f"Length of numbers: {len(numbers)}")
