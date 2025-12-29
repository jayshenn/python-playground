"""
nonlocal 关键字

对应文档: 04-functions.md § 4.9.3
"""

# 使用 nonlocal 在嵌套函数中修改外层函数的变量。

def outer():
    x = 10

    def inner():
        nonlocal x  # 声明使用外层函数的变量
        x += 5
        print(f"Inner: x = {x}")

    inner()
    print(f"Outer: x = {x}")

print("Testing nonlocal:")
outer()

# 实际应用：闭包计数器
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

print("\nClosure counter:")
counter = make_counter()
print(f"Count: {counter()}")
print(f"Count: {counter()}")
print(f"Count: {counter()}")
