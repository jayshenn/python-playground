# --*-- coding:utf-8 --*--
"""
最简单的 Claude Agent SDK 示例
只需要设置环境变量 ANTHROPIC_API_KEY（或使用 .env 文件）
"""

import asyncio
from claude_agent_sdk import query

async def main():
    """向 Claude 问好"""
    async for message in query(prompt="你好"):
        print(message)

asyncio.run(main())
