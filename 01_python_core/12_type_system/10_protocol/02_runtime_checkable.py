"""
runtime_checkable 协议

对应文档: 15-type-system-stdlib.md § 15.protocol
"""

from typing import Protocol, runtime_checkable

# 默认情况下，Protocol 不支持 isinstance/issubclass
# 使用 @runtime_checkable 可以启用运行时检查
@runtime_checkable
class Closable(Protocol):
    def close(self) -> None:
        ...

class DatabaseConnection:
    def close(self) -> None:
        print("Connection closed.")

class SimpleFile:
    def close(self) -> None:
        print("File closed.")

if __name__ == '__main__':
    db = DatabaseConnection()
    sf = SimpleFile()
    text = "just a string"
    
    # 由于加了 @runtime_checkable，以下检查是合法的
    print(f"Is DB closable? {isinstance(db, Closable)}")    # True
    print(f"Is File closable? {isinstance(sf, Closable)}")  # True
    print(f"Is text closable? {isinstance(text, Closable)}") # False
    
    # 结合运行时检查的通用处理函数
    def safe_close(obj: object) -> None:
        if isinstance(obj, Closable):
            obj.close()
        else:
            print(f"Object {type(obj)} is not closable.")

    safe_close(db)
    safe_close(text)
