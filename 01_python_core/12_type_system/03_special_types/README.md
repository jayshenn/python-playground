# 特殊类型形式

本章节介绍了 Python 类型系统中一些特殊的类型注解形式，这些形式提供了更灵活和精确的方式来描述数据。

## 目录

- [01_union_type.py - Union 类型](01_union_type.py)：介绍如何使用 `|` 或 `Union` 允许一个变量接受多种可能的类型。
- [02_optional_type.py - Optional 类型](02_optional_type.py)：介绍如何处理可能为 `None` 的可选值。
- [03_literal_type.py - Literal 类型](03_literal_type.py)：介绍如何限定变量只能取特定的字面值。
- [04_any_type.py - Any 类型](04_any_type.py)：介绍如何表示不受约束的任何类型（应谨慎使用）。
- [05_never_noreturn.py - Never / NoReturn](05_never_noreturn.py)：介绍表示永不返回或穷举检查的底部类型。

## 学习建议

1. 优先使用 Python 3.10+ 引入的 `|` 语法来表示 `Union` 和 `Optional`。
2. 尽量避免滥用 `Any`，因为它会使类型检查失效。
3. `Literal` 非常适合用于配置项、状态机或有限的选项集合。
4. `Never` 在进行穷举检查（Exhaustiveness checking）时非常有用。
