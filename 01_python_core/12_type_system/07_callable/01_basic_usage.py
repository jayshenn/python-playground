"""
Callable 基本用法

对应文档: 15-type-system-stdlib.md § 15.callable
"""

from collections.abc import Callable

# 1. 基本语法: Callable[[参数1, 参数2], 返回类型]
def execute_op(a: int, b: int, op: Callable[[int, int], int]) -> int:
    """接受两个整数和一个操作函数，返回计算结果"""
    return op(a, b)

def add(x: int, y: int) -> int: return x + y
def multiply(x: int, y: int) -> int: return x * y

# 2. 无参数函数
def run_task(task: Callable[[], None]) -> None:
    print("Starting task...")
    task()
    print("Task finished.")

def say_hello() -> None: print("Hello World!")

# 3. 接受任意参数，返回特定类型
def logger(func: Callable[..., str], *args: any, **kwargs: any) -> None:
    result = func(*args, **kwargs)
    print(f"Log: {result}")

if __name__ == '__main__':
    # 测试基本用法
    print(f"5 + 3 = {execute_op(5, 3, add)}")
    print(f"5 * 3 = {execute_op(5, 3, multiply)}")
    
    # 测试无参
    run_task(say_hello)
    
    # 测试任意参数
    logger(lambda name: f"Hello {name}", "Alice")
