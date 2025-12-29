"""
全部导入 import

对应文档: 09-modules-and-packages.md § 9.3.1
"""

# 使用 import 模块名
# 访问时需要使用 模块名.成员名

import my_module

def main():
    # 访问变量
    print(f"版本: {my_module.version}")
    
    # 调用函数
    result = my_module.add(10, 20)
    print(f"加法结果: {result}")
    
    # 实例化类
    obj = my_module.MyClass()

if __name__ == '__main__':
    main()
