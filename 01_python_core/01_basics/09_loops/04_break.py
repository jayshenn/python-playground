"""
break

对应文档: 02-control-flow.md § 2.3.4
"""

# break 语句用于完全终止循环，跳出循环体。

# 找到第一个偶数就退出
print("Find first even number:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"找到第一个偶数：{i}")
        break

# 在列表中查找元素
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
target = "橙子"
print(f"Searching for {target} in {fruits}:")
for fruit in fruits:
    if fruit == target:
        print(f"找到了：{fruit}")
        break
else:
    print(f"没有找到：{target}")

# while 循环中使用 break
print("while loop with break (stop at 5):")
count = 1
while True:
    print(count, end=" ")
    if count >= 5:
        break  # 当 count 达到 5 时退出
    count += 1
print()

# 查找质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("First 10 prime numbers:")
count = 0
number = 2
while count < 10:
    if is_prime(number):
        print(number, end=" ")
        count += 1
    number += 1
print()
