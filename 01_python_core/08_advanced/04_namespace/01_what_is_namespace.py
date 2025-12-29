"""
什么是命名空间

对应文档: 10-advanced-features.md § 10.4.1
"""

# 命名空间本质上是一个字典，保存了变量名到对象的映射

x = 10  # 全局变量

def test():
    y = 20  # 局部变量
    print("--- 局部命名空间 (locals) ---")
    print(locals())

if __name__ == '__main__':
    print("--- 全局命名空间 (globals) ---")
    # 只打印我们定义的 x
    g = globals()
    print(f"x 的映射: x -> {g['x']}")
    
    test()
