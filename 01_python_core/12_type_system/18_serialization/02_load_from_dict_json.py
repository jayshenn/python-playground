"""
从字典和 JSON 加载

对应文档: 16-type-system-pydantic.md § 16.serialization
"""

from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

if __name__ == '__main__':
    # 1. 从字典加载
    raw_dict = {"id": 101, "username": "alice", "email": "alice@msg.com"}
    user1 = User.model_validate(raw_dict)
    print(f"Loaded from dict: {user1.username}")
    
    # 2. 从 JSON 字符串加载
    raw_json = '{"id": 102, "username": "bob", "email": "bob@msg.com"}'
    user2 = User.model_validate_json(raw_json)
    print(f"Loaded from JSON: {user2.username}")
    
    # 注意：model_validate_json 比 json.loads + model_validate 更快
    # 因为它直接在 Rust 层处理 JSON 解析和验证。
