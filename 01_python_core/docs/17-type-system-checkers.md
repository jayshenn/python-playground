# Python 类型系统 - 类型检查工具篇

## 目录

- [类型检查器概览](#类型检查器概览)
- [mypy 使用指南](#mypy-使用指南)
- [pyright 使用指南](#pyright-使用指南)
- [类型检查实战](#类型检查实战)
- [CI/CD 集成](#cicd-集成)
- [类型检查最佳实践](#类型检查最佳实践)

---

## 类型检查器概览

### 什么是类型检查器

类型检查器是**静态分析工具**，在不运行代码的情况下检查类型注解的正确性。

**核心功能**：
- 🔍 **发现类型错误**：在开发阶段捕获类型不匹配
- 📝 **改善代码质量**：强制类型一致性
- 🚀 **提升重构信心**：大规模重构时发现破坏性变更
- 📚 **代码文档化**：类型注解作为活文档

⚠️ **重要**：类型检查器**不影响运行时**，Python 仍然是动态类型语言。

### 主流类型检查器对比

| 特性 | mypy | pyright | basedmypy | basedpyright |
|------|------|---------|-----------|--------------|
| 开发者 | Python 社区 | Microsoft | mypy 增强版 | pyright 增强版 |
| 语言 | Python | TypeScript | Python | TypeScript |
| 性能 | 中等 | 快 | 中等 | 快 |
| 严格度 | 可配置 | 默认严格 | 更严格 | 更严格 |
| IDE 集成 | 良好 | 优秀（VS Code） | 良好 | 优秀 |
| 插件生态 | 丰富 | 一般 | 继承 mypy | 继承 pyright |
| 推荐场景 | 通用项目 | VS Code 用户 | 严格检查 | 高性能需求 |

### 选择建议

**mypy**：
- ✅ 官方支持，文档完善
- ✅ 插件丰富（Django、pytest 等）
- ✅ 渐进式类型化友好
- ❌ 性能相对较慢

**pyright**：
- ✅ 速度快，适合大型项目
- ✅ VS Code 深度集成（Pylance）
- ✅ 默认严格，发现更多问题
- ❌ 插件生态较少

**建议**：
- 新项目：**pyright**（性能更好）
- 老项目：**mypy**（更宽容，易于集成）
- VS Code 用户：**pyright / Pylance**
- 追求极致严格：**basedmypy / basedpyright**

---

## mypy 使用指南

### 安装

```bash
# 使用 uv
uv add --dev mypy

# 或使用 pip
pip install mypy
```

### 基本使用

```bash
# 检查单个文件
mypy script.py

# 检查整个目录
mypy src/

# 检查多个路径
mypy src/ tests/

# 显示详细信息
mypy --verbose src/

# 显示错误代码
mypy --show-error-codes src/
```

### mypy 配置文件

#### `mypy.ini`

```ini
[mypy]
# Python 版本
python_version = 3.12

# 基本配置
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = False  # 不强制所有函数都有类型注解

# 严格选项
strict = False  # 不启用所有严格检查

# 导入发现
namespace_packages = True
explicit_package_bases = True

# 输出
show_error_codes = True
show_column_numbers = True
pretty = True

# 缓存
incremental = True
cache_dir = .mypy_cache

# 第三方库配置
[mypy-numpy.*]
ignore_missing_imports = True

[mypy-pandas.*]
ignore_missing_imports = True
```

#### `pyproject.toml`

```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
show_error_codes = true
pretty = true

[[tool.mypy.overrides]]
module = "numpy.*"
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "pandas.*"
ignore_missing_imports = true
```

### 严格模式选项

```ini
[mypy]
# 启用所有严格检查（等价于下面所有选项）
strict = True

# 或单独启用
disallow_any_generics = True        # 禁止 Any 泛型
disallow_subclassing_any = True     # 禁止继承 Any
disallow_untyped_calls = True       # 禁止调用无类型函数
disallow_untyped_defs = True        # 禁止无类型定义
disallow_incomplete_defs = True     # 禁止不完整的类型定义
check_untyped_defs = True           # 检查无类型函数内部
disallow_untyped_decorators = True  # 禁止无类型装饰器
warn_redundant_casts = True         # 警告多余的 cast
warn_unused_ignores = True          # 警告未使用的 type: ignore
warn_return_any = True              # 警告返回 Any
no_implicit_reexport = True         # 禁止隐式重导出
strict_equality = True              # 严格相等性检查
```

### 常见错误和解决方案

#### 1. 缺少类型注解

```python
# ❌ 错误：Function is missing a type annotation
def greet(name):
    return f"Hello, {name}"

# ✅ 修复
def greet(name: str) -> str:
    return f"Hello, {name}"
```

#### 2. 返回类型不匹配

```python
# ❌ 错误：Incompatible return value type
def get_age() -> int:
    return "25"  # 返回了 str

# ✅ 修复
def get_age() -> int:
    return 25
```

#### 3. 参数类型不匹配

```python
def add(a: int, b: int) -> int:
    return a + b

# ❌ 错误：Argument has incompatible type
result = add("1", "2")

# ✅ 修复
result = add(1, 2)
```

#### 4. 可选值未处理

```python
def get_user(user_id: int) -> str | None:
    if user_id > 0:
        return "User"
    return None

# ❌ 错误：Item "None" has no attribute "upper"
user = get_user(1)
print(user.upper())

# ✅ 修复
user = get_user(1)
if user is not None:
    print(user.upper())
```

### 忽略类型检查

```python
# 忽略单行
result = some_untyped_function()  # type: ignore

# 忽略特定错误（推荐）
result = some_untyped_function()  # type: ignore[no-untyped-call]

# 忽略整个文件
# mypy: ignore-errors

# 忽略某个函数
def legacy_function():  # type: ignore
    # 无类型注解的遗留代码
    pass
```

### Stub 文件 (.pyi)

当第三方库缺少类型信息时，可以创建 stub 文件。

```python
# module.pyi（stub 文件）
def process_data(data: list[str]) -> dict[str, int]: ...

class MyClass:
    def __init__(self, value: int) -> None: ...
    def get_value(self) -> int: ...
```

---

## pyright 使用指南

### 安装

```bash
# 使用 npm（需要 Node.js）
npm install -g pyright

# 使用 uv（推荐）
uv add --dev pyright

# 或使用 pip
pip install pyright
```

### 基本使用

```bash
# 检查当前目录
pyright

# 检查特定文件
pyright script.py

# 检查特定目录
pyright src/

# 显示详细输出
pyright --verbose

# 生成类型报告
pyright --outputjson report.json
```

### pyright 配置文件

#### `pyrightconfig.json`

```json
{
  "include": ["src"],
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    ".venv"
  ],
  "ignore": [],
  "defineConstant": {},
  "stubPath": "typings",
  "venvPath": ".",
  "venv": ".venv",

  "reportMissingImports": true,
  "reportMissingTypeStubs": false,
  "reportUnusedImport": "warning",
  "reportUnusedClass": "warning",
  "reportUnusedFunction": "warning",
  "reportUnusedVariable": "warning",
  "reportDuplicateImport": "warning",

  "pythonVersion": "3.12",
  "pythonPlatform": "All",

  "typeCheckingMode": "basic",
  "useLibraryCodeForTypes": true
}
```

#### `pyproject.toml`

```toml
[tool.pyright]
include = ["src"]
exclude = ["**/node_modules", "**/__pycache__", ".venv"]
ignore = []
stubPath = "typings"
venvPath = "."
venv = ".venv"

reportMissingImports = true
reportMissingTypeStubs = false
reportUnusedImport = "warning"
reportUnusedVariable = "warning"

pythonVersion = "3.12"
pythonPlatform = "All"
typeCheckingMode = "basic"  # 或 "strict"
```

### 类型检查模式

```json
{
  "typeCheckingMode": "off"     // 关闭（仅语法错误）
  "typeCheckingMode": "basic"   // 基本（默认，平衡）
  "typeCheckingMode": "standard" // 标准（较严格）
  "typeCheckingMode": "strict"  // 严格（最严格）
}
```

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| `off` | 只检查语法错误 | 遗留代码 |
| `basic` | 基本类型检查 | 一般项目 |
| `standard` | 更严格的检查 | 新项目 |
| `strict` | 最严格的检查 | 类型安全关键项目 |

### VS Code 集成（Pylance）

Pylance 是基于 pyright 的 VS Code 扩展。

#### `settings.json`

```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.inlayHints.functionReturnTypes": true,
  "python.analysis.inlayHints.variableTypes": true
}
```

### 忽略类型检查

```python
# 忽略单行
result = some_function()  # pyright: ignore

# 忽略特定规则
result = some_function()  # pyright: ignore[reportGeneralTypeIssues]

# 忽略整个文件
# pyright: reportGeneralTypeIssues=false
```

---

## 类型检查实战

### 渐进式类型化策略

对于现有项目，逐步添加类型注解：

#### 阶段 1：核心模块

```python
# 从最核心的模块开始
# src/core/models.py

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

def create_user(name: str, email: str) -> User:
    return User(id=generate_id(), name=name, email=email)

def generate_id() -> int:
    import random
    return random.randint(1000, 9999)
```

#### 阶段 2：公共 API

```python
# src/api.py

from typing import Sequence
from .core.models import User

def get_users() -> list[User]:
    """获取所有用户"""
    # 实现...
    return []

def find_user_by_id(user_id: int) -> User | None:
    """根据 ID 查找用户"""
    # 实现...
    return None

def update_user(user_id: int, **updates: str | int) -> bool:
    """更新用户信息"""
    # 实现...
    return True
```

#### 阶段 3：内部函数

```python
# src/utils.py

def format_name(first: str, last: str) -> str:
    """格式化姓名"""
    return f"{first} {last}".strip()

def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    import re
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))
```

### 处理缺少类型信息的第三方库

#### 方法 1：忽略导入错误

```python
# mypy.ini
[mypy-some_library.*]
ignore_missing_imports = True
```

```python
# 代码中
import some_library  # type: ignore
```

#### 方法 2：安装 stub 包

```bash
# 许多流行库有独立的 stub 包
uv add --dev types-requests
uv add --dev types-redis
uv add --dev pandas-stubs
```

#### 方法 3：创建本地 stub 文件

```python
# typings/some_library/__init__.pyi
def process(data: str) -> dict[str, str]: ...

class SomeClass:
    def __init__(self, value: int) -> None: ...
    def method(self) -> str: ...
```

### 使用 typing_extensions

`typing_extensions` 提供了新版本 Python 的类型特性的向后移植。

```bash
uv add typing_extensions
```

```python
# Python 3.10+ 特性在 3.9 中使用
from typing_extensions import TypeAlias, ParamSpec, Concatenate

# Python 3.11+ 特性在 3.10 中使用
from typing_extensions import Self, Never

# Python 3.12+ 特性在 3.11 中使用
from typing_extensions import TypedDict, override
```

### 常见问题和解决方案

#### 问题 1：循环导入

```python
# models.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .services import UserService

class User:
    def update(self, service: 'UserService') -> None:
        # 使用字符串引用避免运行时导入
        pass
```

#### 问题 2：Any 传播

```python
from typing import Any, cast

def process_data(data: Any) -> dict[str, int]:
    # ❌ 返回 Any 会传播
    return data

# ✅ 使用 cast 明确类型
def process_data_safe(data: Any) -> dict[str, int]:
    result = cast(dict[str, int], data)
    return result
```

#### 问题 3：泛型不完整

```python
# ❌ 不完整的泛型
def get_items() -> list:
    return []

# ✅ 完整的泛型
def get_items() -> list[str]:
    return []
```

---

## CI/CD 集成

### GitHub Actions

```yaml
# .github/workflows/type-check.yml
name: Type Check

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  type-check:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'

    - name: Install uv
      run: pip install uv

    - name: Install dependencies
      run: uv sync

    - name: Run mypy
      run: uv run mypy src/

    - name: Run pyright
      run: uv run pyright src/
```

### pre-commit 集成

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v1.8.0'
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-redis]
        args: [--config-file=mypy.ini]

  - repo: https://github.com/RobertCraigie/pyright-python
    rev: 'v1.1.350'
    hooks:
      - id: pyright
```

安装和使用：

```bash
# 安装 pre-commit
uv add --dev pre-commit

# 安装 hooks
uv run pre-commit install

# 手动运行所有文件
uv run pre-commit run --all-files
```

### 本地 Makefile

```makefile
# Makefile
.PHONY: type-check mypy pyright

type-check: mypy pyright

mypy:
	@echo "Running mypy..."
	@uv run mypy src/

pyright:
	@echo "Running pyright..."
	@uv run pyright src/
```

使用：

```bash
make type-check
```

---

## 类型检查最佳实践

### 1. 何时使用 Any

✅ **合理使用**：

```python
from typing import Any

# 处理真正未知的数据
def load_json(file_path: str) -> Any:
    """从文件加载 JSON，结构未知"""
    import json
    with open(file_path) as f:
        return json.load(f)

# 动态插件系统
def load_plugin(name: str) -> Any:
    """动态加载插件"""
    import importlib
    return importlib.import_module(name)
```

❌ **避免滥用**：

```python
# ❌ 懒惰使用 Any
def process_user(user: Any) -> Any:
    return user.name  # 应该定义具体的 User 类型

# ✅ 使用具体类型
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str

def process_user(user: User) -> str:
    return user.name
```

### 2. 避免过度类型注解

```python
# ❌ 过度注解（类型推断已经足够）
def add(a: int, b: int) -> int:
    result: int = a + b  # 不需要，类型已知
    return result

# ✅ 适度注解
def add(a: int, b: int) -> int:
    return a + b  # 简洁明了
```

### 3. 类型忽略注释

```python
# ❌ 不好的做法
result = legacy_function()  # type: ignore

# ✅ 好的做法（说明原因和错误码）
result = legacy_function()  # type: ignore[no-untyped-call]  # 遗留代码，待重构
```

### 4. 函数签名优先

```python
# ✅ 优先注解函数签名
def calculate_total(items: list[float], tax_rate: float) -> float:
    # 内部变量可以省略类型注解（类型推断）
    subtotal = sum(items)
    tax = subtotal * tax_rate
    return subtotal + tax
```

### 5. 使用 Protocol 而不是抽象基类

```python
from typing import Protocol
from abc import ABC, abstractmethod

# ❌ 不够灵活
class DrawableABC(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

# ✅ 更灵活的 Protocol
class Drawable(Protocol):
    def draw(self) -> str: ...

# 任何实现了 draw 方法的类都满足 Drawable
class Circle:
    def draw(self) -> str:
        return "Circle"

def render(obj: Drawable) -> None:
    print(obj.draw())

render(Circle())  # ✅ 无需继承
```

### 6. 配置文件管理

```python
# config.py
from typing import Literal

Environment = Literal["dev", "staging", "prod"]

class Config:
    env: Environment
    debug: bool
    database_url: str

    def __init__(self, env: Environment = "dev"):
        self.env = env
        self.debug = env != "prod"
        self.database_url = self._get_database_url()

    def _get_database_url(self) -> str:
        # 实现...
        return "postgresql://localhost/db"
```

---

## 综合实战示例

### 完整项目类型检查配置

#### 项目结构

```
my_project/
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── api.py
│   └── utils.py
├── tests/
│   └── test_api.py
├── pyproject.toml
├── mypy.ini
├── pyrightconfig.json
└── .pre-commit-config.yaml
```

#### `pyproject.toml`

```toml
[project]
name = "my_project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "pydantic>=2.0",
    "fastapi>=0.100",
]

[project.optional-dependencies]
dev = [
    "mypy>=1.8",
    "pyright>=1.1.350",
    "pytest>=8.0",
    "ruff>=0.1",
    "pre-commit>=3.0",
]

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
show_error_codes = true
plugins = ["pydantic.mypy"]

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[tool.pyright]
include = ["src"]
exclude = ["**/__pycache__"]
pythonVersion = "3.12"
typeCheckingMode = "basic"
reportUnusedImport = "warning"
reportUnusedVariable = "warning"

[tool.ruff]
line-length = 88
target-version = "py312"
```

#### `mypy.ini`

```ini
[mypy]
python_version = 3.12
strict = True
warn_return_any = True
warn_unused_configs = True
disallow_any_generics = True
disallow_subclassing_any = True
disallow_untyped_calls = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_return_any = True
strict_equality = True
show_error_codes = True

[mypy-tests.*]
disallow_untyped_defs = False

[mypy-some_library.*]
ignore_missing_imports = True
```

#### 示例代码

```python
# src/models.py
from pydantic import BaseModel, Field

class User(BaseModel):
    """用户模型"""
    id: int
    name: str = Field(min_length=1, max_length=100)
    email: str
    is_active: bool = True

class CreateUserRequest(BaseModel):
    """创建用户请求"""
    name: str = Field(min_length=1, max_length=100)
    email: str

class UserResponse(BaseModel):
    """用户响应"""
    id: int
    name: str
    email: str
```

```python
# src/api.py
from typing import Sequence
from .models import User, CreateUserRequest, UserResponse

_users_db: dict[int, User] = {}
_next_id = 1

def create_user(request: CreateUserRequest) -> UserResponse:
    """创建新用户"""
    global _next_id
    user = User(
        id=_next_id,
        name=request.name,
        email=request.email
    )
    _users_db[user.id] = user
    _next_id += 1

    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email
    )

def get_all_users() -> Sequence[UserResponse]:
    """获取所有用户"""
    return [
        UserResponse(id=u.id, name=u.name, email=u.email)
        for u in _users_db.values()
    ]

def get_user_by_id(user_id: int) -> UserResponse | None:
    """根据 ID 获取用户"""
    user = _users_db.get(user_id)
    if user is None:
        return None
    return UserResponse(id=user.id, name=user.name, email=user.email)
```

运行类型检查：

```bash
# mypy
uv run mypy src/

# pyright
uv run pyright src/

# 两者都运行
uv run mypy src/ && uv run pyright src/
```

---

## 总结

### 关键要点

1. **选择合适的工具**：mypy（通用）或 pyright（性能）
2. **渐进式采用**：从核心模块开始，逐步扩展
3. **配置严格度**：根据项目阶段调整严格程度
4. **CI/CD 集成**：自动化类型检查流程
5. **最佳实践**：合理使用 Any，优先注解公共 API

### 常用命令速查

```bash
# mypy
mypy src/                          # 检查目录
mypy --strict src/                 # 严格模式
mypy --show-error-codes src/       # 显示错误代码
mypy --install-types               # 安装缺失的 stub

# pyright
pyright                            # 检查当前目录
pyright src/                       # 检查指定目录
pyright --verbose                  # 详细输出
pyright --outputjson report.json   # JSON 报告

# pre-commit
pre-commit run --all-files         # 运行所有检查
pre-commit run mypy                # 只运行 mypy
```

### 学习路径总结

1. **基础篇**：掌握类型注解语法和基本类型
2. **标准库篇**：学习泛型、Protocol、dataclasses 等高级工具
3. **Pydantic 篇**：使用 Pydantic 进行数据验证
4. **类型检查篇**：集成 mypy/pyright 到开发流程

🎉 **恭喜！** 你已经完成了 Python 类型系统的系统性学习。

---

**参考资料**：
- [mypy 官方文档](https://mypy.readthedocs.io/)
- [pyright 官方文档](https://github.com/microsoft/pyright)
- [typing 官方文档](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [Type Checking Best Practices](https://typing.readthedocs.io/en/latest/source/best_practices.html)
