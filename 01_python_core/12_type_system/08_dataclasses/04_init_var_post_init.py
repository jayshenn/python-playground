"""
InitVar 和 __post_init__

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass, field, InitVar
import hashlib

@dataclass
class UserAccount:
    username: str
    email: str
    
    # 1. init=False: 该字段不会出现在自动生成的 __init__ 参数中
    password_hash: str = field(init=False, repr=False)
    
    # 2. InitVar: 该字段仅用于 __init__ 传参，不会存为实例属性
    password: InitVar[str]

    def __post_init__(self, password: str) -> None:
        """
        在自动生成的 __init__ 执行完毕后调用。
        可以在这里处理计算属性、验证或敏感数据转换。
        """
        # 生成密码哈希，而不存储明文密码
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

if __name__ == '__main__':
    # 传入 password，但生成的实例没有 password 属性
    user = UserAccount(
        username="johndoe", 
        email="john@example.com", 
        password="secret_password_123"
    )
    
    print(f"User: {user.username}, Email: {user.email}")
    print(f"Hash: {user.password_hash}")
    
    # 验证没有 password 属性
    print(f"Has password attribute: {hasattr(user, 'password')}")
