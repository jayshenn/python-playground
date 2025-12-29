"""
常见问题：循环导入

对应文档: 17-type-system-checkers.md § 17.practice
"""

from typing import TYPE_CHECKING

# 1. 场景：Model A 需要 Model B 的类型，Model B 也需要 Model A
# 如果直接 import 会导致运行时死循环。

if TYPE_CHECKING:
    # 2. TYPE_CHECKING 在运行时为 False，在类型检查时为 True。
    # 这里的导入仅用于类型提示。
    from .other_module import Manager

class Employee:
    # 3. 在注解中使用字符串引用 'Manager'，而不是直接使用 Manager。
    # 这避免了在运行时解析该类。
    def __init__(self, name: str, manager: 'Manager'):
        self.name = name
        self.manager = manager

if __name__ == '__main__':
    print("循环导入是大型项目中最常见的问题。")
    print("解决方案：TYPE_CHECKING 保护导入 + 字符串引用类型。")
