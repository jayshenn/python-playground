"""
回顾深拷贝

对应文档: 10-advanced-features.md § 10.1.3
"""

import copy

# 深拷贝：不管多少层，都会在内存中开辟新的空间进行存储

def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    
    # 深度拷贝
    d = copy.deepcopy(c)
    
    print(f"c 的地址: {id(c)}")
    print(f"d 的地址: {id(d)}")
    print(f"c[0] 地址: {id(c[0])} (a)")
    print(f"d[0] 地址: {id(d[0])} (a 的副本)")
    
    # 深拷贝连子对象的地址都改了
    print(f"c[0] is d[0]: {c[0] is d[0]}") # False

if __name__ == '__main__':
    main()
