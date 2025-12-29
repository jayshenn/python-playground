"""
遍历元组

对应文档: 03-data-structures.md § 3.4.8
"""

fruits = ("苹果", "香蕉", "橙子", "葡萄")

print("--- Direct iteration ---")
# 直接遍历元素
for fruit in fruits:
    print(fruit)

print("\n--- Iteration by index ---")
# 通过索引遍历
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print("\n--- Enumerate ---")
# 使用 enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n--- Zip iteration ---")
# 遍历多个元组（zip）
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)

for name, age in zip(names, ages):
    print(f"{name}: {age}")

print("\n--- Nested iteration ---")
# 嵌套元组遍历
nested = ((1, 2), (3, 4), (5, 6))
for sub_tuple in nested:
    for item in sub_tuple:
        print(item, end=" ")
    print()
