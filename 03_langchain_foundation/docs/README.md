# LangChain Foundation 学习文档

## 项目简介

本项目是 **LangChain Foundation** 的完整学习指南，涵盖了构建生产级 LLM 应用所需的全部核心技术栈。文档基于 LangChain 官方资料编写，使用简体中文，适合中文学习者系统学习。

### 技术栈概览

LangChain Foundation 包含四个核心组件，它们相互配合，形成完整的 LLM 应用开发生态：

```
┌─────────────────────────────────────────────────────────────┐
│                    LangChain Foundation                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  LangChain   │  │  LangGraph   │  │ Deep Agents  │      │
│  │              │  │              │  │              │      │
│  │  高级框架     │  │  低级编排     │  │  复杂任务     │      │
│  │  快速开发     │  │  精确控制     │  │  规划分解     │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                 │               │
│         └─────────────────┼─────────────────┘               │
│                           │                                 │
│                  ┌────────▼────────┐                        │
│                  │   LangSmith     │                        │
│                  │                 │                        │
│                  │  可观测性       │                        │
│                  │  评估与部署     │                        │
│                  └─────────────────┘                        │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 学习模块

### [模块 1: LangChain (Python)](./01_langchain/)

**定位**：高级框架，快速构建 LLM 应用

LangChain 是一个开源框架，提供预构建的代理架构和与任何模型或工具的集成能力。它是入门 LLM 应用开发的最佳起点。

**学习内容**：
- [核心组件](./01_langchain/01_核心组件.md) - Agents、Models、Tools、Messages、Memory、Streaming、Structured Output
- [高级特性](./01_langchain/02_高级特性.md) - Middleware、Multi-agent、Context Engineering、Human-in-the-Loop、Guardrails、Runtime

**核心优势**：
- 快速开发：不到 10 行代码即可连接模型和工具
- 统一接口：支持所有主流 LLM 提供商
- 生产就绪：内置中间件、护栏、人在环中等特性

**适用场景**：简单到中等复杂度的代理、聊天机器人、RAG 应用

---

### [模块 2: LangGraph (Python)](./02_langgraph/)

**定位**：低级编排框架，精确控制复杂工作流

LangGraph 提供比 LangChain 更底层的控制能力，使用图（Graph）来表示和管理复杂的有状态工作流。

**学习内容**：
- [基础](./02_langgraph/01_基础.md) - Graph API、Functional API、State Management、API 选择指南
- [高级特性](./02_langgraph/02_高级特性.md) - Persistence、Interrupts、Memory、Durable Execution、Streaming

**核心优势**：
- 精确控制：完全控制每个执行步骤
- 状态管理：内置持久化和恢复能力
- 双 API 设计：声明式和命令式两种编程范式
- 可视化：原生支持工作流可视化

**适用场景**：复杂对话系统、审批工作流、多代理协作、长时间运行任务

---

### [模块 3: Deep Agents (Python)](./03_deepagents/)

**定位**：处理复杂多步骤任务的高级代理系统

Deep Agents 构建在 LangGraph 之上，专门为处理需要规划、分解和长期记忆的复杂任务而设计。

**学习内容**：
- [基础](./03_deepagents/01_基础.md) - Overview、四大核心能力、快速开始、自定义配置、核心功能详解
- [高级特性](./03_deepagents/02_高级特性.md) - Backends、Subagents、Long-term Memory、Human-in-the-Loop

**核心优势**：
- 任务分解：内置 `write_todos` 工具自动规划
- 子代理委派：专业化处理和上下文隔离
- 文件系统：防止上下文窗口溢出
- 长期记忆：跨会话持久化用户偏好

**适用场景**：研究助手、代码分析工具、数据分析代理、内容创作工具

---

### [模块 4: LangSmith](./04_langsmith/)

**定位**：可观测性、评估和部署平台

LangSmith 是 LangChain 团队开发的生产级平台，提供从开发到部署的完整工具链。

**学习内容**：
- [可观测性与评估](./04_langsmith/01_可观测性与评估.md) - Observability、Tracing、Evaluation、Dataset、Experiment
- [部署](./04_langsmith/02_部署.md) - Cloud Deployment、配置管理、生产环境最佳实践

**核心优势**：
- LLM 原生可观测性：深入了解应用执行细节
- 智能评估框架：离线和在线评估
- 托管部署服务：自动化 CI/CD 和扩展
- AI 助手 Polly：智能分析和洞察

**适用场景**：所有 LLM 应用的开发调试、质量保证、性能优化、生产部署

## 学习路径建议

### 🚀 快速入门路径（3-5 天）

**目标**：快速上手，能够构建简单的 LLM 应用

1. **Day 1-2: LangChain 核心组件**
   - 阅读 LangChain 核心组件文档
   - 运行 Agents、Models、Tools 示例
   - 构建一个简单的聊天机器人

2. **Day 3: LangSmith 可观测性**
   - 配置 LangSmith API Key
   - 为聊天机器人添加追踪
   - 浏览 LangSmith Web UI

3. **Day 4-5: 实践项目**
   - 构建一个完整的简单应用（如 FAQ 机器人）
   - 添加工具调用和流式输出
   - 使用 LangSmith 监控和调试

**适合人群**：LLM 应用开发新手、需要快速原型的开发者

---

### 📈 进阶开发路径（2-3 周）

**目标**：掌握高级特性，能够构建生产级应用

**Week 1: 深入 LangChain 和 LangGraph**
- LangChain 高级特性（Middleware、Multi-agent、HITL）
- LangGraph 基础（Graph API、Functional API）
- LangGraph 高级特性（Persistence、Interrupts）

**Week 2: Deep Agents 和复杂任务**
- Deep Agents 基础（规划、子代理、文件系统）
- Deep Agents 高级特性（Backends、长期记忆）
- 实现一个复杂的多步骤任务代理

**Week 3: 评估和部署**
- LangSmith 评估框架（Dataset、Evaluator）
- LangSmith 部署（langgraph.json、环境配置）
- 部署应用到开发环境

**适合人群**：有一定开发经验、需要构建生产应用的开发者

---

### 🏆 生产专家路径（4-6 周）

**目标**：精通整个技术栈，能够设计和部署大规模 LLM 应用

**Week 1-2: 全面掌握核心技术**
- 完成所有模块的学习
- 深入理解每个组件的设计原理
- 阅读官方文档和源代码

**Week 3-4: 架构设计和最佳实践**
- 多代理系统架构设计
- 上下文工程和性能优化
- 安全和合规性（Guardrails）
- 成本优化策略

**Week 5: 评估和质量保证**
- 设计完整的评估流程
- 实现自定义评估器
- 在线反馈和 A/B 测试
- 持续优化策略

**Week 6: 生产部署**
- 配置生产环境（PostgreSQL、Redis）
- 实现蓝绿部署或金丝雀发布
- 监控和告警配置
- 故障恢复和降级策略

**适合人群**：架构师、技术负责人、需要构建大规模应用的团队

---

### 🎯 场景驱动路径

根据具体应用场景选择学习重点：

#### 聊天机器人 / 客服系统
- 重点：LangChain（Messages、Memory、Streaming）+ LangSmith（Tracing、Feedback）
- 次要：LangGraph（Interrupts for HITL）
- 学习时间：1-2 周

#### 复杂研究助手 / 分析工具
- 重点：Deep Agents（全部）+ LangGraph（Persistence、Memory）
- 次要：LangChain（Multi-agent）
- 学习时间：3-4 周

#### RAG 应用 / 知识库问答
- 重点：LangChain（Tools、Context Engineering）+ LangSmith（Evaluation）
- 次要：LangGraph（State Management）
- 学习时间：2-3 周

#### 审批工作流 / 业务流程自动化
- 重点：LangGraph（全部）+ LangChain（Middleware、HITL）
- 次要：Deep Agents（Subagents）
- 学习时间：2-3 周

## 环境配置

### 前置要求

- Python 3.9+
- pip 或 uv（推荐）
- Git

### 安装依赖

本项目使用 `uv` 进行包管理。从项目根目录运行：

```bash
# 安装所有依赖
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### API Keys 配置

