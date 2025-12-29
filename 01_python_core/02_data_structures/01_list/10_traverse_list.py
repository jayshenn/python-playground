"""
遍历列表

对应文档: 03-data-structures.md § 3.2.10
"""

fruits = ["苹果", "香蕉", "橙子", "葡萄"]

print("--- Direct iteration ---")
# 方法1: 直接遍历元素
for fruit in fruits:
    print(fruit)

print("\n--- Iteration by index ---")
# 方法2: 通过索引遍历
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print("\n--- Enumerate ---")
# 方法3: 使用 enumerate()（推荐）
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n--- Enumerate start=1 ---")
# enumerate() 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

print("\n--- Zip iteration ---")
# 遍历多个列表（zip）
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- Nested list iteration ---")
# 遍历嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # 换行

print("\n--- List comprehension ---")
# 使用列表推导式处理
doubled = [x * 2 for x in [1, 2, 3, 4, 5]]
print(doubled)
