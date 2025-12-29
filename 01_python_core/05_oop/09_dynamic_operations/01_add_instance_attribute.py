"""
动态给对象添加属性

对应文档: 06-object-oriented-programming.md § 6.9.1
"""

class Person:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    p1 = Person("张三")
    p2 = Person("李四")
    
    # 动态添加属性，仅对 p1 生效
    p1.age = 18
    print(f"{p1.name} 的年龄: {p1.age}")
    
    # p2 并没有 age 属性
    try:
        print(f"{p2.name} 的年龄: {p2.age}")
    except AttributeError as e:
        print(f"p2 访问失败: {e}")
