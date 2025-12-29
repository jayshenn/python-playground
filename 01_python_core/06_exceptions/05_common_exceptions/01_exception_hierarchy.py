"""
异常基类

对应文档: 08-exception-handling.md § 8.7.1
"""

# Python 的异常也是类，它们之间存在继承关系
# BaseException (顶层基类)
#  ├── SystemExit (解释器请求退出)
#  ├── KeyboardInterrupt (用户中断，如 Ctrl+C)
#  └── Exception (大多数用户定义异常的基类)

def print_mro(cls):
    print(f"异常类 {cls.__name__} 的继承链: ")
    for base in cls.mro():
        print(f" -> {base.__name__}")
    print()

if __name__ == '__main__':
    # 演示几种异常的继承关系
    print_mro(ZeroDivisionError) # 继承自 ArithmeticError -> Exception
    print_mro(IndexError)        # 继承自 LookupError -> Exception
    print_mro(ValueError)        # 继承自 Exception
