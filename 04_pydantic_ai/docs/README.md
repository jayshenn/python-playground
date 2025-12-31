# Pydantic AI 完整学习指南

> Pydantic AI 是由 Pydantic 团队打造的 Python Agent 框架，旨在帮助开发者快速、自信、轻松地构建生产级 GenAI 应用和工作流。

## 📚 文档目录

### 基础篇
- [01_快速开始.md](./01_快速开始.md) - 安装、环境配置、第一个 Agent
- [02_核心概念.md](./02_核心概念.md) - Agent、RunContext、工具、依赖注入等核心概念

### 核心功能篇
- [03_Agent系统.md](./03_Agent系统.md) - Agent 的创建、配置、运行方式详解
- [04_工具系统.md](./04_工具系统.md) - 工具定义、注册、参数、返回值处理
- [05_依赖注入.md](./05_依赖注入.md) - RunContext、依赖类型、测试与覆盖
- [06_模型支持.md](./06_模型支持.md) - 支持的模型提供商、配置、自定义模型

### 高级特性篇
- [07_结构化输出.md](./07_结构化输出.md) - 使用 Pydantic 模型定义和验证输出
- [08_流式传输.md](./08_流式传输.md) - 流式文本和结构化输出
- [09_图工作流.md](./09_图工作流.md) - 基于类型提示的复杂工作流
- [10_持久化执行.md](./10_持久化执行.md) - 长时间运行任务、重试、容错
- [11_人机协作.md](./11_人机协作.md) - 工具审批、人在环中的交互

### 实践篇
- [12_可观测性.md](./12_可观测性.md) - Logfire 集成、追踪、监控、调试
- [13_测试与评估.md](./13_测试与评估.md) - 测试策略、Evals、性能评估
- [14_最佳实践.md](./14_最佳实践.md) - 设计模式、性能优化、安全考虑
- [15_实战案例.md](./15_实战案例.md) - 完整应用案例分析

## 🎯 学习路径

### 初学者路径（1-2天）
1. 阅读 [01_快速开始.md](./01_快速开始.md) 并运行第一个示例
2. 学习 [02_核心概念.md](./02_核心概念.md) 理解基本原理
3. 实践 [03_Agent系统.md](./03_Agent系统.md) 创建自己的 Agent
4. 尝试 [04_工具系统.md](./04_工具系统.md) 给 Agent 添加工具

### 进阶路径（3-5天）
5. 深入 [05_依赖注入.md](./05_依赖注入.md) 学习高级模式
6. 了解 [06_模型支持.md](./06_模型支持.md) 选择合适的模型
7. 掌握 [07_结构化输出.md](./07_结构化输出.md) 控制输出格式
8. 学习 [08_流式传输.md](./08_流式传输.md) 提升用户体验

### 高级路径（1周）
9. 研究 [09_图工作流.md](./09_图工作流.md) 构建复杂应用
10. 掌握 [10_持久化执行.md](./10_持久化执行.md) 处理长任务
11. 实现 [11_人机协作.md](./11_人机协作.md) 安全机制
12. 集成 [12_可观测性.md](./12_可观测性.md) 监控系统

### 生产就绪路径（2周）
13. 完善 [13_测试与评估.md](./13_测试与评估.md) 体系
14. 应用 [14_最佳实践.md](./14_最佳实践.md) 指南
15. 参考 [15_实战案例.md](./15_实战案例.md) 构建完整应用

## 🌟 核心特性

### 1. 类型安全优先
- 完整的类型提示支持
- IDE 自动补全和类型检查
- 在编写时而非运行时发现错误
- 类似 Rust 的"如果编译通过，就能工作"的感觉

### 2. 模型无关设计
支持 20+ 模型提供商：
- **OpenAI**: GPT-4, GPT-4 Turbo, GPT-3.5
- **Anthropic**: Claude 3.5 Sonnet, Claude 3 Opus/Haiku
- **Google**: Gemini Pro, Gemini Flash
- **开源模型**: Groq, Mistral, Cohere, HuggingFace
- **本地模型**: Ollama
- **云平台**: Azure, AWS Bedrock, Google Vertex AI
- 以及任何 OpenAI 兼容的 API

