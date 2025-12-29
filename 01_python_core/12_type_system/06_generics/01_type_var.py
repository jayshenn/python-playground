"""
TypeVar 类型变量

对应文档: 15-type-system-stdlib.md § 15.generics
"""

from typing import TypeVar

# 1. 现代推荐语法 (Python 3.12+)
# 直接在函数名后加 [T]
def first[T](items: list[T]) -> T:
    """返回列表第一个元素，并自动保留其类型"""
    return items[0]

# 2. 约束类型变量 (限制只能是特定几种类型之一)
# 语法: [T: (type1, type2)]
def add[T: (int, float)](a: T, b: T) -> T:
    """只接受 int 或 float 类型的加法"""
    return a + b # type: ignore (mypy 可能需要忽略)

# 3. 指定上界 (Bound)
# 限制 T 必须是某个类或其子类
class Animal:
    def speak(self) -> str: return "..."

class Dog(Animal):
    def speak(self) -> str: return "Woof!"

def make_speak[T: Animal](animal: T) -> str:
    """只接受 Animal 及其子类"""
    return animal.speak()

# 4. 传统语法 (兼容 Python 3.11 及以下)
T_old = TypeVar('T_old')
def get_last(items: list[T_old]) -> T_old:
    return items[-1]

if __name__ == '__main__':
    # 测试泛型推断
    n = first([1, 2, 3])      # n 被推断为 int
    s = first(["a", "b"])     # s 被推断为 str
    print(f"Int: {n}, Str: {s}")
    
    # 测试约束
    print(f"Sum: {add(10, 20.5)}")
    
    # 测试上界
    print(f"Dog says: {make_speak(Dog())}")
