"""
try except

对应文档: 08-exception-handling.md § 8.2.1
"""

def main():
    try:
        # 可能出错的代码
        num = int(input("请输入一个数字: "))
        print(f"你输入的数字是: {num}")
    except:
        # 发生异常时的补救措施
        print("出错了：请输入有效的整数！")

if __name__ == '__main__':
    main()
