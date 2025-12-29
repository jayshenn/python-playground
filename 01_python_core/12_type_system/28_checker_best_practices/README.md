# 类型检查最佳实践

本章节总结了在实际项目中使用类型检查器的核心原则和最佳实践，旨在帮助你编写既严谨又易于维护的代码。

## 目录

- [01_when_use_any.py - 何时使用 Any](01_when_use_any.py)：区分合理使用 `Any` 的场景与应避免的滥用行为。
- [02_avoid_over_annotation.py - 避免过度注解](02_avoid_over_annotation.py)：介绍如何利用类型推断减少冗余注解，保持代码简洁。
- [03_ignore_comments.py - 忽略注释规范](03_ignore_comments.py)：介绍如何正确、有责任感地使用 `# type: ignore`。
- [04_function_signature_first.py - 函数签名优先](04_function_signature_first.py)：强调函数边界注解的重要性。
- [05_protocol_over_abc.py - 协议优先](05_protocol_over_abc.py)：探讨为什么在大多数情况下 `Protocol` 优于抽象基类。
- [06_config_management.py - 配置管理](06_config_management.py)：介绍如何组织和管理类型检查器的配置文件。

## 核心原则

1. **务实主义**：类型注解是为了服务开发者，不要为了追求 100% 的严格而写出难以阅读的代码。
2. **信任推断**：现代检查器非常智能，对于显而易见的局部变量，无需手动重复标注。
3. **接口为重**：函数参数和返回值是类型安全的"关口"，必须严格把关。
4. **解耦为先**：使用结构化子类型（Protocol）来减少类之间的强耦合。

## 学习建议

- 养成阅读 mypy/pyright 官方最佳实践文档的习惯。
- 团队内部应统一一套类型检查配置，避免因环境不同导致的报错不一致。
