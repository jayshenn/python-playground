# Python 类型系统基础篇

## 目录

- [为什么需要类型系统](#为什么需要类型系统)
- [基础类型注解](#基础类型注解)
- [特殊类型形式](#特殊类型形式)
- [容器类型注解](#容器类型注解)
- [Python 3.12+ 新特性](#python-312-新特性)

---

## 为什么需要类型系统

### 类型系统的价值

尽管 Python 是动态类型语言，但从 Python 3.5 开始引入的类型提示（Type Hints）为开发者带来了巨大价值：

#### 1. **IDE 智能提示**

```python
def get_user_name(user_id: int) -> str:
    """获取用户名称"""
    # IDE 知道 user_id 是 int，会提供相应的方法提示
    # IDE 知道返回值是 str，调用者也会得到正确的提示
    return f"User_{user_id}"

# IDE 会自动提示 name 是 str 类型，提供 str 的方法
name = get_user_name(123)
print(name.upper())  # IDE 知道这是合法的
```

#### 2. **静态类型检查**

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

# 类型检查器会发现这个错误
result = calculate_total("100", 5)  # 错误：传入了 str 而不是 float
```

#### 3. **代码文档化**

类型注解本身就是最好的文档：

```python
from datetime import datetime

def format_date(
    date: datetime,
    format_string: str = "%Y-%m-%d"
) -> str:
    """
    格式化日期

    不需要在文档中说明参数类型，类型注解已经清楚表达了
    """
    return date.strftime(format_string)
```

#### 4. **提前发现 Bug**

```python
def get_first_item(items: list[str]) -> str:
    return items[0]

# 类型检查器会警告：list[int] 与 list[str] 不匹配
numbers = [1, 2, 3]
first = get_first_item(numbers)  # 类型错误
```

### Python 动态类型 vs 静态类型提示

⚠️ **重要概念**：Python 的类型提示**不会在运行时强制检查类型**

```python
def add(a: int, b: int) -> int:
    return a + b

# 运行时不会报错，Python 不会检查类型
result = add("hello", "world")  # 运行时正常执行
print(result)  # 输出：helloworld

# 但类型检查器（mypy、pyright）会发现问题
```

类型提示是给**开发工具**和**类型检查器**使用的，不影响运行时行为。

### 现代项目中的最佳实践

✅ **推荐做法**：

1. **新项目**：从一开始就使用类型注解
2. **关键函数**：公共 API、复杂逻辑必须添加类型注解
3. **类型检查**：在 CI/CD 中集成 mypy 或 pyright
4. **渐进式采用**：老项目可以逐步添加类型注解

```python
# ✅ 好的实践
def process_user_data(
    user_id: int,
    data: dict[str, str | int]
) -> bool:
    """处理用户数据"""
    # 实现...
    return True

# ❌ 避免这样
def process_user_data(user_id, data):  # 没有类型信息
    return True
```

---

## 基础类型注解

### 内置类型

Python 的基本类型可以直接用于类型注解：

```python
# 基本类型
name: str = "Alice"
age: int = 30
height: float = 1.75
is_active: bool = True

# None 类型
result: None = None

# 函数参数和返回值
def greet(name: str) -> str:
    return f"Hello, {name}!"

def log_message(message: str) -> None:
    """返回 None 的函数"""
    print(message)
```

### 集合类型

🆕 **Python 3.9+**：可以直接使用内置集合类型进行注解

```python
# Python 3.9+ 推荐写法（小写）
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95, "Bob": 87}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (10.5, 20.3)

# Python 3.8 及更早（需要从 typing 导入）
from typing import List, Dict, Set, Tuple

names: List[str] = ["Alice", "Bob"]  # 不推荐，但兼容旧版本
```

⚠️ **注意**：从 Python 3.9 开始，推荐使用小写的内置类型（`list`、`dict`、`set`、`tuple`），而不是 `typing` 模块的大写版本。

### 类型别名

#### 🆕 Python 3.12+ 推荐：`type` 语句

```python
# 定义类型别名
type UserId = int
type UserName = str
type Coordinates = tuple[float, float]
type JsonData = dict[str, str | int | float | bool | None]

# 使用类型别名
def get_user(user_id: UserId) -> UserName:
    return f"User_{user_id}"

def validate_position(coord: Coordinates) -> bool:
    x, y = coord
    return -180 <= x <= 180 and -90 <= y <= 90
```

#### Python 3.9-3.11：使用 `TypeAlias`

```python
from typing import TypeAlias

UserId: TypeAlias = int
UserName: TypeAlias = str
JsonData: TypeAlias = dict[str, str | int | float | bool | None]
```

#### 复杂类型别名示例

```python
type Headers = dict[str, str]
type ResponseData = dict[str, str | int | list[str]]
type HttpResponse = tuple[int, Headers, ResponseData]

def make_request(url: str) -> HttpResponse:
    status = 200
    headers = {"Content-Type": "application/json"}
    data = {"message": "success", "count": 10}
    return status, headers, data
```

### 函数类型注解

```python
# 基本函数
def add(a: int, b: int) -> int:
    return a + b

# 无返回值
def print_message(msg: str) -> None:
    print(msg)

# 默认参数
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# 可变参数
def sum_numbers(*numbers: int) -> int:
    return sum(numbers)

# 关键字参数
def create_user(**kwargs: str | int) -> dict[str, str | int]:
    return kwargs

# 混合使用
def process_data(
    data: list[int],
    *extras: int,
    verbose: bool = False,
    **options: str
) -> dict[str, int | bool | str]:
    result = {"count": len(data) + len(extras), "verbose": verbose}
    result.update(options)
    return result
```

---

## 特殊类型形式

### Union 类型：多种可能的类型

#### 🆕 Python 3.10+ 推荐：`|` 语法

```python
# 使用 | 操作符（推荐）
def process_id(user_id: int | str) -> str:
    """接受 int 或 str 类型的 ID"""
    return str(user_id)

# 多个类型
def format_value(value: int | float | str) -> str:
    return f"Value: {value}"

# 在类型别名中使用
type NumberOrString = int | str
type OptionalNumber = int | None
```

#### Python 3.9 及更早：`Union`

```python
from typing import Union

def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)
```

### Optional 类型：可选值

```python
# Optional[X] 等价于 X | None
from typing import Optional

# 两种写法等价
def find_user(user_id: int) -> str | None:
    """可能返回 None"""
    if user_id > 0:
        return f"User_{user_id}"
    return None

# 旧写法（仍然有效）
def find_user_old(user_id: int) -> Optional[str]:
    if user_id > 0:
        return f"User_{user_id}"
    return None

# 使用示例
result = find_user(123)
if result is not None:
    print(result.upper())  # 类型检查器知道这里 result 一定是 str
```

⚠️ **注意**：`Optional[X]` 不表示"可选参数"，而是"可能为 None 的值"

```python
# ✅ 正确：Optional 用于返回值
def get_config(key: str) -> str | None:
    return None

# ❌ 混淆：这里 Optional 不表示参数可选
def set_config(key: str, value: str | None) -> None:
    pass

# ✅ 可选参数应该用默认值表示
def set_config(key: str, value: str = "default") -> None:
    pass
```

### Literal 类型：字面值限定

```python
from typing import Literal

# 限定只能是特定的字面值
def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    print(f"Log level set to {level}")

# 正确
set_log_level("INFO")

# 错误：类型检查器会报错
set_log_level("TRACE")  # 不在允许的字面值中

# 数字字面值
def get_http_status(code: Literal[200, 404, 500]) -> str:
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    else:
        return "Internal Server Error"

# 布尔字面值
def create_file(overwrite: Literal[True]) -> None:
    """只接受 True，确保调用者明确意图"""
    pass

create_file(True)  # ✅
create_file(False)  # ❌ 类型错误
```

### Any 类型：不受约束

```python
from typing import Any

# Any 表示任何类型都可以
def process_unknown(data: Any) -> Any:
    """处理未知类型的数据"""
    return data

# Any 会禁用类型检查
value: Any = 123
value = "string"  # ✅ 没问题
value = [1, 2, 3]  # ✅ 没问题
result = value.any_method()  # ✅ 类型检查器不会报错
```

⚠️ **使用建议**：尽量避免使用 `Any`，它会削弱类型检查的作用。只在真正需要时使用。

### Never / NoReturn：底部类型

```python
from typing import Never, NoReturn

# NoReturn：函数永不返回（抛出异常或无限循环）
def raise_error(message: str) -> NoReturn:
    """这个函数总是抛出异常"""
    raise ValueError(message)

def infinite_loop() -> NoReturn:
    """无限循环"""
    while True:
        pass

# 🆕 Never (Python 3.11+)：更通用的底部类型
def assert_never(value: Never) -> Never:
    """用于穷举检查"""
    raise AssertionError(f"Unexpected value: {value}")

# 实际应用：穷举检查
type Color = Literal["red", "green", "blue"]

def handle_color(color: Color) -> str:
    if color == "red":
        return "#FF0000"
    elif color == "green":
        return "#00FF00"
    elif color == "blue":
        return "#0000FF"
    else:
        # 如果所有情况都处理了，这里的 color 类型是 Never
        assert_never(color)
```

---

## 容器类型注解

### 列表注解

```python
# 简单列表
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob"]

# 嵌套列表
matrix: list[list[int]] = [[1, 2], [3, 4]]

# 混合类型（使用 Union）
mixed: list[int | str] = [1, "two", 3, "four"]

# 函数返回列表
def get_even_numbers(limit: int) -> list[int]:
    return [x for x in range(limit) if x % 2 == 0]
```

### 字典注解

```python
# 简单字典
scores: dict[str, int] = {"Alice": 95, "Bob": 87}

# 嵌套字典
user_data: dict[str, dict[str, str | int]] = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}

# 复杂值类型
type ConfigValue = str | int | bool | list[str]
config: dict[str, ConfigValue] = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
    "allowed_hosts": ["127.0.0.1", "localhost"]
}
```

### 集合注解

```python
# 简单集合
unique_ids: set[int] = {1, 2, 3}
tags: set[str] = {"python", "typing", "tutorial"}

# 集合操作
def merge_tags(tags1: set[str], tags2: set[str]) -> set[str]:
    return tags1 | tags2
```

### 元组注解

元组有多种注解方式，取决于元组的性质：

#### 1. 固定长度、固定类型的元组

```python
# 定义具体的元组类型
coordinates: tuple[float, float] = (10.5, 20.3)
rgb_color: tuple[int, int, int] = (255, 128, 0)

# 不同类型的元素
user_info: tuple[str, int, bool] = ("Alice", 30, True)

# 函数返回固定元组
def get_user() -> tuple[str, int]:
    return "Alice", 30

name, age = get_user()  # 类型检查器知道 name 是 str，age 是 int
```

#### 2. 可变长度、单一类型的元组

```python
# 使用 ... 表示可变长度
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
names: tuple[str, ...] = ("Alice", "Bob", "Charlie")

def calculate_average(numbers: tuple[float, ...]) -> float:
    return sum(numbers) / len(numbers)

result = calculate_average((1.5, 2.5, 3.5))  # ✅
```

#### 3. 空元组

```python
empty: tuple[()] = ()
```

#### 4. 混合使用

```python
# 前几个元素固定类型，后面可变
type Response = tuple[int, str, int, ...]

response: Response = (200, "OK", 1, 2, 3)  # ✅
```

### 抽象容器类型

使用 `collections.abc` 中的抽象类型，提供更灵活的类型注解：

```python
from collections.abc import Sequence, Mapping, Iterable, Iterator

# Sequence：接受 list、tuple 等任何序列
def process_items(items: Sequence[str]) -> int:
    return len(items)

process_items(["a", "b"])  # ✅ list
process_items(("a", "b"))  # ✅ tuple
process_items("ab")  # ✅ str 也是 Sequence

# Mapping：接受 dict 等映射类型
def get_value(data: Mapping[str, int], key: str) -> int | None:
    return data.get(key)

# Iterable：可迭代对象
def sum_values(items: Iterable[int]) -> int:
    return sum(items)

sum_values([1, 2, 3])  # ✅ list
sum_values((1, 2, 3))  # ✅ tuple
sum_values({1, 2, 3})  # ✅ set
sum_values(range(10))  # ✅ range

# Iterator：迭代器
def consume_iterator(it: Iterator[str]) -> list[str]:
    return list(it)
```

✅ **最佳实践**：

- 函数参数使用抽象类型（`Sequence`、`Mapping`、`Iterable`），提高灵活性
- 函数返回值使用具体类型（`list`、`dict`），提供明确信息

```python
# ✅ 好的实践
def process(items: Sequence[int]) -> list[int]:
    """参数接受任何序列，返回明确的 list"""
    return [x * 2 for x in items]

# ❌ 不够灵活
def process_list(items: list[int]) -> Sequence[int]:
    """参数太具体，返回值太模糊"""
    return [x * 2 for x in items]
```

---

## Python 3.12+ 新特性

### 1. 新的 `type` 语句

🆕 **Python 3.12** 引入了专门的 `type` 语句，用于定义类型别名。

#### 基本用法

```python
# 旧方法（Python 3.9-3.11）
from typing import TypeAlias
UserId: TypeAlias = int

# 🆕 新方法（Python 3.12+，推荐）
type UserId = int
type UserName = str
type Email = str

def create_user(user_id: UserId, name: UserName, email: Email) -> bool:
    return True
```

#### 优势

```python
# 1. 更清晰的语法
type JsonValue = str | int | float | bool | None | list['JsonValue'] | dict[str, 'JsonValue']

# 2. 自动延迟求值（前向引用）
type Node = dict[str, 'Node' | int]  # 无需引号（虽然这里用了，但实际上 Node 会自动识别）

# 3. 支持泛型（稍后在高级篇介绍）
```

### 2. 类型参数语法 `[T]`

🆕 **Python 3.12** 引入了新的泛型语法，使用方括号 `[T]` 定义类型参数。

#### 泛型函数

```python
# 旧方法（Python 3.11 及更早）
from typing import TypeVar

T = TypeVar('T')

def first_old(items: list[T]) -> T:
    return items[0]

# 🆕 新方法（Python 3.12+，推荐）
def first[T](items: list[T]) -> T:
    """返回列表的第一个元素"""
    return items[0]

# 使用
result1 = first([1, 2, 3])  # 类型推断为 int
result2 = first(["a", "b"])  # 类型推断为 str
```

#### 泛型类

```python
# 旧方法
from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

# 🆕 新方法（Python 3.12+）
class Box[T]:
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

# 使用
int_box = Box(123)  # Box[int]
str_box = Box("hello")  # Box[str]
```

#### 泛型类型别名

```python
# 旧方法
from typing import TypeVar, Generic

T = TypeVar('T')
type Result = tuple[bool, T | None]  # 错误：T 未定义

# 🆕 新方法（Python 3.12+）
type Result[T] = tuple[bool, T | None]

# 使用
def find_user(user_id: int) -> Result[str]:
    if user_id > 0:
        return True, f"User_{user_id}"
    return False, None

success, user = find_user(123)
# 类型检查器知道：success 是 bool，user 是 str | None
```

### 3. TypeAliasType

🆕 **Python 3.12** 引入了 `TypeAliasType` 类，用于运行时表示类型别名。

```python
type UserId = int

# TypeAliasType 允许运行时检查
print(type(UserId))  # <class 'typing.TypeAliasType'>
print(UserId.__name__)  # UserId
print(UserId.__value__)  # <class 'int'>

# 可以用于动态类型检查
def is_user_id_type(value: type) -> bool:
    return isinstance(value, type) and value == int
```

### 实战示例：综合应用

```python
# Python 3.12+ 类型系统综合示例

# 定义类型别名
type UserId = int
type Email = str
type PhoneNumber = str
type Timestamp = float

# 定义联系方式（可以是邮箱或电话）
type ContactInfo = Email | PhoneNumber

# 定义用户数据结构
type UserData = dict[str, str | int | float | bool | None]

# 泛型响应类型
type Response[T] = tuple[bool, T | None, str]

# 业务函数
def validate_contact(contact: ContactInfo) -> bool:
    """验证联系方式"""
    if "@" in contact:
        # 假设是邮箱
        return len(contact) > 5
    else:
        # 假设是电话
        return len(contact) >= 10

def create_user(
    user_id: UserId,
    name: str,
    contact: ContactInfo,
    metadata: UserData | None = None
) -> Response[UserId]:
    """创建用户"""
    if not validate_contact(contact):
        return False, None, "Invalid contact info"

    # 创建用户逻辑...
    return True, user_id, "User created successfully"

# 使用示例
success, uid, message = create_user(
    user_id=12345,
    name="Alice",
    contact="alice@example.com",
    metadata={"role": "admin", "active": True}
)

if success and uid is not None:
    print(f"User {uid} created: {message}")
else:
    print(f"Failed: {message}")
```

---

## 总结

### 关键要点

1. **类型提示不影响运行时**：只用于开发工具和静态检查
2. **Python 3.9+**：使用小写内置类型（`list`、`dict`）
3. **Python 3.10+**：使用 `|` 代替 `Union`
4. **Python 3.12+**：使用 `type` 语句定义类型别名，使用 `[T]` 定义泛型
5. **优先使用抽象类型**：函数参数用 `Sequence`、`Mapping`、`Iterable`

### 最佳实践

✅ **推荐**：
- 所有公共 API 函数添加类型注解
- 复杂类型使用类型别名简化
- 使用 `Literal` 限定字面值
- 避免过度使用 `Any`

❌ **避免**：
- 不要在运行时检查类型注解
- 不要过度复杂化类型定义
- 不要混用新旧语法（统一使用新语法）

### 下一步

在掌握了基础类型注解后，下一篇[《Python 类型系统 - 标准库类型工具篇》](./15-type-system-stdlib.md)将介绍：

- 泛型编程（Generics）
- Callable 和函数类型
- dataclasses
- TypedDict
- Protocol 协议
- 高级类型注解工具

---

**参考资料**：
- [Python typing 官方文档](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP 604 - Union 类型的 | 语法](https://peps.python.org/pep-0604/)
- [PEP 695 - 类型参数语法](https://peps.python.org/pep-0695/)
