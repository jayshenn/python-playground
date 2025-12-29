"""
避免过度类型注解

对应文档: 17-type-system-checkers.md § 17.best
"""

# ❌ 过度注解：对于显而易见的局部变量，重复标注类型
def bad_example():
    x: int = 10
    names: list[str] = ["Alice", "Bob"]
    for name in names:
        upper_name: str = name.upper()
        print(upper_name)

# ✅ 适度注解：信任类型推断
def good_example():
    # 检查器能轻易推断出 x 是 int
    x = 10 
    # names 显然是 list[str]
    names = ["Alice", "Bob"] 
    for name in names:
        # upper_name 被推断为 str
        upper_name = name.upper()
        print(upper_name)

if __name__ == '__main__':
    # 原则：函数签名（参数、返回）必须注解；内部局部变量尽量依靠推断。
    good_example()
