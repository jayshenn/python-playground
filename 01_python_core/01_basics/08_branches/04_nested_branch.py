"""
嵌套分支

对应文档: 02-control-flow.md § 2.2.4
"""

# 分支结构可以嵌套使用，即在一个分支内部再包含另一个分支。

# 用户登录验证（模拟）
username = "admin"
password = "123456"

# 模拟输入
# input_username = input("请输入用户名：")
input_username = "admin"

if input_username == username:
    # input_password = input("请输入密码：")
    input_password = "123456"
    
    if input_password == password:
        print("登录成功！")
    else:
        print("密码错误！")
else:
    print("用户名不存在！")

# 购票系统
age = 65
is_student = False

if age < 18:
    print("儿童票：半价")
elif age >= 60:
    print("老年票：免费")
else:
    if is_student:
        print("学生票：8折")
    else:
        print("成人票：全价")

# 闰年判断（嵌套条件）
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} 是闰年")
        else:
            print(f"{year} 不是闰年")
    else:
        print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
