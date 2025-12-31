# Pydantic AI 高级特性示例

本目录包含高级特性的示例代码。

## 📝 示例列表

### 01_streaming.py
流式传输示例，演示如何：
- 基础文本流式传输
- 结构化数据流式传输
- 带缓冲的流式输出
- 事件流处理

```bash
uv run python 04_pydantic_ai/05_advanced/01_streaming.py
```

### 02_validation.py
输出验证示例，演示如何：
- 使用 Pydantic 自动验证
- 自定义输出验证器
- ModelRetry 自我修正
- 验证失败时的重试机制

```bash
uv run python 04_pydantic_ai/05_advanced/02_validation.py
```

## 📚 相关文档

- [07_结构化输出.md](../docs/07_结构化输出.md) - 结构化输出详解
- [08_流式传输.md](../docs/08_流式传输.md) - 流式传输完整指南
