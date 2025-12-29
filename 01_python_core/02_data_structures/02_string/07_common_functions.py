"""
常用函数

对应文档: 03-data-structures.md § 3.3.7
"""

text = "Hello, Python Programming"
print(f"Text: {text}")

# 长度
print(f"Length: {len(text)}")

# 大小写转换
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title: {text.title()}")
print(f"Swapcase: {'HELLO'.swapcase()}")

# 判断类型
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello'.islower(): {'Hello'.islower()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")

# 字符串分割
text = "apple,banana,orange"
fruits = text.split(",")
print(f"Split by comma: {fruits}")

# 按行分割
text = "line1\nline2\nline3"
lines = text.splitlines()
print(f"Split lines: {lines}")

# 分割次数限制
text = "a-b-c-d"
print(f"Split max 2: {text.split('-', 2)}")

# 字符串连接
words = ["Hello", "World"]
print(f"Join with space: {' '.join(words)}")
print(f"Join with hyphen: {'-'.join(words)}")

# 替换
text = "Hello, World"
print(f"Replace 'World' with 'Python': {text.replace('World', 'Python')}")
print(f"Replace first 'o': {text.replace('o', '0', 1)}")

# 对齐
print(f"Center: '{'Hello'.center(20)}'")
print(f"Ljust: '{'Hello'.ljust(20, '*')}'")
print(f"Rjust: '{'Hello'.rjust(20, '*')}'")
print(f"Zfill: {'42'.zfill(5)}")
