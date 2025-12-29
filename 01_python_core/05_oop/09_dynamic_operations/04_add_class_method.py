"""
动态给类添加方法

对应文档: 06-object-oriented-programming.md § 6.9.4
"""

class Cat:
    def __init__(self, name):
        self.name = name

def eat(self, food):
    print(f"{self.name} 正在吃 {food}")

if __name__ == '__main__':
    # 将外部函数绑定到类
    Cat.eat = eat
    
    c1 = Cat("咪咪")
    c2 = Cat("加菲")
    
    # 所有实例都可以直接调用
    c1.eat("小鱼干")
    c2.eat("猫罐头")
