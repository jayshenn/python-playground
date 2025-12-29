# LangSmith 学习模块

## 模块简介

LangSmith 是 LangChain 团队开发的生产级 LLM 应用开发平台，提供从开发到部署的完整工具链。它是构建、监控和优化 LLM 应用不可或缺的平台。

### 核心优势

- **全生命周期支持**：从原型开发到生产部署的完整工作流
- **LLM 原生可观测性**：深入了解应用执行细节和性能指标
- **智能评估框架**：支持离线和在线评估，持续优化应用质量
- **托管部署服务**：自动化 CI/CD、扩展和监控
- **内置 AI 助手**：Polly 提供智能分析和洞察

## 与其他工具的关系

| 特性 | LangChain/LangGraph | LangSmith |
|-----|---------------------|-----------|
| **主要功能** | 应用开发框架 | 可观测性和部署平台 |
| **开发阶段** | 代码编写和调试 | 监控、评估、部署 |
| **使用方式** | Python/JavaScript 库 | Web 平台 + SDK |
| **典型用途** | 构建代理和工作流 | 追踪、评估、生产部署 |
| **部署支持** | 无 | 完整的托管部署 |
| **监控能力** | 基础日志 | 全面追踪和分析 |

## 学习文档

本模块包含两个主要学习文档：

### 1. [可观测性与评估](./01_可观测性与评估.md)

学习如何监控、调试和评估 LLM 应用：

**第一部分：可观测性（Observability）**：
- **核心概念**：Trace、Run、Project、Metadata
- **环境配置**：API Key 获取和环境变量设置
- **使用方法**：
  - @traceable 装饰器（推荐）
  - LangChain 自动追踪
  - 手动追踪（完全控制）
- **高级功能**：
  - 分布式追踪
  - 自定义 Metadata 和 Tags
  - 过滤和搜索
  - AI 助手 Polly 分析
- **监控和告警**：Dashboard、性能指标、自动化告警

**第二部分：评估（Evaluation）**：
- **核心概念**：Dataset、Evaluator、Experiment、Feedback
- **Dataset 管理**：创建、上传、导出
- **离线评估**：批量测试、多评估器、比较实验
- **在线评估**：实时反馈、用户评分、A/B 测试
- **评估器类型**：LLM-as-Judge、规则基础、嵌入相似度、自定义
- **最佳实践**：评估策略、持续优化、版本管理

**代码示例**：
- 使用 @traceable 装饰器
- LangChain 集成
- 创建和运行实验
- 自定义评估器
- 在线反馈收集

### 2. [部署](./02_部署.md)

学习如何将 LangGraph 应用部署到生产环境：

**核心概念**：
- **Deployment**：部署实例和配置
- **Assistant**：已配置的代理
- **Thread**：会话线程和状态管理
- **Run**：同步、流式、后台运行
- **部署类型**：Cloud、Hybrid、Self-hosted

**使用方法**：
- **应用结构准备**：项目组织、langgraph.json 配置
- **Graph 定义**：状态管理、节点和边
- **本地测试**：LangGraph CLI 工具

**云端部署**：
- 通过 LangSmith UI（图形化界面）
- 通过 API（编程式部署）
- GitHub 集成和自动部署

**部署配置**：
- 环境变量管理（本地和生产）
- 自定义认证
- Dockerfile 自定义
- Monorepo 支持

**代码示例**：
- Python SDK（异步/同步）
- JavaScript/TypeScript SDK
- REST API（cURL 和 requests）
- 不同的 Stream Modes
- 后台运行和 Cron 作业

**生产环境最佳实践**：
- 性能优化（无状态运行、批处理、超时配置）
- 安全最佳实践（密钥管理、输入验证、速率限制）
- 监控和告警（追踪、日志、Dashboard）
- 错误处理（优雅降级、健康检查）
- 成本优化（Token 跟踪、缓存策略）
- 部署策略（蓝绿部署、金丝雀发布）

## 学习路径建议

### 入门路径（1-2 天）
1. 阅读可观测性文档的核心概念部分
2. 配置 LangSmith API Key 和环境
3. 运行简单的追踪示例
4. 了解 Project 和 Trace 的组织方式
5. 浏览 LangSmith Web UI

### 进阶路径（3-5 天）
1. 深入学习 @traceable 装饰器的使用
2. 创建 Dataset 并运行离线评估
3. 掌握不同类型的评估器
4. 配置监控和告警
5. 学习部署文档的基础概念
6. 了解 langgraph.json 配置

### 生产路径（1-2 周）
1. 设计完整的评估流程（离线 + 在线）
2. 实现自定义评估器和反馈收集
3. 准备应用结构和 langgraph.json
4. 配置环境变量和密钥管理
5. 部署到开发环境并测试
6. 配置生产环境的监控和告警
7. 实现蓝绿部署或金丝雀发布
8. 设置性能和成本监控
9. 准备故障恢复和降级策略

