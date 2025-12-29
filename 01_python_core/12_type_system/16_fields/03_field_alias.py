"""
字段别名

对应文档: 16-type-system-pydantic.md § 16.fields
"""

from pydantic import BaseModel, Field

class ExternalUser(BaseModel):
    """
    映射外部 API 的数据结构。
    外部使用 camelCase (驼峰命名)，Python 推荐 snake_case (蛇形命名)。
    """
    user_id: int = Field(alias="userId")
    user_name: str = Field(alias="userName")
    email_addr: str = Field(alias="emailAddress")

if __name__ == '__main__':
    # 1. 输入数据使用别名
    api_response = {
        "userId": 1001,
        "userName": "alice_api",
        "emailAddress": "alice@api.com"
    }
    
    # 使用解包传入，Pydantic 会自动根据 alias 匹配
    user = ExternalUser(**api_response)
    
    # 2. Python 内部使用 snake_case 访问
    print(f"Internal access: {user.user_id}, {user.user_name}")
    
    # 3. 序列化时选择是否使用别名
    print("\nDump without alias (Pythonic):")
    print(user.model_dump())
    
    print("\nDump with alias (For API response):")
    print(user.model_dump(by_alias=True))
