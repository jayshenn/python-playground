# LangGraph (Python) 学习模块

## 模块简介

LangGraph 是一个用于构建**有状态**、**多代理**应用程序的低级编排框架。它提供了比 LangChain 更精确的控制和灵活性，使你能够构建复杂的、生产就绪的 AI 工作流。

### 核心优势

- **状态管理**：内置的状态持久化和管理能力
- **图形化工作流**：使用图（Graph）来表示和控制复杂的工作流
- **双 API 设计**：Graph API（声明式）和 Functional API（命令式）满足不同需求
- **生产就绪**：支持持久化、中断、流式输出、重试等生产级特性
- **可观测性**：与 LangSmith 集成，提供完整的可观测性

## 与 LangChain 的区别

| 特性 | LangChain | LangGraph |
|-----|-----------|-----------|
| **抽象级别** | 高级框架 | 低级编排框架 |
| **控制精度** | 预构建模式 | 精确控制每个步骤 |
| **学习曲线** | 低 | 中等 |
| **适用场景** | 快速原型、简单代理 | 复杂工作流、生产应用 |
| **状态管理** | 基础支持 | 完整的持久化和恢复 |
| **可视化** | 有限 | 原生支持图可视化 |

## 学习文档

本模块包含两个主要学习文档：

### 1. [基础](./01_基础.md)

学习 LangGraph 的核心概念和两种 API：

**核心概念**：
- 图（Graph）、节点（Nodes）、边（Edges）
- 状态（State）及其类型
- 状态归约器（Reducers）
- 特殊节点（START/END）

**Graph API**（声明式）：
- 基本使用流程
- 顺序处理、条件分支、并行处理
- 持久化（Checkpointing）

**Functional API**（命令式）：
- `@entrypoint` 和 `@task` 装饰器
- 基本使用方法
- 与 Graph API 混合使用

**API 选择指南**：
- 何时使用 Graph API
- 何时使用 Functional API
- 混合使用策略
- 详细对比表格

**实际应用示例**：
- 简单的对话机器人
- 数据处理流水线
- 多步骤决策流程

### 2. [高级特性](./02_高级特性.md)

深入学习构建生产级应用的高级功能：

**1. Persistence（持久化）**：
- Checkpointer 的工作原理
- 多种持久化方案（InMemory、SQLite、PostgreSQL）
- 状态管理方法（get_state、update_state、get_state_history）

**2. Interrupts（中断）**：
- 人在回路（HITL）工作流
- `interrupt()` 函数的使用
- 审批工作流实现
- 断点（Breakpoints）设置

**3. Memory（记忆）**：
- 短期记忆 vs 长期记忆
- Store 的初始化和使用
- 语义搜索能力
- 记忆管理最佳实践

**4. Durable Execution（持久化执行）**：
- RetryPolicy 配置
- 自动重试机制
- 指数退避策略
- 故障恢复方案

**5. Streaming（流式输出）**：
- 五种流式模式（updates、values、messages、custom、debug）
- Token 级别流式输出
- 异步流式输出
- 多模式组合使用

## 学习路径建议

### 入门路径（2-3 天）
1. 阅读基础文档的核心概念部分
2. 学习 Graph API 的基本使用
3. 运行简单的顺序处理和条件分支示例
4. 了解 Functional API 的使用场景

### 进阶路径（4-6 天）
1. 深入理解状态管理和归约器
2. 掌握 API 选择指南，知道何时使用哪种 API
3. 学习持久化（Persistence）的基础使用
4. 实践中断（Interrupts）机制

### 生产路径（1-2 周）
1. 学习完整的高级特性（Persistence、Interrupts、Memory、Durable Execution、Streaming）
2. 实现包含人工审批的工作流
3. 配置重试策略和错误处理
4. 集成长期记忆管理
5. 实现流式输出优化用户体验
6. 准备部署到生产环境

## 最佳实践速查

### 持久化
- ✅ 开发环境使用 `InMemorySaver`
- ✅ 生产环境使用 `PostgresSaver`
- ✅ 始终为每个会话提供唯一的 `thread_id`

### 中断与人工干预
- ✅ 中断必须配合 checkpointer 使用
- ✅ 在敏感操作前添加审批节点
- ✅ 向 `interrupt()` 传递清晰的上下文信息

### 记忆管理
- ✅ 短期记忆（对话上下文）使用 State + Checkpointer
- ✅ 长期记忆（用户偏好）使用 Store
- ✅ 仅对需要语义搜索的字段进行嵌入

### 持久化执行
- ✅ 为不稳定的外部调用配置重试策略
- ✅ 使用指数退避避免过载下游服务
- ✅ 结合 checkpointing 实现故障恢复

### 流式输出
- ✅ 聊天应用启用 LLM streaming 和 `"messages"` 模式
- ✅ 使用多模式流式输出获取全面信息
- ✅ 异步应用优先使用 `astream()`

## 实际应用场景

LangGraph 适合以下应用场景：

1. **复杂对话系统**：需要多轮交互、状态保持的聊天机器人
2. **审批工作流**：需要人工干预的业务流程自动化
3. **数据处理管道**：多步骤的数据清洗、转换、验证流程
4. **多代理协作**：多个 AI 代理协同完成复杂任务
5. **长时间运行任务**：需要故障恢复和断点续传的任务
6. **生产级 AI 应用**：需要可靠性、可观测性的企业应用

## 相关资源

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangGraph 教程](https://langchain-ai.github.io/langgraph/tutorials/)
- [LangSmith 平台](https://www.langchain.com/langsmith)

## 下一步

完成 LangGraph 模块后，建议继续学习：
- **Deep Agents** - 用于处理复杂任务的高级代理系统
- **LangSmith** - 部署、监控和评估工具

返回 LangChain Foundation 总索引，了解完整学习路径。
