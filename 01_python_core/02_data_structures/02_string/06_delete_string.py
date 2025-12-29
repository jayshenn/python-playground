"""
删除字符串

对应文档: 03-data-structures.md § 3.3.6
"""

# 字符串是不可变的，不能直接删除，只能创建新字符串

text = "Hello, World!"
print(f"Original: {text}")

# 方法1: 使用切片
new_text = text[:5] + text[7:]
print(f"Using slice: {new_text}")

# 方法2: 使用 replace()
new_text = text.replace(",", "")
print(f"Using replace: {new_text}")

# 删除指定字符
text = "Hello, Python!"
new_text = text.replace("o", "")
print(f"Removing 'o': {new_text}")

# 删除空白字符
text = "  Hello  World  "
print(f"Original with spaces: '{text}'")
print(f"strip(): '{text.strip()}'")   # 删除两端空白
print(f"lstrip(): '{text.lstrip()}'")  # 删除左侧空白
print(f"rstrip(): '{text.rstrip()}'")  # 删除右侧空白

# 删除指定字符
text = "***Hello***"
print(f"strip('*'): '{text.strip('*')}'")

# 使用 filter()
text = "Hello123World456"
letters_only = ''.join(filter(str.isalpha, text))
print(f"Letters only (filter): {letters_only}")
