"""
字符串转义

对应文档: 03-data-structures.md § 3.3.4
"""

# 常用转义字符
print("Hello\nWorld")  # 换行
print("Hello\tWorld")  # 制表符
print("He said \"Hello\"")  # 双引号
print('It\'s OK')  # 单引号
print("C:\\Users\\name")  # 反斜杠

# 转义字符列表
# \n  换行
# \t  制表符
# \\  反斜杠
# \'  单引号
# \"  双引号
# \r  回车
# \b  退格

# 原始字符串（不转义）
path = r"C:\Users\name\Documents"
print(f"Raw string: {path}")

# Unicode 转义
print(f"Unicode: \u4e2d\u6587")  # 中文

# 使用三引号避免转义
text = """He said "Hello" and she replied 'Hi'"""
print(f"Triple quotes: {text}")
