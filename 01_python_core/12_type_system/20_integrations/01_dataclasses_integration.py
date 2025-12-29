"""
与 dataclasses 集成

对应文档: 16-type-system-pydantic.md § 16.integration
"""

# 使用 Pydantic 提供的 dataclass 装饰器，而不是标准库的
from pydantic.dataclasses import dataclass
from pydantic import Field, ValidationError

@dataclass
class User:
    """
    这是一个增强版的 dataclass。
    它保留了 dataclass 的特性 (如 .name 访问)，
    同时在初始化时执行 Pydantic 验证。
    """
    id: int
    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=0, le=120)

if __name__ == '__main__':
    # 1. 正常创建
    u = User(id=1, name="Alice", age=25)
    print(f"Dataclass User: {u.name}")
    
    # 2. 触发验证
    try:
        User(id=2, name="A", age=-1)
    except ValidationError as e:
        print(f"Validation failed: {e.errors()[0]['msg']}")
        
    # 优点：如果你不想让你的模型继承 BaseModel (为了保持与旧代码兼容)，
    # 这是最佳选择。
