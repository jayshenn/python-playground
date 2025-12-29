"""
创建集合

对应文档: 03-data-structures.md § 3.5.1
"""

# 使用花括号
numbers = {1, 2, 3, 4, 5}
fruits = {"苹果", "香蕉", "橙子"}

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")

# 空集合（必须使用 set()）
empty_set = set()  # 正确
empty_dict = {}  # 这是空字典，不是空集合
print(f"Empty set type: {type(empty_set)}")
print(f"Empty dict type: {type(empty_dict)}")

# 使用 set() 构造函数
list_data = [1, 2, 3, 2, 1]  # 有重复元素
set_data = set(list_data)
print(f"From list (unique): {set_data}")

string_set = set("Hello")
print(f"From string: {string_set}")

# 集合推导式
squares = {x**2 for x in range(1, 6)}
print(f"Set comprehension: {squares}")

# 注意：集合是无序的
fruits = {"苹果", "香蕉", "橙子"}
print(f"Unordered set: {fruits}")
