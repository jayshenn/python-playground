# Deep Agents (Python) 学习模块

## 模块简介

Deep Agents 是一个专门用于构建能够处理**复杂、多步骤任务**的智能代理库。它构建在 LangGraph 之上，汲取 Claude Code、Deep Research 和 Manus 等应用的精华，为复杂代理系统提供生产级解决方案。

### 核心优势

- **任务分解与规划**：内置 `write_todos` 工具自动分解复杂任务
- **专业化委派**：通过子代理实现任务隔离和专业化处理
- **上下文管理**：文件系统工具防止上下文窗口溢出
- **长期记忆**：跨会话持久化用户偏好和知识库
- **生产就绪**：支持人在环中审批、错误恢复、监控追踪

## 与其他框架的区别

| 特性 | Shallow Agents | Deep Agents |
|------|---------------|-------------|
| **复杂任务处理** | 容易失败 | 设计目标 |
| **任务规划** | 无 | 内置 todos |
| **上下文管理** | 基础 | 文件系统 + 自动驱逐 |
| **子任务委派** | 无 | 子代理机制 |
| **长期记忆** | 有限 | 完整支持 |
| **适用场景** | 简单查询 | 多步骤研究、分析 |

## 学习文档

本模块包含两个主要学习文档：

### 1. [基础](./01_基础.md)

学习 Deep Agents 的核心概念和基本使用：

**概述部分**：
- Deep Agents 的定义和设计理念
- 与 Shallow Agents 的区别
- 与 LangChain/LangGraph 的关系
- 主要优势和适用场景

**四大核心能力**：
- **规划和任务分解**：`write_todos` 工具的使用
- **子代理生成**：`task` 工具实现任务委托
- **文件系统上下文管理**：7 种文件操作工具（ls、read_file、write_file、edit_file、glob、grep、task）
- **长期记忆**：跨会话持久化机制

**快速开始**：
- 完整的安装和环境配置
- 最小化示例（5 行代码即可开始）
- 自动功能说明

**自定义配置**：
- 模型选择（支持任何 LangChain 兼容模型）
- 系统提示词自定义
- 工具配置
- Backend 配置（4 种存储后端）
- 子代理配置
- Human-in-the-Loop 工作流

**核心功能详解**：
- Harness 代理框架（大结果驱逐、对话摘要、提示词缓存）
- Middleware 架构（TodoList、Filesystem、SubAgent）

**代码示例**：
- 基础研究代理
- 带持久化内存的代理
- 带子代理的复杂任务
- Human-in-the-Loop 工作流
- 自定义 Backend（S3 示例）

### 2. [高级特性](./02_高级特性.md)

深入学习构建生产级代理系统的高级功能：

**1. Backends（后端系统）**：
- **StateBackend**：临时存储（默认）
- **FilesystemBackend**：真实文件系统操作
- **StoreBackend**：跨会话持久化
- **CompositeBackend**：混合路由策略（推荐生产环境）
- 后端选择指南和自定义后端实现

**2. Subagents（子代理）**：
- 上下文隔离机制
- 专业化分工策略
- 配置选项详解（name、description、system_prompt、tools、model）
- 使用示例和最佳实践
- 自定义 LangGraph 图作为子代理

**3. Long-term Memory（长期记忆）**：
- 通过 CompositeBackend + StoreBackend 实现
- 路径组织策略（/memories/ 约定）
- 存储后端对比（InMemoryStore、PostgresStore、RedisStore）
- 结构化存储和内存管理

**4. Human-in-the-Loop（人在环中）**：
- 基于 LangGraph 中断机制
- 三种决策类型：approve、edit、reject
- 完整审批工作流
- 子代理中的 HITL
- 分级审批和条件审批

**5. 最佳实践**：
- 后端选择（开发 vs 生产）
- 子代理设计原则
- 长期记忆管理
- HITL 配置建议
- 综合使用示例

## 学习路径建议

