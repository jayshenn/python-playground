"""
标识符命名规则

对应文档: 01-python-basics.md § 1.2.3
"""

# 规则：
# 1. 只能包含字母、数字和下划线
# 2. 不能以数字开头
# 3. 区分大小写
# 4. 不能使用 Python 关键字

# 推荐规范：
# - 变量名使用小写字母，多个单词用下划线分隔（snake_case）
# - 常量使用全大写字母
# - 类名使用首字母大写（PascalCase）
# - 私有变量以下划线开头

# 正确的命名
user_name = "Alice"
USER_AGE = 25
MAX_SIZE = 100

print(f"user_name: {user_name}")
print(f"USER_AGE: {USER_AGE}")
print(f"MAX_SIZE: {MAX_SIZE}")

# 错误的命名（取消注释会报错）
# 2name = "Bob"    # 不能以数字开头
# user-name = "C"  # 不能包含连字符
# for = 10         # 不能使用关键字
