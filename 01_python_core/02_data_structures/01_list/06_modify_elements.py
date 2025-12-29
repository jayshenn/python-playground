"""
修改列表中的元素

对应文档: 03-data-structures.md § 3.2.6
"""

fruits = ["苹果", "香蕉", "橙子"]
print(f"Original: {fruits}")

# 通过索引修改单个元素
fruits[1] = "葡萄"
print(f"Modified index 1: {fruits}")

# 通过切片修改多个元素
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

numbers[1:4] = [20, 30, 40]
print(f"Modified slice [1:4]: {numbers}")

# 通过切片替换为不同数量的元素
numbers[1:4] = [100, 200]
print(f"Replaced slice with fewer elements: {numbers}")

# 修改嵌套列表中的元素
matrix = [[1, 2], [3, 4], [5, 6]]
print(f"Matrix: {matrix}")

matrix[1][0] = 30
print(f"Modified matrix[1][0]: {matrix}")
