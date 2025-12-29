"""
Union 类型：多种可能的类型

对应文档: 14-type-system-basics.md § 14.special
"""

from typing import Union

# 1. 使用 | 操作符 (Python 3.10+ 推荐)
def process_id(user_id: int | str) -> str:
    """接受 int 或 str 类型的 ID，统一返回字符串格式"""
    return str(user_id)

# 2. 多个类型组合
def format_value(value: int | float | str) -> str:
    """支持多种数值和字符串类型的格式化"""
    return f"Value: {value}"

# 3. 在类型别名中使用
type NumberOrString = int | str

def print_id(uid: NumberOrString) -> None:
    print(f"ID: {uid}")

# 4. 旧版本语法 (Python 3.9 及更早)
def process_id_legacy(user_id: Union[int, str]) -> str:
    """使用 typing.Union 的传统写法"""
    return str(user_id)

if __name__ == '__main__':
    # 测试 | 语法
    print(process_id(101))      # 输出: 101
    print(process_id("A102"))   # 输出: A102
    
    # 测试别名
    val: NumberOrString = 42
    print_id(val)
    val = "forty-two"
    print_id(val)
