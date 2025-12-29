"""
match case 语句

对应文档: 02-control-flow.md § 2.2.5
"""

# Python 3.10+ 引入了 match case 语句（结构模式匹配），类似于其他语言的 switch case。

# 基本用法：匹配具体值
def get_weekday_name(day):
    match day:
        case 1:
            return "星期一"
        case 2:
            return "星期二"
        case 3:
            return "星期三"
        case 4:
            return "星期四"
        case 5:
            return "星期五"
        case 6:
            return "星期六"
        case 7:
            return "星期日"
        case _:
            return "无效的日期"

print(f"Day 3 is {get_weekday_name(3)}")

# 匹配多个值
def check_status_code(code):
    match code:
        case 200:
            return "成功"
        case 404 | 403:  # 匹配多个值
            return "客户端错误"
        case 500 | 502 | 503:
            return "服务器错误"
        case _:
            return "未知错误"

print(f"Status 404: {check_status_code(404)}")

# 匹配序列
def process_command(command):
    match command:
        case ["quit"]:
            return "退出程序"
        case ["load", filename]:
            return f"加载文件：{filename}"
        case ["save", filename]:
            return f"保存文件：{filename}"
        case _:
            return "未知命令"

print(process_command(["load", "data.txt"]))

# 匹配字典
def process_user(user):
    match user:
        case {"name": name, "age": age} if age >= 18:
            return f"{name} 是成年人"
        case {"name": name, "age": age}:
            return f"{name} 是未成年人"
        case _:
            return "无效数据"

print(process_user({"name": "Alice", "age": 25}))
