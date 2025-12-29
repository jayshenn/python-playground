"""
修改字典中的元素

对应文档: 03-data-structures.md § 3.6.4
"""

person = {"name": "Alice", "age": 25, "city": "北京"}
print(f"Original: {person}")

# 直接通过键修改
person["age"] = 26
print(f"Modified age: {person}")

# 使用 update() 修改
person.update({"age": 27, "city": "上海"})
print(f"Updated age and city: {person}")

# 修改嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25}
}
users["user1"]["age"] = 26
print(f"Modified nested user1 age: {users}")

# 如果键不存在，直接赋值会创建新键值对
person["email"] = "alice@example.com"
print(f"Added email by assignment: {person}")
