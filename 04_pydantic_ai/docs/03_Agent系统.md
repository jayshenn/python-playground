# Pydantic AI Agent 系统详解

> 本文档深入讲解 Agent 的创建、配置、运行和管理，帮助你充分发挥 Agent 的能力。

## 📋 目录

- [Agent 的创建](#agent-的创建)
- [System Prompt 和 Instructions](#system-prompt-和-instructions)
- [运行方式详解](#运行方式详解)
- [消息历史管理](#消息历史管理)
- [错误处理和重试](#错误处理和重试)
- [元数据和追踪](#元数据和追踪)
- [高级配置](#高级配置)

## 🏗️ Agent 的创建

### 基础创建

```python
from pydantic_ai import Agent

# 最简单的 Agent
agent = Agent('openai:gpt-4')

# 带系统提示的 Agent
agent = Agent(
    'openai:gpt-4',
    system_prompt='你是一个专业的Python程序员。'
)

# 完整配置的 Agent
from pydantic_ai import Agent, ModelSettings, UsageLimits
from pydantic import BaseModel


class OutputSchema(BaseModel):
    answer: str
    confidence: float


agent = Agent(
    model='anthropic:claude-3-5-sonnet-20241022',
    deps_type=MyDependencies,
    output_type=OutputSchema,
    system_prompt='你是一个有帮助的助手。',
    tools=[tool1, tool2, tool3],
    retries=3,
    model_settings=ModelSettings(
        temperature=0.7,
        max_tokens=2000,
        timeout=60
    ),
    usage_limits=UsageLimits(
        request_limit=10,
        tool_calls_limit=5
    )
)
```

### 构造参数详解

#### `model` - 模型选择

格式：`provider:model_name`

```python
# OpenAI
Agent('openai:gpt-4')
Agent('openai:gpt-4-turbo')
Agent('openai:gpt-3.5-turbo')

# Anthropic
Agent('anthropic:claude-3-5-sonnet-20241022')
Agent('anthropic:claude-3-opus-20240229')

# Google
Agent('google:gemini-1.5-pro')
Agent('google:gemini-1.5-flash')

# Groq (快速且免费)
Agent('groq:llama3-70b-8192')
Agent('groq:mixtral-8x7b-32768')
```

#### `deps_type` - 依赖类型

指定 `RunContext` 的泛型类型：

```python
from dataclasses import dataclass


@dataclass
class DatabaseDeps:
    db_url: str
    api_key: str


agent = Agent(
    'openai:gpt-4',
    deps_type=DatabaseDeps
)

# 类型安全：ctx.deps 的类型是 DatabaseDeps
@agent.tool
def query_db(ctx: RunContext[DatabaseDeps], query: str) -> str:
    # IDE 会提供自动补全
    url = ctx.deps.db_url
    key = ctx.deps.api_key
    return execute_query(url, key, query)
```

#### `output_type` - 输出类型

默认为 `str`，可以是任何 Pydantic 模型：

```python
# 简单类型
agent = Agent('openai:gpt-4', output_type=int)
result = agent.run_sync('1+1等于多少？')
print(result.data)  # 2 (int 类型)

# Pydantic 模型
class Person(BaseModel):
    name: str
    age: int
    occupation: str


agent = Agent('openai:gpt-4', output_type=Person)
result = agent.run_sync('介绍一下爱因斯坦')
print(result.data.name)  # "Albert Einstein"
```

#### `retries` - 重试次数

LLM 失败时的重试次数：

```python
agent = Agent(
    'openai:gpt-4',
    retries=3  # 失败后最多重试3次
)

# 可以在运行时覆盖
result = agent.run_sync('提示', retries=5)
```

#### `model_settings` - 模型设置

```python
from pydantic_ai import ModelSettings

agent = Agent(
    'openai:gpt-4',
    model_settings=ModelSettings(
        temperature=0.7,        # 创造性 (0-2)
        max_tokens=2000,        # 最大生成长度
        timeout=30,             # 超时时间（秒）
        top_p=0.9,             # 核采样
        frequency_penalty=0.5,  # 频率惩罚
        presence_penalty=0.5,   # 存在惩罚
    )
)
```

#### `usage_limits` - 使用限制

```python
from pydantic_ai import UsageLimits

agent = Agent(
    'openai:gpt-4',
    usage_limits=UsageLimits(
        response_tokens_limit=10000,  # 最大响应token数
        request_limit=50,             # 最大请求次数
        tool_calls_limit=20,          # 最大工具调用次数
    )
)
```

## 💬 System Prompt 和 Instructions

### 静态 System Prompt

```python
agent = Agent(
    'openai:gpt-4',
    system_prompt='你是一个专业的数据科学家，擅长数据分析和可视化。'
)
```

### 动态 System Prompt

使用装饰器定义动态提示：

```python
from pydantic_ai import Agent, RunContext


@dataclass
class UserContext:
    user_id: str
    user_level: str  # "beginner", "intermediate", "expert"


agent = Agent('openai:gpt-4', deps_type=UserContext)


@agent.system_prompt
def get_system_prompt(ctx: RunContext[UserContext]) -> str:
    level = ctx.deps.user_level

    prompts = {
        "beginner": "你是一个耐心的导师，用简单的语言解释概念。",
        "intermediate": "你是一个专业的顾问，提供详细的技术建议。",
        "expert": "你是一个技术专家，可以深入探讨高级主题。"
    }

    return prompts.get(level, prompts["beginner"])


# 使用
result = agent.run_sync(
    '解释什么是机器学习',
    deps=UserContext(user_id='123', user_level='beginner')
)
```

### 异步动态 System Prompt

```python
@agent.system_prompt
async def get_system_prompt(ctx: RunContext[UserContext]) -> str:
    # 从数据库异步加载用户偏好
    preferences = await load_user_preferences(ctx.deps.user_id)

    return f'根据用户偏好 {preferences} 定制回答。'
```

### Static Instructions

```python
agent = Agent(
    'openai:gpt-4',
    instructions='提取文本中的关键信息。'
)
```

### 动态 Instructions

```python
@agent.instructions
def get_instructions(ctx: RunContext[MyDeps]) -> str:
    task_type = ctx.deps.task_type

    if task_type == 'summarize':
        return '总结文本的核心要点。'
    elif task_type == 'translate':
        return '将文本翻译成英文。'
    else:
        return '分析文本情感。'
```

### System Prompt vs Instructions

| 特性 | System Prompt | Instructions |
|------|--------------|-------------|
| 保留历史 | ✅ 是 | ❌ 否 |
| 推荐场景 | 定义持久身份 | 定义具体任务 |
| 使用频率 | 较少 | 推荐 |

**推荐做法**：
- 大多数情况使用 `instructions`
- 只在需要保留历史上下文时使用 `system_prompt`

## 🏃 运行方式详解

### 1. run() - 异步运行

**返回**: `RunResult`

```python
async def process():
    result = await agent.run('用户输入')

    # 访问结果
    print(result.data)              # 输出数据
    print(result.usage())           # Token使用
    print(result.cost())            # 估算成本
    print(result.all_messages())    # 完整消息历史
    print(result.timestamp())       # 时间戳
```

**RunResult 属性**：

```python
result.data                 # 输出数据（类型为 output_type）
result.usage()             # UsageInfo 对象
result.cost()              # Optional[Cost] 对象
result.all_messages()      # 所有消息列表
result.new_messages()      # 新消息（用于历史）
result.timestamp()         # 运行时间戳
```

### 2. run_sync() - 同步运行

```python
result = agent.run_sync('用户输入')

# 等价于
import asyncio
result = asyncio.run(agent.run('用户输入'))
```

**注意事项**：
- 底层仍是异步
- 会创建新的事件循环（如果没有运行中的循环）
- 不适合在异步函数中调用

### 3. run_stream() - 流式传输

**返回**: 异步上下文管理器

```python
async def stream_response():
    async with agent.run_stream('生成长文本') as stream:
        # 逐文本流式输出
        async for text in stream.stream_text():
            print(text, end='', flush=True)

        # 获取最终结果
        result = await stream.get_result()
        print(f"\n\n总token数: {result.usage().total_tokens}")
```

**流式结构化输出**：

```python
class Story(BaseModel):
    title: str
    chapters: list[str]


agent = Agent('openai:gpt-4', output_type=Story)


async def stream_story():
    async with agent.run_stream('写一个短篇故事') as stream:
        # 流式接收部分解析的数据
        async for partial in stream.stream():
            if partial.title:
                print(f"标题: {partial.title}")
            if partial.chapters:
                print(f"当前章节数: {len(partial.chapters)}")

        # 最终完整数据
        final = await stream.get_result()
        print(f"\n完整故事: {final.data}")
```

### 4. run_stream_events() - 事件流

**返回**: `AsyncIterator[AgentStreamEvent]`

```python
async def handle_events():
    async for event in agent.run_stream_events('处理复杂任务'):
        if event.type == 'text':
            # 文本生成事件
            print(event.data, end='')

        elif event.type == 'tool_call':
            # 工具调用事件
            print(f"\n调用工具: {event.tool_name}")
            print(f"参数: {event.args}")

        elif event.type == 'tool_return':
            # 工具返回事件
            print(f"工具结果: {event.result}")

        elif event.type == 'thinking':
            # 思考过程（如果模型支持）
            print(f"思考: {event.data}")
```

**事件类型**：
- `text`: 文本生成
- `tool_call`: 工具调用
- `tool_return`: 工具返回
- `thinking`: 思考过程
- `complete`: 完成

### 5. iter() - 图迭代

**返回**: `AsyncIterator[GraphNode]`

低级 API，用于图工作流：

```python
async def graph_iteration():
    async for node in agent.iter('提示'):
        print(f"节点类型: {node.type}")

        if node.type == 'tool_call':
            print(f"调用工具: {node.tool_name}")
            # 可以干预或修改

        elif node.type == 'complete':
            print(f"最终结果: {node.data}")
```

## 📜 消息历史管理

### 构建对话

```python
# 初始对话
result1 = agent.run_sync('我叫张三')

# 继续对话 - 传递历史
result2 = agent.run_sync(
    '我叫什么名字？',
    message_history=result1.new_messages()
)
# 输出: 你叫张三。

# 继续对话
result3 = agent.run_sync(
    '总结我们的对话',
    message_history=result2.new_messages()
)
```

### 合并多轮历史

```python
from pydantic_ai.messages import ModelMessage

# 收集所有历史
history = []
history.extend(result1.new_messages())
history.extend(result2.new_messages())

# 继续对话
result3 = agent.run_sync(
    '新的问题',
    message_history=history
)
```

### 自定义消息

```python
from pydantic_ai.messages import UserMessage, SystemMessage

# 构造自定义历史
custom_history = [
    SystemMessage(content='你是一个历史学家'),
    UserMessage(content='介绍秦始皇', timestamp=...),
    # ... 更多消息
]

result = agent.run_sync(
    '他统一了什么？',
    message_history=custom_history
)
```

## 🔄 错误处理和重试

### ModelRetry - 自我修正

```python
from pydantic_ai import ModelRetry


@agent.output_validator
def validate_output(ctx: RunContext[None], output: MyOutput) -> MyOutput:
    if output.confidence < 0.8:
        # 触发重试，让模型改进
        raise ModelRetry('置信度太低，请提供更准确的答案。')

    return output
```

**ModelRetry 的工作原理**：
1. 验证器抛出 `ModelRetry`
2. 错误消息发送给 LLM
3. LLM 重新生成响应
4. 重复直到成功或达到重试限制

### 捕获运行消息

```python
from pydantic_ai import capture_run_messages


with capture_run_messages() as messages:
    try:
        result = agent.run_sync('可能失败的请求')
    except Exception as e:
        # 检查失败的消息
        print(f"错误: {e}")
        print(f"消息历史: {messages}")
        # 可以用于调试
```

### 自定义重试逻辑

```python
from tenacity import retry, stop_after_attempt, wait_exponential


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
async def robust_run(prompt: str):
    try:
        return await agent.run(prompt)
    except Exception as e:
        print(f"重试中... 错误: {e}")
        raise
```

## 🏷️ 元数据和追踪

### 静态元数据

```python
agent = Agent(
    'openai:gpt-4',
    metadata={
        'app_version': '1.0.0',
        'environment': 'production'
    }
)
```

### 动态元数据

```python
from pydantic_ai import Agent, RunContext


@dataclass
class TenantDeps:
    tenant_id: str
    user_id: str


agent = Agent('openai:gpt-4', deps_type=TenantDeps)


@agent.metadata
def get_metadata(ctx: RunContext[TenantDeps]) -> dict[str, str]:
    return {
        'tenant_id': ctx.deps.tenant_id,
        'user_id': ctx.deps.user_id,
        'request_time': str(datetime.now())
    }
```

**元数据的用途**：
- 在 Logfire 中追踪
- 按租户/用户分组
- 性能分析
- 成本归因

## ⚙️ 高级配置

### 覆盖配置

Agent 的配置可以在多个层级覆盖：

```python
# 1. Agent 级别
agent = Agent(
    'openai:gpt-4',
    model_settings=ModelSettings(temperature=0.5),
    retries=2
)

# 2. 运行时覆盖
result = agent.run_sync(
    '提示',
    model_settings=ModelSettings(temperature=0.9),  # 覆盖
    retries=5  # 覆盖
)
```

### 使用 override() 上下文

用于测试或临时修改：

```python
with agent.override(
    model='openai:gpt-3.5-turbo',  # 临时使用更便宜的模型
    deps=test_deps
):
    result = agent.run_sync('测试提示')
```

### 条件配置

```python
import os

# 根据环境使用不同模型
if os.getenv('ENVIRONMENT') == 'production':
    model = 'openai:gpt-4'
    temperature = 0.3
else:
    model = 'openai:gpt-3.5-turbo'
    temperature = 0.7

agent = Agent(
    model,
    model_settings=ModelSettings(temperature=temperature)
)
```

## 🎯 最佳实践

### 1. 全局 Agent 实例

```python
# ✅ 推荐：模块级别定义
support_agent = Agent('openai:gpt-4', system_prompt='客服助手')
analyst_agent = Agent('openai:gpt-4', system_prompt='数据分析师')

def handle_support(query: str):
    return support_agent.run_sync(query)


def analyze_data(data: str):
    return analyst_agent.run_sync(data)
```

### 2. 使用类型提示

```python
from typing import TypedDict


class MyDeps(TypedDict):
    db_url: str
    api_key: str


class MyOutput(BaseModel):
    answer: str


# ✅ 完整类型注解
agent: Agent[MyDeps, MyOutput] = Agent(
    'openai:gpt-4',
    deps_type=MyDeps,
    output_type=MyOutput
)
```

### 3. 设置合理的限制

```python
agent = Agent(
    'openai:gpt-4',
    usage_limits=UsageLimits(
        request_limit=10,      # 防止无限循环
        tool_calls_limit=5,    # 限制工具调用
        response_tokens_limit=5000  # 控制成本
    ),
    retries=2  # 不要过度重试
)
```

### 4. 优雅处理错误

```python
from pydantic_ai.exceptions import UsageLimitExceeded, ModelRetryError

try:
    result = await agent.run(user_input)
except UsageLimitExceeded as e:
    print(f"达到使用限制: {e}")
except ModelRetryError as e:
    print(f"重试失败: {e}")
except Exception as e:
    print(f"未知错误: {e}")
```

### 5. 记录和监控

```python
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

# Agent 运行会自动追踪到 Logfire
result = await agent.run('提示')
```

## 📚 下一步

继续学习：

1. [04_工具系统.md](./04_工具系统.md) - 给 Agent 添加工具能力
2. [05_依赖注入.md](./05_依赖注入.md) - 深入理解依赖注入
3. [12_可观测性.md](./12_可观测性.md) - 集成 Logfire 监控

## 🔗 参考资源

- [官方文档 - Agents](https://ai.pydantic.dev/agents/)
- [官方文档 - Messages](https://ai.pydantic.dev/messages/)
- [API 参考 - Agent](https://ai.pydantic.dev/api/agent/)
