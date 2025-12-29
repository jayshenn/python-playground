"""
列表删除

对应文档: 03-data-structures.md § 3.2.4
"""

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print(f"Original: {fruits}")

# remove(): 删除指定值（第一个匹配的）
fruits.remove("橙子")
print(f"After remove('橙子'): {fruits}")

# pop(): 删除指定索引的元素（默认最后一个）
last = fruits.pop()  # 删除并返回最后一个
print(f"Popped last item: {last}")
print(f"After pop(): {fruits}")

item = fruits.pop(0)  # 删除并返回索引 0 的元素
print(f"Popped item at index 0: {item}")
print(f"After pop(0): {fruits}")

# del: 删除指定索引或切片
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

del numbers[0]  # 删除索引 0
print(f"After del numbers[0]: {numbers}")

del numbers[1:3]  # 删除索引 1 到 2 的元素
print(f"After del numbers[1:3]: {numbers}")

# clear(): 清空列表
fruits = ["苹果", "香蕉", "橙子"]
print(f"Fruits before clear: {fruits}")
fruits.clear()
print(f"Fruits after clear: {fruits}")
