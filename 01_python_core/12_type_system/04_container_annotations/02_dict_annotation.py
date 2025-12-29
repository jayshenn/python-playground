"""
字典注解

对应文档: 14-type-system-basics.md § 14.container
"""

# 1. 简单字典 (键类型: 值类型)
scores: dict[str, int] = {"Alice": 95, "Bob": 87}

# 2. 嵌套字典
user_data: dict[str, dict[str, str | int]] = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}

# 3. 复杂值类型 (使用类型别名)
type ConfigValue = str | int | bool | list[str]
config: dict[str, ConfigValue] = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
    "allowed_hosts": ["127.0.0.1", "localhost"]
}

# 4. 函数操作字典
def get_score(data: dict[str, int], name: str) -> int:
    """获取指定姓名分数，若不存在则返回 0"""
    return data.get(name, 0)

if __name__ == '__main__':
    print(f"Scores: {scores}")
    print(f"User1 name: {user_data['user1']['name']}")
    print(f"Port: {config['port']}")
    print(f"Alice's score: {get_score(scores, 'Alice')}")
