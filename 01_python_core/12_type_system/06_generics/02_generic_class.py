"""
泛型类

对应文档: 15-type-system-stdlib.md § 15.generics
"""

from typing import Callable
from datetime import datetime, timedelta

# 1. 简单泛型类 (Python 3.12+ 语法)
class Stack[T]:
    """泛型栈容器"""
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# 2. 多类型参数
class Pair[K, V]:
    """键值对容器"""
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

# 3. 实战示例：泛型缓存
class Cache[K, V]:
    """带有过期时间的通用缓存"""
    def __init__(self, ttl_seconds: int = 60):
        self._storage: dict[K, tuple[V, datetime]] = {}
        self._ttl = timedelta(seconds=ttl_seconds)

    def set(self, key: K, value: V) -> None:
        self._storage[key] = (value, datetime.now())

    def get(self, key: K) -> V | None:
        if key not in self._storage:
            return None
        
        val, ts = self._storage[key]
        if datetime.now() - ts > self._ttl:
            del self._storage[key]
            return None
        return val

if __name__ == '__main__':
    # 使用栈
    s = Stack[int]()
    s.push(100)
    print(f"Stack pop: {s.pop()}")
    
    # 使用缓存 (类型推断)
    user_cache = Cache[str, dict]()
    user_cache.set("alice", {"id": 1, "role": "admin"})
    print(f"Cached user: {user_cache.get('alice')}")
