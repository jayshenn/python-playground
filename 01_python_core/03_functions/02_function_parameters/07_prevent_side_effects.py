"""
防止参数修改副作用

对应文档: 04-functions.md § 4.5.7
"""

# 问题：可变默认参数被修改（"陷阱"）
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(f"Bad call 1: {add_item_bad(1)}")  # [1]
print(f"Bad call 2: {add_item_bad(2)}")  # [1, 2]（预期是 [2]）
print(f"Bad call 3: {add_item_bad(3)}")  # [1, 2, 3]（预期是 [3]）

# 解决方案1：使用 None 作为默认值（推荐）
def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"\nGood call 1: {add_item_good(1)}")  # [1]
print(f"Good call 2: {add_item_good(2)}")  # [2]
print(f"Good call 3: {add_item_good(3)}")  # [3]

# 解决方案2：复制参数（如果在函数内需要修改但不希望影响外部）
def process_list(lst):
    lst = lst.copy()  # 创建副本
    lst.append(100)
    return lst

original = [1, 2, 3]
result = process_list(original)
print(f"\nOriginal list: {original}")  # [1, 2, 3]（未改变）
print(f"Result list: {result}")    # [1, 2, 3, 100]
