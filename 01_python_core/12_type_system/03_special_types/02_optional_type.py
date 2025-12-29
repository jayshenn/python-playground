"""
Optional 类型：可选值 (可能为 None)

对应文档: 14-type-system-basics.md § 14.special
"""

from typing import Optional

# 1. 现代推荐写法 (Python 3.10+)
# X | None 等价于 Optional[X]
def find_user(user_id: int) -> str | None:
    """如果找到用户返回姓名，否则返回 None"""
    if user_id > 0:
        return f"User_{user_id}"
    return None

# 2. 传统写法 (使用 typing.Optional)
def find_user_legacy(user_id: int) -> Optional[str]:
    """使用 Optional[str] 的传统写法"""
    if user_id > 0:
        return f"User_{user_id}"
    return None

# 3. 类型检查中的判空处理
def process_user(user_id: int) -> None:
    name = find_user(user_id)
    
    # 类型检查器（如 mypy/pyright）会提示 name 可能为 None
    # print(name.upper())  # 如果直接调用，检查器会报错
    
    if name is not None:
        # 在这个作用域内，类型检查器知道 name 是 str
        print(f"Found user: {name.upper()}")
    else:
        print("User not found")

# 4. 易混淆点：Optional vs 可选参数
# Optional 表示类型，而不是参数是否可以不传
# 传参的可选性通过默认值实现
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

if __name__ == '__main__':
    process_user(123)
    process_user(-1)
    
    print(greet())
    print(greet("Alice"))
