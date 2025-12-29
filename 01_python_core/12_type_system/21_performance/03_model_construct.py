"""
使用 model_construct 跳过验证

对应文档: 16-type-system-pydantic.md § 16.performance
"""

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

if __name__ == '__main__':
    # 场景：你刚从受信任的数据库中查出 10000 条数据。
    # 你知道数据已经是合法的了，不需要重新验证。
    
    trust_data = {"id": 1, "name": "Alice", "email": "alice@msg.com"}
    
    # 1. 正常创建 (慢：执行验证)
    user1 = User(**trust_data)
    
    # 2. 构造创建 (极快：跳过验证)
    # 它不会检查类型，也不会检查必填项，只是直接把数据塞进对象
    user2 = User.model_construct(**trust_data)
    
    print(f"Constructed user: {user2.name}")
    
    # 警告：即使数据是错的，model_construct 也不会报错
    bad_user = User.model_construct(id="not_an_int")
    print(f"Bad user ID: {bad_user.id} (No error thrown!)")
