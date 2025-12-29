"""
检查某值是否在字典中的 key

对应文档: 03-data-structures.md § 3.6.5
"""

person = {"name": "Alice", "age": 25, "city": "北京"}
print(f"Person: {person}")

# 使用 in / not in（检查键）
print(f"'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")
print(f"'email' not in person: {'email' not in person}")

# 检查值（需要使用 values()）
print(f"'Alice' in person.values(): {'Alice' in person.values()}")
print(f"'Bob' in person.values(): {'Bob' in person.values()}")

# 结合条件判断
if "name" in person:
    print(f"Name found: {person['name']}")

# 使用 get() 更安全
email = person.get("email")
if email:
    print(f"Email: {email}")
else:
    print("Email not found")
