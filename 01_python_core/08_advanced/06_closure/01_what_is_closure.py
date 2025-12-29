"""
什么是闭包

对应文档: 10-advanced-features.md § 10.6.1
"""

# 形成闭包的 3 个条件：
# 1. 必须有嵌套函数
# 2. 内部函数引用了外部函数的变量
# 3. 外部函数返回内部函数

def outer(x):
    # x 是外部函数的局部变量
    def inner(y):
        # 内部函数引用了 x
        return x + y
    # 返回内部函数
    return inner

if __name__ == '__main__':
    # add_5 现在是一个闭包，它“记住了” x=5
    add_5 = outer(5)
    
    # 调用闭包
    print(f"5 + 10 = {add_5(10)}")
    print(f"5 + 20 = {add_5(20)}")
