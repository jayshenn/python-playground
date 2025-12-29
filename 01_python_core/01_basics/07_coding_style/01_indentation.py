"""
缩进

对应文档: 01-python-basics.md § 1.7.1
"""

# Python 使用缩进来表示代码块，而不是使用大括号。
# 推荐使用 4 个空格作为缩进。

def example():
    x = 10
    if x > 0:
        print("正数 - 缩进正确")
        if True:
            print("嵌套缩进 - 缩进正确")

# 错误的缩进会导致语法错误
# if True:
# print("这是错误的")  # IndentationError

if __name__ == "__main__":
    example()
