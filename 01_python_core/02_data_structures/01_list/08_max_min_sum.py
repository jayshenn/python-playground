"""
求列表中的最大值、最小值、求和

对应文档: 03-data-structures.md § 3.2.8
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Numbers: {numbers}")

# 最大值
print(f"Max: {max(numbers)}")

# 最小值
print(f"Min: {min(numbers)}")

# 求和
print(f"Sum: {sum(numbers)}")

# 平均值
average = sum(numbers) / len(numbers)
print(f"Average: {average:.2f}")

# 对字符串列表
fruits = ["苹果", "香蕉", "橙子"]
print(f"Fruits: {fruits}")
print(f"Max (string): {max(fruits)}")  # 按字典序
print(f"Min (string): {min(fruits)}")

# 自定义比较（使用 key 参数）
words = ["apple", "banana", "cherry", "date"]
print(f"Words: {words}")
print(f"Longest word: {max(words, key=len)}")
print(f"Shortest word: {min(words, key=len)}")

# 多维列表中的最大值
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 先求每行的最大值，再求这些最大值中的最大值
max_value = max(max(row) for row in matrix)
print(f"Max value in matrix: {max_value}")
