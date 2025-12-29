"""
访问字典

对应文档: 03-data-structures.md § 3.6.2
"""

person = {"name": "Alice", "age": 25, "city": "北京"}
print(f"Person: {person}")

# 通过键访问值
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# 键不存在会报错
try:
    print(person["email"])
except KeyError:
    print("Error: Key 'email' not found")

# 使用 get() 方法（推荐）
print(f"Name (get): {person.get('name')}")
print(f"Email (get): {person.get('email')}")  # None
print(f"Email (get default): {person.get('email', '未提供')}")

# 访问嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(f"User1 Name: {users['user1']['name']}")

# 获取所有键
print(f"Keys: {person.keys()}")

# 获取所有值
print(f"Values: {person.values()}")

# 获取所有键值对
print(f"Items: {person.items()}")
