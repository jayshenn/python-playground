"""
集合类型

对应文档: 14-type-system-basics.md § 14.basic
"""

# 在 Python 3.9+ 中，可以直接使用内置的 list, dict, tuple 等进行泛型注解

def main():
    # 列表注解
    names: list[str] = ["Alice", "Bob"]
    
    # 字典注解 (键类型, 值类型)
    scores: dict[str, int] = {"Math": 95, "English": 88}
    
    # 集合注解
    tags: set[str] = {"python", "coding"}
    
    # 元组注解 (明确指定每一位的类型)
    point: tuple[int, int, int] = (10, 20, 30)
    
    # 可变长度元组
    values: tuple[int, ...] = (1, 2, 3, 4, 5)

if __name__ == '__main__':
    main()
