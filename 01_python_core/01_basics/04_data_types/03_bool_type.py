"""
bool 布尔型

对应文档: 01-python-basics.md § 1.4.3
"""

# 布尔型只有两个值：True 和 False，用于表示真假。

# 布尔值
is_student = True
is_graduated = False

print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Is Graduated: {is_graduated}")

# 布尔值在条件判断中的应用
if is_student:
    print("这是一名学生")

# 布尔值的数值表示
# True 相当于 1, False 相当于 0
print(f"int(True): {int(True)}")  # 1
print(f"int(False): {int(False)}")  # 0
