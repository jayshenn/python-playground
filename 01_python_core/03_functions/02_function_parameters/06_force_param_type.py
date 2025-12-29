"""
强制使用位置参数或关键字参数

对应文档: 04-functions.md § 4.5.6
"""

# Python 3.8+ 支持强制参数传递方式。

# 强制位置参数（/ 之前的参数）
def func_pos_only(a, b, /, c):
    return a + b + c

print(f"Positional only (mixed call): {func_pos_only(1, 2, c=3)}")
# func_pos_only(a=1, b=2, c=3)  # TypeError: a, b 必须用位置传递

# 强制关键字参数（* 之后的参数）
def func_kw_only(a, *, b, c):
    return a + b + c

print(f"Keyword only: {func_kw_only(1, b=2, c=3)}")
# func_kw_only(1, 2, 3)  # TypeError: b, c 必须用关键字传递

# 混合使用
def func_mixed(a, b, /, c, *, d, e):
    """
    a, b: 仅限位置参数
    c: 位置或关键字参数
    d, e: 仅限关键字参数
    """
    return a + b + c + d + e

print(f"Mixed constraints: {func_mixed(1, 2, 3, d=4, e=5)}")
