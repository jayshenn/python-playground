"""
单继承

对应文档: 07-oop-features.md § 7.2.1
"""

# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} 正在吃东西...")

# 子类（派生类）
class Dog(Animal):
    def bark(self):
        print(f"{self.name} 正在汪汪叫...")

if __name__ == '__main__':
    # 子类对象可以使用父类的方法和属性
    my_dog = Dog("旺财")
    my_dog.eat()
    my_dog.bark()
    
    # 检查继承关系
    print(f"Dog 是 Animal 的子类吗: {issubclass(Dog, Animal)}")