## 核心概念速查

### 追踪（Tracing）相关

| 概念 | 说明 |
|------|------|
| `Trace` | 应用执行过程的层次化记录 |
| `Run` | 单个操作单元（chain、llm、tool、retriever、agent） |
| `Project` | Trace 的逻辑分组（dev、test、prod） |
| `Metadata` | 键值对形式的附加信息 |
| `Tags` | 用于分类和过滤的标签 |

### 评估（Evaluation）相关

| 概念 | 说明 |
|------|------|
| `Dataset` | 用于评估的示例集合 |
| `Evaluator` | 评估输出质量的函数或模型 |
| `Experiment` | 在 Dataset 上运行应用的测试 |
| `Feedback` | 评估结果或用户反馈 |

### 部署（Deployment）相关

| 概念 | 说明 |
|------|------|
| `Deployment` | 应用的运行实例 |
| `Assistant` | 在 langgraph.json 中定义的已配置代理 |
| `Thread` | 管理多轮对话状态的会话线程 |
| `Run` | 一次代理执行（同步/流式/后台） |

### 部署类型对比

| 类型 | 控制程度 | 管理复杂度 | 适用场景 |
|------|----------|-----------|----------|
| Cloud | 低 | 低 | 快速开发、中小规模应用 |
| Hybrid | 中 | 中 | 需要数据隐私的场景 |
| Self-hosted | 高 | 高 | 完全控制、大规模定制 |

## 实际应用场景

LangSmith 适合以下应用场景：

1. **开发调试**：追踪复杂代理的执行流程，快速定位问题
2. **质量保证**：离线评估确保新版本不会降低质量
3. **性能优化**：监控延迟和 Token 使用，优化成本和速度
4. **A/B 测试**：对比不同提示词或模型的效果
5. **用户反馈**：收集真实用户反馈，持续改进
6. **生产监控**：实时追踪生产环境的运行状况
7. **自动化部署**：从 GitHub 代码到生产环境的完整 CI/CD
8. **团队协作**：共享 Dataset、评估结果和部署配置

## 最佳实践速查

### 可观测性
- ✅ 为不同环境使用不同的 Project（dev、test、prod）
- ✅ 添加有意义的 Metadata 和 Tags 便于过滤
- ✅ 使用 @traceable 装饰器自动追踪函数
- ❌ 避免在 Metadata 中存储敏感信息

### 评估
- ✅ 创建代表性的 Dataset 覆盖各种场景
- ✅ 使用多个评估器从不同维度评估
- ✅ 定期运行实验对比不同版本
- ✅ 结合离线评估和在线反馈
- ❌ 避免只依赖单一评估指标

### 部署
- ✅ 使用环境变量管理配置和密钥
- ✅ 生产环境使用无状态运行提高性能
- ✅ 配置合理的超时和重试策略
- ✅ 实现健康检查和优雅降级
- ✅ 监控 Token 使用量和成本
- ❌ 避免在代码中硬编码密钥
- ❌ 避免在生产环境频繁使用有状态运行

## 环境配置

### LangSmith 环境变量

在使用 LangSmith 之前，需要配置以下环境变量：

```bash
# 启用 LangSmith 追踪
export LANGSMITH_TRACING=true

# 设置 API 端点（默认：美国区域）
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
# 欧盟区域：
# export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"

# 设置 API Key（从 https://smith.langchain.com 获取）
export LANGSMITH_API_KEY="ls_..."

# 可选：设置项目名称（默认："default"）
export LANGSMITH_PROJECT="my-project"
```

### 获取 API Key

1. 访问 https://smith.langchain.com
2. 登录或注册账户
3. 进入 Settings → API Keys
4. 创建新的 API Key

## 相关资源

- [LangSmith 官方文档](https://docs.smith.langchain.com/)
- [LangSmith 平台](https://smith.langchain.com/)
- [LangSmith SDK (Python)](https://github.com/langchain-ai/langsmith-sdk)
- [LangSmith API 参考](https://docs.smith.langchain.com/api-reference)
- [LangGraph 部署文档](https://langchain-ai.github.io/langgraph/cloud/)

## 下一步

完成 LangSmith 模块后，你已经掌握了 LangChain Foundation 的完整技术栈：

1. ✅ **LangChain** - 快速构建代理应用
2. ✅ **LangGraph** - 低级编排框架，构建复杂工作流
3. ✅ **Deep Agents** - 处理复杂多步骤任务的高级代理系统
4. ✅ **LangSmith** - 可观测性、评估和部署平台

现在你可以：
- 构建生产级的 LLM 应用
- 实现完整的监控和评估流程
- 部署和扩展应用到生产环境
- 持续优化应用质量和性能

返回 LangChain Foundation 总索引，了解完整学习路径。
