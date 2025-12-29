"""
列表查找

对应文档: 03-data-structures.md § 3.2.5
"""

fruits = ["苹果", "香蕉", "橙子", "葡萄", "香蕉"]
print(f"Fruits: {fruits}")

# in / not in: 检查元素是否存在
print(f"'苹果' in fruits: {'苹果' in fruits}")
print(f"'西瓜' in fruits: {'西瓜' in fruits}")
print(f"'西瓜' not in fruits: {'西瓜' not in fruits}")

# index(): 返回元素第一次出现的索引
print(f"Index of '橙子': {fruits.index('橙子')}")
print(f"Index of '香蕉': {fruits.index('香蕉')}")  # 第一个香蕉

# 如果元素不存在会报错
try:
    print(fruits.index("西瓜"))
except ValueError:
    print("Error: '西瓜' not found in list")

# 指定查找范围
# 从索引 2 开始查找 '香蕉'
index = fruits.index("香蕉", 2)
print(f"Index of '香蕉' (searching from index 2): {index}")

# count(): 统计元素出现的次数
print(f"Count of '香蕉': {fruits.count('香蕉')}")
print(f"Count of '苹果': {fruits.count('苹果')}")
print(f"Count of '西瓜': {fruits.count('西瓜')}")
