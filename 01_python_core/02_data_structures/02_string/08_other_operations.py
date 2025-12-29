"""
其他操作

对应文档: 03-data-structures.md § 3.3.8
"""

import re
from string import Template

# 字符串格式化
name = "Alice"
age = 25
score = 95.5

# f-string（推荐）Python 3.6+
print(f"f-string: {name} 今年 {age} 岁，得分 {score:.1f}")

# format() 方法
print("format(): {} 今年 {} 岁".format(name, age))
print("format(named): {name} 今年 {age} 岁".format(name=name, age=age))
print("format(index): {0} 今年 {1} 岁，{0} 很聪明".format(name, age))

# % 格式化（旧式）
print("%% formatting: %s 今年 %d 岁" % (name, age))
print("%% float: 得分: %.2f" % score)

# 进制转换
num = 255
print(f"Decimal: {num}")
print(f"Binary: {bin(num)}")
print(f"Octal: {oct(num)}")
print(f"Hex: {hex(num)}")

# 编码和解码
text = "你好，世界"
encoded = text.encode('utf-8')
print(f"Encoded bytes: {encoded}")

decoded = encoded.decode('utf-8')
print(f"Decoded string: {decoded}")

# 字符和 ASCII 码
print(f"ord('A'): {ord('A')}")
print(f"chr(65): {chr(65)}")
print(f"ord('中'): {ord('中')}")

# 字符串模板
t = Template("$name 今年 $age 岁")
print(f"Template: {t.substitute(name='Alice', age=25)}")

# 正则表达式
text = "联系电话：138-1234-5678"
phone = re.search(r'\d{3}-\d{4}-\d{4}', text)
if phone:
    print(f"Regex match: {phone.group()}")
