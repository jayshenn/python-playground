# 容器类型注解

本章节详细介绍了如何对 Python 中的容器类型（如列表、字典、集合和元组）进行类型注解，以及如何使用抽象容器类型来提高代码的灵活性。

## 目录

- [01_list_annotation.py - 列表注解](01_list_annotation.py)：展示如何注解简单、嵌套和混合类型的列表。
- [02_dict_annotation.py - 字典注解](02_dict_annotation.py)：展示如何注解键值对，处理复杂字典结构。
- [03_set_annotation.py - 集合注解](03_set_annotation.py)：展示如何注解唯一元素集合。
- [04_tuple_annotation.py - 元组注解](04_tuple_annotation.py)：介绍固定长度与可变长度元组的注解差异。
- [05_abstract_containers.py - 抽象容器类型](05_abstract_containers.py)：介绍 `Sequence`、`Mapping`、`Iterable` 等抽象类型的使用。

## 学习建议

1. **优先使用抽象类型**：在函数参数中，优先使用 `Sequence` 或 `Iterable` 而不是 `list`，使用 `Mapping` 而不是 `dict`。这能让你的函数接受更多类型的输入。
2. **返回值使用具体类型**：在函数返回值中，使用具体的 `list` 或 `dict`，这能为调用者提供更明确的类型信息。
3. **元组的特殊性**：记住 `tuple[int, int]` 表示长度为 2 且都是整数，而 `tuple[int, ...]` 表示任意长度的整数元组。
4. **Python 3.9+**：直接使用小写的内置类型名进行注解。
