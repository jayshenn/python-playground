# LangChain (Python) 学习模块

## 模块简介

LangChain 是一个开源框架，专为构建基于大语言模型（LLM）的应用而设计。它提供了预构建的代理架构和与任何模型或工具的集成能力，使开发者能够快速构建智能应用。

### 核心优势

- **快速开发**：可以用不到 10 行代码连接模型和工具
- **统一接口**：为不同的模型提供商（OpenAI、Anthropic、Google 等）提供标准化接口
- **分层架构**：构建在 LangGraph 之上，提供高级抽象
- **生产就绪**：支持中间件、护栏、人在环中等生产级特性

## 学习文档

本模块包含两个主要学习文档：

### 1. [核心组件](./01_核心组件.md)

学习 LangChain 的基础概念和核心功能：

- **Overview & Quickstart** - LangChain 简介和快速开始
- **Agents（代理）** - 理解代理的工作原理和 ReAct 模式
- **Models（模型）** - 模型集成和多提供商支持
- **Messages（消息）** - 消息类型和对话管理
- **Tools（工具）** - 创建和使用工具
- **Short-term Memory（短期记忆）** - 线程管理和状态保持
- **Streaming（流式输出）** - 实时响应和增量输出
- **Structured Output（结构化输出）** - 确保输出符合指定格式

### 2. [高级特性](./02_高级特性.md)

深入学习构建生产级代理系统的高级功能：

- **Middleware（中间件）** - 控制代理执行流程和添加横切关注点
- **Multi-agent（多代理）** - 构建复杂的多代理协作系统
  - Router（路由）、Handoffs（交接）、Subagents（子代理）、Skills（技能）
- **Context Engineering（上下文工程）** - 优化信息传递和上下文管理
- **Human-in-the-Loop（人在环中）** - 添加人工监督和决策
- **Guardrails（护栏）** - 确保安全性和合规性
- **Runtime（运行时）** - 灵活的依赖注入和资源管理

## 学习路径建议

### 入门路径（1-2 天）
1. 阅读 Overview & Quickstart
2. 学习 Agents、Models、Tools 的基础使用
3. 运行几个简单示例

### 进阶路径（3-5 天）
1. 深入学习 Messages 和 Short-term Memory
2. 掌握 Streaming 和 Structured Output
3. 开始使用 Middleware 和简单的 Multi-agent 模式

### 生产路径（1-2 周）
1. 学习完整的 Multi-agent 架构模式
2. 实现 Context Engineering 和 Human-in-the-Loop
3. 配置 Guardrails 和 Runtime 管理
4. 准备部署到生产环境

## 相关资源

- [LangChain 官方文档](https://docs.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangSmith 调试工具](https://smith.langchain.com/)

## 下一步

完成 LangChain 模块后，建议继续学习：
- **LangGraph** - 低级编排框架，用于构建确定性工作流
- **Deep Agents** - 用于处理复杂任务的高级代理系统
- **LangSmith** - 部署、监控和评估工具