### 入门路径（1-2 天）
1. 阅读基础文档的概述和核心概念
2. 运行快速开始示例
3. 了解四大核心能力（规划、子代理、文件系统、长期记忆）
4. 尝试基础研究代理示例

### 进阶路径（3-5 天）
1. 深入学习 Backend 配置
2. 配置和使用子代理
3. 实现长期记忆功能
4. 添加 Human-in-the-Loop 审批
5. 掌握 Harness 和 Middleware 架构

### 生产路径（1-2 周）
1. 设计 CompositeBackend 混合存储策略
2. 实现专业化子代理系统
3. 配置生产级持久化（PostgresStore + PostgresCheckpointer）
4. 实现多级审批流程
5. 集成 LangSmith 监控和追踪
6. 性能优化和错误处理
7. 准备部署到生产环境

## 核心概念速查

### 默认工具（自动提供）

| 工具 | 功能 | 说明 |
|------|------|------|
| `write_todos` | 任务规划 | 分解和跟踪复杂任务 |
| `ls` | 列出文件 | 显示目录内容和元数据 |
| `read_file` | 读取文件 | 支持偏移和限制参数 |
| `write_file` | 创建文件 | 保存数据和结果 |
| `edit_file` | 修改文件 | 精确字符串替换 |
| `glob` | 文件查找 | 基于模式匹配 |
| `grep` | 内容搜索 | 多种输出模式 |
| `task` | 生成子代理 | 委派专门任务 |

### Backend 类型对比

| Backend | 持久化 | 跨会话 | 适用场景 |
|---------|--------|--------|----------|
| StateBackend | ❌ | ❌ | 开发、临时文件 |
| FilesystemBackend | ✅ | ✅ | 项目文件访问 |
| StoreBackend | ✅ | ✅ | 长期记忆、知识库 |
| CompositeBackend | 混合 | 混合 | 生产环境（推荐） |

### 决策类型（HITL）

| 决策 | 效果 |
|------|------|
| approve | 按原参数执行工具 |
| edit | 修改参数后执行 |
| reject | 取消工具调用 |

## 实际应用场景

Deep Agents 特别适合以下场景：

1. **研究助手**：需要多轮搜索、信息整合和报告生成
2. **代码分析工具**：文件扫描、模式识别、重构建议
3. **数据分析代理**：数据加载、统计分析、可视化、报告
4. **客户服务机器人**：跨会话记忆用户偏好，专业化处理不同问题
5. **内容创作工具**：研究、大纲、撰写、审阅的多阶段流程
6. **自动化运维**：需要人工审批的敏感操作

## 最佳实践速查

### 任务规划
- ✅ 在系统提示词中强调使用 `write_todos`
- ✅ 对多步骤任务要求先规划再执行
- ❌ 避免跳过规划阶段直接执行

### 上下文管理
- ✅ 将大量数据保存到文件
- ✅ 使用描述性文件名
- ❌ 避免在消息中包含大量原始数据

### 子代理使用
- ✅ 单一职责，清晰描述
- ✅ 最小化工具集
- ❌ 避免为简单任务创建子代理

### 内存管理
- ✅ 使用 CompositeBackend 分离临时和持久化
- ✅ 将用户偏好保存在 `/memories/`
- ❌ 避免将所有内容都持久化

### HITL 配置
- ✅ 为高风险操作启用审批
- ✅ 提供清晰的审批上下文
- ❌ 避免为低风险操作启用 HITL

## 相关资源

- [Deep Agents 官方文档](https://docs.langchain.com/oss/python/deepagents/overview)
- [Deep Agents GitHub](https://github.com/langchain-ai/deepagents)
- [Deep Agents 博客](https://blog.langchain.com/deep-agents/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangSmith 平台](https://www.langchain.com/langsmith)

## 下一步

完成 Deep Agents 模块后，建议继续学习：
- **LangSmith** - 部署、监控和评估工具

返回 LangChain Foundation 总索引，了解完整学习路径。
