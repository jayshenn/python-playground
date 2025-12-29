"""
返回值

对应文档: 04-functions.md § 4.2.6
"""

# return 语句用于从函数返回值。

# 返回单个值
def square(x):
    return x ** 2

print(f"square(5): {square(5)}")

# 返回多个值（元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [1, 2, 3, 4, 5]
min_val, max_val = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {min_val}, Max: {max_val}")

# 无返回值（返回 None）
def print_message(msg):
    print(msg)
    # 隐式返回 None

result = print_message("Hello from print_message")
print(f"Return value of print_message: {result}")

# 条件返回
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(f"Grade for 85: {get_grade(85)}")

# 提前返回
def find_item(items, target):
    for item in items:
        if item == target:
            return item  # 找到后立即返回
    return None  # 未找到

items = ["apple", "banana", "cherry"]
print(f"Find 'banana': {find_item(items, 'banana')}")
print(f"Find 'date': {find_item(items, 'date')}")
