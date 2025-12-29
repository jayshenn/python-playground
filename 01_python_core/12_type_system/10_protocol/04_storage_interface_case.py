"""
实战案例：存储接口协议

对应文档: 15-type-system-stdlib.md § 15.protocol
"""

from typing import Protocol

# 1. 定义存储协议 (Interface)
class Storage(Protocol):
    def get(self, key: str) -> str | None: ...
    def set(self, key: str, value: str) -> None: ...
    def delete(self, key: str) -> bool: ...

# 2. 内存实现 (适用于测试)
class MemoryStorage:
    def __init__(self):
        self._data: dict[str, str] = {}
        
    def get(self, key: str) -> str | None:
        return self._data.get(key)
    
    def set(self, key: str, value: str) -> None:
        self._data[key] = value
        
    def delete(self, key: str) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False

# 3. 模拟 Redis 实现 (适用于生产)
class RedisStorage:
    def get(self, key: str) -> str | None:
        print(f"Redis: GET {key}")
        return "mock_redis_value"
    
    def set(self, key: str, value: str) -> None:
        print(f"Redis: SET {key}={value}")
        
    def delete(self, key: str) -> bool:
        print(f"Redis: DEL {key}")
        return True

# 4. 业务逻辑只依赖于协议
def save_user_session(storage: Storage, user_id: int, token: str) -> None:
    key = f"session:{user_id}"
    storage.set(key, token)
    print(f"Session saved for user {user_id}")

if __name__ == '__main__':
    # 注入不同的实现
    mem_store = MemoryStorage()
    redis_store = RedisStorage()
    
    print("Using Memory Storage:")
    save_user_session(mem_store, 1001, "TOKEN_A")
    
    print("\nUsing Redis Storage:")
    save_user_session(redis_store, 1002, "TOKEN_B")
