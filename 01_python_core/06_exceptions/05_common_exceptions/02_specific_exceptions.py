"""
具体异常

对应文档: 08-exception-handling.md § 8.7.2
"""

# 下面列举了一些最常遇到的异常类型及其发生场景

def demonstrate_common_errors():
    # 1. AttributeError: 访问不存在的属性
    try:
        s = "hello"
        s.no_such_method()
    except AttributeError as e:
        print(f"AttributeError: {e}")

    # 2. KeyError: 访问字典中不存在的键
    try:
        d = {"name": "张三"}
        print(d["age"])
    except KeyError as e:
        print(f"KeyError: {e}")

    # 3. TypeError: 类型不匹配的操作
    try:
        "hello" + 123
    except TypeError as e:
        print(f"TypeError: {e}")

    # 4. NameError: 使用未定义的变量
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")

if __name__ == '__main__':
    demonstrate_common_errors()
