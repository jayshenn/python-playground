"""
使用普通函数替代参数

对应文档: 04-functions.md § 4.11.2
"""

# 普通函数
def square(x):
    return x ** 2

print(f"square(5): {square(5)}")

# 使用普通函数作为参数
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f"Squared list (using function): {squared}")
