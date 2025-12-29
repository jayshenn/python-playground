"""
什么是生成器

对应文档: 10-advanced-features.md § 10.3.1
"""

import sys

# 生成器是一种特殊的迭代器，边循环边计算，极大地节省内存空间

def main():
    # 1. 列表推导式 (一次性生成所有数据，占用大量内存)
    lst = [x for x in range(10000)]
    print(f"列表占用内存: {sys.getsizeof(lst)} 字节")
    
    # 2. 生成器表达式 (只记录算法，不存储具体数据)
    gen = (x for x in range(10000))
    print(f"生成器占用内存: {sys.getsizeof(gen)} 字节")
    
    # 无论范围多大，生成器占用的空间几乎是恒定的
    gen_large = (x for x in range(100000000))
    print(f"超大生成器占用内存: {sys.getsizeof(gen_large)} 字节")

if __name__ == '__main__':
    main()
