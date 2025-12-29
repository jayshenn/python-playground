# Pydantic 高级特性

本章节介绍了 Pydantic 中一些更具威力的工具，这些特性能够帮助你处理复杂的嵌套数据、通用的 API 响应以及需要动态计算的属性。

## 目录

- [01_config_dict.py - 配置 ConfigDict](01_config_dict.py)：展示如何全局控制模型行为，如禁止额外字段、开启赋值验证等。
- [02_nested_models.py - 嵌套模型](02_nested_models.py)：介绍如何构建层次化的数据结构，实现模型之间的嵌套验证。
- [03_generic_models.py - 泛型模型](03_generic_models.py)：介绍如何定义通用的数据容器（如通用的 `Response[T]` 模型）。
- [04_root_model.py - RootModel](04_root_model.py)：介绍如何定义以列表或字典为顶层结构的模型。
- [05_computed_fields.py - 计算字段](05_computed_fields.py)：展示如何使用 `@computed_field` 定义在序列化时自动生成的动态属性。

## 核心概念

1. **组合与嵌套**：Pydantic 模型可以作为另一个模型的字段类型，从而实现递归验证。
2. **泛型支持**：通过集成 Python 的 `Generic`，Pydantic 能够处理参数化类型。
3. **计算字段**：允许你将类方法（Property）标记为模型的一部分，使其在导出 JSON 时自动包含。

## 学习建议

- 仔细理解 `RootModel` 的用途，它解决了"顶级对象不是字典"的问题（例如顶级是一个数组的 JSON）。
- 合理使用 `computed_field` 来减少客户端的计算压力（例如在服务端计算好总价）。
