"""
验证错误处理

对应文档: 16-type-system-pydantic.md § 16.basemodel
"""

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    name: str
    price: float
    quantity: int

if __name__ == '__main__':
    # 1. 提供错误的数据类型
    invalid_data = {
        "name": "Laptop",
        "price": "not_a_number", # 错误：无法转为 float
        "quantity": "5.5"        # 错误：无法转为 int (丢失精度)
    }
    
    try:
        Product(**invalid_data)
    except ValidationError as e:
        # 2. 打印友好的错误摘要
        print("--- Error Summary ---")
        print(e)
        
        # 3. 获取结构化的错误列表 (常用于 API 返回)
        print("\n--- Structured Errors ---")
        for error in e.errors():
            print(f"Field: {error['loc']}, Message: {error['msg']}, Type: {error['type']}")
            
        # 4. 获取 JSON 格式错误
        # print(e.json())
