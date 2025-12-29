"""
检查某值是否在字符串中存在

对应文档: 03-data-structures.md § 3.3.5
"""

text = "Hello, Python Programming"
print(f"Text: {text}")

# 使用 in / not in
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# find(): 返回子串第一次出现的索引（找不到返回-1）
print(f"find('Python'): {text.find('Python')}")
print(f"find('Java'): {text.find('Java')}")

# 指定查找范围
print(f"find('o', 5): {text.find('o', 5)}")  # 从索引5开始查找

# rfind(): 从右往左查找
print(f"rfind('o'): {text.rfind('o')}")

# index(): 类似 find()，但找不到会报错
try:
    print(text.index("Java"))
except ValueError:
    print("Error: 'Java' not found")

# count(): 统计子串出现次数
print(f"count('o'): {text.count('o')}")

# startswith() / endswith()
print(f"startswith('Hello'): {text.startswith('Hello')}")
print(f"endswith('Programming'): {text.endswith('Programming')}")
print(f"startswith('Python', 7): {text.startswith('Python', 7)}")
