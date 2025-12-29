"""
for 循环

对应文档: 02-control-flow.md § 2.3.2
"""

# for 循环用于遍历序列（如列表、元组、字符串、范围等）。

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print(f"Fruits: {fruits}")
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 遍历字符串
word = "Python"
print("Characters in 'Python':")
for char in word:
    print(char)

# 使用 range() 函数
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 遍历字典
person = {"name": "Alice", "age": 25, "city": "北京"}
print("Dictionary iteration:")
for key, value in person.items():
    print(f"{key}: {value}")

# 使用 enumerate() 获取索引
print("Enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# for-else
print("for-else loop:")
for i in range(3):
    print(i)
else:
    print("循环正常结束")
