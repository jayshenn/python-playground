"""
嵌套模型

对应文档: 16-type-system-pydantic.md § 16.advanced
"""

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    country: str = "China"

class User(BaseModel):
    name: str
    email: str
    # 嵌套模型
    address: Address

if __name__ == '__main__':
    # 1. 从嵌套字典创建
    user_data = {
        "name": "Alice",
        "email": "alice@msg.com",
        "address": {
            "street": "123 Main St",
            "city": "Beijing"
        }
    }
    
    user = User(**user_data)
    
    # 2. 访问嵌套属性
    print(f"User city: {user.address.city}")
    
    # 3. 序列化会保持嵌套结构
    print(f"Dump JSON: {user.model_dump_json(indent=2)}")
    
    # 4. 验证是递归的。如果 address 中的数据不合法，User 的创建也会失败。
