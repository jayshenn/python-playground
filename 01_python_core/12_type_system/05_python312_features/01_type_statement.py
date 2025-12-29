"""
新的 type 语句 (Python 3.12+)

对应文档: 14-type-system-basics.md § 14.new
"""

# 1. 基本用法: 取代 TypeAlias
type UserId = int
type UserName = str
type Email = str

def create_user(uid: UserId, name: UserName, email: Email) -> bool:
    print(f"Creating user {name} with ID {uid}")
    return True

# 2. 优势: 自动处理延迟引用 (不需要字符串引号)
# 可以轻松定义递归类型
type JsonValue = (
    str | int | float | bool | None | 
    list['JsonValue'] | 
    dict[str, 'JsonValue']
)

# 3. 优势: 支持泛型 (简洁语法)
type Result[T] = tuple[bool, T | None]

def find_item[T](items: list[T], target: T) -> Result[T]:
    if target in items:
        return True, target
    return False, None

if __name__ == '__main__':
    # 测试基本别名
    create_user(1001, "Alice", "alice@example.com")
    
    # 测试泛型别名
    success, val = find_item([1, 2, 3], 2)
    print(f"Found: {success}, Value: {val}")
    
    # 运行时查看类型
    print(f"Type of UserId: {type(UserId)}") # <class 'typing.TypeAliasType'>
