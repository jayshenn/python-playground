"""
默认值和工厂函数

对应文档: 16-type-system-pydantic.md § 16.fields
"""

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4, UUID

class Order(BaseModel):
    # 1. 静态默认值
    status: str = "pending"
    
    # 2. 动态默认值 (工厂函数)
    # 每次创建新实例时都会调用该函数
    order_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # 3. 容器类型务必使用 factory
    items: list[str] = Field(default_factory=list)

if __name__ == '__main__':
    # 每个订单都会获得不同的 ID 和时间
    o1 = Order()
    import time
    time.sleep(0.01)
    o2 = Order()
    
    print(f"Order 1 ID: {o1.order_id}, Time: {o1.created_at}")
    print(f"Order 2 ID: {o2.order_id}, Time: {o2.created_at}")
    
    # 验证列表是独立生成的，不是共享的
    o1.items.append("laptop")
    print(f"Order 1 items: {o1.items}")
    print(f"Order 2 items: {o2.items}")
