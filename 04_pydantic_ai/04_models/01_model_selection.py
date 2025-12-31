"""
模型选择示例

演示如何使用不同的模型提供商和配置。

运行方式：
    uv run python 04_pydantic_ai/04_models/01_model_selection.py
"""

from pydantic_ai import Agent, ModelSettings
import os


def demo_openai():
    """OpenAI 模型示例"""
    print("\n" + "=" * 60)
    print("OpenAI 模型示例")
    print("=" * 60)

    agent = Agent('openai:gpt-4')
    result = agent.run_sync('用一句话介绍 Python')
    print(f"GPT-4: {result.data}")

    # 使用 GPT-3.5 (更快更便宜)
    agent_35 = Agent('openai:gpt-3.5-turbo')
    result_35 = agent_35.run_sync('用一句话介绍 Python')
    print(f"GPT-3.5: {result_35.data}")


def demo_model_settings():
    """模型配置示例"""
    print("\n" + "=" * 60)
    print("模型配置示例")
    print("=" * 60)

    # 创造性任务 - 高温度
    creative_agent = Agent(
        'openai:gpt-4',
        model_settings=ModelSettings(
            temperature=0.9,  # 更有创造性
            max_tokens=500
        )
    )

    # 分析任务 - 低温度
    analytical_agent = Agent(
        'openai:gpt-4',
        model_settings=ModelSettings(
            temperature=0.3,  # 更确定性
            max_tokens=500
        )
    )

    prompt = '给我讲一个关于 AI 的故事'

    print("\n高温度输出 (temperature=0.9):")
    result1 = creative_agent.run_sync(prompt)
    print(result1.data[:200] + "...")

    print("\n低温度输出 (temperature=0.3):")
    result2 = analytical_agent.run_sync(prompt)
    print(result2.data[:200] + "...")


def demo_fallback():
    """Fallback 模型示例"""
    print("\n" + "=" * 60)
    print("Fallback 模型示例")
    print("=" * 60)

    from pydantic_ai.models import FallbackModel

    # 优先使用 GPT-4，失败时降级到 GPT-3.5
    fallback = FallbackModel([
        ('openai:gpt-4', ModelSettings(temperature=0.7)),
        ('openai:gpt-3.5-turbo', None),
    ])

    agent = Agent(fallback)
    result = agent.run_sync('解释什么是机器学习')
    print(result.data)


def demo_model_comparison():
    """模型对比示例"""
    print("\n" + "=" * 60)
    print("模型性能对比")
    print("=" * 60)

    import time

    models = [
        'openai:gpt-4',
        'openai:gpt-3.5-turbo',
    ]

    prompt = '解释量子计算的基本原理'

    for model_name in models:
        agent = Agent(model_name)

        start = time.time()
        result = agent.run_sync(prompt)
        duration = time.time() - start

        print(f"\n模型: {model_name}")
        print(f"耗时: {duration:.2f}秒")
        print(f"Tokens: {result.usage().total_tokens}")
        print(f"回答长度: {len(result.data)} 字符")
        print(f"回答: {result.data[:100]}...")


def main():
    """主函数"""
    # 检查 API 密钥
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    print("Pydantic AI 模型选择示例")
    print("=" * 60)

    # 运行示例
    demo_openai()
    demo_model_settings()
    demo_model_comparison()

    # Fallback 示例（可选，需要处理失败情况）
    try:
        demo_fallback()
    except Exception as e:
        print(f"\nFallback 示例跳过: {e}")


if __name__ == '__main__':
    main()
