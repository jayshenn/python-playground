"""
语法

对应文档: 04-functions.md § 4.11.1
"""

# 匿名函数使用 lambda 关键字定义。
# 语法：lambda 参数: 表达式

# 特点：
# - 只能包含一个表达式
# - 不需要 return，表达式的结果就是返回值
# - 可以有多个参数，但只能有一个表达式
# - 通常用于简单的、一次性的函数

# 示例
double = lambda x: x * 2
print(f"Double of 5 is {double(5)}")
