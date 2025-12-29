"""
语法错误

对应文档: 08-exception-handling.md § 8.1.1
"""

# 语法错误是指代码不符合 Python 的语法规范
# 常见的如：缺少冒号、括号不匹配、拼写错误等

def main():
    # 下面这行代码会导致 SyntaxError: expected ':'
    # if True
    #     print("Missing colon")
    
    # 拼写错误导致的语法错误
    # prinnt("Hello") # 这实际上是 NameError (运行时异常)，不是 SyntaxError
    
    print("本文件演示语法错误。注意：存在语法错误的代码在编译阶段就会报错，程序无法开始执行。")

if __name__ == '__main__':
    main()
