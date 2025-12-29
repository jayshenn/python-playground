"""
严格模式提升性能

对应文档: 16-type-system-pydantic.md § 16.performance
"""

from pydantic import BaseModel, ConfigDict

# 在严格模式下，Pydantic 不会尝试解析和转换类型。
# 这减少了逻辑分支，从而在大批量数据处理时更快。

class FastUser(BaseModel):
    model_config = ConfigDict(strict=True)
    
    id: int
    name: str
    age: int

if __name__ == '__main__':
    # 性能提示：
    # 传入正确类型的数据 (int, str, int) 时，严格模式最快。
    user = FastUser(id=1, name="Alice", age=25)
    
    print(f"Validated in strict mode: {user.name}")
    
    # 如果传入 "123"，它会立即抛错，而不是尝试转换。
    # 这种"不成功便成仁"的策略减少了处理损耗。
