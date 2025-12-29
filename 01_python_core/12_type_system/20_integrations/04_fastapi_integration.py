"""
FastAPI 集成示例

对应文档: 16-type-system-pydantic.md § 16.integration
"""

# 需要安装: pip install fastapi
try:
    from fastapi import FastAPI
except ImportError:
    print("Please install fastapi to run this example: pip install fastapi")
    import sys
    sys.exit(0)

from pydantic import BaseModel, Field

app = FastAPI()

# 1. 定义请求模型 (Input)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)
    email: str

# 2. 定义响应模型 (Output)
# 隐藏敏感字段 (如 password)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    """
    FastAPI 会自动：
    1. 验证 POST 请求的 JSON 体是否符合 UserCreate
    2. 如果验证失败，自动返回 422 Unprocessable Entity
    3. 将成功的 UserCreate 实例传给此函数
    4. 将返回的对象按照 UserResponse 结构进行过滤和序列化
    """
    print(f"Creating user {user.username}...")
    
    # 模拟保存到数据库
    new_user_db = {
        "id": 1,
        "username": user.username,
        "email": user.email,
        "password": "hashed_password" # 该字段在 UserResponse 中会被排除
    }
    
    return new_user_db

if __name__ == '__main__':
    print("This is a FastAPI app structure. Run it with `uvicorn` to see it in action.")
    # uvicorn 04_fastapi_integration:app --reload
