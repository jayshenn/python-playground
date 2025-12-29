"""
调用方法

对应文档: 06-object-oriented-programming.md § 6.4.3
"""

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    calc = Calculator()
    
    # 1. 调用方法并接收返回值
    sum_result = calc.add(10, 20)
    mul_result = calc.multiply(5, 6)
    
    print(f"加法结果: {sum_result}")
    print(f"乘法结果: {mul_result}")
    
    # 2. 注意：调用方法时必须带括号，即使没有参数
