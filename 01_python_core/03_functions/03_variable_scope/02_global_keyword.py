"""
global 关键字

对应文档: 04-functions.md § 4.9.2
"""

# 使用 global 在函数内修改全局变量。

count = 0

def increment():
    global count  # 声明使用全局变量
    count += 1
    print(f"Inside increment: count = {count}")

print(f"Before: count = {count}")
increment()
print(f"After 1st call: count = {count}")
increment()
print(f"After 2nd call: count = {count}")

# 实际应用：计数器
total = 0

def add_score(score):
    global total
    total += score
    return total

print(f"\nAdding scores:")
print(f"Add 10: total = {add_score(10)}")
print(f"Add 20: total = {add_score(20)}")
print(f"Add 15: total = {add_score(15)}")
