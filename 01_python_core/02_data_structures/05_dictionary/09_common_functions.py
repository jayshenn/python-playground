"""
常用函数

对应文档: 03-data-structures.md § 3.6.9
"""

import copy

person = {"name": "Alice", "age": 25, "city": "北京"}
print(f"Person: {person}")

# len(): 字典长度
print(f"Length: {len(person)}")

# keys(): 获取所有键
print(f"Keys: {list(person.keys())}")

# values(): 获取所有值
print(f"Values: {list(person.values())}")

# items(): 获取所有键值对
print(f"Items: {list(person.items())}")

# get(): 安全获取值
print(f"Get name: {person.get('name')}")
print(f"Get email: {person.get('email', '无')}")

# copy(): 浅拷贝
person_copy = person.copy()
person_copy["age"] = 26
print(f"Original age after copy modification: {person['age']}")
print(f"Copy age: {person_copy['age']}")

# 深拷贝（嵌套字典）
users = {"user1": {"name": "Alice", "age": 25}}
shallow = users.copy()
deep = copy.deepcopy(users)

shallow["user1"]["age"] = 26  # 影响原字典
deep["user1"]["age"] = 27     # 不影响原字典

print(f"Original nested: {users}")  # {'user1': {'name': 'Alice', 'age': 26}}
print(f"Deep copy nested: {deep}")

# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Python 3.9+ 使用 | 运算符
merged = dict1 | dict2
print(f"Merged (|): {merged}")

# 使用 update()
dict1.update(dict2)
print(f"Merged (update): {dict1}")

# sorted(): 按键排序
person = {"name": "Alice", "city": "北京", "age": 25}
sorted_keys = sorted(person.keys())
print(f"Sorted keys: {sorted_keys}")

# 按值排序
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted scores (desc): {sorted_scores}")
