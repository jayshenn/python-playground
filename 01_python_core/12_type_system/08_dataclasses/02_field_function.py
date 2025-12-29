"""
field() 函数和元数据

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass, field, fields

@dataclass
class Product:
    name: str
    price: float
    # 1. 可变默认值必须使用 default_factory
    # 直接使用 tags: list[str] = [] 会导致所有实例共享同一个列表
    tags: list[str] = field(default_factory=list)
    
    # 2. 控制是否出现在 repr 中 (例如敏感信息或内部 ID)
    _internal_id: int = field(default=0, repr=False)
    
    # 3. 添加自定义元数据 (Metadata)
    # 元数据不影响 dataclass 行为，但可以被第三方库或自定义逻辑读取
    quantity: int = field(default=1, metadata={"unit": "pcs", "min_value": 1})

if __name__ == '__main__':
    p1 = Product("Laptop", 999.9)
    p2 = Product("Mouse", 25.0)
    
    # 测试 default_factory
    p1.tags.append("electronics")
    print(f"P1 tags: {p1.tags}")
    print(f"P2 tags: {p2.tags}") # 依然是空列表，未共享
    
    # 测试 repr=False
    print(f"Product repr: {p1}") # 不会显示 _internal_id
    
    # 测试元数据读取
    quantity_field = [f for f in fields(Product) if f.name == 'quantity'][0]
    print(f"Quantity unit: {quantity_field.metadata['unit']}")
