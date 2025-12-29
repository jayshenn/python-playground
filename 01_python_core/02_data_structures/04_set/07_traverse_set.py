"""
遍历集合

对应文档: 03-data-structures.md § 3.5.7
"""

fruits = {"苹果", "香蕉", "橙子", "葡萄"}

print("--- Direct iteration ---")
# 直接遍历（顺序不确定）
for fruit in fruits:
    print(fruit)

print("\n--- Sorted iteration ---")
# 转换为列表后遍历（可以排序）
for fruit in sorted(fruits):
    print(fruit)

print("\n--- Enumerate ---")
# 使用 enumerate()（顺序不确定）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

print("\n--- Set comprehension ---")
# 集合推导式
numbers = {1, 2, 3, 4, 5}
squares = {x**2 for x in numbers}
print(f"Squares: {squares}")
