"""
创建字典

对应文档: 03-data-structures.md § 3.6.1
"""

# 空字典
empty_dict = {}
empty_dict2 = dict()
print(f"Empty dict: {empty_dict}")

# 包含元素的字典
person = {
    "name": "Alice",
    "age": 25,
    "city": "北京"
}
print(f"Person: {person}")

# 使用 dict() 构造函数
person_kw = dict(name="Alice", age=25, city="北京")
print(f"Person (kwargs): {person_kw}")

# 从元组列表创建
pairs = [("name", "Alice"), ("age", 25)]
person_pairs = dict(pairs)
print(f"Person (pairs): {person_pairs}")

# 使用 zip() 创建
keys = ["name", "age", "city"]
values = ["Alice", 25, "北京"]
person_zip = dict(zip(keys, values))
print(f"Person (zip): {person_zip}")

# 字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# 使用 fromkeys() 创建（所有键共享同一个值）
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"Default dict: {default_dict}")

# 嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(f"Nested users: {users}")
