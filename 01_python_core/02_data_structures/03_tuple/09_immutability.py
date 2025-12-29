"""
元组的不可变

对应文档: 03-data-structures.md § 3.4.9
"""

# 元组是不可变的
fruits = ("苹果", "香蕉", "橙子")
print(f"Original: {fruits}")

# 不能修改元素（会报错）
try:
    fruits[0] = "葡萄"
except TypeError as e:
    print(f"Error modifying tuple: {e}")

# 不能删除元素（会报错）
try:
    del fruits[0]
except TypeError as e:
    print(f"Error deleting from tuple: {e}")

# 但是可以删除整个元组
# del fruits
# print(fruits)  # NameError

# 如果元组包含可变对象，可变对象的内容可以修改
data = ([1, 2, 3], [4, 5, 6])
print(f"Tuple with mutable lists: {data}")

data[0].append(4)  # 修改列表内容（允许）
print(f"Modified inner list: {data}")

# 但不能替换列表对象本身
try:
    data[0] = [10, 20]
except TypeError as e:
    print(f"Error replacing inner object: {e}")

# 如果需要修改，可以转换为列表
fruits = ("苹果", "香蕉", "橙子")
fruits_list = list(fruits)
fruits_list[0] = "葡萄"
fruits = tuple(fruits_list)
print(f"Modified via list conversion: {fruits}")
