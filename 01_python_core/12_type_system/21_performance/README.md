# 性能优化

虽然 Pydantic V2 已经非常快（核心由 Rust 编写），但在处理大规模数据或极高性能敏感的场景下，通过一些技巧进一步提升性能仍然很有意义。

## 目录

- [01_strict_mode.py - 严格模式](01_strict_mode.py)：介绍为什么开启严格模式（Strict Mode）能减少类型转换开销，从而提升速度。
- [02_disable_features.py - 禁用功能](02_disable_features.py)：介绍如何通过配置禁用如赋值验证等功能来减少运行时开销。
- [03_model_construct.py - 跳过验证](03_model_construct.py)：展示如何使用 `model_construct()` 从受信任的数据源直接创建对象，彻底绕过验证逻辑。
- [04_batch_validation.py - 批量验证](04_batch_validation.py)：演示如何使用 `TypeAdapter` 对大型列表进行批量处理，减少重复开销。

## 优化策略

1. **类型匹配**：尽量在输入端就提供正确类型的数据，避免 Pydantic 进行昂贵的类型解析转换。
2. **信任边界**：对于数据库查询结果等已经验证过的数据，使用 `model_construct`。
3. **按需配置**：不要开启不需要的验证选项（如 `validate_assignment`）。

## 学习建议

- 在大多数情况下，Pydantic 的默认性能已经足够。只有在基准测试（Benchmarking）表明验证是瓶颈时，才应用这些优化。
- 慎用 `model_construct`，它虽然最快，但如果数据不合法，后续可能会导致逻辑崩溃。
