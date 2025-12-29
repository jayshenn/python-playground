# 与其他库集成

Pydantic 的强大之处不仅在于其自身，还在于它能与 Python 生态系统中的其他标准和框架无缝协作。

## 目录

- [01_dataclasses_integration.py - 与 dataclasses 集成](01_dataclasses_integration.py)：介绍如何使用 Pydantic 的 `dataclass` 装饰器为标准数据类添加验证功能。
- [02_typeddict_integration.py - 与 TypedDict 集成](02_typeddict_integration.py)：介绍如何使用 `TypeAdapter` 对原始字典进行 Pydantic 风格的验证。
- [03_settings_management.py - Settings 管理](03_settings_management.py)：演示如何使用 `pydantic-settings` 从环境变量和 `.env` 文件自动加载配置。
- [04_fastapi_integration.py - FastAPI 集成示例](04_fastapi_integration.py)：展示 Pydantic 如何作为 FastAPI 的核心，处理请求验证和响应序列化。

## 核心工具

1. **TypeAdapter**：Pydantic V2 引入的核心工具，允许你验证非 `BaseModel` 类型（如 `list[int]`, `TypedDict`, `dataclass`）。
2. **BaseSettings**：来自 `pydantic-settings` 包，是管理生产环境配置的事实标准。

## 学习建议

- 如果你的项目已经大量使用了标准 `dataclasses`，可以通过 Pydantic 的适配器无缝迁移。
- 在构建 Web 应用时，深入理解 Pydantic 模型如何转换为 OpenAPI Schema。
