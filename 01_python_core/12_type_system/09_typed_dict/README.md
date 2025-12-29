# TypedDict

本章节介绍了 `TypedDict`，它允许你为字典定义精确的结构和类型。这在处理 JSON API 响应、配置字典或其他基于键值对的数据结构时非常有用。

## 目录

- [01_basic_usage.py - 基本用法](01_basic_usage.py)：介绍如何定义 `TypedDict` 以及如何创建符合结构的字典。
- [02_optional_keys.py - 可选键](02_optional_keys.py)：介绍如何使用 `NotRequired` (Python 3.11+) 或 `total=False` 来定义可选的字典键。
- [03_inheritance.py - 继承和扩展](03_inheritance.py)：展示如何通过继承来复用和扩展字典结构。
- [04_vs_dataclass.py - TypedDict vs dataclass](04_vs_dataclass.py)：对比两种数据结构的优缺点和适用场景。

## 核心概念

1. **结构化字典**：`TypedDict` 本质上还是一个普通的 Python 字典，但它在静态类型检查层面提供了约束。
2. **非强制性**：与 `dataclass` 不同，`TypedDict` 在运行时不会验证数据，也不会改变对象的行为。
3. **NotRequired**：允许某些键在字典中缺失，而不会触发类型检查错误。

## 学习建议

- 当你需要将数据直接转换为 JSON 或从 JSON 加载时，优先考虑 `TypedDict`。
- 如果你需要数据对象具有方法、默认值或运行时属性访问（`.` 语法），请选择 `dataclass`。
