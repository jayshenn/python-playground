"""
Self 类型 (Python 3.11+)

对应文档: 15-type-system-stdlib.md § 15.advanced
"""

from typing import Self

class Builder:
    """建造者模式示例"""
    def __init__(self):
        self._data: dict = {}

    def set_name(self, name: str) -> Self:
        """返回 self，类型注解为 Self"""
        self._data["name"] = name
        return self

    def set_value(self, value: int) -> Self:
        self._data["value"] = value
        return self

class ExtendedBuilder(Builder):
    """
    继承 Builder。
    由于父类使用了 Self，子类调用 set_name 返回的类型将被正确推断为 ExtendedBuilder
    """
    def set_extra(self, extra: str) -> Self:
        self._data["extra"] = extra
        return self

if __name__ == '__main__':
    # 链式调用
    b = Builder().set_name("base").set_value(10)
    print(f"Builder data: {b._data}")
    
    # 继承中的链式调用
    eb = ExtendedBuilder().set_name("ext").set_extra("special")
    print(f"ExtendedBuilder data: {eb._data}")
    # 类型检查器知道 eb 有 set_extra 方法
