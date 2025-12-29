"""
查看闭包中的值

对应文档: 10-advanced-features.md § 10.6.3
"""

def outer(a, b):
    def inner():
        print(a + b)
    return inner

if __name__ == '__main__':
    f = outer(10, 20)
    
    # 1. 检查一个函数是否是闭包 (如果有 __closure__ 属性且不为 None)
    print(f"是否为闭包: {f.__closure__ is not None}")
    
    # 2. 查看闭包捕获的变量 (cell 对象)
    if f.__closure__:
        print(f"捕获变量的数量: {len(f.__closure__)}")
        for i, cell in enumerate(f.__closure__):
            print(f"变量 {i} 的值: {cell.cell_contents}")
