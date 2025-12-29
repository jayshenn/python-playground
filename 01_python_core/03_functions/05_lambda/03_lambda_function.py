"""
使用匿名函数替代参数

对应文档: 04-functions.md § 4.11.3
"""

# 匿名函数
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

# 使用匿名函数作为参数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared list (using lambda): {squared}")

# 常见应用场景
# 1. 排序
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"Sorted students: {sorted_students}")

# 2. 过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# 3. 映射
words = ["hello", "world", "python"]
upper_words = list(map(lambda s: s.upper(), words))
print(f"Upper words: {upper_words}")
