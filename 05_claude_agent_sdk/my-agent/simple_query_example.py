"""
最简单的 Claude Agent SDK 示例
================================

使用无状态 query() 函数的最简单方式来使用 Claude Agent SDK。

"""

import asyncio
from colorama import Fore, Style
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage


async def main():
    """简单的单次查询示例，显示原始消息。"""

    # 配置选项
    options = ClaudeAgentOptions(
        system_prompt="你是一个乐于助人的 Python 专家。",
    )

    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}Claude Agent SDK - Simple Query Example")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print(f"\n{Style.DIM}System: {options.system_prompt}")
    print(f"Query: 用一句话解释 async/await 在 Python 中的作用。{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}{'─' * 60}{Style.RESET_ALL}\n")

    # 简单查询 - 流式传输消息
    async for message in query(
        prompt="用一句话解释 async/await 在 Python 中的作用。",
        options=options
    ):
        # 只显示助手的回复内容
        if isinstance(message, AssistantMessage):
            print(f"{Fore.GREEN}Claude 回复:{Style.RESET_ALL}\n")
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
            print()

        # 显示结果统计信息
        elif isinstance(message, ResultMessage):
            print(f"\n{Fore.YELLOW}{'─' * 60}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}统计信息:{Style.RESET_ALL}")
            print(f"  • 耗时: {message.duration_ms}ms (API: {message.duration_api_ms}ms)")
            print(f"  • 轮数: {message.num_turns}")
            print(f"  • 成本: ${message.total_cost_usd:.6f}")
            if hasattr(message, 'usage') and message.usage:
                usage = message.usage
                print(f"  • Token 使用:")
                print(f"    - 输入: {usage.get('input_tokens', 0)} tokens")
                print(f"    - 输出: {usage.get('output_tokens', 0)} tokens")
                if usage.get('cache_read_input_tokens'):
                    print(f"    - 缓存读取: {usage.get('cache_read_input_tokens', 0)} tokens")

    print(f"\n{Fore.CYAN}✓ 完成!{Style.RESET_ALL}\n")


if __name__ == "__main__":
    asyncio.run(main())