"""
输出

对应文档: 01-python-basics.md § 1.5.2
"""

# 使用 print() 函数向控制台输出内容。

# 基本输出
print("Hello, World!")

# 输出多个值
name = "Alice"
age = 25
print("姓名:", name, "年龄:", age)

# 格式化输出
# 方法1：f-string（推荐）
print(f"姓名: {name}, 年龄: {age}")

# 方法2：format()
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {n}, 年龄: {a}".format(n=name, a=age))

# 方法3：% 格式化（旧式）
print("姓名: %s, 年龄: %d" % (name, age))

# 控制输出格式
print("圆周率:", 3.14159)
print(f"圆周率（保留2位小数）: {3.14159:.2f}")

# 控制输出的结束符
print("Hello", end=" ")
print("World")  # 输出: Hello World

# 控制输出的分隔符
print("apple", "banana", "orange", sep=", ")
# 输出: apple, banana, orange
