"""
Pydantic AI 最简单的示例

运行方式：
    uv run python 04_pydantic_ai/examples/01_hello_world.py
"""

from pydantic_ai import Agent


def main():
    """最简单的 Agent 示例"""
    # 创建 Agent
    agent = Agent('openai:gpt-4')

    # 同步运行
    result = agent.run_sync('你好，请介绍一下你自己。')

    print("=" * 50)
    print("Agent 响应：")
    print("=" * 50)
    print(result.data)
    print()
    print("=" * 50)
    print(f"使用的 Token 数：{result.usage().total_tokens}")
    print("=" * 50)


if __name__ == '__main__':
    # 确保设置了 OPENAI_API_KEY 环境变量
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        print("示例：export OPENAI_API_KEY='sk-...'")
        exit(1)

    main()
