"""
方法重写和重载

对应文档: 07-oop-features.md § 7.2.4
"""

# 1. 方法重写 (Override)
# 子类定义了与父类同名的方法，执行时会调用子类的版本

class Father:
    def hobby(self):
        print("父亲喜欢钓鱼")

class Son(Father):
    def hobby(self):
        print("儿子喜欢打篮球") # 重写了父类的方法

# 2. 方法重载 (Overload)
# 注意：Python 并不像 Java/C++ 那样支持原生语法层面的同名不同参重载
# 在 Python 中，如果定义同名函数，后面的会覆盖前面的

class Demo:
    def test(self):
        print("测试1")
        
    def test(self, a): # 这会覆盖上面的 test()
        print(f"测试2: {a}")

if __name__ == '__main__':
    s = Son()
    s.hobby() # 输出子类逻辑
    
    d = Demo()
    d.test(10)
    # d.test() # 报错，因为无参版本已被覆盖
