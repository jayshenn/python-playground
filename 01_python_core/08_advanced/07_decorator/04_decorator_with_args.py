"""
带参数的装饰器

对应文档: 10-advanced-features.md § 10.7.4
"""

# 带参数的装饰器实际上是一个函数，它返回一个真正的装饰器

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    greet("World")
