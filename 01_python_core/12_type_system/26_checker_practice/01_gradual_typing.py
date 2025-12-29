"""
渐进式类型化策略

对应文档: 17-type-system-checkers.md § 17.practice
"""

# 阶段 1: 核心模型 (Models)
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

# 阶段 2: 公共接口 (API)
def get_user_by_id(user_id: int) -> User | None:
    # 模拟从数据库获取
    if user_id > 0:
        return User(user_id, "Alice")
    return None

# 阶段 3: 复杂逻辑 (Logic)
def process_user_data(user: User) -> dict[str, str]:
    return {
        "summary": f"User {user.name} (ID: {user.id})"
    }

if __name__ == '__main__':
    # 通过分阶段添加注解，可以在不重构整个项目的情况下逐步提升类型安全性。
    u = get_user_by_id(1)
    if u:
        print(process_user_data(u))
