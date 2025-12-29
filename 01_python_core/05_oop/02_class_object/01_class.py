"""
类 (Class)

对应文档: 06-object-oriented-programming.md § 6.2.1
"""

# 类是对象的模板或蓝图
# 它定义了对象应该具有的属性（数据）和方法（行为）

class Dog:
    """这是一个简单的狗类"""
    
    # 初始化方法（构造函数）
    def __init__(self, name, age):
        self.name = name  # 属性
        self.age = age
        
    # 方法
    def bark(self):
        print(f"{self.name} says Woof!")
        
    def get_info(self):
        return f"Dog(Name: {self.name}, Age: {self.age})"

if __name__ == '__main__':
    # 打印类本身的信息
    print(f"Class: {Dog}")
    print(f"Docstring: {Dog.__doc__}")
