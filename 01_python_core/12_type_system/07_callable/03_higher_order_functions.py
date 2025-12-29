"""
高阶函数：返回函数的函数

对应文档: 15-type-system-stdlib.md § 15.callable
"""

from collections.abc import Callable

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    返回一个函数，该函数将输入乘以 factor。
    返回值类型为 Callable[[int], int]
    """
    def multiplier(x: int) -> int:
        return x * factor
    
    return multiplier

def get_formatter(prefix: str) -> Callable[[str], str]:
    """返回一个带前缀的格式化函数"""
    return lambda s: f"[{prefix}] {s}"

if __name__ == '__main__':
    # 创建乘法器
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {double(5)}") # 10
    print(f"Triple 5: {triple(5)}") # 15
    
    # 创建格式化器
    info_log = get_formatter("INFO")
    print(info_log("Server started"))
