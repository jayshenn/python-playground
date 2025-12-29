"""
TypeVarTuple - 可变泛型 (Python 3.11+)

对应文档: 15-type-system-stdlib.md § 15.generics
"""

from typing import TypeVarTuple

# 定义可变类型变量
Ts = TypeVarTuple('Ts')

# 使用 Python 3.12+ 语法 [T, *Ts]
def move_first_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    """
    接收一个元组，将第一个元素移动到末尾。
    *Ts 捕获元组中间的所有类型。
    """
    # 在运行时，tup 是一个普通的元组
    return (*tup[1:], tup[0])

if __name__ == '__main__':
    # 示例 1: (int, str, bool) -> (str, bool, int)
    r1 = move_first_to_last((1, "hello", True))
    print(f"Result 1: {r1}, Types: {type(r1[0])}, {type(r1[1])}, {type(r1[2])}")
    
    # 示例 2: 不同长度的元组
    r2 = move_first_to_last(("start", 1, 2, 3, "end"))
    print(f"Result 2: {r2}")
