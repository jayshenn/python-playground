"""
多层装饰器

对应文档: 10-advanced-features.md § 10.7.3
"""

def decorator_a(func):
    print("--- 装饰器 A 被加载 ---")
    def wrapper():
        print("A-前置")
        func()
        print("A-后置")
    return wrapper

def decorator_b(func):
    print("--- 装饰器 B 被加载 ---")
    def wrapper():
        print("B-前置")
        func()
        print("B-后置")
    return wrapper

@decorator_a
@decorator_b
def test():
    print("--- 目标函数执行 ---")

if __name__ == '__main__':
    # 装饰顺序：从下往上 (B 先装饰，A 后装饰)
    # 执行顺序：从上往下 (A 先拦截，B 后拦截)
    test()
