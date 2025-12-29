"""
__all__

对应文档: 09-modules-and-packages.md § 9.3.5
"""

# __all__ 变量是一个字符串列表，它定义了当使用 from module import * 时
# 哪些成员会被导入。它是一种模块的“公开接口”声明。

# 示例：假设我们在 my_module.py 中写了：
# __all__ = ['add', 'info']

from my_module import *

if __name__ == '__main__':
    # 这些是在 __all__ 中的
    info()
    
    # 这些是不在 __all__ 中的（即便它们在模块里是公开定义的）
    try:
        c = MyClass()
    except NameError:
        print("MyClass 未被导入，因为它不在 my_module 的 __all__ 列表中")
        
    # 注意：直接 import my_module 或 from my_module import MyClass 依然有效
    # __all__ 仅限制 * 导入。
