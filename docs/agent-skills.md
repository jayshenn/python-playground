# Agent Skills 学习指南

> 一个简单、开放的格式，用于为 AI Agent 提供新的能力和专业知识。

## 目录

- [概述](#概述)
- [核心概念](#核心概念)
- [工作原理](#工作原理)
- [格式规范](#格式规范)
- [创建技能](#创建技能)
- [集成技能](#集成技能)
- [最佳实践](#最佳实践)
- [参考资源](#参考资源)

## 概述

### 什么是 Agent Skills？

Agent Skills 是一种文件夹格式的指令、脚本和资源集合，AI Agent 可以发现并使用它们来更准确、高效地完成任务。

### 为什么需要 Agent Skills？

虽然 Agent 越来越强大，但它们往往缺少可靠完成实际工作所需的上下文。Skills 通过提供程序性知识和特定于公司、团队、用户的上下文来解决这个问题，Agent 可以按需加载这些内容。

**对于技能作者**：构建一次，跨多个 Agent 产品部署。

**对于兼容的 Agent**：开箱即用地支持用户为 Agent 提供新能力。

**对于团队和企业**：将组织知识捕获为可移植、版本控制的包。

### Agent Skills 能实现什么？

- **领域专业知识**：将专业知识打包成可重用的指令，从法律审查流程到数据分析管道。
- **新能力**：为 Agent 提供新能力（如创建演示文稿、构建 MCP 服务器、分析数据集）。
- **可重复工作流**：将多步骤任务转化为一致且可审计的工作流。
- **互操作性**：在不同的技能兼容 Agent 产品中重用相同的技能。

### 支持的工具

Agent Skills 被主流 AI 开发工具支持：

- **Cursor** - AI 代码编辑器
- **Claude Code** - Anthropic 的代码助手
- **Claude.ai** - Claude 聊天界面
- **GitHub Copilot** - GitHub 的 AI 编程助手
- **VS Code** - Visual Studio Code
- **OpenCode** - 开放代码平台
- **Amp** - AI 代码编辑器
- **Letta** - Agent 平台
- **Goose** - 命令行 Agent
- **OpenAI Codex** - OpenAI 的代码 Agent

## 核心概念

### 基本结构

一个技能就是一个包含 `SKILL.md` 文件的文件夹：

```
my-skill/
├── SKILL.md          # 必需：指令 + 元数据
├── scripts/          # 可选：可执行代码
├── references/       # 可选：文档
└── assets/           # 可选：模板、资源
```

### SKILL.md 文件

每个技能都以一个包含 YAML frontmatter 和 Markdown 指令的 `SKILL.md` 文件开始：

```markdown
---
name: pdf-processing
description: 从 PDF 文件中提取文本和表格，填写表单，合并文档。
---

# PDF 处理

## 何时使用此技能
当用户需要处理 PDF 文件时使用此技能...

## 如何提取文本
1. 使用 pdfplumber 进行文本提取...

## 如何填写表单
...
```

#### 必需的 Frontmatter 字段

- `name`：简短标识符（1-64 字符，小写字母、数字和连字符）
- `description`：何时使用此技能（1-1024 字符）

#### 可选的 Frontmatter 字段

- `license`：许可证名称或引用
- `compatibility`：环境要求（最多 500 字符）
- `metadata`：任意键值对，用于额外的元数据
- `allowed-tools`：预先批准的工具列表（实验性）

## 工作原理

### 渐进式披露 (Progressive Disclosure)

技能使用渐进式披露来高效管理上下文：

1. **发现阶段**：启动时，Agent 只加载每个可用技能的名称和描述，刚好足以知道何时可能相关。

2. **激活阶段**：当任务匹配技能描述时，Agent 将完整的 `SKILL.md` 指令读入上下文。

3. **执行阶段**：Agent 遵循指令，根据需要可选地加载引用的文件或执行捆绑的代码。

这种方法在保持 Agent 快速响应的同时，让它们能够按需访问更多上下文。

### 上下文使用

技能应该分层结构化以高效使用上下文：

1. **元数据**（约 100 tokens）：启动时加载所有技能的 `name` 和 `description` 字段
2. **指令**（建议 < 5000 tokens）：技能激活时加载完整的 `SKILL.md` 主体
3. **资源**（按需）：仅在需要时加载文件（如 `scripts/`、`references/` 或 `assets/` 中的文件）

**建议**：将主 `SKILL.md` 保持在 500 行以下。将详细的参考资料移到单独的文件中。

## 格式规范

### 目录结构

最小的技能目录包含一个 `SKILL.md` 文件：

```
skill-name/
└── SKILL.md          # 必需
```

完整的技能可以包含：

```
skill-name/
├── SKILL.md          # 必需：核心指令和元数据
├── scripts/          # 可选：可执行脚本
│   ├── extract.py
│   └── process.sh
├── references/       # 可选：详细文档
│   ├── REFERENCE.md
│   └── api-docs.md
└── assets/           # 可选：模板和资源
    ├── template.json
    └── diagram.png
```

### name 字段规则

`name` 字段：
- 必须是 1-64 字符
- 只能包含 Unicode 小写字母数字字符和连字符（`a-z` 和 `-`）
- 不能以 `-` 开头或结尾
- 不能包含连续的连字符（`--`）
- 必须与父目录名称匹配

**有效示例**：
```yaml
name: pdf-processing
name: data-analysis
name: code-review
```

**无效示例**：
```yaml
name: PDF-Processing  # 不允许大写
name: -pdf            # 不能以连字符开头
name: pdf--processing # 不允许连续连字符
```

### description 字段规则

`description` 字段：
- 必须是 1-1024 字符
- 应该描述技能的功能和使用时机
- 应该包含帮助 Agent 识别相关任务的特定关键字

**好的示例**：
```yaml
description: 从 PDF 文件中提取文本和表格，填写 PDF 表单，合并多个 PDF。在处理 PDF 文档或用户提到 PDF、表单或文档提取时使用。
```

**差的示例**：
```yaml
description: 帮助处理 PDF。
```

### 可选目录

#### scripts/

包含 Agent 可以运行的可执行代码。脚本应该：
- 自包含或明确记录依赖项
- 包含有用的错误消息
- 优雅地处理边缘情况

支持的语言取决于 Agent 实现。常见选项包括 Python、Bash 和 JavaScript。

#### references/

包含 Agent 在需要时可以读取的额外文档：
- `REFERENCE.md` - 详细的技术参考
- `FORMS.md` - 表单模板或结构化数据格式
- 特定领域的文件（`finance.md`、`legal.md` 等）

保持单个引用文件的重点。Agent 按需加载这些文件，因此较小的文件意味着更少的上下文使用。

#### assets/

包含静态资源：
- 模板（文档模板、配置模板）
- 图像（图表、示例）
- 数据文件（查找表、模式）

### 文件引用

在技能中引用其他文件时，使用从技能根目录开始的相对路径：

```markdown
详情请参阅[参考指南](references/REFERENCE.md)。

运行提取脚本：
scripts/extract.py
```

保持文件引用从 `SKILL.md` 一级深度。避免深度嵌套的引用链。

## 创建技能

### 步骤 1：创建目录结构

```bash
mkdir my-skill
cd my-skill
touch SKILL.md
```

### 步骤 2：编写 SKILL.md

创建 `SKILL.md` 文件，内容如下：

````markdown
---
name: my-skill
description: 简短描述技能的功能和使用场景。
license: MIT
metadata:
  author: your-name
  version: "1.0"
---

# 我的技能

## 何时使用此技能

当用户需要 [具体场景] 时使用此技能。

## 如何使用

### 步骤 1：准备

[详细说明]

### 步骤 2：执行

[详细说明]

### 步骤 3：验证

[详细说明]

## 示例

### 输入示例

```
[示例输入]
```

### 输出示例

```
[示例输出]
```

## 常见问题

### 问题 1

[解决方案]

### 问题 2

[解决方案]

## 注意事项

- [重要提示 1]
- [重要提示 2]
````

### 步骤 3：添加脚本（可选）

```bash
mkdir scripts
```

创建 Python 脚本示例：

```python
# scripts/process.py
#!/usr/bin/env python3
"""
处理数据的示例脚本
"""

import sys
import json

def main():
    if len(sys.argv) < 2:
        print("用法: process.py <input_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # 处理逻辑
        result = process_data(data)
        
        print(json.dumps(result, indent=2))
    
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

def process_data(data):
    # 实现处理逻辑
    return {"status": "success", "data": data}

if __name__ == "__main__":
    main()
```

### 步骤 4：添加参考文档（可选）

```bash
mkdir references
```

创建 `references/REFERENCE.md` 文件，内容如下：

````markdown
# 详细参考

## API 文档

### 函数 1

**描述**：[功能说明]

**参数**：
- `param1` (string): [说明]
- `param2` (number): [说明]

**返回值**：[说明]

**示例**：
```python
result = function1("value", 42)
```

## 配置选项

### 选项 1

[详细说明]

### 选项 2

[详细说明]
````

### 步骤 5：验证技能

使用 [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) 库验证：

```bash
# 安装 skills-ref
pip install skills-ref

# 验证技能
skills-ref validate ./my-skill
```

## 集成技能

### 集成方式

两种主要的集成方式：

1. **基于文件系统的 Agent**：在计算机环境（bash/unix）中操作，是最强大的选项。通过 shell 命令（如 `cat /path/to/my-skill/SKILL.md`）激活技能。

2. **基于工具的 Agent**：在没有专用计算机环境的情况下运行。实现工具允许模型触发技能并访问捆绑的资源。

### 集成步骤

一个兼容技能的 Agent 需要：

1. **发现**：在配置的目录中发现技能
2. **加载元数据**：启动时加载名称和描述
3. **匹配**：将用户任务匹配到相关技能
4. **激活**：通过加载完整指令来激活技能
5. **执行**：根据需要执行脚本并访问资源

### 加载元数据

启动时，仅解析每个 `SKILL.md` 文件的 frontmatter。这保持初始上下文使用量低。

#### 解析 Frontmatter 伪代码

```python
def parse_metadata(skill_path):
    content = read_file(skill_path + "/SKILL.md")
    frontmatter = extract_yaml_frontmatter(content)
    
    return {
        'name': frontmatter['name'],
        'description': frontmatter['description'],
        'path': skill_path
    }
```

#### 注入到上下文

将技能元数据包含在系统提示中，以便模型知道有哪些技能可用。

对于 Claude 模型，推荐格式使用 XML：

```xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>从 PDF 文件中提取文本和表格，填写表单，合并文档。</description>
    <location>/path/to/skills/pdf-processing/SKILL.md</location>
  </skill>
  <skill>
    <name>data-analysis</name>
    <description>分析数据集，生成图表，创建摘要报告。</description>
    <location>/path/to/skills/data-analysis/SKILL.md</location>
  </skill>
</available_skills>
```

### 安全考虑

脚本执行带来安全风险。考虑：

- **沙箱化**：在隔离环境中运行脚本
- **白名单**：仅执行来自受信任技能的脚本
- **确认**：在运行潜在危险操作之前询问用户
- **日志记录**：记录所有脚本执行以进行审计

## 最佳实践

### 1. 保持指令清晰简洁

- 使用简单、直接的语言
- 提供逐步说明
- 包含具体示例

### 2. 优化上下文使用

- 将主 `SKILL.md` 保持在 500 行以下
- 将详细文档移到 `references/`
- 使用清晰的文件引用

### 3. 编写健壮的脚本

- 验证输入
- 提供有用的错误消息
- 记录依赖项
- 优雅地处理边缘情况

### 4. 提供全面的文档

- 解释何时使用技能
- 包含输入/输出示例
- 记录常见问题
- 列出限制和约束

### 5. 版本控制和维护

- 使用语义化版本
- 在 `metadata` 中记录版本
- 保持更新日志
- 测试跨版本兼容性

### 6. 编写好的描述

好的描述应该：
- 清楚说明技能的功能
- 包含相关关键字
- 提到典型用例
- 简明扼要但信息丰富

**示例**：

```yaml
# 好的描述
description: 从 PDF 文件中提取文本和表格，填写 PDF 表单，合并多个 PDF。在处理 PDF 文档或用户提到 PDF、表单或文档提取时使用。

# 差的描述
description: PDF 工具。
```

### 7. 结构化指令

使用清晰的层次结构：

```markdown
# 主标题

## 何时使用

[清楚说明使用场景]

## 前提条件

[列出要求]

## 主要功能

### 功能 1

#### 何时使用
[说明]

#### 如何使用
1. [步骤 1]
2. [步骤 2]

#### 示例
[具体示例]

### 功能 2

...
```

## 实际示例

### 示例 1：简单的文本处理技能

```
text-formatter/
├── SKILL.md
└── scripts/
    └── format.py
```

**SKILL.md** 内容：

````markdown
---
name: text-formatter
description: 格式化和转换文本，包括大小写转换、空白处理和字符计数。
---

# 文本格式化器

## 何时使用此技能

当用户需要格式化或转换文本时使用此技能。

## 功能

### 大小写转换

将文本转换为不同的大小写格式：

```bash
python scripts/format.py uppercase "hello world"
# 输出: HELLO WORLD

python scripts/format.py lowercase "HELLO WORLD"
# 输出: hello world

python scripts/format.py titlecase "hello world"
# 输出: Hello World
```

### 空白处理

```bash
python scripts/format.py trim "  hello world  "
# 输出: hello world
```

### 字符计数

```bash
python scripts/format.py count "hello world"
# 输出: 11 characters (excluding spaces: 10)
```
````

### 示例 2：数据分析技能

```
data-analyzer/
├── SKILL.md
├── scripts/
│   ├── analyze.py
│   └── visualize.py
├── references/
│   ├── REFERENCE.md
│   └── statistics.md
└── assets/
    └── template.json
```

**SKILL.md** 内容：

````markdown
---
name: data-analyzer
description: 分析数据集，计算统计信息，生成可视化图表。支持 CSV、JSON 和 Excel 格式。
license: MIT
metadata:
  author: data-team
  version: "2.1"
---

# 数据分析器

## 何时使用此技能

当用户需要分析数据集或生成统计报告时使用此技能。

## 支持的格式

- CSV (.csv)
- JSON (.json)
- Excel (.xlsx, .xls)

## 快速开始

### 1. 基本统计分析

```bash
python scripts/analyze.py stats data.csv
```

这将生成：
- 均值、中位数、众数
- 标准差和方差
- 最小值和最大值
- 分位数

### 2. 生成可视化

```bash
python scripts/visualize.py histogram data.csv column_name
python scripts/visualize.py scatter data.csv x_column y_column
python scripts/visualize.py boxplot data.csv column_name
```

## 详细说明

详细的 API 文档和高级功能请参阅：
- [完整参考](references/REFERENCE.md)
- [统计方法](references/statistics.md)

## 示例

### 分析销售数据

```bash
# 计算销售统计
python scripts/analyze.py stats sales_data.csv --column revenue

# 生成收入分布直方图
python scripts/visualize.py histogram sales_data.csv revenue --bins 20
```

### 输出示例

```json
{
  "column": "revenue",
  "count": 1000,
  "mean": 45678.90,
  "median": 42000.00,
  "std": 15234.56,
  "min": 10000.00,
  "max": 95000.00,
  "quartiles": {
    "Q1": 35000.00,
    "Q2": 42000.00,
    "Q3": 55000.00
  }
}
```
````

## 参考资源

### 官方资源

- **规范文档**：[https://agentskills.io/specification](https://agentskills.io/specification)
- **GitHub 仓库**：[https://github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)
- **示例技能**：[https://github.com/anthropics/skills](https://github.com/anthropics/skills)
- **参考库**：[https://github.com/agentskills/agentskills/tree/main/skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref)

### 工具和库

- **skills-ref**：验证技能和生成提示 XML 的 Python 库
  ```bash
  pip install skills-ref
  skills-ref validate ./my-skill
  skills-ref to-prompt ./skills/*
  ```

### 最佳实践文档

- **Anthropic 最佳实践**：[https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

### 社区

- **GitHub Discussions**：在 agentskills 仓库中参与讨论
- **示例集合**：浏览社区创建的技能

## 总结

Agent Skills 提供了一个简单但强大的方式来扩展 AI Agent 的能力：

1. **简单格式**：只需要一个带有 YAML frontmatter 的 Markdown 文件
2. **渐进式披露**：高效管理上下文使用
3. **可扩展**：从简单指令到复杂的可执行工作流
4. **可移植**：跨多个 Agent 平台重用
5. **开放标准**：由 Anthropic 发起，社区驱动

通过遵循本指南，你可以创建有效的技能来增强你的 AI Agent，或将技能支持集成到你自己的 Agent 产品中。

---

*最后更新：2025-12-31*
