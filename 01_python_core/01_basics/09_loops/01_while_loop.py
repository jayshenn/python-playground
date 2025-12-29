"""
while 循环

对应文档: 02-control-flow.md § 2.3.1
"""

# while 循环会在条件为真时重复执行代码块。

# 基本用法：打印 1 到 5
print("Counting 1 to 5:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 计算 1 到 100 的和
sum_value = 0
number = 1
while number <= 100:
    sum_value += number
    number += 1
print(f"1 到 100 的和是：{sum_value}")

# 计算阶乘
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")

# while-else
count = 0
print("while-else loop:")
while count < 3:
    print(count)
    count += 1
else:
    print("while 循环正常结束")
