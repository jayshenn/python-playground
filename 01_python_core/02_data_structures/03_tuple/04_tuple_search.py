"""
元组查找

对应文档: 03-data-structures.md § 3.4.4
"""

fruits = ("苹果", "香蕉", "橙子", "葡萄", "香蕉")
print(f"Fruits: {fruits}")

# in / not in
print(f"'苹果' in fruits: {'苹果' in fruits}")
print(f"'西瓜' in fruits: {'西瓜' in fruits}")

# index(): 返回元素第一次出现的索引
print(f"Index of '橙子': {fruits.index('橙子')}")
print(f"Index of '香蕉': {fruits.index('香蕉')}")

# 指定查找范围
# 从索引2开始查找
print(f"Index of '香蕉' (from index 2): {fruits.index('香蕉', 2)}")

# count(): 统计元素出现次数
print(f"Count of '香蕉': {fruits.count('香蕉')}")
print(f"Count of '西瓜': {fruits.count('西瓜')}")

# 查找不存在的元素会报错
try:
    print(fruits.index("西瓜"))
except ValueError:
    print("Error: '西瓜' not found")
