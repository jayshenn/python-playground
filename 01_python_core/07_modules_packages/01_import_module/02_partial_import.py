"""
局部导入 from import

对应文档: 09-modules-and-packages.md § 9.3.2
"""

# 使用 from 模块名 import 成员名
# 访问时直接使用成员名，不需要模块名作前缀

from my_module import add, info

def main():
    # 直接调用函数
    print(f"1 + 2 = {add(1, 2)}")
    info()
    
    # 也可以使用 as 起别名防止冲突
    from my_module import version as v
    print(f"起别名后的版本号: {v}")

if __name__ == '__main__':
    main()
