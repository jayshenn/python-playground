"""
输出验证示例

演示如何使用验证器确保 LLM 输出的质量。

运行方式：
    uv run python 04_pydantic_ai/05_advanced/02_validation.py
"""

from pydantic_ai import Agent, RunContext, ModelRetry
from pydantic import BaseModel, Field, field_validator
import re


class Email(BaseModel):
    """邮件模型"""
    recipient: str = Field(description="收件人邮箱")
    subject: str = Field(description="邮件主题", min_length=5)
    body: str = Field(description="邮件正文", min_length=20)

    @field_validator('recipient')
    def validate_email(cls, v):
        """验证邮箱格式"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, v):
            raise ValueError('邮箱格式不正确')
        return v


def demo_pydantic_validation():
    """Pydantic 自动验证"""
    print("=" * 60)
    print("Pydantic 自动验证示例")
    print("=" * 60)

    agent = Agent(
        'openai:gpt-4',
        output_type=Email,
        system_prompt='根据用户需求生成邮件。'
    )

    result = agent.run_sync(
        '给 john@example.com 写一封邮件，主题是项目更新，内容关于本周进展'
    )

    print(f"\n收件人: {result.data.recipient}")
    print(f"主题: {result.data.subject}")
    print(f"正文: {result.data.body}")


class ProductReview(BaseModel):
    """产品评论"""
    product_name: str
    rating: int = Field(ge=1, le=5, description="评分 1-5")
    review: str
    sentiment: str = Field(description="positive, negative, or neutral")


def demo_output_validator():
    """使用输出验证器"""
    print("\n" + "=" * 60)
    print("输出验证器示例")
    print("=" * 60)

    agent = Agent(
        'openai:gpt-4',
        output_type=ProductReview,
        system_prompt='分析产品评论并提取结构化信息。'
    )

    @agent.output_validator
    def validate_review(ctx: RunContext[None], output: ProductReview) -> ProductReview:
        """验证评论的一致性"""
        # 检查评分和情感是否一致
        if output.rating >= 4 and output.sentiment == 'negative':
            raise ModelRetry(
                '评分和情感不一致：高评分不应该是负面情感。请重新分析。'
            )

        if output.rating <= 2 and output.sentiment == 'positive':
            raise ModelRetry(
                '评分和情感不一致：低评分不应该是正面情感。请重新分析。'
            )

        # 检查产品名称不为空
        if not output.product_name or output.product_name == 'unknown':
            raise ModelRetry('请提供具体的产品名称。')

        return output

    # 测试评论
    review_text = """
    这款笔记本电脑真的太棒了！
    性能强劲，屏幕清晰，续航时间长。
    非常满意这次购买！
    """

    result = agent.run_sync(f'分析以下评论：\n{review_text}')

    print(f"\n产品: {result.data.product_name}")
    print(f"评分: {result.data.rating}/5")
    print(f"情感: {result.data.sentiment}")
    print(f"评论: {result.data.review}")


class DataExtraction(BaseModel):
    """数据提取"""
    name: str
    phone: str
    email: str


def demo_retry_on_validation_failure():
    """验证失败时自动重试"""
    print("\n" + "=" * 60)
    print("验证失败自动重试示例")
    print("=" * 60)

    agent = Agent(
        'openai:gpt-4',
        output_type=DataExtraction,
        retries=3  # 最多重试3次
    )

    @agent.output_validator
    def validate_data(ctx: RunContext[None], output: DataExtraction) -> DataExtraction:
        """严格验证提取的数据"""
        # 验证电话格式（简单示例）
        if not re.match(r'^\d{3}-?\d{4}-?\d{4}$', output.phone.replace(' ', '')):
            raise ModelRetry(
                f'电话格式不正确: {output.phone}。'
                '请使用格式: 138-1234-5678 或 13812345678'
            )

        # 验证邮箱
        if '@' not in output.email or '.' not in output.email:
            raise ModelRetry(f'邮箱格式不正确: {output.email}')

        # 验证姓名不为空
        if len(output.name) < 2:
            raise ModelRetry('请提供完整姓名')

        print(f"[✓ 验证通过]")
        return output

    text = """
    联系人：张三
    电话：13812345678
    邮箱：zhangsan@example.com
    """

    try:
        result = agent.run_sync(f'从以下文本提取联系信息：\n{text}')

        print(f"\n姓名: {result.data.name}")
        print(f"电话: {result.data.phone}")
        print(f"邮箱: {result.data.email}")
        print(f"\n重试次数: {result.usage().request_count - 1}")

    except Exception as e:
        print(f"\n验证失败: {e}")


def main():
    """主函数"""
    print("Pydantic AI 输出验证示例")
    print("=" * 60)

    demo_pydantic_validation()
    demo_output_validator()
    demo_retry_on_validation_failure()


if __name__ == '__main__':
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    main()
