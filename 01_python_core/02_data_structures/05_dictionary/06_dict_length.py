"""
获取字典长度

对应文档: 03-data-structures.md § 3.6.6
"""

person = {"name": "Alice", "age": 25, "city": "北京"}

# len(): 获取键值对数量
print(f"Length of person: {len(person)}")

# 空字典
empty = {}
print(f"Length of empty: {len(empty)}")

# 嵌套字典（只计算外层）
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(f"Length of users (outer): {len(users)}")
print(f"Length of user1 (inner): {len(users['user1'])}")
