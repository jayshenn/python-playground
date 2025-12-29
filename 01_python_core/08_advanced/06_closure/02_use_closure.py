"""
使用闭包

对应文档: 10-advanced-features.md § 10.6.2
"""

# 闭包可以用来保存状态，且比类更轻量

def counter_factory(start=0):
    count = [start]  # 使用列表以绕过 python2 的限制，或 python3 使用 nonlocal
    
    def count_up():
        count[0] += 1
        return count[0]
        
    return count_up

if __name__ == '__main__':
    c1 = counter_factory(10)
    print(f"c1 计数: {c1()}") # 11
    print(f"c1 计数: {c1()}") # 12
    
    c2 = counter_factory(100)
    print(f"c2 计数: {c2()}") # 101
    
    # c1 和 c2 维护着各自独立的状态
    print(f"c1 最终计数: {c1()}") # 13
