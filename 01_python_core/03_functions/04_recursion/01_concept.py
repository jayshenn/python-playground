"""
概念

对应文档: 04-functions.md § 4.10.1
"""

# 递归是函数调用自身的编程技巧。

# 递归的两个要素：
# 1. 基线条件（Base Case）：递归终止的条件
# 2. 递归条件（Recursive Case）：函数调用自身

def countdown(n):
    """一个简单的递归倒计时"""
    # 基线条件
    if n <= 0:
        print("Blastoff!")
    else:
        # 递归条件
        print(n)
        countdown(n - 1)

countdown(3)
