"""
严格模式 vs 宽松模式

对应文档: 16-type-system-pydantic.md § 16.basemodel
"""

from pydantic import BaseModel, ConfigDict, ValidationError

# 1. 宽松模式 (Lax Mode - 默认)
class LaxModel(BaseModel):
    item_id: int

# 2. 严格模式 (Strict Mode)
class StrictModel(BaseModel):
    model_config = ConfigDict(strict=True)
    item_id: int

if __name__ == '__main__':
    # 宽松模式允许转换
    lax = LaxModel(item_id="123")
    print(f"Lax value: {lax.item_id}")
    
    # 严格模式禁止转换
    try:
        StrictModel(item_id="123")
    except ValidationError as e:
        print(f"Strict mode rejected string for int: {e.errors()[0]['msg']}")
        
    # 严格模式只接受完全匹配的类型
    strict_ok = StrictModel(item_id=123)
    print(f"Strict OK value: {strict_ok.item_id}")
