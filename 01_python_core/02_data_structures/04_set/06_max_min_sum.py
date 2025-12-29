"""
求集合中的最大值、最小值、加和

对应文档: 03-data-structures.md § 3.5.6
"""

numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5}
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

# 对字符串集合
fruits = {"苹果", "香蕉", "橙子"}
print(f"Fruits: {fruits}")
print(f"Max (string): {max(fruits)}")
print(f"Min (string): {min(fruits)}")
