"""
数据类配置选项

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass

# 1. frozen=True: 使实例不可变 (类似元组)
@dataclass(frozen=True)
class Point:
    x: float
    y: float

# 2. order=True: 自动生成比较方法 (__lt__, __le__, 等)
# 默认按字段定义的顺序进行比较
@dataclass(order=True)
class Person:
    # 调整定义顺序可以改变排序逻辑
    age: int
    name: str

# 3. slots=True: 使用 __slots__ 优化内存并提升属性访问速度 (Python 3.10+)
@dataclass(slots=True)
class OptimizedUser:
    id: int
    username: str

if __name__ == '__main__':
    # 测试 frozen
    pt = Point(1.0, 2.0)
    try:
        pt.x = 3.0 # type: ignore
    except Exception as e:
        print(f"Frozen error: {e}")
        
    # 测试 order
    people = [Person(30, "Bob"), Person(25, "Alice")]
    print(f"Sorted people: {sorted(people)}") # 按 age 排序
    
    # 测试 slots
    user = OptimizedUser(1, "alice")
    print(f"User: {user.username}")
    # slots 类没有 __dict__
    print(f"Has __dict__: {hasattr(user, '__dict__')}")
