"""
递归案例，求一个整数 n 的阶乘

对应文档: 04-functions.md § 4.10.4
"""

def factorial(n):
    """
    计算 n 的阶乘

    n! = n × (n-1)!
    0! = 1
    """
    # 基线条件
    if n == 0 or n == 1:
        return 1

    # 递归条件
    return n * factorial(n - 1)

# 测试
print(f"factorial(0) = {factorial(0)}")
print(f"factorial(1) = {factorial(1)}")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(10) = {factorial(10)}")
