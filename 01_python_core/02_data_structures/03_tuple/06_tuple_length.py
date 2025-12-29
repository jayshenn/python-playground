"""
获取元组长度

对应文档: 03-data-structures.md § 3.4.6
"""

fruits = ("苹果", "香蕉", "橙子", "葡萄")

# len(): 获取元组长度
print(f"Length of fruits: {len(fruits)}")

# 空元组
empty = ()
print(f"Length of empty tuple: {len(empty)}")

# 单元素元组
single = (42,)
print(f"Length of single tuple: {len(single)}")

# 嵌套元组
nested = ((1, 2), (3, 4), (5, 6))
print(f"Length of nested tuple: {len(nested)}")
print(f"Length of nested[0]: {len(nested[0])}")
