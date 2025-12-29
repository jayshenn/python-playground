"""
单分支

对应文档: 02-control-flow.md § 2.2.1
"""

# 单分支结构只有一个 if 语句，当条件为真时执行代码块。

# 判断年龄是否成年
age = 20
if age >= 18:
    print(f"Age {age}: 你已经成年了")

# 判断成绩是否及格
score = 85
if score >= 60:
    print(f"Score {score}: 恭喜你，考试及格了！")

# 判断数字是否为正数
number = 10
if number > 0:
    print(f"{number} 是正数")
