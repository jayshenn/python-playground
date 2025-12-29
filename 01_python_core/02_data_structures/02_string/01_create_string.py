"""
创建字符串

对应文档: 03-data-structures.md § 3.3.1
"""

# 单引号
str1 = 'Hello'
print(f"Single quotes: {str1}")

# 双引号
str2 = "World"
print(f"Double quotes: {str2}")

# 三引号（多行字符串）
str3 = """这是
多行
字符串"""
print(f"Triple double quotes:\n{str3}")

str4 = '''这也是
多行字符串'''
print(f"Triple single quotes:\n{str4}")

# 空字符串
empty = ""
empty2 = str()
print(f"Empty string: '{empty}'")

# 使用 str() 构造函数
num_str = str(123)
bool_str = str(True)
print(f"From number: {num_str}, type: {type(num_str)}")
print(f"From bool: {bool_str}, type: {type(bool_str)}")

# 原始字符串（r前缀）
path = r"C:\Users\name\Documents"  # 不转义反斜杠
print(f"Raw string: {path}")

# f-string（格式化字符串）Python 3.6+
name = "Alice"
age = 25
greeting = f"我叫{name}，今年{age}岁"
print(f"f-string: {greeting}")
