"""
何时使用 Any

对应文档: 17-type-system-checkers.md § 17.best
"""

from typing import Any

# ✅ 合理使用场景：处理真正未知的数据 (如 JSON 解析、动态加载)
def load_dynamic_data(source: str) -> Any:
    # 外部数据源返回的数据结构在编写时是未知的
    return {"id": 1, "meta": "..."}

# ❌ 避免使用场景：原本可以定义具体类型
# 错误: def process_user(user: Any) -> Any:
# 应该定义一个具体的类或 TypedDict

class User:
    def __init__(self, name: str):
        self.name = name

def process_user(user: User) -> str: # ✅ 使用具体类型
    return user.name

if __name__ == '__main__':
    data = load_dynamic_data("api")
    print(f"Loaded: {data}")
