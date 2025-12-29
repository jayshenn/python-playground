"""
类型系统的价值

对应文档: 14-type-system-basics.md § 14.why
"""

# 类型提示 (Type Hints) 不会影响 Python 程序的运行性能
# 它的核心价值在于：人、工具

def get_full_name(first_name: str, last_name: str) -> str:
    """
    带有类型注解的函数：
    1. 读代码的人一眼就能看出参数要求
    2. IDE 可以提供精准的补全提示
    3. 类型检查器 (如 mypy) 可以发现潜在错误
    """
    return f"{first_name.title()} {last_name.title()}"

if __name__ == '__main__':
    name = get_full_name("guido", "van rossum")
    print(f"Full Name: {name}")
