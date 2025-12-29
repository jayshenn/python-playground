"""
注意事项

对应文档: 06-object-oriented-programming.md § 6.5.3
"""

class Demo:
    def __init__(self, value):
        self.value = value
        
        # 1. __init__ 必须返回 None (通常不需要显式写 return)
        # 如果返回非 None 值，实例化时会抛出 TypeError
        # return "Error"  # 这样写会报错
        
    def show(self):
        print(f"Value is {self.value}")

if __name__ == '__main__':
    # 2. 如果 __init__ 定义了除了 self 以外的参数，实例化时必须提供这些参数
    try:
        d = Demo() # 缺少参数
    except TypeError as e:
        print(f"实例化失败: {e}")
        
    # 3. 可以在构造方法中设置默认值
    class DefaultDemo:
        def __init__(self, name="Guest"):
            self.name = name
            
    d1 = DefaultDemo()
    d2 = DefaultDemo("Admin")
    print(f"d1: {d1.name}, d2: {d2.name}")

    # 4. 构造方法名必须是确定的 __init__ (双下划线)
