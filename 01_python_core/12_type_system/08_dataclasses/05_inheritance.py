"""
数据类继承

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass

@dataclass
class BaseEntity:
    id: int
    created_at: str

@dataclass
class User(BaseEntity):
    """子类会自动合并父类的字段"""
    username: str
    email: str

@dataclass
class Admin(User):
    """多层继承"""
    role: str = "superadmin"

if __name__ == '__main__':
    # 构造函数参数顺序: BaseEntity.id -> BaseEntity.created_at -> User.username -> User.email
    user = User(1, "2023-01-01", "alice", "alice@example.com")
    print(f"User: {user}")
    
    admin = Admin(2, "2023-02-01", "bob", "bob@example.com")
    print(f"Admin: {admin}")
    
    # 注意：如果父类有默认值的字段，子类定义的所有字段也必须有默认值
    # 否则会抛出参数顺序错误 (TypeError)
