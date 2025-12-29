"""
代码格式统一—行代码

对应文档: 01-python-basics.md § 1.7.7
"""

# 保持代码格式统一，提高可读性。

# 运算符两边加空格
x = 10
y = x + 5

# 函数定义
def add(a, b):
    return a + b

# 函数调用
result = add(10, 20)

# 列表索引和切片不加空格
my_list = [1, 2, 3, 4, 5]
item = my_list[0]
sub_list = my_list[1:5]

# 字典
person = {'name': 'Alice', 'age': 25}

# 命名规范
# 变量和函数：小写+下划线
user_name = "Alice"

def get_user_info():
    pass

# 类名：大驼峰
class UserProfile:
    pass

# 常量：全大写+下划线
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30

print("代码格式示例展示完毕")
