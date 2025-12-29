"""
向集合中添加元素

对应文档: 03-data-structures.md § 3.5.2
"""

fruits = {"苹果", "香蕉"}
print(f"Original: {fruits}")

# add(): 添加单个元素
fruits.add("橙子")
print(f"After add('橙子'): {fruits}")

# 添加已存在的元素（无效果）
fruits.add("苹果")
print(f"After adding existing '苹果': {fruits}")

# update(): 添加多个元素
fruits.update(["葡萄", "西瓜"])
print(f"After update(['葡萄', '西瓜']): {fruits}")

# update() 可以接受多个可迭代对象
fruits.update(["草莓"], {"芒果"})
print(f"After update multiple iterables: {fruits}")

# 使用 | 运算符（创建新集合）
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(f"Union using |: {result}")
