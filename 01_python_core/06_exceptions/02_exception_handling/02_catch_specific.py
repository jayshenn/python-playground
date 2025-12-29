"""
捕获指定类型的异常以及获取异常描述信息

对应文档: 08-exception-handling.md § 8.2.2
"""

def main():
    try:
        a = int(input("被除数: "))
        b = int(input("除数: "))
        result = a / b
        print(f"结果: {result}")
    except ValueError as e:
        # 捕获输入非数字的异常
        print(f"输入错误: {e}")
    except ZeroDivisionError as e:
        # 捕获除数为零的异常
        print(f"运算错误: {e}")
    except Exception as e:
        # 捕获其他所有未预见异常
        print(f"未知错误: {e}")

if __name__ == '__main__':
    main()
