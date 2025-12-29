"""
分号

对应文档: 01-python-basics.md § 1.7.5
"""

# Python 中不需要使用分号来结束语句（除非在一行中写多条语句）。

# 正确：不使用分号
print("Hello")
x = 10

# 虽然允许，但不推荐
print("Hello with semicolon");
x = 10;

# 一行多条语句时使用分号（不推荐）
x = 10; y = 20
print(f"x={x}, y={y}")
