"""
方法对比总结

对应文档: 06-object-oriented-programming.md § 6.8.6
"""

class MethodDemo:
    name = "类属性"

    def __init__(self, value):
        self.value = value

    # 1. 实例方法：有 self，能访实例属性 + 类属性
    def instance_m(self):
        print(f"实例方法: 实例值={self.value}, 类值={self.name}")

    # 2. 类方法：有 cls，只能访问类属性
    @classmethod
    def class_m(cls):
        print(f"类方法: 类值={cls.name}")
        # print(cls.value) # 报错：类无法访问实例属性

    # 3. 静态方法：无 self/cls，啥都不能直接访
    @staticmethod
    def static_m():
        print("静态方法: 谁都访不了")

if __name__ == '__main__':
    obj = MethodDemo("对象值")
    
    print("--- 各种方法的调用 ---")
    obj.instance_m()
    MethodDemo.class_m()
    MethodDemo.static_m()
    
    # 总结：
    # - 需要访问 self 的 -> 实例方法
    # - 只需访问 cls 的  -> 类方法
    # - 谁都不需要访的   -> 静态方法
