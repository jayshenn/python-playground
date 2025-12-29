"""
String 字符串初识

对应文档: 01-python-basics.md § 1.4.4
"""

# 字符串是用于表示文本的数据类型，使用单引号或双引号定义。

# 字符串定义
name = "Alice"
message = 'Hello, World!'
multiline = """
这是多行
字符串
"""

print(f"Name: {name}, Type: {type(name)}")
print(f"Message: {message}")
print(f"Multiline:\n{multiline}")

# 字符串操作
greeting = "Hello"
target = "World"
full_message = greeting + " " + target  # 拼接
print(f"Full Message: {full_message}")

# 字符串方法
print(f"Upper: {name.upper()}")  # ALICE
print(f"Lower: {name.lower()}")  # alice
print(f"Length: {len(name)}")  # 5
