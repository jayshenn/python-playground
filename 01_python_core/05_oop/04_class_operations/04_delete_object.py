"""
删除对象

对应文档: 06-object-oriented-programming.md § 6.4.4
"""

class TempObject:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        """析构方法，在对象被销毁时调用"""
        print(f"对象 {self.name} 已被销毁")

if __name__ == '__main__':
    obj = TempObject("测试对象")
    print(f"创建了对象: {obj.name}")
    
    # 1. 使用 del 删除对象引用
    print("准备手动删除对象...")
    del obj
    
    # 2. 删除后尝试访问会报错 (NameError)
    try:
        print(obj.name)
    except NameError:
        print("访问失败：对象引用已不存在")

    print("程序结束")
