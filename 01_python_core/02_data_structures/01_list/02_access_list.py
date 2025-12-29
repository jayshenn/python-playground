"""
访问列表

对应文档: 03-data-structures.md § 3.2.2
"""

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print(f"Fruits: {fruits}")

# 正向索引（从 0 开始）
print(f"Index 0: {fruits[0]}")   # 苹果
print(f"Index 2: {fruits[2]}")   # 橙子

# 负向索引（从 -1 开始）
print(f"Index -1: {fruits[-1]}")  # 西瓜（最后一个）
print(f"Index -2: {fruits[-2]}")  # 葡萄（倒数第二个）

# 切片 [start:stop:step]
print(f"Slice [1:4]: {fruits[1:4]}")    # ['香蕉', '橙子', '葡萄']
print(f"Slice [:3]: {fruits[:3]}")     # ['苹果', '香蕉', '橙子']
print(f"Slice [2:]: {fruits[2:]}")     # ['橙子', '葡萄', '西瓜']
print(f"Slice [::2]: {fruits[::2]}")    # ['苹果', '橙子', '西瓜'] (步长为2)
print(f"Slice [::-1]: {fruits[::-1]}")   # ['西瓜', '葡萄', '橙子', '香蕉', '苹果'] (反转)

# 多维列表访问
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix[0]: {matrix[0]}")      # [1, 2, 3]
print(f"Matrix[1][2]: {matrix[1][2]}")   # 6