需要配置以下 API Keys：

```bash
# 进入 langchain foundation 目录
cd 03_langchain_foundation

# 复制环境变量示例文件
cp example.env .env

# 编辑 .env 文件，添加你的 API 密钥
```

**必需的 API Keys**：
- `OPENAI_API_KEY` - OpenAI API 访问（或其他 LLM 提供商）
- `TAVILY_API_KEY` - Tavily 搜索工具（用于网络搜索）
- `LANGSMITH_API_KEY` - LangSmith 平台访问

**可选的 API Keys**：
- `ANTHROPIC_API_KEY` - Anthropic Claude 模型
- `GOOGLE_API_KEY` - Google Gemini 模型
- `LANGSMITH_PROJECT` - LangSmith 项目名称（默认：default）

### 验证环境配置

```bash
# 运行环境验证脚本
uv run python utils/env_utils.py
```

### LangSmith 配置

使用 LangSmith 需要额外配置：

```bash
# 启用 LangSmith 追踪
export LANGSMITH_TRACING=true

# 设置 API 端点（默认：美国区域）
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"

# 设置 API Key
export LANGSMITH_API_KEY="ls_..."

# 设置项目名称
export LANGSMITH_PROJECT="my-project"
```

**获取 LangSmith API Key**：
1. 访问 https://smith.langchain.com
2. 登录或注册账户
3. 进入 Settings → API Keys
4. 创建新的 API Key

