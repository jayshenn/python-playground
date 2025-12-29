"""
continue

对应文档: 02-control-flow.md § 2.3.3
"""

# continue 语句用于跳过当前循环的剩余部分，直接进入下一次循环。

# 跳过偶数，只打印奇数
print("Odd numbers (skipping evens):")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()

# 跳过特定值
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print("Fruits excluding '橙子':")
for fruit in fruits:
    if fruit == "橙子":
        continue  # 跳过橙子
    print(f"我喜欢吃{fruit}")

# while 循环中使用 continue
print("while loop with continue (skipping multiples of 3):")
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue
    print(count, end=" ")
print()
