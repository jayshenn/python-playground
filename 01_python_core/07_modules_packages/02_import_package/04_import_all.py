"""
局部导入 from import * 从包中导入模块

对应文档: 09-modules-and-packages.md § 9.7.4
"""

# 使用 * 导入包下的所有（在 __all__ 中声明的）模块

from my_package import *

if __name__ == '__main__':
    module_a.func_a()
    module_b.func_b()
