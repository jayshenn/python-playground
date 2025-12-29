"""
TypedDict 可选键

对应文档: 15-type-system-stdlib.md § 15.typeddict
"""

from typing import TypedDict, NotRequired

# 1. 使用 NotRequired 定义具体的可选键 (Python 3.11+ 推荐)
class UserProfile(TypedDict):
    username: str
    email: str
    # bio 和 website 是可选的
    bio: NotRequired[str]
    website: NotRequired[str]

# 2. 使用 total=False 使所有键都变为可选 (Python 3.8+)
class PartialUser(TypedDict, total=False):
    id: int
    name: str
    age: int

if __name__ == '__main__':
    # 有效：只包含必需键
    u1: UserProfile = {"username": "alice", "email": "alice@msg.com"}
    
    # 有效：包含部分可选键
    u2: UserProfile = {
        "username": "bob", 
        "email": "bob@msg.com",
        "bio": "Python developer"
    }
    
    # PartialUser 的所有键都是可选的
    p1: PartialUser = {"id": 101}
    p2: PartialUser = {"name": "Charlie", "age": 20}
    
    print(f"U1: {u1}")
    print(f"U2: {u2}")
    print(f"P1: {p1}")
