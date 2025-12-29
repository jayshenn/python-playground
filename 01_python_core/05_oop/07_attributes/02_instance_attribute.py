"""
实例属性

对应文档: 06-object-oriented-programming.md § 6.7.2
"""

# 实例属性是属于具体对象的，每个对象各有一份，互不影响

class Laptop:
    def __init__(self, brand, memory):
        # 实例属性
        self.brand = brand
        self.memory = memory

if __name__ == '__main__':
    pc1 = Laptop("Dell", "16G")
    pc2 = Laptop("MacBook", "32G")
    
    # 修改 pc1 的属性，不会影响 pc2
    pc1.memory = "64G"
    
    print(f"pc1 品牌: {pc1.brand}, 内存: {pc1.memory}")
    print(f"pc2 品牌: {pc2.brand}, 内存: {pc2.memory}")
    
    # 尝试通过类名访问实例属性会报错
    try:
        print(Laptop.brand)
    except AttributeError as e:
        print(f"报错: {e}")
