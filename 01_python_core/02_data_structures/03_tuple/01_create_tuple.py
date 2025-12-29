"""
创建元组

对应文档: 03-data-structures.md § 3.4.1
"""

# 空元组
empty_tuple = ()
empty_tuple2 = tuple()
print(f"Empty tuple: {empty_tuple}")

# 包含元素的元组
numbers = (1, 2, 3, 4, 5)
fruits = ("苹果", "香蕉", "橙子")
mixed = (1, "hello", 3.14, True)

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# 单元素元组（必须有逗号）
single = (42,)  # 正确
not_tuple = (42)  # 这是整数，不是元组
print(f"Single tuple type: {type(single)}")
print(f"Not tuple type: {type(not_tuple)}")

# 不使用括号（元组打包）
coords = 10, 20
print(f"Tuple packing: {coords}, type: {type(coords)}")

# 使用 tuple() 构造函数
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(f"From list: {tuple_data}")

string_tuple = tuple("Hello")
print(f"From string: {string_tuple}")

# 嵌套元组
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")
