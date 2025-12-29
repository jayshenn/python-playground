"""
对象 (Object)

对应文档: 06-object-oriented-programming.md § 6.2.2
"""

# 对象是类的实例
# 类是抽象的模板，对象是具体的实体

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} is barking!")

if __name__ == '__main__':
    # 1. 实例化：创建对象
    dog1 = Dog('旺财', 3)
    dog2 = Dog('大黄', 5)
    
    # 2. 访问属性
    print(f"Dog 1 name: {dog1.name}")
    print(f"Dog 2 name: {dog2.name}")
    
    # 3. 调用方法
    dog1.bark()
    dog2.bark()
    
    # 4. 对象是独立的实例
    print(f"dog1 ID: {id(dog1)}")
    print(f"dog2 ID: {id(dog2)}")
    print(f"dog1 is dog2: {dog1 is dog2}") # False
    
    # 5. 类型检查
    print(f"dog1 type: {type(dog1)}")
    print(f"Is dog1 a Dog? {isinstance(dog1, Dog)}")
