"""
全部导入 import

对应文档: 09-modules-and-packages.md § 9.7.1
"""

# 方式 1: 导入包下的模块
import my_package.module_a

if __name__ == '__main__':
    # 访问时需要写全路径
    my_package.module_a.func_a()
