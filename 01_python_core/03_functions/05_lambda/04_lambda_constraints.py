"""
匿名函数体内只能有有效的参数

对应文档: 04-functions.md § 4.11.4
"""

# 正确：单个表达式
add = lambda a, b: a + b
print(f"add(3, 5): {add(3, 5)}")

# 正确：多个参数
multiply = lambda a, b, c: a * b * c
print(f"multiply(2, 3, 4): {multiply(2, 3, 4)}")

# 正确：条件表达式
max_value = lambda a, b: a if a > b else b
print(f"max_value(10, 20): {max_value(10, 20)}")

# 错误：不能包含多条语句
# invalid = lambda x:
#     y = x + 1  # SyntaxError
#     return y

# Lambda 的限制
# 1. 只能是单个表达式
# 2. 不能包含语句（如 print、赋值等）
# 3. 不能包含注解
# 4. 不便于调试
