"""
工具使用示例

演示如何给 Agent 添加工具函数，让 LLM 可以调用 Python 函数。

运行方式：
    uv run python 04_pydantic_ai/03_tools/01_tools_example.py
"""

from pydantic_ai import Agent, RunContext
import random
from datetime import datetime


# 创建 Agent
agent = Agent(
    'openai:gpt-4',
    system_prompt='你是一个有用的助手，可以使用工具帮助用户。'
)


@agent.tool
def get_current_time(ctx: RunContext[None]) -> str:
    """
    获取当前时间。

    Returns:
        当前时间的字符串表示
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@agent.tool
def roll_dice(ctx: RunContext[None], sides: int = 6, count: int = 1) -> dict:
    """
    掷骰子。

    Args:
        sides: 骰子的面数，默认为 6
        count: 掷骰子的次数，默认为 1

    Returns:
        包含结果的字典
    """
    rolls = [random.randint(1, sides) for _ in range(count)]
    return {
        'rolls': rolls,
        'total': sum(rolls),
        'average': sum(rolls) / len(rolls)
    }


@agent.tool_plain
def calculate(a: float, b: float, operation: str) -> float:
    """
    执行基本算术运算。

    Args:
        a: 第一个数字
        b: 第二个数字
        operation: 运算类型（add, subtract, multiply, divide）

    Returns:
        运算结果
    """
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else float('inf')
    }

    if operation not in operations:
        raise ValueError(f"不支持的运算: {operation}")

    return operations[operation](a, b)


def main():
    """工具使用示例"""
    # 测试查询列表
    queries = [
        '现在几点了？',
        '帮我掷 3 个 20 面的骰子',
        '计算 (15 + 27) * 3',
        '先告诉我现在的时间，然后掷两个骰子'
    ]

    for query in queries:
        print(f"\n{'=' * 60}")
        print(f"用户：{query}")
        print('=' * 60)

        result = agent.run_sync(query)

        print(f"Agent：{result.data}")

        # 显示调用的工具
        print("\n调用的工具：")
        for message in result.all_messages():
            if hasattr(message, 'parts'):
                for part in message.parts:
                    if hasattr(part, 'tool_name'):
                        print(f"  - {part.tool_name}({part.args})")
                        print(f"    结果: {part.content}")


if __name__ == '__main__':
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    main()
