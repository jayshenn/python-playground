# Python 类型系统 - 标准库类型工具篇

## 目录

- [泛型编程 (Generics)](#泛型编程-generics)
- [Callable 和函数类型](#callable-和函数类型)
- [dataclasses](#dataclasses)
- [TypedDict](#typeddict)
- [Protocol - 结构化子类型](#protocol---结构化子类型)
- [高级类型注解](#高级类型注解)
- [类型工具函数](#类型工具函数)

---

## 泛型编程 (Generics)

泛型允许我们编写可以处理多种类型的代码，同时保持类型安全。

### TypeVar 类型变量

#### 基本用法

```python
from typing import TypeVar

# 定义类型变量
T = TypeVar('T')

def first[T](items: list[T]) -> T:
    """返回列表的第一个元素"""
    return items[0]

# 类型推断
num = first([1, 2, 3])  # num 的类型是 int
name = first(["Alice", "Bob"])  # name 的类型是 str

# 也可以使用旧语法（兼容 Python 3.11 及更早）
def last(items: list[T]) -> T:
    return items[-1]
```

#### 约束类型变量

```python
from typing import TypeVar

# 限定 T 只能是 int 或 float
T = TypeVar('T', int, float)

def add[T: (int, float)](a: T, b: T) -> T:
    """只接受 int 或 float"""
    return a + b  # type: ignore

result1 = add(1, 2)  # ✅ int
result2 = add(1.5, 2.5)  # ✅ float
# result3 = add("a", "b")  # ❌ 类型错误

# 使用 bound 限定上界
class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

A = TypeVar('A', bound=Animal)

def make_speak[A: Animal](animal: A) -> str:
    """接受 Animal 或其子类"""
    return animal.speak()

dog = Dog()
print(make_speak(dog))  # ✅
```

#### 协变和逆变

```python
from typing import TypeVar

# 协变（covariant）：保持子类型关系
T_co = TypeVar('T_co', covariant=True)

class Producer[T_co]:
    """只产出 T_co，不消费"""
    def produce(self) -> T_co:
        ...

# Dog 是 Animal 的子类型
# 则 Producer[Dog] 是 Producer[Animal] 的子类型

# 逆变（contravariant）：反转子类型关系
T_contra = TypeVar('T_contra', contravariant=True)

class Consumer[T_contra]:
    """只消费 T_contra，不产出"""
    def consume(self, item: T_contra) -> None:
        ...

# Dog 是 Animal 的子类型
# 则 Consumer[Animal] 是 Consumer[Dog] 的子类型
```

### 泛型类

#### Python 3.12+ 新语法

```python
# 🆕 Python 3.12+ 推荐写法
class Stack[T]:
    """泛型栈"""
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

# 使用
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # "world"
```

#### Python 3.11 及更早版本

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

#### 多类型参数

```python
class Pair[K, V]:
    """键值对"""
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def get_key(self) -> K:
        return self.key

    def get_value(self) -> V:
        return self.value

# 使用
pair1 = Pair[str, int]("age", 30)
pair2 = Pair[int, str](1, "first")

# 类型推断（不需要显式指定）
pair3 = Pair("name", "Alice")  # Pair[str, str]
```

#### 实战示例：泛型缓存

```python
from typing import Callable
from datetime import datetime, timedelta

class Cache[K, V]:
    """通用缓存类"""
    def __init__(self, ttl_seconds: int = 300):
        self._cache: dict[K, tuple[V, datetime]] = {}
        self._ttl = timedelta(seconds=ttl_seconds)

    def set(self, key: K, value: V) -> None:
        """设置缓存"""
        self._cache[key] = (value, datetime.now())

    def get(self, key: K) -> V | None:
        """获取缓存，过期返回 None"""
        if key not in self._cache:
            return None

        value, timestamp = self._cache[key]
        if datetime.now() - timestamp > self._ttl:
            del self._cache[key]
            return None

        return value

    def get_or_compute(
        self,
        key: K,
        compute: Callable[[], V]
    ) -> V:
        """获取缓存，不存在则计算并缓存"""
        cached = self.get(key)
        if cached is not None:
            return cached

        value = compute()
        self.set(key, value)
        return value

# 使用
user_cache = Cache[int, str](ttl_seconds=60)
user_cache.set(123, "Alice")
print(user_cache.get(123))  # "Alice"

# 带计算函数
def get_user_name() -> str:
    return "Bob"

name = user_cache.get_or_compute(456, get_user_name)
```

### TypeVarTuple - 可变泛型

🆕 **Python 3.11+**：处理可变数量的类型参数

```python
from typing import TypeVarTuple

Ts = TypeVarTuple('Ts')

# 使用新语法（Python 3.12+）
def move_first_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    """将元组的第一个元素移到最后"""
    return (*tup[1:], tup[0])

# 使用
result1 = move_first_to_last((1, "a", True))
# result1 类型: tuple[str, bool, int]

result2 = move_first_to_last(("x", 1, 2, 3))
# result2 类型: tuple[int, int, int, str]
```

### ParamSpec - 参数规范

🆕 **Python 3.10+**：保留函数的参数签名

```python
from typing import ParamSpec, TypeVar, Callable
from functools import wraps
import time

P = ParamSpec('P')
R = TypeVar('R')

def timer(func: Callable[P, R]) -> Callable[P, R]:
    """装饰器：记录函数执行时间，保留原函数签名"""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

@timer
def process_data(data: list[int], multiplier: int = 2) -> list[int]:
    """处理数据"""
    time.sleep(0.1)
    return [x * multiplier for x in data]

# 类型检查器知道 process_data 的完整签名
result = process_data([1, 2, 3], multiplier=3)
# 输出: process_data took 0.10s
```

---

## Callable 和函数类型

### 基本用法

```python
from collections.abc import Callable

# Callable[[参数类型...], 返回类型]

# 接受一个字符串参数，返回整数
def process(func: Callable[[str], int]) -> int:
    return func("test")

def string_length(s: str) -> int:
    return len(s)

result = process(string_length)  # 4

# 无参数函数
def run_task(task: Callable[[], None]) -> None:
    task()

def hello() -> None:
    print("Hello!")

run_task(hello)

# 多个参数
def apply_operation(
    a: int,
    b: int,
    operation: Callable[[int, int], int]
) -> int:
    return operation(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply_operation(5, 3, add)  # 8
```

### 回调函数

```python
from collections.abc import Callable

type Callback = Callable[[str], None]
type ErrorCallback = Callable[[Exception], None]

def fetch_data(
    url: str,
    on_success: Callback,
    on_error: ErrorCallback
) -> None:
    """异步获取数据（模拟）"""
    try:
        # 模拟数据获取
        data = f"Data from {url}"
        on_success(data)
    except Exception as e:
        on_error(e)

def handle_success(data: str) -> None:
    print(f"Success: {data}")

def handle_error(error: Exception) -> None:
    print(f"Error: {error}")

fetch_data("https://api.example.com", handle_success, handle_error)
```

### 高阶函数

```python
from collections.abc import Callable

def create_multiplier(factor: int) -> Callable[[int], int]:
    """返回一个乘法函数"""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### 装饰器的类型注解

```python
from typing import TypeVar, ParamSpec, Callable
from functools import wraps

P = ParamSpec('P')
R = TypeVar('R')

def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    """记录函数调用"""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# 类型检查器知道 greet 的完整签名
message = greet("Alice", greeting="Hi")
# 输出:
# Calling greet
# greet returned Hi, Alice!
```

---

## dataclasses

`dataclasses` 模块提供了一个装饰器，自动生成特殊方法（`__init__`、`__repr__`、`__eq__` 等）。

### 基本用法

```python
from dataclasses import dataclass

@dataclass
class User:
    """用户类"""
    id: int
    name: str
    email: str
    active: bool = True  # 默认值

# 自动生成 __init__
user = User(id=1, name="Alice", email="alice@example.com")

# 自动生成 __repr__
print(user)  # User(id=1, name='Alice', email='alice@example.com', active=True)

# 自动生成 __eq__
user2 = User(id=1, name="Alice", email="alice@example.com")
print(user == user2)  # True
```

### field() 函数和元数据

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)  # 可变默认值
    _internal_id: int = field(default=0, repr=False)  # 不在 repr 中显示
    quantity: int = field(default=1, metadata={"unit": "pieces"})

# default_factory 用于可变类型
p1 = Product("Laptop", 999.99)
p2 = Product("Mouse", 29.99)
p1.tags.append("electronics")
print(p1.tags)  # ['electronics']
print(p2.tags)  # []  不会被共享

# 元数据
import dataclasses
quantity_field = dataclasses.fields(Product)[3]
print(quantity_field.metadata)  # {'unit': 'pieces'}
```

### 配置选项

```python
from dataclasses import dataclass

# frozen=True: 不可变（类似 namedtuple）
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# p.x = 3.0  # ❌ 错误：frozen dataclass 不能修改

# order=True: 自动生成比较方法
@dataclass(order=True)
class Person:
    name: str
    age: int

people = [Person("Bob", 30), Person("Alice", 25)]
sorted_people = sorted(people)  # 按字段顺序比较
print(sorted_people)  # [Person(name='Alice', age=25), Person(name='Bob', age=30)]

# slots=True: 使用 __slots__ 优化内存（Python 3.10+）
@dataclass(slots=True)
class OptimizedUser:
    id: int
    name: str
```

### InitVar 和 __post_init__

```python
from dataclasses import dataclass, field, InitVar

@dataclass
class User:
    name: str
    email: str
    password_hash: str = field(init=False, repr=False)
    password: InitVar[str]  # 只在 __init__ 中使用

    def __post_init__(self, password: str) -> None:
        """初始化后处理"""
        import hashlib
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

user = User(name="Alice", email="alice@example.com", password="secret123")
print(user.name)  # Alice
# print(user.password)  # ❌ 错误：没有 password 属性
print(user.password_hash)  # 哈希值
```

### 继承

```python
from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str

    def bark(self) -> str:
        return f"{self.name} says Woof!"

dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
print(dog)  # Dog(name='Buddy', age=3, breed='Golden Retriever')
print(dog.bark())  # Buddy says Woof!
```

### 实战示例：配置管理

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "mydb"
    username: str = ""
    password: str = field(default="", repr=False)

@dataclass
class CacheConfig:
    enabled: bool = True
    ttl_seconds: int = 300
    max_size: int = 1000

@dataclass
class AppConfig:
    env: Literal["dev", "staging", "prod"] = "dev"
    debug: bool = True
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    cache: CacheConfig = field(default_factory=CacheConfig)

# 使用
config = AppConfig(
    env="prod",
    debug=False,
    database=DatabaseConfig(
        host="db.example.com",
        database="production",
        username="app_user",
        password="secret"
    )
)

print(f"Connecting to {config.database.host}:{config.database.port}")
```

---

## TypedDict

`TypedDict` 用于定义字典的结构，指定每个键的类型。

### 基本用法

```python
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str
    active: bool

# 创建符合类型的字典
user: User = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": True
}

def get_user_name(user: User) -> str:
    return user["name"]

print(get_user_name(user))  # Alice

# 类型检查器会发现错误
# bad_user: User = {"id": 1}  # ❌ 缺少必需的键
```

### 可选键

```python
from typing import TypedDict, NotRequired

# Python 3.11+ 使用 NotRequired
class UserProfile(TypedDict):
    id: int
    name: str
    email: str
    bio: NotRequired[str]  # 可选字段
    avatar_url: NotRequired[str]

# 有效
profile1: UserProfile = {"id": 1, "name": "Alice", "email": "alice@example.com"}
profile2: UserProfile = {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "bio": "Software Engineer"
}

# Python 3.8-3.10 使用 total=False
class OptionalFields(TypedDict, total=False):
    bio: str
    avatar_url: str

class UserProfile2(TypedDict):
    id: int
    name: str
    email: str

class UserProfileComplete(UserProfile2, OptionalFields):
    pass
```

### 继承和扩展

```python
from typing import TypedDict

class BaseUser(TypedDict):
    id: int
    name: str

class AdminUser(BaseUser):
    role: str
    permissions: list[str]

admin: AdminUser = {
    "id": 1,
    "name": "Admin",
    "role": "superadmin",
    "permissions": ["read", "write", "delete"]
}
```

### TypedDict vs dataclass

| 特性 | TypedDict | dataclass |
|------|-----------|-----------|
| 数据结构 | 字典 | 类实例 |
| 语法 | 字典语法 `{}` | 对象语法 `.` |
| 性能 | 更快（原生字典） | 稍慢（对象开销） |
| 序列化 | 天然支持 JSON | 需要转换 |
| IDE 支持 | 较弱 | 更强（自动补全） |
| 方法 | 不支持 | 支持 |
| 不可变 | 否 | 可选（frozen） |

**使用建议**：
- **API 响应、配置文件**：使用 `TypedDict`（易于序列化）
- **领域模型、业务对象**：使用 `dataclass`（更面向对象）

```python
from typing import TypedDict
from dataclasses import dataclass

# API 响应：使用 TypedDict
class ApiResponse(TypedDict):
    status: int
    message: str
    data: dict[str, str | int]

# 业务模型：使用 dataclass
@dataclass
class Order:
    order_id: int
    customer_name: str
    total: float

    def apply_discount(self, percentage: float) -> float:
        return self.total * (1 - percentage)
```

---

## Protocol - 结构化子类型

`Protocol` 实现了"鸭子类型"的静态类型化，基于结构而不是继承。

### 基本概念

```python
from typing import Protocol

class Drawable(Protocol):
    """定义可绘制对象的协议"""
    def draw(self) -> str:
        ...

class Circle:
    """不需要继承 Drawable，只需实现 draw 方法"""
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render(obj: Drawable) -> None:
    """接受任何实现了 draw 方法的对象"""
    print(obj.draw())

# 两者都可以传入，因为它们都实现了 draw 方法
render(Circle())  # Drawing a circle
render(Square())  # Drawing a square
```

### runtime_checkable

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closable(Protocol):
    def close(self) -> None:
        ...

class File:
    def close(self) -> None:
        print("File closed")

f = File()

# 运行时检查
print(isinstance(f, Closable))  # True

# 类型检查器也会检查
def close_resource(resource: Closable) -> None:
    resource.close()

close_resource(f)  # ✅
```

### 带属性的协议

```python
from typing import Protocol

class Named(Protocol):
    """必须有 name 属性"""
    name: str

class NamedWithMethod(Protocol):
    """必须有 name 属性和 get_name 方法"""
    name: str

    def get_name(self) -> str:
        ...

class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

def print_name(obj: Named) -> None:
    print(obj.name)

user = User("Alice")
print_name(user)  # ✅ User 有 name 属性
```

### 实战示例：存储接口

```python
from typing import Protocol

class Storage(Protocol):
    """存储接口协议"""
    def get(self, key: str) -> str | None:
        ...

    def set(self, key: str, value: str) -> None:
        ...

    def delete(self, key: str) -> bool:
        ...

# 内存存储实现
class MemoryStorage:
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._data.get(key)

    def set(self, key: str, value: str) -> None:
        self._data[key] = value

    def delete(self, key: str) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False

# Redis 存储实现（模拟）
class RedisStorage:
    def get(self, key: str) -> str | None:
        # 实际会调用 Redis
        return None

    def set(self, key: str, value: str) -> None:
        # 实际会调用 Redis
        pass

    def delete(self, key: str) -> bool:
        # 实际会调用 Redis
        return False

# 业务逻辑不关心具体实现
def cache_user_data(storage: Storage, user_id: int, data: str) -> None:
    key = f"user:{user_id}"
    storage.set(key, data)

# 两种实现都可以使用
mem_storage = MemoryStorage()
redis_storage = RedisStorage()

cache_user_data(mem_storage, 123, "Alice")
cache_user_data(redis_storage, 456, "Bob")
```

---

## 高级类型注解

### ClassVar - 类变量

```python
from typing import ClassVar

class Counter:
    """计数器类"""
    total_count: ClassVar[int] = 0  # 类变量

    def __init__(self, name: str):
        self.name: str = name  # 实例变量
        Counter.total_count += 1

    @classmethod
    def get_total(cls) -> int:
        return cls.total_count

c1 = Counter("first")
c2 = Counter("second")
print(Counter.get_total())  # 2
```

### Final - 不可变类型

```python
from typing import Final

# 常量
MAX_CONNECTIONS: Final = 100
API_URL: Final[str] = "https://api.example.com"

# MAX_CONNECTIONS = 200  # ❌ 类型检查器会警告

class Config:
    """配置类"""
    MAX_RETRIES: Final = 3  # 类常量

    def __init__(self):
        self.timeout: Final[int] = 30  # 实例常量
        # self.timeout = 60  # ❌ 不能重新赋值

# 防止方法被重写
class Base:
    def process(self) -> str:
        return "base"

class Derived(Base):
    # 如果 Base.process 标记为 Final，这里会报错
    def process(self) -> str:
        return "derived"
```

### Self 类型

🆕 **Python 3.11+**：表示当前类的类型

```python
from typing import Self

class Builder:
    """建造者模式"""
    def __init__(self):
        self._config: dict[str, str | int] = {}

    def set_name(self, name: str) -> Self:
        """返回 self，支持链式调用"""
        self._config["name"] = name
        return self

    def set_value(self, value: int) -> Self:
        self._config["value"] = value
        return self

    def build(self) -> dict[str, str | int]:
        return self._config.copy()

# 链式调用
result = Builder().set_name("test").set_value(42).build()
print(result)  # {'name': 'test', 'value': 42}

# Self 在继承中的好处
class ExtendedBuilder(Builder):
    def set_extra(self, extra: str) -> Self:
        self._config["extra"] = extra
        return self

# 类型检查器知道返回的是 ExtendedBuilder
extended = ExtendedBuilder().set_name("test").set_extra("data").build()
```

### Annotated - 带元数据的类型

```python
from typing import Annotated

# 带约束的类型
type PositiveInt = Annotated[int, "positive"]
type MaxLength50 = Annotated[str, "max_length=50"]
type EmailAddress = Annotated[str, "email_format"]

def create_user(
    user_id: PositiveInt,
    username: MaxLength50,
    email: EmailAddress
) -> bool:
    """类型注解包含了额外的验证信息"""
    return True

# 与 Pydantic 等库配合使用
from typing import Annotated

# Pydantic 会读取元数据并应用验证
type Username = Annotated[str, "min_length=3", "max_length=20"]
type Age = Annotated[int, "ge=0", "le=150"]
```

---

## 类型工具函数

### get_type_hints()

```python
from typing import get_type_hints

def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

# 获取类型提示
hints = get_type_hints(greet)
print(hints)
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}

# 用于运行时验证
def validate_args(func, *args, **kwargs):
    hints = get_type_hints(func)
    # 可以在这里添加验证逻辑
    return func(*args, **kwargs)
```

### get_origin() 和 get_args()

```python
from typing import get_origin, get_args

# 获取泛型的原始类型和参数
type UserDict = dict[str, int]
type UserList = list[str]

print(get_origin(UserDict))  # <class 'dict'>
print(get_args(UserDict))  # (<class 'str'>, <class 'int'>)

print(get_origin(UserList))  # <class 'list'>
print(get_args(UserList))  # (<class 'str'>,)

# 实战：检查是否是特定的泛型类型
def is_list_of_str(tp) -> bool:
    return get_origin(tp) is list and get_args(tp) == (str,)

print(is_list_of_str(list[str]))  # True
print(is_list_of_str(list[int]))  # False
```

### cast() - 类型转换

```python
from typing import cast

# cast 不做运行时检查，只告诉类型检查器
def get_config() -> dict:
    """返回配置字典"""
    return {"key": "value"}

# 告诉类型检查器这是 dict[str, str]
config = cast(dict[str, str], get_config())

# 现在类型检查器知道 config 是 dict[str, str]
value: str = config["key"]  # ✅
```

⚠️ **注意**：`cast()` 不做运行时类型转换或验证，只是给类型检查器一个提示。

### assert_never() - 穷举检查

🆕 **Python 3.11+**

```python
from typing import assert_never, Literal

type Status = Literal["pending", "approved", "rejected"]

def handle_status(status: Status) -> str:
    if status == "pending":
        return "处理中"
    elif status == "approved":
        return "已批准"
    elif status == "rejected":
        return "已拒绝"
    else:
        # 如果所有情况都处理了，这里永远不会执行
        # 类型检查器会确保这一点
        assert_never(status)

# 如果添加了新的状态但忘记处理，类型检查器会报错
```

### reveal_type() - 调试类型推断

```python
from typing import reveal_type

# reveal_type 在类型检查时显示推断的类型
x = [1, 2, 3]
reveal_type(x)  # 类型检查器输出: list[int]

y = {"a": 1, "b": 2}
reveal_type(y)  # 类型检查器输出: dict[str, int]

# 主要用于调试复杂的类型推断
```

---

## 综合实战示例

### 泛型 API 客户端

```python
from typing import TypeVar, Generic, Protocol
from dataclasses import dataclass
from collections.abc import Callable

# 定义响应协议
class ApiResponse(Protocol):
    status_code: int

    def json(self) -> dict:
        ...

T = TypeVar('T')

@dataclass
class Result(Generic[T]):
    """通用结果类型"""
    success: bool
    data: T | None
    error: str | None

class ApiClient(Generic[T]):
    """泛型 API 客户端"""
    def __init__(
        self,
        base_url: str,
        parser: Callable[[dict], T]
    ):
        self.base_url = base_url
        self.parser = parser

    def get(self, endpoint: str) -> Result[T]:
        """GET 请求"""
        # 模拟 HTTP 请求
        try:
            # response = requests.get(f"{self.base_url}/{endpoint}")
            # 这里模拟响应
            response_data = {"id": 1, "name": "Test"}
            data = self.parser(response_data)
            return Result(success=True, data=data, error=None)
        except Exception as e:
            return Result(success=False, data=None, error=str(e))

# 定义数据模型
@dataclass
class User:
    id: int
    name: str

# 使用泛型客户端
def parse_user(data: dict) -> User:
    return User(id=data["id"], name=data["name"])

user_client = ApiClient[User](
    base_url="https://api.example.com",
    parser=parse_user
)

result = user_client.get("users/1")
if result.success and result.data:
    print(f"User: {result.data.name}")
```

---

## 总结

### 关键要点

1. **泛型**：使用 `[T]` 语法（Python 3.12+）编写类型安全的通用代码
2. **Callable**：为函数类型提供精确的类型注解
3. **dataclasses**：快速创建数据类，减少样板代码
4. **TypedDict**：为字典结构提供类型定义
5. **Protocol**：实现结构化子类型，灵活的接口定义
6. **高级注解**：`ClassVar`、`Final`、`Self`、`Annotated` 提供更细粒度的控制

### 最佳实践

✅ **推荐**：
- 公共 API 使用泛型提高复用性
- 装饰器使用 `ParamSpec` 保留函数签名
- 配置类使用 `dataclass` 或 `TypedDict`
- 接口定义使用 `Protocol` 而不是抽象基类
- 常量使用 `Final` 标记

❌ **避免**：
- 过度使用泛型导致代码复杂
- 在不必要的地方使用 `cast()`
- 混用 `dataclass` 和 `TypedDict` 导致不一致

### 下一步

掌握了标准库类型工具后，下一篇[《Python 类型系统 - Pydantic 实战篇》](./16-type-system-pydantic.md)将介绍：

- Pydantic 核心概念
- BaseModel 和字段验证
- 数据序列化与反序列化
- 与 FastAPI 等框架的集成
- 高级特性和性能优化

---

**参考资料**：
- [Python typing 官方文档](https://docs.python.org/3/library/typing.html)
- [Python dataclasses 官方文档](https://docs.python.org/3/library/dataclasses.html)
- [PEP 544 - Protocols](https://peps.python.org/pep-0544/)
- [PEP 612 - Parameter Specification Variables](https://peps.python.org/pep-0612/)
- [PEP 673 - Self Type](https://peps.python.org/pep-0673/)
