"""
向字典中添加元素

对应文档: 03-data-structures.md § 3.6.3
"""

person = {"name": "Alice", "age": 25}
print(f"Original: {person}")

# 直接赋值添加
person["city"] = "北京"
print(f"Added city: {person}")

# update(): 添加多个键值对
person.update({"email": "alice@example.com", "phone": "123-4567"})
print(f"Updated with dict: {person}")

# update() 也可以接受关键字参数
person.update(job="工程师", salary=10000)
print(f"Updated with kwargs: {person}")

# setdefault(): 如果键不存在则添加，存在则返回值
val = person.setdefault("country", "中国")
print(f"setdefault 'country': {person} (returns {val})")

val_exist = person.setdefault("name", "Bob")  # name 已存在，不修改
print(f"setdefault existing 'name': {person['name']} (returns {val_exist})")
