"""
Any 类型：不受约束

对应文档: 14-type-system-basics.md § 14.special
"""

from typing import Any

# 1. Any 表示任何类型都可以接受
def process_data(data: Any) -> Any:
    """处理未知类型或极度灵活的数据"""
    # Any 类型会禁用静态类型检查
    return data

# 2. 滥用 Any 的风险
def risky_function(value: Any) -> None:
    # 即使 value 没有 upper 方法，类型检查器也不会在这里报错
    # 错误将推迟到运行时发生
    try:
        print(value.upper())
    except AttributeError as e:
        print(f"Runtime Error: {e}")

# 3. Any 与 object 的区别
# object 是所有类型的基类，但如果你注解为 object，
# 你不能在它上面调用任何非 object 的方法。
# Any 则允许你调用任何方法。

def use_object(item: object) -> None:
    # print(item.upper()) # 类型检查器会在这里直接报错
    pass

if __name__ == '__main__':
    # Any 可以被赋予任何值
    x: Any = 123
    x = "hello"
    x = [1, 2, 3]
    
    process_data(x)
    
    risky_function(123)  # 运行时报错，但静态检查通过