## 技术栈对比

### 何时使用哪个组件？

| 场景 | 推荐组件 | 理由 |
|-----|---------|------|
| 快速原型开发 | **LangChain** | 高级抽象，快速上手 |
| 简单聊天机器人 | **LangChain** | 预构建的对话模式 |
| 复杂工作流 | **LangGraph** | 精确控制执行流程 |
| 需要人工审批 | **LangGraph** + HITL | 内置中断机制 |
| 多步骤研究任务 | **Deep Agents** | 自动规划和分解 |
| 需要长期记忆 | **Deep Agents** + Store | 跨会话持久化 |
| 大量文件操作 | **Deep Agents** | 文件系统管理 |
| 开发调试 | **LangSmith** | 全面追踪和分析 |
| 质量评估 | **LangSmith** | 评估框架 |
| 生产部署 | **LangSmith** | 托管部署服务 |

### 组件组合使用

实际项目中通常会组合使用多个组件：

**示例 1：智能客服系统**
- LangChain：快速构建对话流程
- LangGraph：实现复杂的多轮对话和工单创建
- LangSmith：监控对话质量和用户满意度

**示例 2：研究助手**
- Deep Agents：处理复杂的多步骤研究任务
- LangGraph：管理研究流程的状态
- LangSmith：评估研究结果的质量

**示例 3：文档分析工具**
- LangChain：文档解析和向量化
- Deep Agents：文件系统管理和分析流程
- LangSmith：追踪分析性能和准确度

## 核心概念速查

### LangChain
- **Agents**：使用 LLM 决策和工具调用的系统
- **ReAct**：Reasoning + Acting 的代理模式
- **Tools**：代理可以调用的外部函数
- **Middleware**：控制代理执行流程的插件

### LangGraph
- **Graph**：工作流的图形表示
- **State**：在节点间传递的数据
- **Checkpointer**：持久化状态的机制
- **Interrupt**：人在环中的中断点

### Deep Agents
- **write_todos**：任务规划工具
- **task**：生成子代理的工具
- **Backend**：文件存储后端（State、Filesystem、Store、Composite）
- **Harness**：代理执行框架

### LangSmith
- **Trace**：应用执行的层次化记录
- **Run**：单个操作单元
- **Dataset**：用于评估的示例集合
- **Evaluator**：评估质量的函数或模型
- **Deployment**：应用的运行实例

## 常见问题

### Q: 应该从哪个模块开始学习？

**A:** 推荐按顺序学习：LangChain → LangGraph → Deep Agents → LangSmith

- **LangChain** 提供基础概念和快速上手体验
- **LangGraph** 建立在 LangChain 之上，提供更精确的控制
- **Deep Agents** 建立在 LangGraph 之上，专注于复杂任务
- **LangSmith** 贯穿始终，用于监控和部署

### Q: 需要学习所有模块吗？

**A:** 取决于你的需求：

- **最小化路径**：LangChain + LangSmith（适合简单应用）
- **推荐路径**：全部学习（适合生产应用）
- **场景驱动**：根据具体场景选择重点模块

### Q: LangChain 和 LangGraph 有什么区别？

