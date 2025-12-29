"""
数据类型转换

对应文档: 01-python-basics.md § 1.4.5
"""

# Python 提供了多种函数来进行数据类型转换。

# 转换为整数
x = int("123")  # 字符串转整数
y = int(3.14)  # 浮点数转整数（截断小数部分）
z = int(True)  # 布尔值转整数

print(f"int('123'): {x}, Type: {type(x)}")
print(f"int(3.14): {y}")
print(f"int(True): {z}")

# 转换为浮点数
a = float("3.14")  # 字符串转浮点数
b = float(10)  # 整数转浮点数
c = float(True)  # 布尔值转浮点数

print(f"float('3.14'): {a}, Type: {type(a)}")
print(f"float(10): {b}")
print(f"float(True): {c}")

# 转换为字符串
s1 = str(123)  # 整数转字符串
s2 = str(3.14)  # 浮点数转字符串
s3 = str(True)  # 布尔值转字符串

print(f"str(123): '{s1}', Type: {type(s1)}")

# 转换为布尔值
b1 = bool(1)  # 非零数转为 True
b2 = bool(0)  # 0 转为 False
b3 = bool("text")  # 非空字符串转为 True
b4 = bool("")  # 空字符串转为 False

print(f"bool(1): {b1}")
print(f"bool(0): {b2}")
print(f"bool('text'): {b3}")
print(f"bool(''): {b4}")
