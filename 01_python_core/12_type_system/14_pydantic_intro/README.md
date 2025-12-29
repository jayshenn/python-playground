# Pydantic 简介

Pydantic 是 Python 中最流行的第三方数据验证库，它通过 Python 的类型注解来强制执行类型检查和数据转换。

## 目录

- [01_what_is_pydantic.py - 什么是 Pydantic](01_what_is_pydantic.py)：展示 Pydantic 的核心功能——自动验证和智能类型转换。
- [02_version_comparison.py - 版本对比](02_version_comparison.py)：介绍 Pydantic 1.x 和 2.x 的主要区别（推荐使用 2.x）。
- [03_installation.py - 安装说明](03_installation.py)：关于如何安装 Pydantic 及其可选功能的代码注释说明。

## 为什么选择 Pydantic？

1. **开发者体验**：利用原生 Python 类型注解，无需学习复杂的特定领域语言。
2. **性能**：Pydantic V2 的核心逻辑由 Rust 编写，处理速度比 V1 快 5-50 倍。
3. **生态系统**：被 FastAPI、LangChain 等数千个顶级项目深度集成。
4. **验证与解析**：它不仅验证数据，还能将输入数据转换为你声明的类型。

## 学习建议

- 如果你是新项目，务必从 Pydantic 2.x 开始。
- 理解 Pydantic 是"解析"（Parsing）库而不仅仅是"验证"（Validation）库——它会尝试修复你的数据。
