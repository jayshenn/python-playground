"""
类属性

对应文档: 06-object-oriented-programming.md § 6.7.1
"""

# 类属性是属于类的，所有对象共享同一个类属性

class Bird:
    # 类属性：定义在类中，方法外
    wings = 2
    count = 0  # 记录一共创建了多少只鸟

    def __init__(self, name):
        self.name = name
        # 修改类属性通常建议通过 类名.属性名
        Bird.count += 1

if __name__ == '__main__':
    # 1. 访问类属性（通过类名或实例）
    print(f"鸟类都有 {Bird.wings} 只翅膀")
    
    b1 = Bird("麻雀")
    print(f"{b1.name} 有 {b1.wings} 只翅膀")
    
    b2 = Bird("大雁")
    print(f"当前小鸟总数: {Bird.count}")
    
    # 2. 修改类属性（全局生效）
    Bird.wings = 3
    print(f"变异后，b1 的翅膀数: {b1.wings}")
