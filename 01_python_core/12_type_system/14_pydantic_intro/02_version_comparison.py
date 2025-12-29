"""
Pydantic 1.x vs 2.x 对比

对应文档: 16-type-system-pydantic.md § 16.intro
"""

from pydantic import BaseModel, ConfigDict

# --- Pydantic 2.x (推荐) ---
class NewUser(BaseModel):
    # 配置现在使用 model_config 字典，而不是内部 Config 类
    model_config = ConfigDict(strict=True) 
    
    id: int
    name: str

    # 常用方法名变更对照表：
    # 1.x: user.dict()      -> 2.x: user.model_dump()
    # 1.x: user.json()      -> 2.x: user.model_dump_json()
    # 1.x: User.parse_obj() -> 2.x: User.model_validate()
    # 1.x: User.schema()    -> 2.x: User.model_json_schema()

if __name__ == '__main__':
    user = NewUser(id=1, name="Alice")
    
    # 使用 2.x 的新方法
    print(f"2.x model dump: {user.model_dump()}")
    print(f"2.x json schema: {NewUser.model_json_schema()}")
