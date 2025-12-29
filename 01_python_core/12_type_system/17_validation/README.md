# 数据验证

Pydantic 提供了多层次的验证机制，从基础的类型检查到复杂的业务逻辑验证。本章节介绍如何利用这些机制确保数据的完整性和正确性。

## 目录

- [01_builtin_validators.py - 内置验证器](01_builtin_validators.py)：介绍 Pydantic 提供的专用验证类型，如 `EmailStr`、`HttpUrl` 等。
- [02_custom_field_validator.py - 自定义字段验证器](02_custom_field_validator.py)：介绍如何使用 `@field_validator` 为单个或多个字段编写自定义验证逻辑。
- [03_model_validator.py - 模型验证器](03_model_validator.py)：介绍如何使用 `@model_validator` 访问整个模型的数据，实现跨字段的逻辑检查。
- [04_conditional_validation.py - 条件验证](04_conditional_validation.py)：展示如何根据某些字段的值来决定其他字段的合法性（如根据支付方式验证不同的必填项）。

## 验证流程

1. **基础类型转换**：首先尝试将输入数据转换为声明的类型。
2. **字段约束检查**：执行 `Field()` 中定义的约束（如 `min_length`, `gt`）。
3. **字段验证器**：执行 `@field_validator` 装饰的函数。
4. **模型验证器**：最后执行 `@model_validator` 装饰的函数，进行全局检查。

## 学习建议

- 始终优先使用 Pydantic 的内置类型（如 `EmailStr`），因为它们已经过严格测试。
- 字段验证器应该是"纯"的，即只关注数据校验，不应产生副作用。
- 如果需要比较两个字段（如密码确认），必须使用模型验证器（`mode='after'`）。
