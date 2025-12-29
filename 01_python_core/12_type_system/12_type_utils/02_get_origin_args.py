"""
get_origin() 和 get_args()：泛型自省

对应文档: 15-type-system-stdlib.md § 15.utils
"""

from typing import get_origin, get_args

# 定义一些复杂的泛型类型
type IntList = list[int]
type UserScores = dict[str, float]
type OptionalStr = str | None

def inspect_type(tp: any, name: str):
    origin = get_origin(tp)
    args = get_args(tp)
    print(f"--- {name} ---")
    print(f"Type: {tp}")
    print(f"Origin: {origin}")
    print(f"Arguments: {args}")

if __name__ == '__main__':
    inspect_type(IntList, "IntList")
    inspect_type(UserScores, "UserScores")
    inspect_type(OptionalStr, "OptionalStr")
    
    # 实际应用：判断是否为列表类型
    def is_list_type(tp):
        return get_origin(tp) is list

    print(f"\nIs IntList a list? {is_list_type(IntList)}")
    print(f"Is UserScores a list? {is_list_type(UserScores)}")
