"""
结构化输出示例

演示如何使用 Pydantic 模型定义和验证 Agent 输出。

运行方式：
    uv run python 04_pydantic_ai/examples/02_structured_output.py
"""

from pydantic_ai import Agent
from pydantic import BaseModel, Field


class CityInfo(BaseModel):
    """城市信息模型"""
    city: str = Field(description="城市名称")
    country: str = Field(description="国家名称")
    population: int = Field(description="人口数量")
    famous_landmarks: list[str] = Field(description="著名地标列表")
    best_time_to_visit: str = Field(description="最佳旅游时间")


def main():
    """结构化输出示例"""
    # 创建 Agent，指定输出类型
    agent = Agent(
        'openai:gpt-4',
        output_type=CityInfo,
        system_prompt='提取并结构化城市信息。'
    )

    # 测试城市列表
    cities = ['巴黎', '东京', '纽约']

    for city_name in cities:
        print(f"\n{'=' * 60}")
        print(f"查询城市：{city_name}")
        print('=' * 60)

        result = agent.run_sync(f'请提供关于{city_name}的信息')

        # result.data 是一个 CityInfo 实例
        city = result.data

        print(f"城市：{city.city}")
        print(f"国家：{city.country}")
        print(f"人口：{city.population:,}")
        print(f"著名地标：{', '.join(city.famous_landmarks)}")
        print(f"最佳旅游时间：{city.best_time_to_visit}")

        # 验证数据
        assert isinstance(city, CityInfo)
        assert city.population > 0


if __name__ == '__main__':
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    main()
