"""
局部导入模块下的成员 from import

对应文档: 09-modules-and-packages.md § 9.7.2
"""

# 方式 2: 从包中导入具体的模块
from my_package import module_b

if __name__ == '__main__':
    # 只需要使用模块名
    module_b.func_b()
