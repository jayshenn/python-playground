"""
类型参数语法 [T] (Python 3.12+)

对应文档: 14-type-system-basics.md § 14.new
"""

# 1. 泛型函数
# 语法: def func_name[T](param: T) -> T
def first[T](items: list[T]) -> T:
    """返回列表的第一个元素，并自动保留类型信息"""
    return items[0]

# 2. 多个类型参数
def pair[T, U](left: T, right: U) -> tuple[T, U]:
    return left, right

# 3. 泛型类
class Box[T]:
    """一个简单的泛型容器类"""
    def __init__(self, value: T):
        self.value = value
    
    def get(self) -> T:
        return self.value
    
    def set(self, value: T) -> None:
        self.value = value

# 4. 类型约束 (Upper bound)
# 限制 T 必须是 str 或其子类
def greet_all[T: str](names: list[T]) -> None:
    for name in names:
        print(f"Hello, {name.upper()}")

if __name__ == '__main__':
    # 测试泛型函数
    n = first([1, 2, 3]) # n 被推断为 int
    s = first(["a", "b"]) # s 被推断为 str
    print(f"Int: {n}, Str: {s}")
    
    # 测试泛型类
    int_box = Box(123)
    print(f"Box value: {int_box.get()}")
    
    # 测试类型约束
    greet_all(["alice", "bob"])
    # greet_all([1, 2]) # 这将导致类型检查错误
