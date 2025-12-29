"""
配置 ConfigDict

对应文档: 16-type-system-pydantic.md § 16.advanced
"""

from pydantic import BaseModel, ConfigDict, ValidationError

class User(BaseModel):
    # 1. 使用 ConfigDict 进行全局配置
    model_config = ConfigDict(
        # 赋值时也执行验证 (默认 False)
        validate_assignment=True,
        
        # 额外字段处理: 'allow' (允许), 'ignore' (忽略 - 默认), 'forbid' (禁止)
        extra='forbid',
        
        # 冻结模型 (不可变)
        frozen=False,
        
        # 字符串去前后空格
        str_strip_whitespace=True
    )

    name: str
    age: int

if __name__ == '__main__':
    user = User(name=" Alice ", age=25)
    
    # 测试 str_strip_whitespace
    print(f"Name stripped: '{user.name}'") # 'Alice'
    
    # 测试 extra='forbid'
    try:
        User(name="Bob", age=30, city="NYC")
    except ValidationError as e:
        print(f"Extra field error: {e.errors()[0]['msg']}")
        
    # 测试 validate_assignment=True
    try:
        user.age = "not_a_number" # type: ignore
    except ValidationError:
        print("Assignment validation failed as expected.")
