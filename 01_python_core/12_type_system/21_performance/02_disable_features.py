"""
禁用不必要的功能

对应文档: 16-type-system-pydantic.md § 16.performance
"""

from pydantic import BaseModel, ConfigDict

class OptimizedModel(BaseModel):
    model_config = ConfigDict(
        # 1. 禁用赋值验证：如果你的代码不会动态修改 user.age = 30，
        # 则关闭此项可以减少每次修改时的开销。
        validate_assignment=False,
        
        # 2. 禁用默认值验证：如果你的默认值是可控且正确的。
        validate_default=False,
        
        # 3. 使用枚举值而非枚举对象
        use_enum_values=True,
    )

    name: str
    score: int = 100

if __name__ == '__main__':
    m = OptimizedModel(name="test")
    print(f"Optimized model: {m}")
