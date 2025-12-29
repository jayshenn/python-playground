# dataclasses

本章节介绍了 Python 标准库中的 `dataclasses` 模块。它提供了一个装饰器和一系列工具，用于自动为类生成样板代码（如 `__init__`、`__repr__`、`__eq__` 等），极大地简化了数据对象的定义。

## 目录

- [01_basic_usage.py - 基本用法](01_basic_usage.py)：展示 `@dataclass` 装饰器的核心功能和自动生成的方法。
- [02_field_function.py - field() 函数](02_field_function.py)：介绍如何通过 `field()` 控制属性的默认值、是否参与比较/显示以及元数据。
- [03_config_options.py - 配置选项](03_config_options.py)：展示 `frozen`（不可变）、`order`（排序）、`slots`（内存优化）等配置。
- [04_init_var_post_init.py - 初始化处理](04_init_var_post_init.py)：介绍 `InitVar` 和 `__post_init__` 用于处理复杂的初始化逻辑。
- [05_inheritance.py - 继承](05_inheritance.py)：展示数据类之间的继承行为。
- [06_config_management_case.py - 实战示例](06_config_management_case.py)：展示如何使用嵌套的数据类构建复杂的配置管理系统。

## 核心特性

1. **自动生成代码**：减少了大量重复的手写方法。
2. **类型驱动**：基于类属性的类型注解来识别字段。
3. **可读性强**：生成的 `__repr__` 非常清晰，便于调试。
4. **性能优化**：支持 `slots=True` 减少内存占用。

## 学习建议

- 对于纯粹的数据容器（只有属性，没有或很少有复杂逻辑），优先使用 `dataclass` 而不是普通的类。
- 注意可变默认值问题：列表或字典作为默认值时，务必使用 `field(default_factory=...)`。
