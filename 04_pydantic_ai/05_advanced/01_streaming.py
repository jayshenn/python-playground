"""
流式传输示例

演示如何使用流式传输实现实时响应。

运行方式：
    uv run python 04_pydantic_ai/05_advanced/01_streaming.py
"""

from pydantic_ai import Agent
from pydantic import BaseModel
import asyncio


async def demo_basic_streaming():
    """基础流式传输"""
    print("=" * 60)
    print("基础流式传输示例")
    print("=" * 60)

    agent = Agent('openai:gpt-4')

    print("\n正在生成...\n")

    async with agent.run_stream('写一个关于 AI 的短故事（100字左右）') as stream:
        # 逐字符流式输出
        async for text in stream.stream_text():
            print(text, end='', flush=True)

        # 获取最终结果
        result = await stream.get_result()

        print(f"\n\n{'=' * 60}")
        print(f"总 Token 数: {result.usage().total_tokens}")
        print("=" * 60)


async def demo_structured_streaming():
    """结构化数据流式传输"""
    print("\n" + "=" * 60)
    print("结构化数据流式传输")
    print("=" * 60)

    class Story(BaseModel):
        title: str
        content: str
        tags: list[str]

    agent = Agent('openai:gpt-4', output_type=Story)

    print("\n正在生成故事...\n")

    async with agent.run_stream('写一个科幻短故事') as stream:
        # 流式接收部分数据
        async for partial in stream.stream():
            if partial.title:
                print(f"\r标题: {partial.title}", end='', flush=True)

            if partial.content:
                # 显示内容长度
                print(f"\r标题: {partial.title} | 内容: {len(partial.content)} 字符",
                      end='', flush=True)

        # 获取完整结果
        final = await stream.get_result()

        print(f"\n\n{'=' * 60}")
        print(f"完整故事:")
        print(f"标题: {final.data.title}")
        print(f"内容: {final.data.content}")
        print(f"标签: {', '.join(final.data.tags)}")
        print("=" * 60)


async def demo_streaming_with_buffer():
    """带缓冲的流式传输"""
    print("\n" + "=" * 60)
    print("带缓冲的流式传输")
    print("=" * 60)

    agent = Agent('openai:gpt-4')

    buffer = []
    buffer_size = 10  # 每 10 个字符输出一次

    print("\n正在生成（带缓冲）...\n")

    async with agent.run_stream('解释什么是深度学习') as stream:
        async for text in stream.stream_text():
            buffer.append(text)

            # 当缓冲区足够大时输出
            if len(''.join(buffer)) >= buffer_size:
                print(''.join(buffer), end='', flush=True)
                buffer = []

        # 输出剩余内容
        if buffer:
            print(''.join(buffer), end='', flush=True)

    print("\n")


async def demo_event_streaming():
    """事件流示例"""
    print("\n" + "=" * 60)
    print("事件流示例")
    print("=" * 60)

    agent = Agent('openai:gpt-4')

    # 添加一个工具
    @agent.tool
    async def get_info(ctx, topic: str) -> str:
        """获取信息"""
        await asyncio.sleep(0.5)  # 模拟延迟
        return f"关于 {topic} 的信息"

    print("\n监听所有事件...\n")

    event_count = 0
    async for event in agent.run_stream_events('使用工具获取关于 Python 的信息'):
        event_count += 1

        if event.type == 'text':
            print(event.data, end='', flush=True)

        elif event.type == 'tool_call':
            print(f"\n[🔧 调用工具: {event.tool_name}]", flush=True)

        elif event.type == 'tool_return':
            print(f"\n[✅ 工具返回]", flush=True)

        elif event.type == 'complete':
            print(f"\n\n[✓ 完成，共 {event_count} 个事件]")


async def main():
    """主函数"""
    print("Pydantic AI 流式传输示例")
    print("=" * 60)

    # 运行各个示例
    await demo_basic_streaming()
    await demo_structured_streaming()
    await demo_streaming_with_buffer()
    await demo_event_streaming()


if __name__ == '__main__':
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    asyncio.run(main())
