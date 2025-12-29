"""
JSON Schema 生成

对应文档: 16-type-system-pydantic.md § 16.serialization
"""

from pydantic import BaseModel, Field

class Product(BaseModel):
    """一个简单的产品模型，用于展示 Schema 生成"""
    name: str = Field(..., description="产品名称")
    price: float = Field(..., gt=0, description="价格，必须大于 0")
    tags: list[str] = Field(default_factory=list)

if __name__ == '__main__':
    # 1. 生成标准的 JSON Schema (字典形式)
    schema = Product.model_json_schema()
    
    # 2. 打印关键部分
    print("--- JSON Schema Keys ---")
    print(schema.keys())
    
    print("\n--- Properties ---")
    import json
    print(json.dumps(schema['properties'], indent=2, ensure_ascii=False))
    
    # 3. 这对于 OpenAPI/Swagger 等工具的自动生成至关重要
