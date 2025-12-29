"""
泛型模型

对应文档: 16-type-system-pydantic.md § 16.advanced
"""

from pydantic import BaseModel
from typing import Generic, TypeVar

# 定义类型变量
T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    """通用的 API 响应结构"""
    success: bool
    data: T | None = None
    error: str | None = None

class User(BaseModel):
    id: int
    name: str

if __name__ == '__main__':
    # 1. 使用 User 填充泛型
    user_resp = Response[User](
        success=True,
        data=User(id=1, name="Alice")
    )
    print(f"User Response: {user_resp.data.name if user_resp.data else 'None'}")
    
    # 2. 使用列表填充泛型
    list_resp = Response[list[int]](
        success=True,
        data=[1, 2, 3]
    )
    print(f"List Response Data: {list_resp.data}")
    
    # 3. 序列化
    print(user_resp.model_dump_json())
