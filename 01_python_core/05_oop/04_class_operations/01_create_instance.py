"""
创建对象（实例化）

对应文档: 06-object-oriented-programming.md § 6.4.1
"""

class Person:
    pass

if __name__ == '__main__':
    # 1. 实例化：类名 + ()
    p1 = Person()
    p2 = Person()
    
    # 2. 每个实例都是独立的对象，拥有不同的内存地址
    print(f"p1 的内存地址: {id(p1)}")
    print(f"p2 的内存地址: {id(p2)}")
    
    # 3. 验证类型
    print(f"p1 是否为 Person 的实例: {isinstance(p1, Person)}")
