"""
常用函数

对应文档: 03-data-structures.md § 3.2.15
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# len(): 列表长度
print(f"Length: {len(numbers)}")

# sum(): 求和
print(f"Sum: {sum(numbers)}")

# max() / min(): 最大值 / 最小值
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# all(): 所有元素都为 True
print(f"all([True, True, True]): {all([True, True, True])}")
print(f"all([True, False, True]): {all([True, False, True])}")
print(f"all([1, 2, 3]): {all([1, 2, 3])}")
print(f"all([0, 1, 2]): {all([0, 1, 2])}")

# any(): 至少一个元素为 True
print(f"any([False, False, True]): {any([False, False, True])}")
print(f"any([0, 0, 1]): {any([0, 0, 1])}")

# map(): 映射（应用函数）
squared = list(map(lambda x: x**2, numbers))
print(f"Squared (map): {squared}")

# filter(): 过滤
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (filter): {evens}")

# reduce(): 累积
product = reduce(lambda x, y: x * y, numbers)
print(f"Product (reduce): {product}")  # 120 (1*2*3*4*5)
