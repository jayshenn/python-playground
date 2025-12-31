"""
多轮对话示例

演示如何使用消息历史构建多轮对话。

运行方式：
    uv run python 04_pydantic_ai/examples/05_conversation.py
"""

from pydantic_ai import Agent


def main():
    """多轮对话示例"""
    agent = Agent(
        'openai:gpt-4',
        system_prompt='你是一个友好的对话助手，能够记住对话历史。'
    )

    print("=" * 60)
    print("多轮对话示例（输入 'quit' 退出）")
    print("=" * 60)

    # 消息历史
    history = []

    while True:
        # 获取用户输入
        user_input = input("\n你：").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break

        if not user_input:
            continue

        # 运行 Agent，传递历史消息
        result = agent.run_sync(
            user_input,
            message_history=history
        )

        # 显示响应
        print(f"\nAgent：{result.data}")

        # 更新历史（使用 new_messages() 获取本轮的新消息）
        history = result.new_messages()

        # 显示统计信息
        print(f"\n[本轮使用 {result.usage().total_tokens} tokens]")


def demo_conversation():
    """预定义的对话演示"""
    agent = Agent(
        'openai:gpt-4',
        system_prompt='你是一个友好的对话助手。'
    )

    conversations = [
        "你好，我叫张三。",
        "我今年 25 岁，是一名程序员。",
        "我喜欢用 Python 编程。",
        "你还记得我的名字吗？",
        "我的职业是什么？",
        "总结一下我们的对话内容。"
    ]

    print("\n" + "=" * 60)
    print("预定义对话演示")
    print("=" * 60)

    history = []

    for user_msg in conversations:
        print(f"\n用户：{user_msg}")

        result = agent.run_sync(
            user_msg,
            message_history=history
        )

        print(f"Agent：{result.data}")

        # 更新历史
        history = result.new_messages()


if __name__ == '__main__':
    import os
    import sys

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    # 检查是否使用演示模式
    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        demo_conversation()
    else:
        main()
