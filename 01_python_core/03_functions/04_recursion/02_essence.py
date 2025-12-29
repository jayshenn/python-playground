"""
本质

对应文档: 04-functions.md § 4.10.2
"""

# 递归将大问题分解为相似的小问题，直到问题简单到可以直接解决。

# 示例：斐波那契数列
def fibonacci(n):
    # 基线条件
    if n <= 1:
        return n
    # 递归关系
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print(f"Fibonacci({n}) = {fibonacci(n)}")
# F(6) = F(5) + F(4) = 5 + 3 = 8
