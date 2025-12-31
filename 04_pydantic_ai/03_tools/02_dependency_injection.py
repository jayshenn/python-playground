"""
依赖注入示例

演示如何使用依赖注入传递数据库连接、API 密钥等上下文信息。

运行方式：
    uv run python 04_pydantic_ai/03_tools/02_dependency_injection.py
"""

from pydantic_ai import Agent, RunContext
from dataclasses import dataclass
import sqlite3
from pathlib import Path


@dataclass
class DatabaseDeps:
    """数据库依赖"""
    db_path: str

    def get_connection(self):
        """获取数据库连接"""
        return sqlite3.connect(self.db_path)


# 创建 Agent，指定依赖类型
agent = Agent(
    'openai:gpt-4',
    deps_type=DatabaseDeps,
    system_prompt='你是一个数据库查询助手，可以帮助用户查询和分析数据。'
)


@agent.tool
def query_users(ctx: RunContext[DatabaseDeps], limit: int = 10) -> list[dict]:
    """
    查询用户列表。

    Args:
        limit: 返回的最大用户数

    Returns:
        用户列表
    """
    # 通过 ctx.deps 访问依赖
    conn = ctx.deps.get_connection()
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM users LIMIT {limit}')

    # 获取列名
    columns = [desc[0] for desc in cursor.description]

    # 转换为字典列表
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    conn.close()
    return results


@agent.tool
def count_users(ctx: RunContext[DatabaseDeps]) -> int:
    """
    统计用户总数。

    Returns:
        用户总数
    """
    conn = ctx.deps.get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    conn.close()
    return count


@agent.tool
def search_users(ctx: RunContext[DatabaseDeps], name: str) -> list[dict]:
    """
    按名字搜索用户。

    Args:
        name: 用户名（支持模糊搜索）

    Returns:
        匹配的用户列表
    """
    conn = ctx.deps.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM users WHERE name LIKE ?',
        (f'%{name}%',)
    )

    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    conn.close()
    return results


def setup_database(db_path: str):
    """设置示例数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 创建表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    ''')

    # 插入示例数据
    users = [
        (1, '张三', 'zhangsan@example.com', 25),
        (2, '李四', 'lisi@example.com', 30),
        (3, '王五', 'wangwu@example.com', 28),
        (4, '赵六', 'zhaoliu@example.com', 35),
        (5, '钱七', 'qianqi@example.com', 22),
    ]

    cursor.executemany(
        'INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)',
        users
    )

    conn.commit()
    conn.close()


def main():
    """依赖注入示例"""
    # 设置数据库
    db_path = '/tmp/pydantic_ai_example.db'
    setup_database(db_path)

    print(f"数据库路径：{db_path}\n")

    # 创建依赖实例
    deps = DatabaseDeps(db_path=db_path)

    # 测试查询
    queries = [
        '有多少个用户？',
        '显示所有用户',
        '查找名字包含"张"的用户',
        '显示前 3 个用户的信息'
    ]

    for query in queries:
        print(f"\n{'=' * 60}")
        print(f"用户：{query}")
        print('=' * 60)

        # 运行时传递依赖
        result = agent.run_sync(query, deps=deps)

        print(f"Agent：{result.data}")

    # 清理
    Path(db_path).unlink(missing_ok=True)


if __name__ == '__main__':
    import os

    if not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误：请设置 OPENAI_API_KEY 环境变量")
        exit(1)

    main()
