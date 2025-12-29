"""
多分支

对应文档: 02-control-flow.md § 2.2.3
"""

# 多分支结构使用 if、elif、else 组合，可以处理多个条件。

# 成绩等级判断
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"你的成绩等级是：{grade}")

# 季节判断
month = 5
if month in [12, 1, 2]:
    season = "冬季"
elif month in [3, 4, 5]:
    season = "春季"
elif month in [6, 7, 8]:
    season = "夏季"
elif month in [9, 10, 11]:
    season = "秋季"
else:
    season = "无效月份"
print(f"{month}月是{season}")

# BMI 指数判断
height = 1.75  # 米
weight = 70    # 千克
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "偏胖"
else:
    status = "肥胖"
print(f"你的 BMI 是 {bmi:.2f}，属于{status}")
