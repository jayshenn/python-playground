# 类型检查实战

本章节通过具体的实践场景，展示了如何处理现实开发中遇到的类型检查难题，如遗留代码迁移、三方库缺失、循环导入等。

## 目录

- [01_gradual_typing.py - 渐进式类型化](01_gradual_typing.py)：介绍如何将现有的无注解项目逐步迁移到带类型的状态。
- [02_third_party_libs.py - 处理第三方库](02_third_party_libs.py)：介绍处理缺少类型信息的第三方库的三种方法：忽略、安装 Stub 或自定义 Stub。
- [03_typing_extensions.py - 兼容性工具](03_typing_extensions.py)：介绍如何使用 `typing_extensions` 在旧版本 Python 中使用新特性。
- [04_common_issues.py - 常见问题](04_common_issues.py)：分析循环导入、Any 传播和泛型不完整等典型问题的解决方案。

## 核心策略

1. **核心优先**：从项目的底层数据模型和关键公共 API 开始添加注解。
2. **信任但验证**：对于没有类型的外部库，使用 Stub 文件或 `cast()` 来恢复类型安全。
3. **向后兼容**：利用 `typing_extensions` 保证代码在不同 Python 版本间的一致性。

## 学习建议

- 遇到类型检查报错不要沮丧，它是你的"哨兵"，正在帮你拦截未来的线上事故。
- 学习如何阅读和编写 `.pyi` 存根文件，这是提升进阶类型技能的关键。
