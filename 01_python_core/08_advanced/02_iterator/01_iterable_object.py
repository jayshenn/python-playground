"""
可迭代对象

对应文档: 10-advanced-features.md § 10.2.1
"""

from typing import Iterable

# 只要实现了 __iter__ 方法的对象都是可迭代对象

def main():
    # 常见的可迭代对象
    lst = [1, 2, 3]
    tup = (1, 2)
    s = "abc"
    d = {"a": 1}
    
    print(f"列表是否可迭代: {isinstance(lst, Iterable)}")
    print(f"字符串是否可迭代: {isinstance(s, Iterable)}")
    print(f"整数是否可迭代: {isinstance(100, Iterable)}")
    
    # 获取迭代器
    it = iter(lst)
    print(f"迭代器类型: {type(it)}")

if __name__ == '__main__':
    main()
