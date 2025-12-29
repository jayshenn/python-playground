"""
自定义迭代器

对应文档: 10-advanced-features.md § 10.2.3
"""

# 自定义一个能够生成指定范围内平方数的迭代器
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # 迭代器协议要求 __iter__ 返回迭代器本身
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            # 必须抛出 StopIteration 信号告知迭代结束
            raise StopIteration

if __name__ == '__main__':
    # 使用自定义迭代器
    sq_it = SquareIterator(1, 5)
    
    print("遍历自定义迭代器结果:")
    for num in sq_it:
        print(num)
