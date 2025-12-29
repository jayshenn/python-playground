"""
综合实战：泛型 API 客户端

对应文档: 15-type-system-stdlib.md § 15.case
"""

from typing import TypeVar, Generic, Protocol, runtime_checkable
from dataclasses import dataclass
from collections.abc import Callable

# 1. 定义响应对象协议 (鸭子类型)
@runtime_checkable
class ResponseProto(Protocol):
    status_code: int
    def json(self) -> dict: ...

# 2. 定义通用结果包装器 (泛型)
T = TypeVar('T')

@dataclass
class Result(Generic[T]):
    success: bool
    data: T | None = None
    error: str | None = None

# 3. 业务模型
@dataclass
class User:
    id: int
    name: str

@dataclass
class Product:
    sku: str
    price: float

# 4. 泛型 API 客户端实现
class ApiClient[T]:
    """
    一个泛型的 API 客户端，能够根据传入的解析器自动返回正确的模型类型。
    """
    def __init__(self, base_url: str, parser: Callable[[dict], T]):
        self.base_url = base_url
        self.parser = parser

    def request(self, endpoint: str) -> Result[T]:
        """模拟 HTTP 请求逻辑"""
        print(f"GET {self.base_url}/{endpoint}")
        
        try:
            # 模拟获取到原始响应数据
            # 实际场景中会检查 response.status_code == 200 等
            if "error" in endpoint:
                return Result(success=False, error="Resource not found")
            
            # 模拟 JSON 数据
            raw_data = {"id": 1, "name": "Alice", "sku": "ABC-123", "price": 99.0}
            
            # 使用传入的解析器转换为具体模型
            parsed_data = self.parser(raw_data)
            return Result(success=True, data=parsed_data)
        except Exception as e:
            return Result(success=False, error=str(e))

# 5. 解析器函数
def parse_user(data: dict) -> User:
    return User(id=data["id"], name=data["name"])

def parse_product(data: dict) -> Product:
    return Product(sku=data["sku"], price=data["price"])

if __name__ == '__main__':
    # 使用 User 客户端
    user_client = ApiClient(base_url="https://api.v1", parser=parse_user)
    user_res = user_client.request("users/1")
    if user_res.success and user_res.data:
        print(f"Fetched User: {user_res.data.name}")

    # 使用 Product 客户端
    prod_client = ApiClient(base_url="https://api.v1", parser=parse_product)
    prod_res = prod_client.request("products/sku-001")
    if prod_res.success and prod_res.data:
        print(f"Fetched Product SKU: {prod_res.data.sku}")
