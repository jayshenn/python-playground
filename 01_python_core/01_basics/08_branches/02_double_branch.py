"""
双分支

对应文档: 02-control-flow.md § 2.2.2
"""

# 双分支结构包含 if 和 else，当条件为真时执行 if 代码块，否则执行 else 代码块。

# 判断奇偶数
number = 7
if number % 2 == 0:
    print(f"{number} 是偶数")
else:
    print(f"{number} 是奇数")

# 判断成绩是否及格
score = 55
if score >= 60:
    print(f"Score {score}: 及格")
else:
    print(f"Score {score}: 不及格")

# 判断用户年龄（模拟输入）
# age = int(input("请输入你的年龄："))
age = 16
if age >= 18:
    print("你可以观看此内容")
else:
    print("抱歉，你还未成年")
