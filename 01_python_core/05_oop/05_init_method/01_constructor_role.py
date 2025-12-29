"""
构造方法的作用

对应文档: 06-object-oriented-programming.md § 6.5.1
"""

# __init__ 方法是一个特殊的方法（魔法方法）
# 当创建类的一个新实例时，Python 会自动调用它。
# 它的主要作用是：初始化对象的属性。

class Car:
    def __init__(self):
        print("--- 执行 __init__ 方法 ---")
        # 为对象绑定初始属性
        self.wheels = 4
        self.engine_started = False

if __name__ == '__main__':
    print("准备实例化 car1...")
    car1 = Car()
    print(f"car1 轮子数量: {car1.wheels}")
    
    print("\n准备实例化 car2...")
    car2 = Car()
    print(f"car2 轮子数量: {car2.wheels}")
