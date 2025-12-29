"""
列表推导式

对应文档: 03-data-structures.md § 3.2.13
"""

# 基本用法：生成平方数
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# 带条件：生成偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Evens: {evens}")

# 处理字符串
words = ["Hello", "World", "Python"]
upper_words = [word.upper() for word in words]
print(f"Upper words: {upper_words}")

# 条件表达式
numbers = [1, 2, 3, 4, 5]
labels = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
print(f"Labels: {labels}")

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"Flattened matrix: {flattened}")

# 二维列表（矩阵转置）
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Transposed matrix: {transposed}")

# 过滤和转换
strings = ["1", "hello", "2", "world", "3"]
numbers = [int(s) for s in strings if s.isdigit()]
print(f"Numbers from strings: {numbers}")

# 生成坐标对
coords = [(x, y) for x in range(2) for y in range(2)]
print(f"Coordinates: {coords}")
