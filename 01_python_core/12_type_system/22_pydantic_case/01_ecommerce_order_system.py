"""
综合实战：电商订单系统

对应文档: 16-type-system-pydantic.md § 16.case
"""

from pydantic import BaseModel, Field, field_validator, computed_field
from datetime import datetime
from typing import Literal
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ProductItem(BaseModel):
    """订单商品项"""
    product_id: int
    product_name: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    @computed_field
    @property
    def subtotal(self) -> float:
        """计算该项商品的小计"""
        return round(self.quantity * self.unit_price, 2)

class ShippingAddress(BaseModel):
    """收货地址"""
    recipient: str = Field(min_length=1)
    phone: str = Field(pattern=r"^1[3-9]\d{9}$") # 简单的中国手机号正则
    province: str
    city: str
    detail: str = Field(min_length=5)

class Order(BaseModel):
    """订单模型"""
    order_id: str
    user_id: int
    status: OrderStatus = OrderStatus.PENDING
    items: list[ProductItem] = Field(min_length=1)
    shipping_address: ShippingAddress
    created_at: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def total_amount(self) -> float:
        """计算订单总额"""
        return sum(item.subtotal for item in self.items)

    @field_validator('items')
    @classmethod
    def check_items_not_empty(cls, v: list[ProductItem]) -> list[ProductItem]:
        """业务规则：订单必须包含至少一个商品"""
        if not v:
            raise ValueError('订单必须包含至少一个商品')
        return v

if __name__ == '__main__':
    # 创建订单数据
    order_data = {
        "order_id": "ORD-2025-0001",
        "user_id": 9527,
        "items": [
            {"product_id": 1, "product_name": "Python Book", "quantity": 1, "unit_price": 59.9},
            {"product_id": 2, "product_name": "Mechanical Keyboard", "quantity": 1, "unit_price": 499.0}
        ],
        "shipping_address": {
            "recipient": "张三",
            "phone": "13812345678",
            "province": "上海市",
            "city": "上海市",
            "detail": "徐家汇街道某某路 88 号"
        }
    }
    
    # 实例化并自动验证
    order = Order(**order_data)
    
    print(f"Order created for: {order.shipping_address.recipient}")
    print(f"Total Amount: ¥{order.total_amount}")
    
    # 导出 JSON 结果，包含计算出的 subtotal 和 total_amount
    print("\nOrder JSON summary:")
    print(order.model_dump_json(indent=2, ensure_ascii=False))
