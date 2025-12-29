"""
带属性的协议

对应文档: 15-type-system-stdlib.md § 15.protocol
"""

from typing import Protocol

class Named(Protocol):
    # 协议要求实现者必须具有 name 属性 (str 类型)
    name: str

class Product:
    def __init__(self, name: str, price: float):
        self.name = name  # 实现了属性要求
        self.price = price

class User:
    def __init__(self, name: str):
        self.name = name  # 实现了属性要求

def print_name(obj: Named) -> None:
    """该函数不关心 obj 是产品还是用户，只要它有名字"""
    print(f"Name attribute: {obj.name}")

if __name__ == '__main__':
    p = Product("iPhone", 999.9)
    u = User("Alice")
    
    print_name(p)
    print_name(u)
