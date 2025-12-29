# Python 3.12+ 类型系统新特性

本章节介绍了 Python 3.12 引入的重大类型系统改进，包括更简洁的类型别名定义和泛型语法。

## 目录

- [01_type_statement.py - 新的 type 语句](01_type_statement.py)：介绍如何使用新的 `type` 关键字定义类型别名，取代旧的 `TypeAlias`。
- [02_type_parameter_syntax.py - 类型参数语法 [T]](02_type_parameter_syntax.py)：介绍如何使用方括号直接在函数或类名后定义泛型参数。
- [03_type_alias_type.py - TypeAliasType](03_type_alias_type.py)：介绍如何使用运行时对象 `TypeAliasType` 进行类型元编程。
- [04_comprehensive_example.py - 综合应用](04_comprehensive_example.py)：展示如何结合使用上述新特性来构建类型安全的业务逻辑。

## 核心改进

1. **更简单的泛型**：不再需要显式定义 `TypeVar`，直接使用 `[T]`。
2. **延迟求值**：新的 `type` 语句定义的别名支持延迟求值（Lazy evaluation），方便定义递归类型。
3. **更清晰的语法**：`type` 语句让类型别名的意图更加明确，且避免了导入 `TypeAlias` 的繁琐。

## 注意事项

- 这些特性仅在 **Python 3.12 及更高版本**中可用。
- 如果你的项目需要兼容旧版本 Python，请查阅前几个章节介绍的传统语法。
