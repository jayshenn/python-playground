"""
局部导入包下模块的成员 from import

对应文档: 09-modules-and-packages.md § 9.7.3
"""

# 方式 3: 直接从包内的模块导入具体的函数或类
from my_package.module_a import func_a

if __name__ == '__main__':
    # 像本地函数一样直接调用
    func_a()
