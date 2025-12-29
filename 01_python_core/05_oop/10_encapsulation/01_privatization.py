"""
私有化

对应文档: 07-oop-features.md § 7.1.1
"""

# 在 Python 中，通过在名字前面加 __ (双下划线) 来实现私有化
# 私有成员在类外部不能直接访问

class Secret:
    def __init__(self):
        self.public_data = "这是公开的"
        self.__private_data = "这是私密的"

if __name__ == '__main__':
    s = Secret()
    print(s.public_data)
    
    # 尝试访问私有成员会报错
    try:
        print(s.__private_data)
    except AttributeError as e:
        print(f"无法直接访问私有数据: {e}")
        
    # 本质：Python 进行了名称修饰 (Name Mangling)
    # 实际上可以通过 _类名__私有名 访问，但不建议这样做
    print(f"‘破解’后的私有数据: {s._Secret__private_data}")
