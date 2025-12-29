"""
基本语法

对应文档: 06-object-oriented-programming.md § 6.3.1
"""

# 使用 class 关键字定义类
# 语法结构：
# class 类名:
#     类体 (属性和方法)

class EmptyClass:
    """这是一个最简单的空类"""
    pass

if __name__ == '__main__':
    # 实例化
    obj = EmptyClass()
    print(f"创建的对象: {obj}")
    print(f"对象所属类: {type(obj)}")
