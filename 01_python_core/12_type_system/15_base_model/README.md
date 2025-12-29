# BaseModel 基础

`BaseModel` 是 Pydantic 的核心基类。通过继承它，你可以定义复杂的数据结构，并享受到自动验证、类型转换和序列化等功能。

## 目录

- [01_first_model.py - 第一个 Pydantic 模型](01_first_model.py)：展示如何定义模型、设置默认值以及 Pydantic 的智能类型转换。
- [02_validation_errors.py - 验证错误处理](02_validation_errors.py)：介绍当输入数据不符合预期时，如何捕获并解析 `ValidationError`。
- [03_strict_vs_lax.py - 严格模式 vs 宽松模式](03_strict_vs_lax.py)：展示两种验证模式的区别，以及如何通过 `ConfigDict` 进行切换。
- [04_model_inheritance.py - 模型继承](04_model_inheritance.py)：演示如何通过继承复用字段，构建层次化的数据模型。

## 核心概念

1. **类型转换**：在宽松模式下，Pydantic 会尝试将数据转换为目标类型（如 `"123"` -> `123`）。
2. **ValidationError**：当数据无法解析为目标类型或不符合约束时抛出的异常。
3. **ConfigDict**：用于控制模型行为的配置字典（如是否允许额外字段、是否开启严格模式等）。

## 学习建议

- 理解 Pydantic 是如何处理 `None` 和默认值的。
- 习惯查阅 `ValidationError.errors()` 返回的结构，它对于 API 错误提示非常有用。
