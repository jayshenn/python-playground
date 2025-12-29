"""
reveal_type()：调试类型推断

对应文档: 15-type-system-stdlib.md § 15.utils
"""

from typing import reveal_type

# 注意：reveal_type 仅在类型检查期间有效 (如 mypy 或 pyright)。
# 在运行时运行此脚本通常会报错 (除非你使用了特定的运行时工具)。

def complex_inference[T](items: list[T]) -> dict[str, T]:
    result = {"first": items[0]}
    
    # 想要知道 result 在这里的推断类型？
    reveal_type(result) 
    # Mypy 将输出类似: Revealed type is "builtins.dict[builtins.str, T`-1]"
    
    return result

if __name__ == '__main__':
    data = [1, 2, 3]
    res = complex_inference(data)
    
    reveal_type(res)
    # Mypy 将输出: Revealed type is "builtins.dict[builtins.str, builtins.int]"

    print("Note: Run this file with `mypy` to see the reveal_type output.")
