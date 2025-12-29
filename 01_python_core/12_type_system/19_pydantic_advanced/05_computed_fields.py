"""
计算字段 (Computed Fields)

对应文档: 16-type-system-pydantic.md § 16.advanced
"""

from pydantic import BaseModel, computed_field

class Product(BaseModel):
    name: str
    price: float
    discount: float = 0.0

    # 使用 @computed_field 装饰 property
    # 这使得该属性会出现在 model_dump() 和 model_dump_json() 的结果中
    @computed_field
    @property
    def final_price(self) -> float:
        """计算折后价格"""
        return self.price * (1 - self.discount)

    @computed_field
    def price_label(self) -> str:
        """甚至可以不用 property (但建议使用)"""
        return f"{self.name}: ${self.final_price:.2f}"

if __name__ == '__main__':
    p = Product(name="Smartphone", price=500.0, discount=0.1)
    
    # 1. 正常访问
    print(f"Final Price: {p.final_price}")
    
    # 2. 序列化：你会发现 final_price 和 price_label 出现在了字典中
    data = p.model_dump()
    print(f"Dumped data: {data}")
    
    # 这对于需要将计算逻辑传给前端的场景非常方便
    print(f"JSON with computed: {p.model_dump_json()}")
