# Claude Agent SDK - my-agent

基于 Claude Agent SDK 的学习实践项目。采用**文档驱动学习**的方式，通过阅读文档并在此项目中实验和探索。

## 📋 快速开始

### 1. 配置认证信息

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，配置以下之一：
```

**方式 1: 使用官方 Anthropic API（推荐）**
```bash
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```
从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥。

**方式 2: 使用自定义 API 代理或网关**
```bash
ANTHROPIC_BASE_URL=https://your-api-gateway.com/api
ANTHROPIC_AUTH_TOKEN=your-auth-token-here
```
如果你使用第三方 API 服务或企业内部的 API 网关。

### 2. 运行第一个示例

```bash
# 从项目根目录运行 Hello World 示例
uv run python 05_claude_agent_sdk/my-agent/hello.py
```

## 📁 文件说明

当前项目包含：

- `hello.py` - 最简单的 Hello World 示例（已实现）
- `.env.example` - 环境变量模板
- `.env` - 实际的环境变量文件（不提交到 Git）
- `.gitignore` - Git 忽略配置
- `__init__.py` - Python 包初始化文件

## 🔧 当前示例：hello.py

这是一个最简单的 Claude Agent SDK 示例，展示基础用法：

```python
import asyncio
from claude_agent_sdk import query

async def main():
    """向 Claude 问好"""
    async for message in query(prompt="你好"):
        print(message)

asyncio.run(main())
```

### 运行效果

程序会：
1. 加载 `.env` 中的 API 认证信息
2. 向 Claude 发送问候
3. 流式输出 Claude 的回复

## 📖 学习方式：文档驱动

本项目采用**文档驱动学习**的方式，不会预先提供大量示例代码。推荐的学习流程：

### 第一步：阅读文档

完整阅读 `../docs/` 目录中的学习文档：

1. **[01_Agent SDK 概览.md](../docs/01_Agent%20SDK%20概览.md)** - 了解 SDK 的整体架构和能力
2. **[02_快速开始.md](../docs/02_快速开始.md)** - 理解基础概念和快速入门
3. **[03_Agent SDK 参考 - Python.md](../docs/03_Agent%20SDK%20参考%20-%20Python.md)** - 完整的 Python API 参考

或访问 [官方在线文档](https://platform.claude.com/docs/zh-CN/agent-sdk/overview)

### 第二步：在此项目中实验

在理解文档后，在此项目中创建你的实验代码：

```bash
# 创建新的实验文件
# 例如：experiment_tools.py, test_hooks.py, my_agent.py 等
```

### 第三步：记录学习笔记

推荐在 `../docs/` 目录下记录你的学习笔记和总结。

## 🚀 下一步学习

完成 Hello World 后，建议按以下顺序学习：

1. **内置工具** - 尝试 Read、Write、Edit、Bash、Grep、Glob 等工具
2. **权限控制** - 理解 `bypassPermissions`、`acceptEdits`、`interactive` 模式
3. **钩子系统** - 实现审计日志、自定义验证等功能
4. **子代理** - 创建专门的代理处理特定任务
5. **会话管理** - 实现多轮对话和上下文保持
6. **MCP 集成** - 连接外部系统和工具

每个主题都可以在此项目中创建对应的实验文件进行实践。

## 🔒 安全注意事项

- ⚠️  **永远不要将 `.env` 文件提交到 Git**
- ✅ 已在 `.gitignore` 中排除 `.env` 文件
- ✅ 使用 `.env.example` 作为模板
- ✅ 审慎使用 `bypassPermissions` 模式（仅在安全环境中）

## 📚 参考资源

- **项目文档**：[../docs/README.md](../docs/README.md) - 完整的学习文档索引
- **主项目说明**：[../../README.md](../../README.md) - Python Playground 项目总览
- **官方文档**：https://platform.claude.com/docs/zh-CN/agent-sdk/overview
- **Python SDK**：https://github.com/anthropics/claude-agent-sdk-python
- **官方示例**：https://github.com/anthropics/claude-agent-sdk-demos
