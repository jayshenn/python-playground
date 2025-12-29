"""
模型继承

对应文档: 16-type-system-pydantic.md § 16.basemodel
"""

from pydantic import BaseModel

class BaseUser(BaseModel):
    """基础用户模型"""
    user_id: int
    username: str
    email: str

class AdminUser(BaseUser):
    """管理员模型，继承自 BaseUser 并添加额外字段"""
    # 继承了 user_id, username, email
    role: str = "admin"
    permissions: list[str] = ["read"]

if __name__ == '__main__':
    # 创建管理员实例
    admin = AdminUser(
        user_id=1,
        username="super_alice",
        email="alice@admin.com",
        permissions=["read", "write", "delete"]
    )
    
    print(f"Admin Info: {admin}")
    print(f"Permissions: {admin.permissions}")
    print(f"Is instance of BaseUser: {isinstance(admin, BaseUser)}")
