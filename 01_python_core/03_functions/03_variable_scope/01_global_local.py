"""
全局变量和局部变量

对应文档: 04-functions.md § 4.9.1
"""

# 全局变量
global_var = 100

def func():
    # 局部变量
    local_var = 50
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")

print("Calling func:")
func()

print(f"\nOutside function - global_var: {global_var}")
# print(local_var)  # NameError: 局部变量在函数外不可见

# 变量查找顺序：LEGB
# L (Local): 局部作用域
# E (Enclosing): 嵌套函数的外层函数作用域
# G (Global): 全局作用域
# B (Built-in): 内置作用域

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"Inner: x = {x}")  # local

    inner()
    print(f"Outer: x = {x}")  # enclosing

print("\nScope resolution (LEGB):")
outer()
print(f"Global: x = {x}")  # global
