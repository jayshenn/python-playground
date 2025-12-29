"""
字符串拼接

对应文档: 03-data-structures.md § 3.3.3
"""

# 方法1: 使用 + 运算符
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(f"Using +: {result}")

# 方法2: 使用 join()（推荐，效率高）
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(f"Using join(): {result}")

# 方法3: 使用 f-string
name = "Alice"
greeting = f"Hello, {name}!"
print(f"Using f-string: {greeting}")

# 方法4: 使用 format()
result = "{} {}".format("Hello", "World")
print(f"Using format(): {result}")

# 方法5: 使用 % 格式化
result = "%s %s" % ("Hello", "World")
print(f"Using %: {result}")

# 方法6: 重复字符串
print(f"Repeat string: {'=' * 20}")
print(f"Repeat string: {'Hello ' * 3}")

# 拼接数字和字符串
age = 25
text = "我今年" + str(age) + "岁"
print(f"Concatenating number: {text}")
