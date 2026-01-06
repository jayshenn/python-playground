# Claude Agent SDK 学习文档

> 文档驱动的学习方式 - 通过阅读、理解、实践来掌握 Claude Agent SDK

## 📚 文档索引

本目录用于存放你的学习笔记和文档。建议按照官方文档的结构来组织：

### 推荐的文档结构

```
docs/
├── README.md                   # 本文档
├── 01_基础概念.md              # 快速入门、工具、权限
├── 02_钩子系统.md              # Hooks 详解
├── 03_子代理.md                # Subagents 详解
├── 04_会话管理.md              # Sessions 详解
├── 05_MCP集成.md               # MCP 集成
├── 06_最佳实践.md              # 总结和最佳实践
├── 07_常见问题.md              # FAQ 和故障排查
└── examples/                   # 代码片段和示例
    ├── basic_examples.py
    ├── hooks_examples.py
    └── advanced_examples.py
```

## 📖 学习方法

### 1. 阅读官方文档

先完整阅读一遍官方文档章节，理解核心概念：

- [概览](https://platform.claude.com/docs/zh-CN/agent-sdk/overview) - 了解 SDK 的整体架构
- [快速入门](https://platform.claude.com/docs/zh-CN/agent-sdk/quickstart) - 第一个代理
- [Python API](https://platform.claude.com/docs/zh-CN/agent-sdk/python) - 完整 API 参考

### 2. 记录笔记

在 `docs/` 目录下创建对应的 Markdown 文件，记录：

- **核心概念**：用自己的话解释概念
- **代码示例**：记录有用的代码片段
- **遇到的问题**：记录问题和解决方案
- **最佳实践**：总结经验

### 3. 实践验证

在 `my-agent` 项目或新项目中验证所学：

```bash
# 创建新的实验项目
mkdir -p experiments/test-hooks
cd experiments/test-hooks

# 编写测试代码
# 运行验证
uv run python test.py
```

### 4. 迭代改进

不断回顾和更新文档：

- 发现新的用法 → 补充到笔记
- 遇到问题 → 记录到 FAQ
- 总结经验 → 更新最佳实践

## 📝 文档模板

### 基础概念文档模板

创建 `01_基础概念.md`：

```markdown
# Claude Agent SDK 基础概念

## 1. Agent（代理）

### 概念
[用自己的话解释什么是代理]

### 核心特点
- 特点1
- 特点2

### 代码示例
\`\`\`python
# 基础代理示例
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="你的任务描述",
        options=ClaudeAgentOptions(...)
    ):
        print(message)

asyncio.run(main())
\`\`\`

### 笔记
- 注意事项1
- 注意事项2

## 2. Tools（工具）

### 内置工具列表
| 工具 | 用途 | 示例 |
|------|------|------|
| Read | 读取文件 | ... |
| Write | 创建文件 | ... |

### 工具使用技巧
[记录你发现的技巧]

## 3. Permissions（权限）

### 权限模式对比
...
```

### 专题文档模板

创建 `02_钩子系统.md`：

```markdown
# 钩子系统（Hooks）

## 官方文档
https://platform.claude.com/docs/zh-CN/agent-sdk/hooks

## 概念理解
[用自己的话解释钩子的作用]

## 可用的钩子类型

### PreToolUse
**触发时机**：工具使用前
**用途**：[你的理解]
**示例**：
\`\`\`python
[代码示例]
\`\`\`

### PostToolUse
...

## 实践案例

### 案例1：审计日志
**需求**：记录所有文件修改操作
**实现**：
\`\`\`python
[完整代码]
\`\`\`
**效果**：[运行结果]

### 案例2：...

## 常见问题

### Q: 如何在钩子中访问工具的返回值？
A: [答案]

## 最佳实践
1. ...
2. ...
```

## 🔗 推荐的学习顺序

### Week 1: 基础（官方文档 → 笔记 → 实践）

**Day 1-2: 快速入门**
- 阅读：[快速入门文档](https://platform.claude.com/docs/zh-CN/agent-sdk/quickstart)
- 实践：运行 `my-agent` 项目
- 笔记：创建 `01_基础概念.md`

**Day 3-4: 内置工具**
- 阅读：[概览 - 功能部分](https://platform.claude.com/docs/zh-CN/agent-sdk/overview#功能)
- 实践：尝试不同的工具组合
- 笔记：补充工具使用示例

**Day 5-7: 权限和安全**
- 阅读：[权限文档](https://platform.claude.com/docs/zh-CN/agent-sdk/permissions)
- 实践：测试不同权限模式
- 笔记：总结权限最佳实践

### Week 2: 高级特性

**Day 8-10: 钩子系统**
- 阅读：[钩子文档](https://platform.claude.com/docs/zh-CN/agent-sdk/hooks)
- 实践：实现审计日志、自定义验证
- 笔记：创建 `02_钩子系统.md`

**Day 11-14: 子代理和会话**
- 阅读：[子代理文档](https://platform.claude.com/docs/zh-CN/agent-sdk/subagents) 和 [会话文档](https://platform.claude.com/docs/zh-CN/agent-sdk/sessions)
- 实践：构建多代理系统
- 笔记：创建 `03_子代理.md` 和 `04_会话管理.md`

### Week 3: 集成和项目

**Day 15-17: MCP 集成**
- 阅读：[MCP 文档](https://platform.claude.com/docs/zh-CN/agent-sdk/mcp)
- 实践：集成一个 MCP 服务器
- 笔记：创建 `05_MCP集成.md`

**Day 18-21: 综合项目**
- 扩展 `my-agent` 或创建新项目
- 应用所学的所有技术
- 笔记：总结最佳实践和经验

## 💡 学习技巧

### 主动学习
- ✅ 不要只是复制代码，理解每一行的作用
- ✅ 尝试修改参数，观察效果变化
- ✅ 思考：为什么这样设计？有什么替代方案？

### 记录清晰
- ✅ 用自己的话解释概念
- ✅ 记录代码为什么这样写，而不只是怎么写
- ✅ 截图保存有用的错误信息和解决方案

### 实践为主
- ✅ 每学一个概念，立即写代码验证
- ✅ 从简单示例开始，逐步增加复杂度
- ✅ 失败的实验也要记录，避免重复踩坑

### 定期回顾
- ✅ 每周回顾笔记，更新理解
- ✅ 重构之前的代码，应用新学的技术
- ✅ 总结一周的收获和疑问

## 📚 参考资源

### 官方资源
- [官方文档](https://platform.claude.com/docs/zh-CN/agent-sdk/overview)
- [Python SDK GitHub](https://github.com/anthropics/claude-agent-sdk-python)
- [官方示例](https://github.com/anthropics/claude-agent-sdk-demos)

### 社区资源
- [MCP 服务器列表](https://github.com/modelcontextprotocol/servers)
- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code/setup)

### 相关技术
- [Python asyncio 文档](https://docs.python.org/3/library/asyncio.html)
- [Pydantic 文档](https://docs.pydantic.dev/)

## 🎯 学习目标检查

完成学习后，你应该能够：

- [ ] 独立创建和配置代理
- [ ] 熟练使用所有内置工具
- [ ] 理解和应用权限控制
- [ ] 使用钩子实现自定义逻辑
- [ ] 创建和管理子代理
- [ ] 实现多轮对话和上下文保持
- [ ] 集成 MCP 服务器
- [ ] 构建完整的生产级应用

开始你的学习之旅吧！记住：**文档在手，探索无忧**。
