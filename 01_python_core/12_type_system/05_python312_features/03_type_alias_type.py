"""
TypeAliasType (Python 3.12+)

对应文档: 14-type-system-basics.md § 14.new
"""

from typing import TypeAliasType

# 使用 type 语句定义的别名在运行时是 TypeAliasType 的实例
type UserId = int
type Point[T] = tuple[T, T]

def explore_type_alias():
    # 1. 检查类型
    print(f"UserId is TypeAliasType: {isinstance(UserId, TypeAliasType)}")
    
    # 2. 获取名称
    print(f"Alias name: {UserId.__name__}")
    
    # 3. 获取底层真实类型
    print(f"Alias value: {UserId.__value__}")
    
    # 4. 泛型别名的参数
    print(f"Point type parameters: {Point.__type_params__}")

if __name__ == '__main__':
    explore_type_alias()
