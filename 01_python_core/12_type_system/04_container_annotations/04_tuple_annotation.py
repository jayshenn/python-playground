"""
元组注解

对应文档: 14-type-system-basics.md § 14.container
"""

# 1. 固定长度、固定类型的元组
# tuple[T1, T2, ...] 表示具体位置的类型
coordinates: tuple[float, float] = (10.5, 20.3)
rgb_color: tuple[int, int, int] = (255, 128, 0)
user_info: tuple[str, int, bool] = ("Alice", 30, True)

# 2. 可变长度、单一类型的元组
# 使用 ... 表示任意长度
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
names: tuple[str, ...] = ("Alice", "Bob")

# 3. 空元组
empty: tuple[()] = ()

# 4. 函数返回元组
def get_user_location() -> tuple[float, float]:
    """返回 (经度, 纬度)"""
    return 116.397, 39.908

def calculate_average(nums: tuple[float, ...]) -> float:
    """计算变长元组的平均值"""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

if __name__ == '__main__':
    loc = get_user_location()
    print(f"Location: {loc}")
    
    avg = calculate_average((1.0, 2.0, 3.0, 4.0))
    print(f"Average: {avg}")