### 3. 无缝可观测性
- 与 Pydantic Logfire 深度集成
- 基于 OpenTelemetry 标准
- 实时调试和性能监控
- 成本追踪和行为分析
- 支持任何 OTel 兼容平台

### 4. 强大的工具系统
- 简单的装饰器注册
- 自动从文档字符串生成描述
- 类型安全的参数和返回值
- 支持同步和异步工具
- 工具集管理和复用

### 5. 依赖注入
- 类型安全的上下文传递
- 灵活的依赖定义
- 便于测试和模拟
- 支持同步和异步依赖

### 6. 结构化输出
- 使用 Pydantic 模型定义输出
- 自动验证和解析
- 流式结构化输出
- 输出验证器

### 7. 高级特性
- **图工作流**: 复杂的多步骤流程
- **持久化执行**: 长时间运行任务
- **流式传输**: 实时响应
- **人机协作**: 工具审批机制
- **协议支持**: MCP、Agent2Agent

## 🛠️ 技术栈

### 核心依赖
```toml
pydantic-ai = "^0.0.14"  # 核心框架
pydantic = "^2.10"       # 数据验证
httpx = "^0.28"          # HTTP 客户端
```

### 可选依赖
```toml
# 模型提供商
pydantic-ai-slim[openai]      # OpenAI
pydantic-ai-slim[anthropic]   # Anthropic
pydantic-ai-slim[google]      # Google Gemini
pydantic-ai-slim[groq]        # Groq
pydantic-ai-slim[mistral]     # Mistral
pydantic-ai-slim[cohere]      # Cohere
pydantic-ai-slim[bedrock]     # AWS Bedrock
pydantic-ai-slim[huggingface] # HuggingFace

# 功能增强
pydantic-ai-slim[logfire]     # 可观测性
pydantic-ai-slim[evals]       # 评估工具
pydantic-ai-slim[cli]         # 命令行工具
pydantic-ai-slim[mcp]         # MCP 协议
```

## 📖 与其他框架对比

### vs LangChain
- **Pydantic AI**: 更注重类型安全、简洁的 API、FastAPI 风格
- **LangChain**: 更成熟的生态、更多的集成、更复杂的抽象

### vs LlamaIndex
- **Pydantic AI**: 通用 Agent 框架、灵活的工具系统
- **LlamaIndex**: 专注于 RAG 和数据索引

### vs Haystack
- **Pydantic AI**: Python 原生、Pydantic 验证
- **Haystack**: 面向生产的管道、更多的组件

## 🔗 相关资源

- [官方文档](https://ai.pydantic.dev/)
- [GitHub 仓库](https://github.com/pydantic/pydantic-ai)
- [Pydantic Logfire](https://docs.pydantic.dev/logfire/)
- [示例代码](https://github.com/pydantic/pydantic-ai/tree/main/examples)
- [社区讨论](https://github.com/pydantic/pydantic-ai/discussions)

## 📝 快速示例

```python
from pydantic_ai import Agent
from pydantic import BaseModel

# 定义结构化输出
class CityInfo(BaseModel):
    city: str
    country: str
    population: int

# 创建 Agent
agent = Agent(
    'openai:gpt-4',
    output_type=CityInfo,
    system_prompt='提取城市信息。'
)

# 运行 Agent
result = agent.run_sync('巴黎有多少人口？')
print(result.data)
# CityInfo(city='Paris', country='France', population=2161000)
```

## 🎓 学习建议

1. **动手实践**: 每个概念都配有示例代码，建议亲自运行
2. **循序渐进**: 按照学习路径逐步深入，不要跳过基础
3. **关注类型**: 充分利用类型提示，让 IDE 帮助你
4. **阅读源码**: Pydantic AI 代码质量高，值得学习
5. **参与社区**: 在 GitHub Discussions 提问和分享

## 🚀 开始学习

现在就开始你的 Pydantic AI 学习之旅吧！建议从 [01_快速开始.md](./01_快速开始.md) 开始。
