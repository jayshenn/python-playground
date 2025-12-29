"""
动态给对象添加方法

对应文档: 06-object-oriented-programming.md § 6.9.3
"""

import types

class Dog:
    def __init__(self, name):
        self.name = name

def run(self):
    print(f"{self.name} 正在跑...")

if __name__ == '__main__':
    d1 = Dog("旺财")
    d2 = Dog("大黄")
    
    # 错误做法：直接赋值（这会变成一个普通函数调用，不会自动传 self）
    # d1.run = run 
    
    # 正确做法：使用 types.MethodType 进行绑定
    d1.run = types.MethodType(run, d1)
    
    d1.run()
    
    # d2 并没有被绑定该方法
    try:
        d2.run()
    except AttributeError as e:
        print(f"d2 没有跑的方法: {e}")
