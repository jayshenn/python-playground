"""
集合注解

对应文档: 14-type-system-basics.md § 14.container
"""

# 1. 简单集合
unique_ids: set[int] = {1, 2, 3, 1, 2} # 实际存储 {1, 2, 3}
tags: set[str] = {"python", "typing", "tutorial"}

# 2. 集合操作函数
def merge_tags(tags1: set[str], tags2: set[str]) -> set[str]:
    """合并两个标签集合"""
    return tags1 | tags2

def has_common_elements[T](s1: set[T], s2: set[T]) -> bool:
    """检查两个集合是否有交集 (使用了 3.12+ 泛型语法)"""
    return not s1.isdisjoint(s2)

if __name__ == '__main__':
    print(f"Unique IDs: {unique_ids}")
    
    t1 = {"a", "b"}
    t2 = {"b", "c"}
    print(f"Merged tags: {merge_tags(t1, t2)}")
    print(f"Has common: {has_common_elements(t1, t2)}")
