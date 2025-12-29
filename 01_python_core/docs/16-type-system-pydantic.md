# Python 类型系统 - Pydantic 实战篇

## 目录

- [Pydantic 简介](#pydantic-简介)
- [BaseModel 基础](#basemodel-基础)
- [字段配置 (Fields)](#字段配置-fields)
- [数据验证](#数据验证)
- [序列化与反序列化](#序列化与反序列化)
- [高级特性](#高级特性)
- [与其他库集成](#与其他库集成)
- [性能优化](#性能优化)

---

## Pydantic 简介

### 什么是 Pydantic

Pydantic 是一个数据验证库，使用 Python 类型注解来验证数据。其核心用 Rust 编写，性能出色。

**核心特性**：
- 🚀 **高性能**：核心验证逻辑用 Rust 实现
- 📝 **类型驱动**：基于 Python 类型注解自动验证
- 🔄 **智能转换**：支持严格模式和宽松模式
- 📊 **JSON Schema**：自动生成 JSON Schema
- 🌐 **广泛集成**：FastAPI、LangChain 等 8000+ 包使用

### Pydantic 1.x vs 2.x

| 特性 | Pydantic 1.x | Pydantic 2.x |
|------|--------------|--------------|
| 核心实现 | Python | Rust (pydantic-core) |
| 性能 | 基准 | 5-50x 提升 |
| 配置方式 | `Config` 类 | `ConfigDict` |
| 验证器语法 | `@validator` | `@field_validator` |
| JSON Schema | `schema()` | `model_json_schema()` |
| 序列化 | `dict()`, `json()` | `model_dump()`, `model_dump_json()` |

⚠️ **重要**：本文档基于 Pydantic 2.x（推荐版本）

### 安装

```bash
# 安装 Pydantic 2.x
uv add pydantic

# 或使用 pip
pip install pydantic

# 安装额外功能（如 email 验证）
uv add "pydantic[email]"
```

---

## BaseModel 基础

### 第一个 Pydantic 模型

```python
from pydantic import BaseModel

class User(BaseModel):
    """用户模型"""
    id: int
    name: str
    email: str
    is_active: bool = True  # 默认值

# 创建实例（自动验证）
user = User(id=1, name="Alice", email="alice@example.com")
print(user)
# User(id=1, name='Alice', email='alice@example.com', is_active=True)

# 访问字段
print(user.name)  # Alice
print(user.is_active)  # True

# 自动类型转换（宽松模式，默认）
user2 = User(id="123", name="Bob", email="bob@example.com", is_active="yes")
print(user2.id)  # 123 (str 转 int)
print(user2.is_active)  # True (非空字符串转 True)
```

### 验证错误处理

```python
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    name: str
    price: float
    quantity: int

# 捕获验证错误
try:
    # price 不能是字符串 "invalid"
    product = Product(name="Laptop", price="invalid", quantity="10")
except ValidationError as e:
    print(e)
    """
    输出：
    2 validation errors for Product
    price
      Input should be a valid number, unable to parse string as a number
    quantity
      Input should be a valid integer, unable to parse string as an integer
    """

# 获取详细错误信息
try:
    product = Product(name="Laptop", price="abc", quantity=5)
except ValidationError as e:
    print(e.json())  # JSON 格式的错误信息
    print(e.errors())  # 错误列表
    """
    [
        {
            'type': 'float_parsing',
            'loc': ('price',),
            'msg': 'Input should be a valid number...',
            'input': 'abc'
        }
    ]
    """
```

### 严格模式 vs 宽松模式

```python
from pydantic import BaseModel, ConfigDict

# 宽松模式（默认）：尝试类型转换
class LaxUser(BaseModel):
    id: int
    age: int

lax_user = LaxUser(id="123", age="25")
print(lax_user.id)  # 123 (成功转换)

# 严格模式：不允许类型转换
class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    age: int

try:
    strict_user = StrictUser(id="123", age=25)
except ValidationError as e:
    print("严格模式拒绝了字符串")  # 会触发错误
```

### 模型继承

```python
from pydantic import BaseModel

class BaseUser(BaseModel):
    """基础用户"""
    id: int
    name: str
    email: str

class AdminUser(BaseUser):
    """管理员用户，继承 BaseUser"""
    role: str = "admin"
    permissions: list[str]

admin = AdminUser(
    id=1,
    name="Admin",
    email="admin@example.com",
    permissions=["read", "write", "delete"]
)
print(admin)
# AdminUser(id=1, name='Admin', email='admin@example.com',
#           role='admin', permissions=['read', 'write', 'delete'])
```

---

## 字段配置 (Fields)

### Field 函数

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    """产品模型"""
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="产品价格，必须大于 0")
    quantity: int = Field(default=0, ge=0, description="库存数量")
    tags: list[str] = Field(default_factory=list, max_length=10)
    description: str | None = Field(default=None, max_length=500)

# ... 表示必需字段（无默认值）
product = Product(name="Laptop", price=999.99, quantity=5)
print(product)

# 验证会检查约束
try:
    Product(name="", price=-10, quantity=5)  # name 太短，price 为负
except ValidationError as e:
    print(e)
```

### 字段约束

```python
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    # 字符串约束
    username: str = Field(min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")

    # 数值约束
    age: int = Field(ge=0, le=150)  # ge: >=, le: <=
    score: float = Field(gt=0, lt=100)  # gt: >, lt: <

    # 集合约束
    tags: list[str] = Field(max_length=5)  # 最多 5 个元素
    metadata: dict[str, str] = Field(default_factory=dict)

# 测试
profile = UserProfile(
    username="alice_123",
    age=25,
    score=95.5,
    tags=["python", "typing"]
)
```

### 字段别名

```python
from pydantic import BaseModel, Field

class ApiUser(BaseModel):
    """API 响应中的用户数据"""
    user_id: int = Field(alias="userId")  # JSON 中是 userId
    user_name: str = Field(alias="userName")
    email_address: str = Field(alias="emailAddress")

# 从 API 数据创建（使用别名）
api_data = {
    "userId": 123,
    "userName": "Alice",
    "emailAddress": "alice@example.com"
}
user = ApiUser(**api_data)
print(user.user_id)  # 123

# 序列化时也使用别名
print(user.model_dump(by_alias=True))
# {'userId': 123, 'userName': 'Alice', 'emailAddress': 'alice@example.com'}
```

### 默认值和工厂函数

```python
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

class Order(BaseModel):
    # 静态默认值
    status: str = "pending"

    # 工厂函数（每次创建时调用）
    order_id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)
    items: list[str] = Field(default_factory=list)

# 每个实例有独立的默认值
order1 = Order()
order2 = Order()

print(order1.order_id)  # 唯一 ID
print(order2.order_id)  # 不同的唯一 ID
print(order1.created_at)  # 创建时间
```

---

## 数据验证

### 内置验证器

```python
from pydantic import BaseModel, EmailStr, HttpUrl, conint, constr

# 需要安装: uv add "pydantic[email]"

class User(BaseModel):
    # Email 验证
    email: EmailStr

    # URL 验证
    website: HttpUrl | None = None

    # 带约束的类型
    age: conint(ge=0, le=150)  # 约束整数
    username: constr(min_length=3, max_length=20)  # 约束字符串

user = User(
    email="alice@example.com",
    website="https://example.com",
    age=25,
    username="alice"
)

# 验证失败示例
try:
    User(email="invalid-email", age=-1, username="ab")
except ValidationError as e:
    print(e)
```

### 自定义字段验证器

```python
from pydantic import BaseModel, field_validator

class UserRegistration(BaseModel):
    username: str
    password: str
    password_confirm: str

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """用户名必须是字母数字"""
        if not v.isalnum():
            raise ValueError('用户名必须是字母和数字')
        return v

    @field_validator('password')
    @classmethod
    def password_strength(cls, v: str) -> str:
        """密码强度检查"""
        if len(v) < 8:
            raise ValueError('密码至少 8 位')
        if not any(c.isupper() for c in v):
            raise ValueError('密码必须包含大写字母')
        if not any(c.isdigit() for c in v):
            raise ValueError('密码必须包含数字')
        return v

# 测试
try:
    user = UserRegistration(
        username="alice",
        password="Password123",
        password_confirm="Password123"
    )
    print("验证通过")
except ValidationError as e:
    print(e)
```

### 模型验证器

```python
from pydantic import BaseModel, model_validator

class UserRegistration(BaseModel):
    username: str
    password: str
    password_confirm: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UserRegistration':
        """检查两次密码是否一致（模型级别验证）"""
        if self.password != self.password_confirm:
            raise ValueError('两次密码不一致')
        return self

# 测试
try:
    user = UserRegistration(
        username="alice",
        password="Password123",
        password_confirm="DifferentPassword"
    )
except ValidationError as e:
    print(e)  # 两次密码不一致
```

### 条件验证

```python
from pydantic import BaseModel, field_validator, model_validator
from typing import Literal

class Payment(BaseModel):
    method: Literal["credit_card", "paypal", "bank_transfer"]
    amount: float

    # 信用卡相关字段
    card_number: str | None = None
    cvv: str | None = None

    # PayPal 相关字段
    paypal_email: str | None = None

    # 银行转账相关字段
    bank_account: str | None = None

    @model_validator(mode='after')
    def check_payment_details(self) -> 'Payment':
        """根据支付方式验证必需字段"""
        if self.method == "credit_card":
            if not self.card_number or not self.cvv:
                raise ValueError('信用卡支付需要卡号和 CVV')
        elif self.method == "paypal":
            if not self.paypal_email:
                raise ValueError('PayPal 支付需要邮箱')
        elif self.method == "bank_transfer":
            if not self.bank_account:
                raise ValueError('银行转账需要账号')
        return self

# 有效的支付
payment = Payment(
    method="credit_card",
    amount=100.0,
    card_number="1234567890123456",
    cvv="123"
)

# 无效的支付
try:
    Payment(method="credit_card", amount=100.0)  # 缺少卡号和 CVV
except ValidationError as e:
    print(e)
```

---

## 序列化与反序列化

### 导出为字典和 JSON

```python
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    name: str
    timestamp: datetime
    participants: list[str]

event = Event(
    name="Meeting",
    timestamp=datetime(2025, 1, 15, 10, 0),
    participants=["Alice", "Bob"]
)

# 导出为字典
print(event.model_dump())
# {'name': 'Meeting',
#  'timestamp': datetime.datetime(2025, 1, 15, 10, 0),
#  'participants': ['Alice', 'Bob']}

# 导出为 JSON（自动处理 datetime）
print(event.model_dump_json())
# {"name":"Meeting","timestamp":"2025-01-15T10:00:00","participants":["Alice","Bob"]}

# 导出为 JSON，格式化
print(event.model_dump_json(indent=2))
```

### 从字典和 JSON 加载

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# 从字典创建
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
user = User(**user_data)
# 或
user = User.model_validate(user_data)

# 从 JSON 字符串创建
json_str = '{"id": 2, "name": "Bob", "email": "bob@example.com"}'
user2 = User.model_validate_json(json_str)
print(user2)
```

### 排除和包含字段

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str = Field(exclude=True)  # 总是排除
    internal_id: int

user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    password_hash="hashed_password",
    internal_id=999
)

# 排除敏感字段
print(user.model_dump())
# password_hash 已被排除

# 动态排除字段
print(user.model_dump(exclude={"internal_id"}))
# {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}

# 只包含特定字段
print(user.model_dump(include={"id", "name"}))
# {'id': 1, 'name': 'Alice'}
```

### JSON Schema 生成

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    """产品模型"""
    name: str = Field(..., description="产品名称")
    price: float = Field(..., gt=0, description="产品价格")
    tags: list[str] = Field(default_factory=list)

# 生成 JSON Schema
schema = Product.model_json_schema()
print(schema)
"""
{
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'description': '产品名称'},
        'price': {'type': 'number', 'exclusiveMinimum': 0.0, 'description': '产品价格'},
        'tags': {'type': 'array', 'items': {'type': 'string'}, 'default': []}
    },
    'required': ['name', 'price']
}
"""
```

---

## 高级特性

### 配置 ConfigDict

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        # 字段验证赋值时也触发
        validate_assignment=True,

        # 允许额外字段
        extra='allow',

        # 冻结模型（不可变）
        frozen=False,

        # 使用枚举值而不是枚举对象
        use_enum_values=True,

        # 字段别名生成器
        alias_generator=lambda field_name: field_name.title(),

        # 严格模式
        strict=False,
    )

    name: str
    age: int

user = User(name="Alice", age=25)

# validate_assignment=True 使赋值也会验证
user.age = 30  # ✅
# user.age = "invalid"  # ❌ 验证错误

# extra='allow' 允许额外字段
user2 = User(name="Bob", age=25, city="NYC")
print(user2.model_dump())  # 包含 city
```

### 嵌套模型

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    name: str
    email: str
    address: Address  # 嵌套模型

# 创建嵌套数据
user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}

user = User(**user_data)
print(user.address.city)  # New York

# 序列化保持嵌套结构
print(user.model_dump())
```

### 泛型模型

```python
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    """通用响应模型"""
    success: bool
    data: T | None
    error: str | None = None

class User(BaseModel):
    id: int
    name: str

# 使用泛型模型
user_response = Response[User](
    success=True,
    data=User(id=1, name="Alice")
)

list_response = Response[list[str]](
    success=True,
    data=["item1", "item2"]
)

print(user_response.data.name)  # Alice
```

### RootModel - 根类型

```python
from pydantic import RootModel

# 列表模型
class UserList(RootModel[list[str]]):
    """用户名列表"""
    pass

users = UserList(["Alice", "Bob", "Charlie"])
print(users.root)  # ['Alice', 'Bob', 'Charlie']

# 字典模型
class Config(RootModel[dict[str, int]]):
    """配置字典"""
    pass

config = Config({"max_connections": 100, "timeout": 30})
print(config.root["max_connections"])  # 100

# 可以直接迭代
for key, value in config.root.items():
    print(f"{key}: {value}")
```

### 计算字段

```python
from pydantic import BaseModel, computed_field

class Product(BaseModel):
    name: str
    price: float
    tax_rate: float = 0.1

    @computed_field
    @property
    def price_with_tax(self) -> float:
        """计算含税价格"""
        return self.price * (1 + self.tax_rate)

product = Product(name="Laptop", price=1000, tax_rate=0.2)
print(product.price_with_tax)  # 1200.0

# 计算字段包含在序列化中
print(product.model_dump())
# {'name': 'Laptop', 'price': 1000.0, 'tax_rate': 0.2, 'price_with_tax': 1200.0}
```

---

## 与其他库集成

### 与 dataclasses 集成

```python
from pydantic.dataclasses import dataclass
from pydantic import Field

# 使用 Pydantic 的 dataclass 装饰器
@dataclass
class User:
    id: int
    name: str = Field(min_length=1)
    email: str
    age: int = Field(ge=0, le=150)

# 自动验证
user = User(id=1, name="Alice", email="alice@example.com", age=25)

# 验证失败会抛出异常
try:
    User(id=2, name="", email="bob@example.com", age=-1)
except ValidationError as e:
    print(e)
```

### 与 TypedDict 集成

```python
from typing import TypedDict
from pydantic import TypeAdapter

class UserDict(TypedDict):
    id: int
    name: str
    email: str

# 使用 TypeAdapter 验证 TypedDict
adapter = TypeAdapter(UserDict)

# 验证数据
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
validated = adapter.validate_python(user_data)
print(validated)  # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}

# 验证失败
try:
    adapter.validate_python({"id": "invalid"})
except ValidationError as e:
    print(e)
```

### Settings 管理（环境变量）

```python
from pydantic_settings import BaseSettings
from pydantic import Field

# 需要安装: uv add pydantic-settings

class Settings(BaseSettings):
    """应用配置（从环境变量加载）"""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = Field(..., alias="DATABASE_URL")
    api_key: str = Field(..., alias="API_KEY")
    max_connections: int = 100

    class Config:
        env_file = ".env"  # 从 .env 文件加载
        env_file_encoding = "utf-8"

# 自动从环境变量加载
# export DATABASE_URL="postgresql://localhost/mydb"
# export API_KEY="secret-key"

settings = Settings()
print(settings.database_url)
print(settings.api_key)
```

### FastAPI 集成示例

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserCreate(BaseModel):
    """创建用户请求"""
    name: str = Field(min_length=1, max_length=100)
    email: str
    age: int = Field(ge=0, le=150)

class UserResponse(BaseModel):
    """用户响应"""
    id: int
    name: str
    email: str
    age: int

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    """创建用户 API"""
    # Pydantic 自动验证请求数据
    # FastAPI 自动生成 OpenAPI 文档
    new_user = UserResponse(
        id=1,
        name=user.name,
        email=user.email,
        age=user.age
    )
    return new_user

# FastAPI 会：
# 1. 自动验证请求 JSON
# 2. 自动生成 API 文档
# 3. 自动序列化响应
```

---

## 性能优化

### 严格模式提升性能

```python
from pydantic import BaseModel, ConfigDict

# 严格模式跳过类型转换，提升性能
class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    name: str
    age: int

# 直接传入正确类型，避免转换开销
user = StrictUser(id=1, name="Alice", age=25)
```

### 禁用不必要的功能

```python
from pydantic import BaseModel, ConfigDict

class OptimizedModel(BaseModel):
    model_config = ConfigDict(
        # 禁用赋值验证（如果不需要）
        validate_assignment=False,

        # 禁用默认值验证
        validate_default=False,

        # 使用枚举值而不是枚举对象
        use_enum_values=True,
    )

    name: str
    value: int
```

### 使用 model_construct 跳过验证

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# 正常创建（带验证）
user1 = User(id=1, name="Alice", email="alice@example.com")

# 跳过验证（从可信数据源创建，性能更好）
user2 = User.model_construct(id=2, name="Bob", email="bob@example.com")

# ⚠️ model_construct 不验证数据，确保数据可信
```

### 批量验证

```python
from pydantic import BaseModel, TypeAdapter

class User(BaseModel):
    id: int
    name: str

# 使用 TypeAdapter 批量验证
adapter = TypeAdapter(list[User])

users_data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# 一次性验证所有用户
users = adapter.validate_python(users_data)
print(len(users))  # 3
```

---

## 综合实战示例

### 电商订单系统

```python
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
        """小计"""
        return self.quantity * self.unit_price

class ShippingAddress(BaseModel):
    """收货地址"""
    recipient: str = Field(min_length=1)
    phone: str = Field(pattern=r"^1[3-9]\d{9}$")
    province: str
    city: str
    district: str
    detail: str = Field(min_length=5)

class Order(BaseModel):
    """订单模型"""
    order_id: str
    user_id: int
    status: OrderStatus = OrderStatus.PENDING
    items: list[ProductItem] = Field(min_length=1)
    shipping_address: ShippingAddress
    created_at: datetime = Field(default_factory=datetime.now)
    note: str | None = None

    @computed_field
    @property
    def total_amount(self) -> float:
        """订单总额"""
        return sum(item.subtotal for item in self.items)

    @field_validator('items')
    @classmethod
    def check_items_not_empty(cls, v: list[ProductItem]) -> list[ProductItem]:
        """确保至少有一个商品"""
        if not v:
            raise ValueError('订单必须包含至少一个商品')
        return v

# 创建订单
order = Order(
    order_id="ORD-2025-001",
    user_id=12345,
    items=[
        ProductItem(
            product_id=1,
            product_name="MacBook Pro",
            quantity=1,
            unit_price=12999.00
        ),
        ProductItem(
            product_id=2,
            product_name="Magic Mouse",
            quantity=2,
            unit_price=649.00
        )
    ],
    shipping_address=ShippingAddress(
        recipient="张三",
        phone="13800138000",
        province="北京市",
        city="北京市",
        district="朝阳区",
        detail="某某街道某某小区 1 号楼 101"
    ),
    note="请在工作日配送"
)

print(f"订单总额: ¥{order.total_amount}")
print(order.model_dump_json(indent=2))
```

---

## 总结

### 关键要点

1. **BaseModel**：Pydantic 的核心，提供自动验证和序列化
2. **Field**：细粒度控制字段约束和元数据
3. **验证器**：`@field_validator` 和 `@model_validator` 实现自定义验证
4. **序列化**：`model_dump()` 和 `model_dump_json()` 导出数据
5. **配置**：`ConfigDict` 控制模型行为
6. **集成**：与 FastAPI、Settings 等无缝集成

### 最佳实践

✅ **推荐**：
- API 开发使用 Pydantic 定义请求/响应模型
- 配置管理使用 `pydantic-settings`
- 复杂验证使用 `@model_validator`
- 性能敏感场景使用严格模式
- 敏感字段使用 `Field(exclude=True)`

❌ **避免**：
- 过度使用 `Any` 类型
- 在可信数据上重复验证
- 忽略 ValidationError 的详细信息

### 下一步

在掌握 Pydantic 后，下一篇[《Python 类型系统 - 类型检查工具篇》](./17-type-system-checkers.md)将介绍：

- mypy 和 pyright 的使用
- 类型检查配置
- CI/CD 集成
- 常见问题和解决方案

---

**参考资料**：
- [Pydantic 官方文档](https://docs.pydantic.dev/)
- [Pydantic V2 迁移指南](https://docs.pydantic.dev/latest/migration/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [pydantic-settings 文档](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
