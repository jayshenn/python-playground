"""
删除字典元素

对应文档: 03-data-structures.md § 3.6.8
"""

person = {"name": "Alice", "age": 25, "city": "北京", "email": "alice@example.com"}
print(f"Original: {person}")

# pop(): 删除指定键并返回值
age = person.pop("age")
print(f"Popped age: {age}")
print(f"After pop('age'): {person}")

# pop() 提供默认值（键不存在时不报错）
phone = person.pop("phone", "未提供")
print(f"Popped non-existent phone: {phone}")

# popitem(): 删除并返回最后一个键值对（Python 3.7+）
item = person.popitem()
print(f"Popped item: {item}")
print(f"After popitem(): {person}")

# del: 删除指定键
del person["city"]
print(f"After del person['city']: {person}")

# 删除不存在的键会报错
try:
    del person["age"]
except KeyError:
    print("Error: Key 'age' not found")

# clear(): 清空字典
person.clear()
print(f"After clear(): {person}")
