# Claude Agent SDK 学习模块

> 使用 Claude Code 作为库构建生产级 AI 代理

## 📚 概述

本模块是学习 Claude Agent SDK 的文档和实践项目。采用**文档驱动学习**的方式，通过阅读官方文档并在实际项目中探索和实验。

**官方文档：** https://platform.claude.com/docs/zh-CN/agent-sdk/overview

## ✨ 核心功能

Claude Agent SDK 提供了与 Claude Code 相同的工具、代理循环和上下文管理：

- **内置工具**：Read、Write、Edit、Bash、Glob、Grep、WebSearch、WebFetch
- **钩子系统**：在代理生命周期关键点运行自定义代码
- **子代理**：生成专门的代理处理专注的子任务
- **MCP 集成**：通过模型上下文协议连接外部系统
- **权限控制**：精确控制代理可以使用哪些工具
- **会话管理**：在多次交互中保持上下文

## 📁 目录结构

```
05_claude_agent_sdk/
├── my-agent/           # 示例项目：Bug 检测和修复代理
│   ├── agent.py        # 主代理脚本
│   ├── agent_debug.py  # 调试版本
│   ├── utils.py        # 测试代码
│   ├── .env.example    # 环境变量模板
│   └── README.md       # 项目说明
├── docs/               # 学习文档
│   └── README.md       # 文档索引
├── notebooks/          # Jupyter notebooks（可选）
├── tests/              # 测试代码
└── README.md           # 本文档
```

## 🚀 快速开始

### 1. 安装 Claude Code

Claude Agent SDK 使用 Claude Code 作为运行时：

```bash
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash

# 或使用 Homebrew
brew install --cask claude-code

# 或使用 npm
npm install -g @anthropic-ai/claude-code
```

### 2. 安装依赖

```bash
# 项目依赖已在 pyproject.toml 中配置
uv sync
```

### 3. 配置认证

**方式 1: 使用官方 Anthropic API**
```bash
export ANTHROPIC_API_KEY=your-api-key
```

**方式 2: 使用自定义 API 代理**
```bash
export ANTHROPIC_BASE_URL=https://your-api-gateway.com/api
export ANTHROPIC_AUTH_TOKEN=your-auth-token
```

或者在项目中使用 `.env` 文件（推荐）。

### 4. 运行示例项目

```bash
cd 05_claude_agent_sdk/my-agent
uv run python agent_debug.py
```

## 📖 学习路径

### 阶段 1：了解基础概念（1-2 天）

通过官方文档学习核心概念：

