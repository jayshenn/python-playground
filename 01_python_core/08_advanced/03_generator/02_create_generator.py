"""
创建生成器

对应文档: 10-advanced-features.md § 10.3.2
"""

# 使用 yield 关键字定义生成器函数

def fibonacci(n):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a  # 产出一个值并暂停执行
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    # 调用函数返回的是一个生成器对象，代码并不会立即执行
    f = fibonacci(5)
    print(f"类型: {type(f)}")
    
    print("开始获取数据:")
    for num in f:
        print(num)
