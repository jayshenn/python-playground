"""
property

对应文档: 07-oop-features.md § 7.1.4
"""

# @property 可以将一个方法变成属性调用的形式，常用于 getter 和 setter

class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        """Getter: 获取年龄"""
        return self.__age

    @age.setter
    def age(self, value):
        """Setter: 设置年龄并增加逻辑校验"""
        if 0 <= value <= 150:
            self.__age = value
            print(f"年龄修改成功: {value}")
        else:
            print("错误：非法年龄值！")

if __name__ == '__main__':
    p = Person(20)
    
    # 像访问属性一样使用方法
    print(f"当前年龄: {p.age}")
    
    # 修改年龄（会自动触发 setter 方法）
    p.age = 25
    p.age = -1  # 触发校验
    
    print(f"最终年龄: {p.age}")
