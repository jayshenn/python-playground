"""
Protocol 基本概念

对应文档: 15-type-system-stdlib.md § 15.protocol
"""

from typing import Protocol

# 1. 定义协议：规定必须有 draw 方法
class Drawable(Protocol):
    def draw(self) -> str:
        ... # 在协议定义中，方法体通常使用 ...

# 2. 实现类：无需显式继承 Drawable
class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

# 3. 使用协议作为类型注解
def render(obj: Drawable) -> None:
    """接受任何实现了 draw 方法的对象"""
    print(f"Render output: {obj.draw()}")

if __name__ == '__main__':
    # Circle 和 Square 都符合 Drawable 协议
    render(Circle())
    render(Square())
    
    # 以下代码静态检查会报错，因为 str 没有 draw 方法
    # render("not a drawable")
