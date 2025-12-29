"""
成员运算符

对应文档: 01-python-basics.md § 1.6.6
"""

# 用于检查一个值是否在序列中。
# in：存在于序列中
# not in：不存在于序列中

# 字符串
text = "Hello, World!"
print(f"text = '{text}'")
print(f"'H' in text: {'H' in text}")       # True
print(f"'h' in text: {'h' in text}")       # False
print(f"'Python' not in text: {'Python' not in text}")  # True

# 列表
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")      # True
print(f"10 not in numbers: {10 not in numbers}") # True

# 字典
person = {'name': 'Alice', 'age': 25}
print(f"person = {person}")
print(f"'name' in person: {'name' in person}")  # True（检查键）
print(f"'Alice' in person: {'Alice' in person}") # False（不检查值）
