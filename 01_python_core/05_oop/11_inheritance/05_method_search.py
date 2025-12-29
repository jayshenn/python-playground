"""
方法搜索

对应文档: 07-oop-features.md § 7.2.5
"""

# MRO (Method Resolution Order) 是 Python 搜索方法的顺序
# 当调用一个方法时，Python 会按照 MRO 列表的顺序查找，找到即停止

class A:
    def test(self):
        print("A.test")

class B(A):
    def test(self):
        print("B.test")

class C(A):
    def test(self):
        print("C.test")

class D(B, C):
    pass

if __name__ == '__main__':
    d = D()
    d.test() # 调用哪一个？
    
    # 查看 MRO 顺序
    print("\n--- MRO 搜索顺序 ---")
    for cls in D.mro():
        print(cls)
        
    # 结果：D -> B -> C -> A -> object
    # 这种顺序算法被称为 C3 线性化算法
