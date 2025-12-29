"""
函数名

对应文档: 04-functions.md § 4.2.3
"""

# 函数名是函数的标识符，命名应该遵循规范。

# 命名规则：
# - 只能包含字母、数字、下划线
# - 不能以数字开头
# - 不能使用 Python 关键字
# - 区分大小写

# 命名规范（PEP 8）：
# - 使用小写字母
# - 多个单词用下划线分隔（snake_case）
# - 名称应该描述函数的功能（动词开头）

# 好的函数名
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_even(number):
    return number % 2 == 0

def get_user_info():
    return {"name": "Alice", "age": 25}

# 测试
nums = [1, 2, 3, 4, 5]
print(f"Average: {calculate_average(nums)}")
print(f"Is 4 even? {is_even(4)}")
print(f"User info: {get_user_info()}")

# 不好的函数名（不推荐）
# def calc():  # 太简短，不清楚
#     pass
# def MyFunction():  # 不符合规范（应该用小写）
#     pass
# def x():  # 无意义的名称
#     pass
