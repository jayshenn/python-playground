"""
检查某值是否在元组中存在

对应文档: 03-data-structures.md § 3.4.5
"""

fruits = ("苹果", "香蕉", "橙子")
print(f"Fruits: {fruits}")

# 使用 in 运算符
if "苹果" in fruits:
    print("苹果在元组中")

if "西瓜" not in fruits:
    print("西瓜不在元组中")

# 结合条件判断
search = "葡萄"
if search in fruits:
    print(f"找到了 {search}")
else:
    print(f"没有找到 {search}")

# 嵌套元组中查找
nested = ((1, 2, 3), (4, 5, 6))
if 5 in nested[1]:
    print("5 在第二个子元组中")

# 检查多个值
targets = ("苹果", "香蕉")
if all(item in fruits for item in targets):
    print("所有目标都在元组中")
