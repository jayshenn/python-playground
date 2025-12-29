"""
装饰器的类型注解 (结合 ParamSpec)

对应文档: 15-type-system-stdlib.md § 15.callable
"""

from typing import TypeVar, ParamSpec, Callable
from functools import wraps

# 定义类型变量以保留原函数的签名
P = ParamSpec('P')
R = TypeVar('R')

def log_execution(func: Callable[P, R]) -> Callable[P, R]:
    """
    通用日志装饰器。
    Callable[P, R] 确保了装饰器的返回函数与原函数具有完全相同的参数 (P) 和返回值 (R) 类型。
    """
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    
    return wrapper

@log_execution
def greet(name: str, age: int) -> str:
    """被装饰的函数"""
    return f"Hello {name}, you are {age} years old."

if __name__ == '__main__':
    # 装饰后的 greet 依然保持正确的类型提示
    msg = greet("Alice", age=30)
    print(msg)
