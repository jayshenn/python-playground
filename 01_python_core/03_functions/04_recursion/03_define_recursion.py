"""
在定义递归函数的时候，主要确定两点

对应文档: 04-functions.md § 4.10.3
"""

# 1. 确定基线条件：什么时候停止递归
# 2. 确定递归关系：如何将问题分解为子问题

def sum_list(numbers):
    """递归求和"""
    # 1. 基线条件：列表为空，和为 0
    if not numbers:
        return 0
    
    # 2. 递归关系：第一个元素 + 剩余元素的和
    return numbers[0] + sum_list(numbers[1:])

nums = [1, 2, 3, 4, 5]
print(f"Sum of {nums} is {sum_list(nums)}")
