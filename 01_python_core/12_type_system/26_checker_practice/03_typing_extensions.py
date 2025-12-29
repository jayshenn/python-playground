"""
使用 typing_extensions

对应文档: 17-type-system-checkers.md § 17.practice
"""

# 如果你的项目需要运行在 3.9，但你想使用 3.11 的 Self 或 3.12 的 override
# 那么你需要使用 typing_extensions 库。

try:
    # 示例：在 Python 3.11 以下版本使用 Self
    from typing_extensions import Self, override
except ImportError:
    # 也可以在运行时通过环境判断
    print("pip install typing_extensions to run this properly.")
    import sys
    sys.exit(0)

class Base:
    def process(self) -> Self:
        return self

class Derived(Base):
    @override # 告诉检查器这确实是在重写父类方法
    def process(self) -> Self:
        return super().process()

if __name__ == '__main__':
    d = Derived().process()
    print(f"Object: {d}")
