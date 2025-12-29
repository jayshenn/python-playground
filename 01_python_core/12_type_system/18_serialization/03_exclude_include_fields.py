"""
包含与排除字段

对应文档: 16-type-system-pydantic.md § 16.serialization
"""

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    # 1. 在定义时永久排除 (例如密码、内部 ID)
    password_hash: str = Field(exclude=True)
    internal_token: str

if __name__ == '__main__':
    user = User(
        id=1, 
        username="alice", 
        password_hash="SECRET_HASH", 
        internal_token="TOKEN_123"
    )
    
    # 2. 默认 dump: password_hash 会被自动排除
    print(f"Default dump: {user.model_dump()}")
    
    # 3. 动态排除特定字段
    print(f"Exclude internal_token: {user.model_dump(exclude={'internal_token'})}")
    
    # 4. 只包含特定字段
    print(f"Only include username: {user.model_dump(include={'username'})}")
