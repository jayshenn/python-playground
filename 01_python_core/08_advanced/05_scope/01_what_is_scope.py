"""
什么是作用域

对应文档: 10-advanced-features.md § 10.5.1
"""

# 作用域决定了变量名在何处有效

total = 0  # 全局作用域 (Global)

def multiply(a, b):
    # a, b, res 都在局部作用域 (Local)
    res = a * b
    return res

if __name__ == '__main__':
    print(f"访问全局变量: {total}")
    print(f"调用函数结果: {multiply(5, 5)}")
    
    # 尝试在外部访问局部变量会报错
    try:
        print(res)
    except NameError as e:
        print(f"访问失败: {e}")
