"""
Stub 文件 (.pyi)

对应文档: 17-type-system-checkers.md § 17.mypy
"""

# Stub 文件是只包含类型信息的 Python 文件，后缀为 .pyi。
# 它们通常用于为无法修改的二进制模块或没有注解的旧代码提供类型提示。

STUB_EXAMPLE = """
# math_utils.pyi

def add(a: int, b: int) -> int: ...

class Calculator:
    def __init__(self, name: str) -> None: ...
    def power(self, base: float, exp: float) -> float: ...
"""

if __name__ == '__main__':
    print("Mypy 会优先查找同名的 .pyi 文件来获取类型信息。")
    print("这就是为什么你可以给 C 扩展库添加类型提示。")
