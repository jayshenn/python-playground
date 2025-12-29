"""
空行

对应文档: 01-python-basics.md § 1.7.3
"""

# 使用空行来分隔代码的逻辑部分，提高可读性。

# 顶级函数和类之间空两行
def function1():
    pass


def function2():
    pass


class MyClass:
    pass


# 类中的方法之间空一行
class Example:
    def method1(self):
        pass

    def method2(self):
        pass


# 函数内部可以使用空行分隔逻辑段
def complex_function():
    # 第一部分
    x = 10
    y = 20

    # 第二部分
    result = x + y
    return result

print("空行示例展示完毕")
