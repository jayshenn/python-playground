"""
简单的类定义

对应文档: 06-object-oriented-programming.md § 6.3.3
"""

class Cat:
    # 属性 (在方法外定义的通常是类属性，在 __init__ 中定义的是实例属性)
    species = "猫科动物"

    # 方法
    def eat(self):
        print("猫正在吃鱼...")

    def sleep(self):
        print("猫正在睡觉...")

if __name__ == '__main__':
    # 创建对象
    my_cat = Cat()
    
    # 访问属性
    print(f"这只猫属于: {my_cat.species}")
    
    # 调用方法
    my_cat.eat()
    my_cat.sleep()
