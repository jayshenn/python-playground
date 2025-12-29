"""
函数类型注解

对应文档: 14-type-system-basics.md § 14.basic
"""

# 标注参数类型和返回值类型

def greet_users(names: list[str], greeting: str = "Hello") -> list[str]:
    """接收姓名列表，返回问候语列表"""
    results: list[str] = []
    for name in names:
        results.append(f"{greeting}, {name}")
    return results

if __name__ == '__main__':
    users = ["Alice", "Bob"]
    messages = greet_users(users, "Hi")
    for msg in messages:
        print(msg)
