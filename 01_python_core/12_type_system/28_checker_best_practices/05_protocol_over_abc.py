"""
Protocol 优于抽象基类 (ABC)

对应文档: 17-type-system-checkers.md § 17.best
"""

from typing import Protocol

# 1. 使用 Protocol (结构化子类型 - 推荐)
class Reader(Protocol):
    def read(self) -> str: ...

# 任何具有 read 方法的类都自动满足 Reader
class File:
    def read(self) -> str: return "file data"

class NetworkStream:
    def read(self) -> str: return "stream data"

def process_data(source: Reader):
    print(f"Reading from source: {source.read()}")

# 2. 对比：使用 ABC (名义子类型 - 较死板)
# 如果使用 ABC，File 和 NetworkStream 必须显式继承它。
# 这在处理第三方提供的类时非常困难。

if __name__ == '__main__':
    # Protocol 无需继承即可工作，极大地降低了代码间的耦合。
    process_data(File())
    process_data(NetworkStream())
