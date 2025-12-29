"""
实例方法

对应文档: 06-object-oriented-programming.md § 6.8.1
"""

# 实例方法：属于实例对象，第一个参数必须是 self

class Person:
    def __init__(self, name):
        self.name = name
    
    # 实例方法：操作实例属性
    def say_hello(self):
        print(f"你好，我是 {self.name}")

if __name__ == '__main__':
    p = Person("小明")
    p.say_hello()
    
    # 本质上，p.say_hello() 等同于 Person.say_hello(p)
    Person.say_hello(p)
