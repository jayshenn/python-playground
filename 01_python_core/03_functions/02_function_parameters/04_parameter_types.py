"""
函数有哪几种的参数形式

对应文档: 04-functions.md § 4.5.4
"""

# 1. 位置参数（必需参数）
def greet_pos(name, age):
    return f"{name} is {age} years old"

print(f"Positional: {greet_pos('Alice', 25)}")

# 2. 默认参数（关键字参数）
def greet_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(f"Default (using default): {greet_default('Alice')}")
print(f"Default (providing value): {greet_default('Bob', 'Hi')}")

# 3. 可变位置参数 (*args)
def sum_all(*numbers):
    """接受任意数量的位置参数"""
    return sum(numbers)

print(f"*args (3 args): {sum_all(1, 2, 3)}")
print(f"*args (5 args): {sum_all(1, 2, 3, 4, 5)}")

# 4. 可变关键字参数 (**kwargs)
def print_info(**kwargs):
    """接受任意数量的关键字参数"""
    return kwargs

print(f"**kwargs: {print_info(name='Alice', age=25, city='Beijing')}")

# 5. 混合使用参数
# 正确的顺序：位置参数 → 默认参数 → *args → **kwargs
def complex_function(a, b, c=3, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

print("\nComplex function call 1:")
complex_function(1, 2)

print("\nComplex function call 2:")
complex_function(1, 2, 4, 5, 6, x=10, y=20)
