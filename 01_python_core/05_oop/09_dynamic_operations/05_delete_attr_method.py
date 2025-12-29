"""
动态删除属性与方法

对应文档: 06-object-oriented-programming.md § 6.9.5
"""

class Demo:
    def __init__(self):
        self.a = 1
        self.b = 2

if __name__ == '__main__':
    d = Demo()
    print(f"原始属性: a={d.a}, b={d.b}")
    
    # 1. 使用 del 关键字
    del d.a
    
    # 2. 使用 delattr() 函数
    delattr(d, 'b')
    
    try:
        print(d.a)
    except AttributeError:
        print("属性 a 已被删除")
        
    # 也可以动态删除类的方法
    # del Demo.method_name
