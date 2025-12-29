"""
局部导入 from import *

对应文档: 09-modules-and-packages.md § 9.3.3
"""

# 使用 from 模块名 import * 导入该模块中允许导出的所有成员
# 注意：这种方式不推荐使用，因为容易导致命名空间污染

from my_module import *

def main():
    # 由于 my_module 中定义了 __all__ = ['add', 'info']
    # 只有 add 和 info 会被导入
    
    info()
    print(add(100, 200))
    
    # version 不在 __all__ 中，会导致 NameError
    try:
        print(version)
    except NameError as e:
        print(f"导入失败 (不在 __all__ 中): {e}")

if __name__ == '__main__':
    main()
