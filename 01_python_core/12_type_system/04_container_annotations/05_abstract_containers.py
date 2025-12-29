"""
抽象容器类型

对应文档: 14-type-system-basics.md § 14.container
"""

from collections.abc import Sequence, Mapping, Iterable, Iterator

# 1. Sequence: 接受 list, tuple, str 等任何序列 (支持索引和长度)
def get_first_item(items: Sequence[str]) -> str:
    """接受任何字符串序列，并返回第一个元素"""
    return items[0]

# 2. Mapping: 接受 dict 等映射类型
def print_keys(data: Mapping[str, int]) -> None:
    """遍历任何映射并打印键"""
    for key in data:
        print(f"Key: {key}")

# 3. Iterable: 可迭代对象 (支持 for 循环)
def sum_values(items: Iterable[int]) -> int:
    """接受任何可迭代的整数对象"""
    return sum(items)

# 4. Iterator: 迭代器
def get_names_iterator(names: list[str]) -> Iterator[str]:
    return iter(names)

# ✅ 最佳实践示例
# 参数使用抽象类型，返回值使用具体类型
def double_numbers(nums: Sequence[int]) -> list[int]:
    """
    参数 nums 接受 list, tuple, range 等
    返回值明确为 list
    """
    return [x * 2 for x in nums]

if __name__ == '__main__':
    # 测试 Sequence
    print(get_first_item(["Alice", "Bob"]))  # list
    print(get_first_item(("Charlie", "David"))) # tuple
    
    # 测试 Mapping
    print_keys({"a": 1, "b": 2})
    
    # 测试 Iterable
    print(f"Sum list: {sum_values([1, 2, 3])}")
    print(f"Sum range: {sum_values(range(10))}")
    
    # 测试最佳实践函数
    result = double_numbers(range(5))
    print(f"Doubled range: {result}")
