"""
递归执行流程分析

对应文档: 04-functions.md § 4.10.5
"""

# 计算 factorial(5) 的执行流程
"""
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
"""

# 递归深度限制
import sys
limit = sys.getrecursionlimit()
print(f"Recursion limit: {limit}")  # 默认 1000

# 递归 vs 迭代
# 递归实现
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 迭代实现（通常更高效）
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Recursive(5): {factorial_recursive(5)}")
print(f"Iterative(5): {factorial_iterative(5)}")
