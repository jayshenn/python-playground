"""
字段约束详解

对应文档: 16-type-system-pydantic.md § 16.fields
"""

from pydantic import BaseModel, Field, ValidationError

class UserProfile(BaseModel):
    # 1. 字符串约束: 长度 + 正则表达式 (pattern)
    username: str = Field(
        min_length=3, 
        max_length=20, 
        pattern=r"^[a-zA-Z0-9_]+$" # 只允许字母数字下划线
    )
    
    # 2. 数值约束: ge (>=), le (<=)
    age: int = Field(ge=0, le=150)
    
    # 3. 集合约束: 元素个数限制
    tags: list[str] = Field(default_factory=list, max_length=5)

if __name__ == '__main__':
    try:
        # 尝试创建一个不符合约束的用户
        UserProfile(username="a!", age=200, tags=["1", "2", "3", "4", "5", "6"])
    except ValidationError as e:
        for error in e.errors():
            print(f"Error in {error['loc']}: {error['msg']}")
            
    # 正确的示例
    ok_user = UserProfile(username="alice_2025", age=25, tags=["python", "pydantic"])
    print(f"User validated: {ok_user.username}")
