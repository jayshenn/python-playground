"""
什么是装饰器

对应文档: 10-advanced-features.md § 10.7.1
"""

# 装饰器本质上是一个闭包，其参数是被装饰的函数

def my_decorator(func):
    def wrapper():
        print("--- 函数执行前：记录日志 ---")
        func()
        print("--- 函数执行后：清理现场 ---")
    return wrapper

# 使用 @ 语法糖
@my_decorator
def say_hello():
    print("Hello, Python!")

if __name__ == '__main__':
    # 调用 say_hello() 实际上是调用了 wrapper()
    say_hello()
