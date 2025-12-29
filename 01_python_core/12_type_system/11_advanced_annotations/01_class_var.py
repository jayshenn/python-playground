"""
ClassVar：类变量

对应文档: 15-type-system-stdlib.md § 15.advanced
"""

from typing import ClassVar

class Counter:
    # 1. ClassVar 明确指出该属性由类共享，不应通过实例赋值
    total_count: ClassVar[int] = 0
    
    def __init__(self, name: str):
        self.name: str = name # 实例变量
        # 修改类变量
        Counter.total_count += 1

if __name__ == '__main__':
    c1 = Counter("A")
    c2 = Counter("B")
    
    print(f"Total count from class: {Counter.total_count}")
    print(f"Total count from instance: {c1.total_count}")
    
    # 静态检查器会警告以下行为 (因为 total_count 被标记为 ClassVar):
    # c1.total_count = 100 
