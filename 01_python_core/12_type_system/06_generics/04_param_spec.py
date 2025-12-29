"""
ParamSpec - 参数规范 (Python 3.10+)

对应文档: 15-type-system-stdlib.md § 15.generics
"""

from typing import ParamSpec, TypeVar, Callable
from functools import wraps
import time

# P 代表参数规范 (形参列表)
# R 代表返回值类型
P = ParamSpec('P')
R = TypeVar('R')

def timer(func: Callable[P, R]) -> Callable[P, R]:
    """
    装饰器：记录执行时间。
    使用 ParamSpec 确保被装饰函数的参数签名不丢失。
    """
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def heavy_computation(x: int, y: int, name: str = "default") -> int:
    """模拟耗时计算"""
    time.sleep(0.1)
    print(f"Processing {name}...")
    return x * y

if __name__ == '__main__':
    # 即使经过装饰，类型检查器依然知道 heavy_computation 需要两个 int 参数
    res = heavy_computation(10, 20, name="Task-1")
    print(f"Result: {res}")
