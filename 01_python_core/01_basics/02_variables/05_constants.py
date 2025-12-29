"""
常量

对应文档: 01-python-basics.md § 1.2.5
"""

# Python 中没有真正的常量，通常使用全大写的变量名来表示常量，提醒开发者不要修改。

# 常量（约定俗成）
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432"

print(f"PI: {PI}")
print(f"MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"DATABASE_URL: {DATABASE_URL}")

# 虽然可以修改，但不建议这样做
# PI = 3.14  # 不推荐
