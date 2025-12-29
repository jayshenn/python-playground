# 字段配置 (Fields)

Pydantic 的 `Field` 函数提供了对模型字段的超细粒度控制。通过它，你可以定义校验规则、描述信息、别名以及动态默认值。

## 目录

- [01_field_function.py - Field 函数](01_field_function.py)：介绍 `Field` 的基本用法，包括描述、必需性声明等。
- [02_field_constraints.py - 字段约束](02_field_constraints.py)：展示如何设置数值范围（`gt`, `le`）、字符串长度（`min_length`）和正则表达式约束。
- [03_field_alias.py - 字段别名](03_field_alias.py)：介绍如何处理 Python 命名规范与外部数据源（如 JSON）不一致的情况。
- [04_default_factory.py - 默认值和工厂函数](04_default_factory.py)：演示如何为字段提供动态生成的默认值（如 UUID、当前时间）。

## 核心特性

1. **元数据声明**：通过 `description` 和 `examples` 为自动生成的文档提供支持。
2. **校验内置**：很多常见的校验（如数值大小、字符串长度）直接内置在 `Field` 参数中。
3. **别名系统**：支持在输入和输出时使用不同的字段名。
4. **必需性**：使用 `...` 作为 `Field` 的第一个参数来明确表示该字段是必需的。

## 学习建议

- 尽量在模型中添加 `description`，这不仅能作为代码文档，还能在生成 OpenAPI 文档时非常有用。
- 对于 `list`、`dict` 等可变类型，永远使用 `default_factory`。
