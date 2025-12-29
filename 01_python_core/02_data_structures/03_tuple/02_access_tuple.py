"""
访问元组

对应文档: 03-data-structures.md § 3.4.2
"""

fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")
print(f"Fruits: {fruits}")

# 索引访问
print(f"Index 0: {fruits[0]}")   # 苹果
print(f"Index -1: {fruits[-1]}")  # 西瓜

# 切片
print(f"Slice [1:4]: {fruits[1:4]}")   # ('香蕉', '橙子', '葡萄')
print(f"Slice [:3]: {fruits[:3]}")    # ('苹果', '香蕉', '橙子')
print(f"Slice [2:]: {fruits[2:]}")    # ('橙子', '葡萄', '西瓜')
print(f"Slice [::2]: {fruits[::2]}")   # ('苹果', '橙子', '西瓜')
print(f"Slice [::-1]: {fruits[::-1]}")  # ('西瓜', '葡萄', '橙子', '香蕉', '苹果')

# 元组解包
point = (10, 20)
x, y = point
print(f"Unpacked: x={x}, y={y}")

# 交换变量
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # 使用元组解包交换
print(f"After swap: a={a}, b={b}")

# 多个返回值
def get_user_info():
    return "Alice", 25, "Beijing"

name, age, city = get_user_info()
print(f"Multiple returns: {name}, {age}, {city}")

# 嵌套元组访问
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested[1]: {nested[1]}")
print(f"Nested[1][0]: {nested[1][0]}")
