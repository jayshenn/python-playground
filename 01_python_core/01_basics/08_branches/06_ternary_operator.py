"""
三目运算符

对应文档: 02-control-flow.md § 2.2.6
"""

# 三目运算符（条件表达式）是一种简洁的条件判断方式，用于简单的 if-else 语句。
# 语法：值1 if 条件 else 值2

# 基本用法
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(f"Age {age}: {status}")

# 求最大值
a = 10
b = 20
max_value = a if a > b else b
print(f"最大值是：{max_value}")

# 判断奇偶
number = 7
result = "奇数" if number % 2 != 0 else "偶数"
print(f"{number} 是{result}")

# 嵌套三目运算符（不推荐，影响可读性）
score = 85
grade = 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'D'))
print(f"成绩等级：{grade}")

# 实际应用：设置默认值
user_input = ""
username = user_input if user_input else "游客"
print(f"欢迎，{username}")

# 列表推导式中使用
numbers = [1, 2, 3, 4, 5, 6]
labels = ["奇数" if n % 2 != 0 else "偶数" for n in numbers]
print(f"Labels: {labels}")
