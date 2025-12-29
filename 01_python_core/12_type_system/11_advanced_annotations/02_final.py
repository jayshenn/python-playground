"""
Final：不可变类型

对应文档: 15-type-system-stdlib.md § 15.advanced
"""

from typing import Final

# 1. 模块级常量
MAX_CONNECTIONS: Final = 100

# 2. 类属性常量
class Config:
    DEFAULT_TIMEOUT: Final[int] = 30
    
    def __init__(self):
        # 3. 实例级常量
        self.version: Final[str] = "1.0.0"

# 4. 类型检查器会阻止对 Final 变量的二次赋值
# MAX_CONNECTIONS = 200 # 警告

# 5. Final 还可以用于装饰类或方法，防止被重写 (仅类型检查层面)
from typing import final

@final
class Base:
    pass

# class Sub(Base): # 警告：不能继承被标记为 @final 的类
#     pass

class Processor:
    @final
    def run(self) -> None:
        print("Running...")

class MyProcessor(Processor):
    # def run(self): # 警告：不能重写被标记为 @final 的方法
    #     pass
    pass

if __name__ == '__main__':
    print(f"Max: {MAX_CONNECTIONS}")
    cfg = Config()
    print(f"Timeout: {cfg.DEFAULT_TIMEOUT}")
