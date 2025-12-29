"""
从集合中删除元素

对应文档: 03-data-structures.md § 3.5.3
"""

fruits = {"苹果", "香蕉", "橙子", "葡萄", "西瓜"}
print(f"Original: {fruits}")

# remove(): 删除指定元素（不存在会报错）
fruits.remove("橙子")
print(f"After remove('橙子'): {fruits}")

try:
    fruits.remove("榴莲")
except KeyError:
    print("Error: '榴莲' not found")

# discard(): 删除指定元素（不存在不报错）
fruits.discard("葡萄")
print(f"After discard('葡萄'): {fruits}")

fruits.discard("榴莲")  # 不报错
print(f"After discard('榴莲'): {fruits}")

# pop(): 随机删除并返回一个元素
item = fruits.pop()
print(f"Popped item: {item}")
print(f"After pop(): {fruits}")

# clear(): 清空集合
fruits.clear()
print(f"After clear(): {fruits}")
