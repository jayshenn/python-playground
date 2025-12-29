# Protocol - 结构化子类型

本章节介绍了 `Protocol`（协议），它实现了 Python 中的静态"鸭子类型"。通过 `Protocol`，你可以定义一个类必须实现的方法或属性，而不需要这些类显式地继承某个基类。

## 目录

- [01_basic_concept.py - 基本概念](01_basic_concept.py)：介绍如何定义协议以及如何编写接受该协议参数的函数。
- [02_runtime_checkable.py - 运行时检查](02_runtime_checkable.py)：介绍 `@runtime_checkable` 装饰器，使 `isinstance()` 能够用于协议。
- [03_protocol_with_attributes.py - 带属性的协议](03_protocol_with_attributes.py)：展示如何定义不仅包含方法，还包含变量属性的协议。
- [04_storage_interface_case.py - 实战示例](04_storage_interface_case.py)：展示如何使用 `Protocol` 定义统一的存储接口（Mock 存储 vs 真实存储）。

## 核心价值

1. **解耦**：调用方只依赖于"能力"（方法签名），而不依赖于具体的继承层次。
2. **灵活**：任何实现了协议要求的类都自动符合类型要求，无需修改原有类代码。
3. **安全**：在静态检查阶段就能发现不符合接口的对象，避免运行时 `AttributeError`。

## 学习建议

- 优先使用 `Protocol` 而不是传统的 `abc.ABC`（抽象基类），除非你需要提供默认的方法实现或强制显式继承关系。
- 只有在真正需要运行时进行类型判断时，才使用 `@runtime_checkable`，因为它会带来一定的运行时开销。
