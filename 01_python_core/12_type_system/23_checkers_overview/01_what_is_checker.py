"""
什么是类型检查器

对应文档: 17-type-system-checkers.md § 17.overview
"""

def add(a: int, b: int) -> int:
    return a + b

# 1. 类型检查器的作用 (静态阶段)
# 如果你在 IDE 中使用 mypy 或 pyright，
# 下面这行代码会被标记为红色错误：
# result = add("1", 2) 

# 2. Python 运行时的行为
# 尽管有类型注解，Python 运行时并不会阻止非法类型的传入。
if __name__ == '__main__':
    print("Runtime is starting...")
    
    # 下面这行代码在运行时可以执行成功 (字符串拼接)，但逻辑是错的
    # 类型检查器旨在防止此类代码进入生产环境
    wrong_res = add("Hello ", "World") 
    print(f"Result (wrong but executed): {wrong_res}")
    
    print("\n结论：类型检查器是开发者的助手，不影响 Python 的动态本质。")