**A:**
- **LangChain**：高级框架，快速开发，预构建模式
- **LangGraph**：低级编排，精确控制，自定义工作流
- LangChain 构建在 LangGraph 之上

### Q: Deep Agents 和普通 Agents 有什么区别？

**A:**
- **普通 Agents**：适合简单、单步骤任务
- **Deep Agents**：专门处理需要规划、分解、长期记忆的复杂任务

### Q: 必须使用 LangSmith 吗？

**A:** 不是必须，但强烈推荐：

- **开发阶段**：免费层足够用于调试和追踪
- **生产环境**：部署和监控功能非常有价值
- **替代方案**：可以使用其他 observability 工具，但集成度不如 LangSmith

### Q: 如何选择 LangGraph 的 API？

**A:**
- **Graph API**：适合复杂工作流、需要可视化的场景
- **Functional API**：适合简单流程、熟悉传统编程的开发者
- 两者可以混合使用

### Q: 部署到生产环境需要注意什么？

**A:** 关键要点：

1. **安全**：环境变量管理、输入验证、速率限制
2. **性能**：使用无状态运行、配置超时和重试
3. **监控**：LangSmith 追踪、日志、告警
4. **成本**：Token 使用量跟踪、缓存策略
5. **可靠性**：健康检查、优雅降级、故障恢复

详见 [LangSmith 部署文档](./04_langsmith/02_部署.md)

## 相关资源

### 官方文档

- [LangChain 官方文档](https://docs.langchain.com/)
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [Deep Agents 文档](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangSmith 平台](https://smith.langchain.com/)

### GitHub 仓库

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Deep Agents](https://github.com/langchain-ai/deepagents)
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk)

### 学习资源

- [LangChain 官方博客](https://blog.langchain.com/)
- [LangGraph 教程](https://langchain-ai.github.io/langgraph/tutorials/)
- [Deep Agents 博客](https://blog.langchain.com/deep-agents/)
- [LangSmith 文档](https://docs.smith.langchain.com/)

### 社区

- [LangChain Discord](https://discord.gg/langchain)
- [GitHub Discussions](https://github.com/langchain-ai/langchain/discussions)
- [Twitter/X @LangChainAI](https://twitter.com/LangChainAI)

## 项目结构

```
03_langchain_foundation/
├── docs/                          # 学习文档（本目录）
│   ├── README.md                  # 总索引（本文件）
│   ├── 01_langchain/              # LangChain 模块
│   │   ├── README.md              # 模块索引
│   │   ├── 01_核心组件.md          # 核心组件文档
│   │   └── 02_高级特性.md          # 高级特性文档
│   ├── 02_langgraph/              # LangGraph 模块
│   │   ├── README.md              # 模块索引
│   │   ├── 01_基础.md              # 基础文档
│   │   └── 02_高级特性.md          # 高级特性文档
│   ├── 03_deepagents/             # Deep Agents 模块
│   │   ├── README.md              # 模块索引
│   │   ├── 01_基础.md              # 基础文档
│   │   └── 02_高级特性.md          # 高级特性文档
│   └── 04_langsmith/              # LangSmith 模块
│       ├── README.md              # 模块索引
│       ├── 01_可观测性与评估.md     # 可观测性与评估文档
│       └── 02_部署.md              # 部署文档
├── utils/                         # 工具函数
│   └── env_utils.py               # 环境配置工具
├── tests/                         # 测试代码
├── example.env                    # 环境变量示例
└── README.md                      # 项目说明

```

## 贡献指南

本项目是个人学习项目，欢迎：

- 报告文档中的错误或不准确之处
- 建议改进文档结构或内容
- 分享你的学习心得和实践经验

## 许可证

本项目遵循 MIT 许可证。

## 致谢

本学习文档基于 LangChain 官方文档和 [langchain-ai/lca-lc-foundations](https://github.com/langchain-ai/lca-lc-foundations) 项目整理而成，感谢 LangChain 团队的优秀工作。

---

**开始学习之旅** 👉 选择一个模块开始：
- [模块 1: LangChain](./01_langchain/) - 快速入门
- [模块 2: LangGraph](./02_langgraph/) - 精确控制
- [模块 3: Deep Agents](./03_deepagents/) - 复杂任务
- [模块 4: LangSmith](./04_langsmith/) - 可观测性和部署

祝学习愉快！🚀
