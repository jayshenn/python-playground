# Callable 和函数类型

本章节介绍了如何对函数、回调和装饰器进行类型注解。在 Python 中，函数是"一等公民"，能够被传递和返回，因此对其进行准确的类型注解至关重要。

## 目录

- [01_basic_usage.py - 基本用法](01_basic_usage.py)：介绍 `Callable[[参数类型...], 返回类型]` 的基本语法。
- [02_callback_functions.py - 回调函数](02_callback_functions.py)：展示如何注解作为参数传递的异步或同步回调函数。
- [03_higher_order_functions.py - 高阶函数](03_higher_order_functions.py)：介绍返回函数的函数（闭包）的类型注解。
- [04_decorator_annotations.py - 装饰器的类型注解](04_decorator_annotations.py)：展示如何使用 `ParamSpec` 和 `TypeVar` 编写类型安全的装饰器。

## 核心概念

1. **Callable**：来自 `collections.abc` (推荐) 或 `typing`，用于定义可调用对象的签名。
2. **签名语法**：`Callable[[int, str], bool]` 表示接受一个整数和一个字符串，返回布尔值。
3. **... 语法**：`Callable[..., int]` 表示接受任意参数，返回整数。
4. **ParamSpec**：用于在装饰器中透传被装饰函数的参数列表。

## 学习建议

- 始终尽量明确回调函数的参数和返回类型，避免使用 `Callable[..., Any]`。
- 对于复杂的函数签名，可以使用类型别名（`type` 语句）来简化。
