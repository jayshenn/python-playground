# 🔗 LangChain Foundation 学习项目

## 项目简介

欢迎来到 LangChain Foundation 学习项目！本项目基于 LangChain Academy 的官方课程，提供了完整的中文学习文档和代码示例，帮助你系统掌握 LangChain 生态系统的核心技术。

### 项目特色

- **完整的中文文档** - 系统化的学习文档，覆盖 LangChain、LangGraph、Deep Agents 和 LangSmith
- **实战代码示例** - 100+ 个可运行的 Python 代码示例
- **三个学习模块** - 从基础到生产级的完整学习路径
- **生产就绪** - 包含部署、监控、评估等生产环境最佳实践

---

## 🚀 环境配置

### 前置要求

- 推荐使用 Chrome 浏览器
- Python 版本：>=3.12, <3.14 [查看更多](#python-虚拟环境)
- 包管理器：[uv](https://docs.astral.sh/uv/)（推荐）或 [pip](https://pypi.org/project/pip/)
  - 注意：模块 2 课程 1 中需要使用 `uv` 来运行 MCP 服务器（通过 `uvx` 命令）

### 安装步骤

**1. 克隆代码仓库**

```bash
# 如果你是从 LangChain Academy 官方仓库开始
git clone https://github.com/langchain-ai/lca-lc-foundations.git
cd lca-lc-foundations

# 或者直接在本项目目录中
cd 03_langchain_foundation
```

**2. 配置环境变量**

```bash
# 复制环境变量示例文件
cp example.env .env
```

编辑 `.env` 文件，添加你的 API 密钥：[查看更多](#模型提供商)

```bash
# 必需：用于模型调用
OPENAI_API_KEY='your_openai_api_key_here'
TAVILY_API_KEY='your_tavily_api_key_here'

# 可选：仅在课程 1 中使用一次
ANTHROPIC_API_KEY='your_anthropic_api_key_here'
GOOGLE_API_KEY='your_google_api_key_here'

# 可选：用于评估和追踪
LANGSMITH_API_KEY='your_langsmith_api_key_here'
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=lca-lc-foundation
# 如果你使用欧盟实例，取消下面这行的注释：
#LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
```

**3. 安装依赖**

创建虚拟环境并安装依赖包：[查看更多](#python-虚拟环境)

<details open>
<summary>使用 uv（推荐）</summary>

```bash
uv sync
```

</details>

<details>
<summary>使用 pip</summary>

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 系统：.venv\Scripts\activate
pip install -r requirements.txt
```

</details>

### 快速验证

完成上述配置后，运行以下命令验证环境是否正确：

<details open>
<summary>使用 uv</summary>

```bash
uv run python utils/env_utils.py
```

</details>

<details>
<summary>使用 pip</summary>

```bash
source .venv/bin/activate  # Windows 系统：.venv\Scripts\activate
python utils/env_utils.py
```

</details>

### 运行 Jupyter Notebook

[查看更多信息](#开发环境)

<details open>
<summary>使用 uv（推荐）</summary>

```bash
uv run jupyter lab
```

</details>

<details>
<summary>使用 pip</summary>

```bash
source .venv/bin/activate  # Windows 系统：.venv\Scripts\activate
jupyter lab
```

</details>

---

## 📚 学习内容

本项目包含三个模块，涵盖 LangChain 最常用的功能特性。

### 模块 1: 创建代理（Create Agent）

**学习目标**：掌握构建基础 AI 代理的核心技能

- 基础模型（Foundational Models）
- 工具调用（Tools）
- 短期记忆（Short-Term Memory）
- 多模态消息（Multimodal Messages）
- **实战项目**：个人厨师助手（Personal Chef）

**推荐学习时间**：3-5 天

---

### 模块 2: 高级代理（Advanced Agent）

**学习目标**：构建具有复杂功能的高级代理系统

- 模型上下文协议（Model Context Protocol - MCP）
- 上下文和状态管理（Context and State）
- 多代理系统（Multi-Agent Systems）
- **实战项目**：婚礼策划助手（Wedding Planner）

**推荐学习时间**：1-2 周

---

### 模块 3: 生产就绪代理（Production-Ready Agent）

**学习目标**：掌握部署生产级代理所需的所有技能

- 中间件系统（Middleware）
- 长对话管理（Managing Long Conversations）
- 人在环中机制（Human In The Loop - HITL）
- 动态代理（Dynamic Agents）
- **实战项目**：邮件助手（Email Assistant）
- **额外内容**：代理聊天界面（Agent Chat UI）

**推荐学习时间**：2-3 周

---

## 📖 学习文档

本项目提供了完整的中文学习文档，位于 `docs/` 目录：

### [📘 完整学习指南](./docs/README.md)

总索引文档，包含：
- LangChain Foundation 技术栈概览
- 四种学习路径建议（快速入门、进阶开发、生产专家、场景驱动）
- 环境配置详细说明
- 技术栈对比和选择指南
- 常见问题解答

### 四大核心模块文档

1. **[LangChain (Python)](./docs/01_langchain/)** - 高级框架，快速构建 LLM 应用
   - [核心组件](./docs/01_langchain/01_核心组件.md) - Agents、Models、Tools、Messages、Memory、Streaming
   - [高级特性](./docs/01_langchain/02_高级特性.md) - Middleware、Multi-agent、Context Engineering、HITL、Guardrails

2. **[LangGraph (Python)](./docs/02_langgraph/)** - 低级编排框架，精确控制复杂工作流
   - [基础](./docs/02_langgraph/01_基础.md) - Graph API、Functional API、State Management
   - [高级特性](./docs/02_langgraph/02_高级特性.md) - Persistence、Interrupts、Memory、Durable Execution、Streaming

3. **[Deep Agents (Python)](./docs/03_deepagents/)** - 处理复杂多步骤任务的高级代理系统
   - [基础](./docs/03_deepagents/01_基础.md) - 四大核心能力、快速开始、自定义配置
   - [高级特性](./docs/03_deepagents/02_高级特性.md) - Backends、Subagents、Long-term Memory、HITL

4. **[LangSmith](./docs/04_langsmith/)** - 可观测性、评估和部署平台
   - [可观测性与评估](./docs/04_langsmith/01_可观测性与评估.md) - Observability、Tracing、Evaluation
   - [部署](./docs/04_langsmith/02_部署.md) - Cloud Deployment、配置管理、生产环境最佳实践

---

## 🎯 学习路径建议

### 🚀 快速入门路径（3-5 天）

**适合人群**：LLM 应用开发新手、需要快速原型的开发者

1. **Day 1-2**: 学习 LangChain 核心组件 + 模块 1
2. **Day 3**: 配置 LangSmith 并添加追踪
3. **Day 4-5**: 完成个人厨师助手项目

### 📈 进阶开发路径（2-3 周）

**适合人群**：有一定开发经验、需要构建生产应用的开发者

1. **Week 1**: 完成模块 1 和 2，深入学习 LangGraph
2. **Week 2**: 学习 Deep Agents 和高级特性
3. **Week 3**: 完成模块 3，学习部署和评估

### 🏆 生产专家路径（4-6 周）

**适合人群**：架构师、技术负责人、需要构建大规模应用的团队

1. **Week 1-2**: 全面掌握所有模块和文档
2. **Week 3-4**: 架构设计和最佳实践
3. **Week 5**: 评估和质量保证
4. **Week 6**: 生产部署实践

详细学习路径请参见 [完整学习指南](./docs/README.md)

---

## 🔧 相关资源

### Python 虚拟环境

使用虚拟环境管理 Python 版本是最佳实践，这样可以为本课程选择独立于系统 Python 版本的 Python 环境。

<details open>
<summary>使用 uv（推荐）</summary>

`uv` 会根据 `pyproject.toml` 中指定的版本，在 `.venv` 目录中安装兼容的 Python 版本。运行 `uv run` 时会自动使用这个版本。更多信息请参见 [uv 文档](https://docs.astral.sh/uv/)。

</details>

<details>
<summary>使用 pyenv + pip</summary>

如果你使用 pip 而不是 uv，可以使用 pyenv 管理 Python 版本。更多信息请参见 [pyenv](https://github.com/pyenv/pyenv)。

```bash
pyenv install 3.12
pyenv local 3.12
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</details>

### 模型提供商

**OpenAI**

如果你没有 OpenAI API 密钥，可以在[这里](https://openai.com/index/openai-api/)注册。本课程主要使用 gpt-4o-mini，价格非常实惠。

**其他提供商**

你也可以获取 [Anthropic](https://console.anthropic.com) 或 [Google](https://docs.langchain.com/oss/python/integrations/providers/google) 的 API 密钥。这些模型仅在第一课中使用。

本课程使用特定的模型和提供商创建。你可以使用其他提供商，但需要更新 `.env` 文件中的 API 密钥并进行必要的代码更改。LangChain 支持多种聊天模型提供商，请参见[这里](https://docs.langchain.com/oss/python/integrations/providers/all_providers)。

**Tavily 搜索**

Tavily 是一个搜索提供商，以 LLM 友好的方式返回搜索结果。他们有慷慨的免费套餐。[Tavily 官网](https://tavily.com)

### LangSmith 入门

1. 创建 [LangSmith](https://smith.langchain.com/) 账户
2. 创建 LangSmith API 密钥

<img width="600" alt="LangSmith Dashboard" src="https://github.com/user-attachments/assets/e39b8364-c3e3-4c75-a287-d9d4685caad5" />

<img width="600" alt="LangSmith API Keys" src="https://github.com/user-attachments/assets/2e916b2d-e3b0-4c59-a178-c5818604b8fe" />

3. 使用新的 LangSmith API Key 更新你创建的 `.env` 文件

更多 LangSmith 信息请参见[文档](https://docs.langchain.com/langsmith/home)。

### 环境变量

本课程使用 [dotenv](https://pypi.org/project/python-dotenv) 模块从 `.env` 文件读取键值对，并在 Jupyter notebook 中设置到环境中。不需要在系统环境中全局设置。

### 开发环境

本课程使用 [Jupyter](https://jupyter.org/) notebooks。Jupyter 已经安装，可以按上述说明运行。Jupyter notebooks 也可以在 VSCode 或其他 VSCode 变体（如 Windsurf 或 Cursor）中编辑和运行。

---

## 📁 项目结构

```
03_langchain_foundation/
├── README.md                      # 项目说明（本文件）
├── docs/                          # 完整学习文档
│   ├── README.md                  # 学习文档总索引
│   ├── 01_langchain/              # LangChain 模块文档
│   ├── 02_langgraph/              # LangGraph 模块文档
│   ├── 03_deepagents/             # Deep Agents 模块文档
│   └── 04_langsmith/              # LangSmith 模块文档
├── 01_module1/                    # 模块 1: 创建代理（代码和 notebooks）
├── 02_module2/                    # 模块 2: 高级代理（代码和 notebooks）
├── 03_module3/                    # 模块 3: 生产就绪代理（代码和 notebooks）
├── utils/                         # 工具函数
│   └── env_utils.py               # 环境配置验证工具
├── tests/                         # 测试代码
├── example.env                    # 环境变量示例
├── requirements.txt               # pip 依赖列表
└── pyproject.toml                 # uv 项目配置
```

---

## 🌟 推荐学习流程

### 第一步：环境配置（1 小时）
1. 按照上述步骤完成环境安装
2. 运行环境验证脚本
3. 配置所有必需的 API 密钥
4. 浏览 LangSmith 平台

### 第二步：阅读文档（2-3 天）
1. 从 [docs/README.md](./docs/README.md) 开始
2. 根据你的学习路径选择合适的模块
3. 边学习文档边运行代码示例

### 第三步：完成模块（2-6 周）
1. 按顺序完成三个模块的 notebooks
2. 完成每个模块的实战项目
3. 在 LangSmith 中追踪和评估你的代理

### 第四步：进阶学习
1. 阅读 Deep Agents 和 LangSmith 高级文档
2. 学习生产环境部署最佳实践
3. 构建自己的完整项目

---

## 📞 获取帮助

- **官方文档**: [docs.langchain.com](https://docs.langchain.com/)
- **社区论坛**: [GitHub Discussions](https://github.com/langchain-ai/langchain/discussions)
- **Discord**: [LangChain Discord](https://discord.gg/langchain)
- **Twitter**: [@LangChainAI](https://twitter.com/LangChainAI)

---

## 📄 许可证

本项目遵循 MIT 许可证。

---

## 🙏 致谢

本学习项目基于 LangChain Academy 的官方课程 [lca-lc-foundations](https://github.com/langchain-ai/lca-lc-foundations)，感谢 LangChain 团队的优秀工作。

---

**开始你的学习之旅** 👉

1. 📘 [查看完整学习文档](./docs/README.md)
2. 💻 [开始模块 1：创建代理](./01_module1/)
3. 🎓 [访问 LangChain Academy](https://academy.langchain.com/)

祝学习愉快！🚀
