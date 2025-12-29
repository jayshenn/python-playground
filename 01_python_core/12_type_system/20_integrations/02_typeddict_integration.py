"""
与 TypedDict 集成

对应文档: 16-type-system-pydantic.md § 16.integration
"""

from typing import TypedDict
from pydantic import TypeAdapter, ValidationError

class UserDict(TypedDict):
    id: int
    username: str
    email: str

if __name__ == '__main__':
    # 1. 创建 TypeAdapter
    adapter = TypeAdapter(UserDict)
    
    # 2. 验证原始字典
    raw_data = {"id": "101", "username": "alice", "email": "alice@msg.com"}
    
    try:
        # validate_python 会执行类型转换和验证
        validated_data = adapter.validate_python(raw_data)
        print(f"Validated Dict: {validated_data}")
        print(f"ID type: {type(validated_data['id'])}") # 已转为 int
        
    except ValidationError as e:
        print(e)
        
    # 3. 也可以用于验证非模型类型 (如 list[int])
    list_adapter = TypeAdapter(list[int])
    print(list_adapter.validate_python(["1", "2", "3"])) # [1, 2, 3]
