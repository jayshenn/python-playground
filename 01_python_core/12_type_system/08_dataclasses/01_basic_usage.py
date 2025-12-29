"""
dataclasses 基本用法

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass

@dataclass
class User:
    """用户类"""
    id: int
    name: str
    email: str
    active: bool = True  # 带有默认值的字段

if __name__ == '__main__':
    # 1. 自动生成 __init__
    user1 = User(id=1, name="Alice", email="alice@example.com")
    
    # 2. 自动生成 __repr__ (清晰的打印输出)
    print(f"User representation: {user1}")
    
    # 3. 自动生成 __eq__ (基于值的比较)
    user2 = User(id=1, name="Alice", email="alice@example.com")
    print(f"User1 == User2: {user1 == user2}") # True
    
    # 4. 修改属性
    user1.active = False
    print(f"Modified user: {user1}")
