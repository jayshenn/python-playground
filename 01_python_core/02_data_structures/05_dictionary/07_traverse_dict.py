"""
遍历字典

对应文档: 03-data-structures.md § 3.6.7
"""

person = {"name": "Alice", "age": 25, "city": "北京"}

print("--- Keys ---")
# 遍历键
for key in person:
    print(key)

print("\n--- Keys (explicit) ---")
# 或显式使用 keys()
for key in person.keys():
    print(key)

print("\n--- Values ---")
# 遍历值
for value in person.values():
    print(value)

print("\n--- Items ---")
# 遍历键值对（推荐）
for key, value in person.items():
    print(f"{key}: {value}")

print("\n--- Enumerate Items ---")
# 使用 enumerate()
for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")

print("\n--- Nested Dictionary ---")
# 嵌套字典遍历
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}

for user_id, user_info in users.items():
    print(f"{user_id}:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

print("\n--- Filtered Dictionary ---")
# 过滤字典
person = {"name": "Alice", "age": 25, "city": "北京", "email": "alice@example.com"}
filtered = {k: v for k, v in person.items() if isinstance(v, str)}
print(f"String values only: {filtered}")
