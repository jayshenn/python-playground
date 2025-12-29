"""
TypedDict 基本用法

对应文档: 15-type-system-stdlib.md § 15.typeddict
"""

from typing import TypedDict

# 1. 定义字典结构
class User(TypedDict):
    id: int
    name: str
    email: str
    is_active: bool

def process_user(u: User) -> None:
    """处理符合 User 结构的字典"""
    print(f"Processing user {u['name']} (ID: {u['id']})")

if __name__ == '__main__':
    # 2. 创建字典 (必须包含所有非可选键)
    alice: User = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True
    }
    
    process_user(alice)
    
    # 3. TypedDict 只是一个字典
    print(f"Type of alice: {type(alice)}") # <class 'dict'>
    
    # 4. 静态检查器会警告以下情况：
    # missing_keys: User = {"id": 2, "name": "Bob"} # 错误：缺少 email 和 is_active
    # extra_keys: User = {**alice, "age": 30} # 错误：多出了 age 键
