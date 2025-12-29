"""
注释的作用

对应文档: 01-python-basics.md § 1.1.2
"""

# 1. 提高代码可读性
# 2. 帮助他人理解代码逻辑
# 3. 方便后期维护和修改
# 4. 记录重要的设计决策
# 5. 临时禁用某段代码


def calculate_area(radius):
    """
    计算圆的面积

    参数:
        radius: 圆的半径
    返回:
        圆的面积
    """
    pi = 3.14159  # 使用高精度的 PI 值
    return pi * (radius**2)


# 测试函数
# print(calculate_area(5))  # 暂时禁用此行
print(f"半径为 10 的圆面积: {calculate_area(10)}")
