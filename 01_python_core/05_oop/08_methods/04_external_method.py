"""
在类外定义方法

对应文档: 06-object-oriented-programming.md § 6.8.4
"""

# Python 允许在类定义后，动态地将一个函数绑定到类或实例上

class User:
    def __init__(self, name):
        self.name = name

# 1. 定义一个外部函数，注意必须带一个 self 参数（如果要作为实例方法）
def external_run(self):
    print(f"{self.name} 正在跑步...")

if __name__ == '__main__':
    # 2. 将函数绑定到类
    User.run = external_run
    
    u = User("小明")
    u.run() # 现在 User 的所有实例都有 run 方法了
    
    # 3. 也可以直接绑定到具体对象（不推荐，除非有特殊需求）
    def external_jump(self):
         print(f"{self.name} 跳了一下")
    
    import types
    u.jump = types.MethodType(external_jump, u)
    u.jump()
