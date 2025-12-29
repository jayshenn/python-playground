"""
使用迭代器

对应文档: 10-advanced-features.md § 10.2.2
"""

def main():
    nums = [10, 20, 30]
    
    # 1. 获取迭代器
    it = iter(nums)
    
    # 2. 逐个取值
    print(next(it))
    print(next(it))
    print(next(it))
    
    # 3. 再次获取会抛出 StopIteration
    try:
        print(next(it))
    except StopIteration:
        print("迭代已完成，没有更多元素了")

if __name__ == '__main__':
    main()
