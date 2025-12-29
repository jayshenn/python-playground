"""
第一个 Pydantic 模型

对应文档: 16-type-system-pydantic.md § 16.basemodel
"""

from pydantic import BaseModel

# 1. 定义模型
class User(BaseModel):
    """用户模型定义"""
    id: int
    name: str
    email: str
    # 2. 设置默认值
    is_active: bool = True

if __name__ == '__main__':
    # 3. 创建实例 (正常数据)
    user = User(id=1, name="Alice", email="alice@example.com")
    print(f"User object: {user}")
    
    # 4. 自动类型转换 (智能解析)
    # Pydantic 默认处于宽松模式，会尝试转换数据类型
    user2 = User(
        id="123",           # 字符串转 int
        name="Bob", 
        email="bob@msg.com",
        is_active="false"   # 字符串 "false" 转 bool False
    )
    
    print(f"User2 ID type: {type(user2.id)}")       # <class 'int'>
    print(f"User2 Active: {user2.is_active}")     # False
    
    # 5. 访问字段
    print(f"Name: {user.name}")
