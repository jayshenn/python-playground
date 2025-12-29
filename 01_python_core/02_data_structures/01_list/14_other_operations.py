"""
其他操作

对应文档: 03-data-structures.md § 3.2.14
"""

import copy

# sort(): 排序（原地修改）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

numbers.sort()  # 升序
print(f"Sorted (asc): {numbers}")

numbers.sort(reverse=True)  # 降序
print(f"Sorted (desc): {numbers}")

# sorted(): 排序（返回新列表）
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(f"Original after sorted(): {numbers}")
print(f"New sorted list: {sorted_numbers}")

# 自定义排序
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # 按长度排序
print(f"Sorted by length: {words}")

# reverse(): 反转列表
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed: {numbers}")

# reversed(): 返回反转迭代器
numbers = [1, 2, 3, 4, 5]
reversed_list = list(reversed(numbers))
print(f"Reversed list from iterator: {reversed_list}")

# copy(): 复制列表（浅拷贝）
original = [1, 2, 3]
copied = original.copy()
copied[0] = 100
print(f"Original after shallow copy modification: {original}")
print(f"Copied list: {copied}")

# 深拷贝（嵌套列表）
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 100  # 影响原列表
deep[1][0] = 200     # 不影响原列表

print(f"Original nested: {original}")  # [[100, 2], [3, 4]]
print(f"Shallow copy: {shallow}")   # [[100, 2], [3, 4]]
print(f"Deep copy: {deep}")      # [[100, 2], [200, 4]]
