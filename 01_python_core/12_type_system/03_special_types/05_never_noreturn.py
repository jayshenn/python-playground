"""
Never 和 NoReturn：底部类型

对应文档: 14-type-system-basics.md § 14.special
"""

from typing import NoReturn, Never, Literal

# 1. NoReturn: 函数永远不会正常返回
# (总是抛出异常或进入无限循环)
def stop_program(reason: str) -> NoReturn:
    """该函数执行后，程序将终止或抛出异常"""
    print(f"Stopping: {reason}")
    raise SystemExit(1)

# 2. Never: 表示永远不应该发生的类型 (Python 3.11+)
# 常用于穷举检查 (Exhaustiveness checking)

type Direction = Literal["North", "South", "East", "West"]

def assert_never(value: Never) -> Never:
    """
    一个辅助函数，用于告诉类型检查器：
    '这段代码不应该被执行到'
    """
    raise AssertionError(f"Unhandled value: {value}")

def move(direction: Direction) -> str:
    if direction == "North":
        return "Moving up"
    elif direction == "South":
        return "Moving down"
    elif direction == "East":
        return "Moving right"
    elif direction == "West":
        return "Moving left"
    else:
        # 如果漏掉了某个 Direction 情况，
        # 这里的 direction 类型将不是 Never，类型检查器会报错
        return assert_never(direction)

if __name__ == '__main__':
    print(move("North"))
    
    try:
        stop_program("End of demo")
    except SystemExit:
        print("Caught expected exit")
