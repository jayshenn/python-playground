"""
异常

对应文档: 08-exception-handling.md § 8.1.2
"""

# 异常是指程序运行过程中发生的错误
# 即使语法正确，代码也可能因为各种原因抛出异常

def demonstrate_exceptions():
    # 1. ZeroDivisionError: 除零异常
    try:
        1 / 0
    except ZeroDivisionError:
        print("捕获到异常: 除数不能为零")

    # 2. IndexError: 索引越界
    try:
        lst = [1, 2]
        print(lst[5])
    except IndexError:
        print("捕获到异常: 列表索引越界")

    # 3. FileNotFoundError: 文件未找到
    try:
        open("not_exist.txt", "r")
    except FileNotFoundError:
        print("捕获到异常: 找不到指定的文件")

if __name__ == '__main__':
    demonstrate_exceptions()
    print("\n程序即使遇到这些‘意外’，只要经过处理，依然可以继续运行。")
