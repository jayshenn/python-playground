"""
向列表中添加元素

对应文档: 03-data-structures.md § 3.2.3
"""

fruits = ["苹果", "香蕉"]
print(f"Original: {fruits}")

# append(): 在末尾添加单个元素
fruits.append("橙子")
print(f"After append('橙子'): {fruits}")

# insert(): 在指定位置插入元素
fruits.insert(1, "葡萄")  # 在索引 1 处插入
print(f"After insert(1, '葡萄'): {fruits}")

# extend(): 添加多个元素（扩展列表）
fruits.extend(["西瓜", "草莓"])
print(f"After extend(['西瓜', '草莓']): {fruits}")

# 使用 + 运算符（创建新列表）
new_fruits = fruits + ["芒果", "榴莲"]
print(f"Using + operator: {new_fruits}")

# 使用 += 运算符（原地修改）
fruits += ["火龙果"]
print(f"Using += operator: {fruits}")
