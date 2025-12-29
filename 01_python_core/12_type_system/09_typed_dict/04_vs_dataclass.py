"""
TypedDict vs dataclass

对应文档: 15-type-system-stdlib.md § 15.typeddict
"""

from typing import TypedDict
from dataclasses import dataclass
import json

# 1. TypedDict：适用于 JSON/API 数据，序列化方便
class UserDict(TypedDict):
    id: int
    name: str

# 2. dataclass：适用于领域模型，支持方法、逻辑和属性访问
@dataclass
class UserObj:
    id: int
    name: str
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}"

if __name__ == '__main__':
    # --- TypedDict 示例 ---
    d: UserDict = {"id": 1, "name": "Alice"}
    # 优点：天然支持 json.dumps
    print(f"JSON from dict: {json.dumps(d)}")
    # 缺点：必须用字符串索引访问，没有方法
    print(f"Access dict: {d['name']}")
    
    # --- dataclass 示例 ---
    o = UserObj(id=1, name="Alice")
    # 优点：支持点语法访问，支持方法
    print(f"Access obj: {o.name}")
    print(o.greet())
    # 缺点：序列化需要额外转换 (如 vars(o))
    print(f"JSON from obj: {json.dumps(vars(o))}")

"""
总结建议：
- 使用 TypedDict: 当你主要处理原始字典（如来自 requests.json()）且不打算添加业务方法时。
- 使用 dataclass: 当你需要一个真正的"对象"，具有属性验证、默认值、计算属性或业务方法时。
"""