1. **快速入门**
   - [官方快速开始](https://platform.claude.com/docs/zh-CN/agent-sdk/quickstart)
   - 理解代理循环、工具、权限等基本概念
   - 运行 `my-agent` 示例项目

2. **内置工具**
   - 文件操作：Read、Write、Edit
   - 系统命令：Bash
   - 搜索工具：Glob、Grep
   - 网络工具：WebSearch、WebFetch

3. **权限控制**
   - `bypassPermissions`：自动批准所有操作
   - `acceptEdits`：自动批准编辑操作
   - `interactive`：需要用户确认（默认）

### 阶段 2：掌握高级特性（3-5 天）

通过文档和实验学习高级功能：

4. **钩子系统**
   - [钩子文档](https://platform.claude.com/docs/zh-CN/agent-sdk/hooks)
   - PreToolUse、PostToolUse
   - SessionStart、SessionEnd
   - 实战：添加审计日志、自定义验证

5. **子代理**
   - [子代理文档](https://platform.claude.com/docs/zh-CN/agent-sdk/subagents)
   - 任务委派和并行处理
   - 自定义代理类型
   - 实战：创建专门的分析代理

6. **会话管理**
   - [会话文档](https://platform.claude.com/docs/zh-CN/agent-sdk/sessions)
   - 上下文保持和多轮对话
   - 会话恢复和分叉
   - 实战：构建对话式代理

7. **MCP 集成**
   - [MCP 文档](https://platform.claude.com/docs/zh-CN/agent-sdk/mcp)
   - 连接外部系统（数据库、浏览器等）
   - 使用社区 MCP 服务器
   - 实战：集成 Playwright 进行浏览器自动化

### 阶段 3：构建生产级应用（1-2 周）

通过项目实践巩固所学：

8. **项目实践**
   - 扩展 `my-agent` 项目
   - 添加新功能和工具
   - 实现错误处理和日志
   - 性能优化

9. **最佳实践**
   - 安全性：API 密钥管理、工具限制
   - 性能：成本控制、响应时间优化
   - 可维护性：代码组织、测试覆盖

## 💡 使用示例

### 基础示例：文件操作

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="读取 README.md 并总结主要内容",
        options=ClaudeAgentOptions(
            allowed_tools=["Read"],
            permission_mode="bypassPermissions"
        )
    ):
        print(message)

asyncio.run(main())
```

### 进阶示例：使用钩子

```python
async def main():
    async for message in query(
        prompt="分析代码质量",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep"],
            permission_mode="bypassPermissions",
            hooks={
                "PostToolUse": [{
                    "matcher": "Read",
                    "hooks": [{
                        "type": "command",
                        "command": "echo 'File read at $(date)' >> audit.log"
                    }]
                }]
            }
        )
    ):
        print(message)
```

## 🔧 认证配置说明

### 方式 1: 官方 Anthropic API

```bash
# 设置环境变量
export ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# 或使用 .env 文件
echo "ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx" > .env
```

### 方式 2: 自定义 API 代理

适用于使用第三方 API 服务或企业内部 API 网关：

```bash
# 设置环境变量
export ANTHROPIC_BASE_URL=https://your-api-gateway.com/api
export ANTHROPIC_AUTH_TOKEN=your-auth-token

# 或使用 .env 文件
cat > .env << EOF
ANTHROPIC_BASE_URL=https://your-api-gateway.com/api
ANTHROPIC_AUTH_TOKEN=your-auth-token
EOF
```

在代码中，SDK 会自动处理这些配置：

```python
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 如果使用自定义端点，需要将 AUTH_TOKEN 设置为 API_KEY
import os
if os.environ.get("ANTHROPIC_BASE_URL"):
    os.environ["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_AUTH_TOKEN"]
```

## 📚 参考资源

### 官方文档

- [概览](https://platform.claude.com/docs/zh-CN/agent-sdk/overview)
- [快速入门](https://platform.claude.com/docs/zh-CN/agent-sdk/quickstart)
- [Python API 参考](https://platform.claude.com/docs/zh-CN/agent-sdk/python)
- [TypeScript API 参考](https://platform.claude.com/docs/zh-CN/agent-sdk/typescript)

### GitHub 仓库

- [Python SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [TypeScript SDK](https://github.com/anthropics/claude-agent-sdk-typescript)
- [示例代理](https://github.com/anthropics/claude-agent-sdk-demos)

### 社区资源

- [MCP 服务器列表](https://github.com/modelcontextprotocol/servers)
- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code/setup)

## 🤝 与其他模块的关系

- **Python 基础** (`01_python_core/`)：需要掌握 async/await
- **LangChain Foundation** (`03_langchain_foundation/`)：互补的 AI 代理框架
- **Pydantic AI** (`04_pydantic_ai/`)：另一个现代 AI 代理框架

### 框架对比

| 特性 | Claude Agent SDK | LangChain | Pydantic AI |
|------|------------------|-----------|-------------|
| 定位 | Claude 原生 SDK | 通用 LLM 框架 | 类型安全框架 |
| 工具执行 | 内置自动化 | 需要实现循环 | 类型驱动 |
| 学习曲线 | 低 | 中 | 低-中 |
| 最佳场景 | Claude 专用任务 | 多 LLM 支持 | 类型安全应用 |

## 🎯 学习目标

完成本模块后，你将能够：

1. ✅ 创建和配置 Claude 代理
2. ✅ 使用内置工具完成各种任务
3. ✅ 实现安全的权限控制
4. ✅ 使用钩子进行审计和验证
5. ✅ 创建和管理子代理
6. ✅ 维护跨多轮对话的上下文
7. ✅ 集成 MCP 服务器扩展功能
8. ✅ 构建生产级 AI 代理应用

## 📝 学习建议

1. **先读文档，再动手**
   - 完整阅读官方文档的相关章节
   - 理解概念和原理
   - 然后在 `my-agent` 或新项目中实验

2. **边学边记录**
   - 在 `docs/` 目录下创建你的学习笔记
   - 记录遇到的问题和解决方案
   - 总结最佳实践

3. **从简单到复杂**
   - 先掌握基本的文件操作和命令执行
   - 再学习钩子、子代理等高级特性
   - 最后构建复杂的生产级应用

4. **多看示例代码**
   - [官方示例仓库](https://github.com/anthropics/claude-agent-sdk-demos)
   - 学习他人的实现方式
   - 理解不同场景的最佳实践

5. **实践项目驱动**
   - 基于 `my-agent` 扩展功能
   - 或创建自己的项目解决实际问题
   - 在实践中深化理解

## 🆚 Agent SDK vs Client SDK

选择 Agent SDK 的场景：

- ✅ 需要文件操作、命令执行等内置工具
- ✅ 希望 Claude 自主决策工具使用
- ✅ 构建自动化工作流
- ✅ 需要子代理和复杂任务委派

选择 Client SDK 的场景：

- ⚠️ 需要完全控制工具执行逻辑
- ⚠️ 自定义代理循环
- ⚠️ 集成到现有的复杂系统

## 📄 许可证

遵循项目根目录的许可证。Claude Agent SDK 的使用受 Anthropic 商业服务条款管制。
