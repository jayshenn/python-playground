# 类型工具函数

本章节介绍了一些在运行时操作或检查类型信息的实用工具函数。这些函数通常用于框架开发、数据验证或复杂的调试场景。

## 目录

- [01_get_type_hints.py - get_type_hints](01_get_type_hints.py)：介绍如何在运行时获取函数或类的完整类型注解信息。
- [02_get_origin_args.py - get_origin 和 get_args](02_get_origin_args.py)：展示如何拆解泛型类型（如 `list[int]` -> `list`, `int`）。
- [03_cast.py - cast](03_cast.py)：介绍如何强制告诉类型检查器一个变量的类型（不影响运行时）。
- [04_assert_never.py - assert_never](04_assert_never.py)：展示如何利用 `Never` 类型进行运行时和静态的穷举性检查。
- [05_reveal_type.py - reveal_type](05_reveal_type.py)：介绍在开发期间让类型检查器输出推断类型的调试技巧。

## 核心价值

1. **类型反射**：在运行时访问类型提示，支持自动化的序列化/反序列化。
2. **泛型自省**：能够编写感知泛型参数的通用逻辑。
3. **开发辅助**：通过 `cast` 和 `reveal_type` 解决复杂的类型检查报错或疑惑。

## 学习建议

- `cast()` 是一种"逃生舱"，只在类型检查器无法自动推断正确类型时使用。
- `get_type_hints()` 优于直接访问 `__annotations__`，因为它能处理延迟引用和继承。
- 在编写 `match` 语句或长 `if-elif` 链时，始终尝试在末尾添加 `assert_never()`。
