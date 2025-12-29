"""
self 作为定义传参

对应文档: 06-object-oriented-programming.md § 6.6.1
"""

# self 代表当前对象本身
# 1. 它是实例方法的第一个位置参数
# 2. 调用方法时，Python 解释器会自动把调用者（对象）传给 self

class Demo:
    def check_self(self):
        print(f"self 的地址: {id(self)}")

if __name__ == '__main__':
    obj1 = Demo()
    print(f"obj1 的地址: {id(obj1)}")
    obj1.check_self()  # 结果应该与 obj1 的地址一致
    
    print("-" * 20)
    
    obj2 = Demo()
    print(f"obj2 的地址: {id(obj2)}")
    obj2.check_self()  # 结果应该与 obj2 的地址一致
