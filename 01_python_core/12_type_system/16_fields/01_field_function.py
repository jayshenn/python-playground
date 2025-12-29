"""
Field 函数基础

对应文档: 16-type-system-pydantic.md § 16.fields
"""

from pydantic import BaseModel, Field

class Product(BaseModel):
    """产品模型"""
    
    # 1. 使用 ... 表示必需字段 (无默认值)
    # min_length, max_length 是字符串约束
    name: str = Field(..., min_length=1, max_length=50, description="产品名称")
    
    # 2. 数值约束: gt (大于), le (小于等于)
    price: float = Field(..., gt=0, description="产品单价，必须大于 0")
    
    # 3. 带有默认值的字段
    quantity: int = Field(default=0, ge=0, description="库存数量")

if __name__ == '__main__':
    # 正常创建
    p = Product(name="Coffee", price=25.5)
    print(f"Product: {p.name}, Price: {p.price}, Qty: {p.quantity}")
    
    # 查看字段描述 (这在自动生成文档时很有用)
    print(f"Price description: {Product.model_fields['price'].description}")
