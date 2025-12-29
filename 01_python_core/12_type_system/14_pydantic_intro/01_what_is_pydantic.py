"""
什么是 Pydantic

对应文档: 16-type-system-pydantic.md § 16.intro
"""

from pydantic import BaseModel

# 1. 定义一个简单的模型
class User(BaseModel):
    id: int
    name: str
    signup_ts: int | None = None
    # 甚至可以包含嵌套类型和列表
    friends: list[int] = []

if __name__ == '__main__':
    # 2. 正常数据创建
    external_data = {
        "id": "123",      # 字符串会被自动转为 int
        "name": "John",
        "friends": [1, "2", b"3"] # 列表内的元素也会被递归转换
    }
    
    user = User(**external_data)
    
    print(f"User ID (int): {user.id}")
    print(f"Friends list: {user.friends}")
    print(f"Model representation: {user}")
    
    # 3. 访问属性
    print(f"User Name: {user.name}")
    
    # 4. 导出为字典
    print(f"As dict: {user.model_dump()}")
