"""
函数装饰器 (通用写法)

对应文档: 10-advanced-features.md § 10.7.2
"""

import time

# 一个通用的装饰器模板，支持任意参数和返回值
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # 执行原函数并获取返回值
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"函数 {func.__name__} 执行耗时: {end_time - start_time:.4f}s")
        
        return result
    return wrapper

@timer
def heavy_computation(n):
    sum_val = 0
    for i in range(n):
        sum_val += i
    return sum_val

if __name__ == '__main__':
    res = heavy_computation(1000000)
    print(f"计算结果: {res}")
