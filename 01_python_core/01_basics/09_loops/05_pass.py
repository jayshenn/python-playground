"""
pass

对应文档: 02-control-flow.md § 2.3.5
"""

# pass 是一个空语句，不执行任何操作，通常用作占位符。

# 占位符：稍后实现的函数
def future_function():
    pass  # TODO: 稍后实现

# 空的类定义
class EmptyClass:
    pass

# 条件语句中的占位符
x = 10
if x > 5:
    pass  # 暂时不做任何处理
else:
    print("x <= 5")

# 循环中的占位符
print("Loop with pass for 2:")
for i in range(5):
    if i == 2:
        pass  # 偶数暂不处理
    else:
        print(i, end=" ")
print()

# 异常处理中使用
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # 忽略除零错误
    print("Caught ZeroDivisionError, but passing.")
