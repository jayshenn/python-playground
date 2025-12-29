"""
列表注解

对应文档: 14-type-system-basics.md § 14.container
"""

# 1. 简单列表
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob"]

# 2. 嵌套列表 (矩阵)
matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6]
]

# 3. 混合类型 (使用 Union / |)
mixed: list[int | str] = [1, "two", 3, "four"]

# 4. 函数返回列表
def get_even_numbers(limit: int) -> list[int]:
    """返回一个包含偶数的列表"""
    return [x for x in range(limit) if x % 2 == 0]

def process_matrix(m: list[list[int]]) -> list[int]:
    """将矩阵扁平化为列表"""
    return [item for row in m for item in row]

if __name__ == '__main__':
    print(f"Numbers: {numbers}")
    print(f"Even numbers to 10: {get_even_numbers(10)}")
    
    m = [[1, 2], [3, 4]]
    print(f"Flattened matrix: {process_matrix(m)}")
