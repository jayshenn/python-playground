"""
创建列表

对应文档: 03-data-structures.md § 3.2.1
"""

# 空列表
empty_list = []
empty_list2 = list()

# 包含元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "hello", 3.14, True]  # 混合类型

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# 使用 list() 构造函数
chars = list("Python")
range_list = list(range(5))

print(f"Chars from 'Python': {chars}")
print(f"Range list: {range_list}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Evens: {evens}")

# 嵌套列表（二维列表）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)
