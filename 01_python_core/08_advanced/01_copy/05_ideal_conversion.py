"""
理想的转换情况

对应文档: 10-advanced-features.md § 10.1.5
"""

import copy

def main():
    # 原始对象
    origin = [1, [2, 3]]
    
    # 1. 赋值
    assign_obj = origin
    
    # 2. 浅拷贝
    shallow_obj = copy.copy(origin)
    
    # 3. 深拷贝
    deep_obj = copy.deepcopy(origin)
    
    print(f"{'操作类型':<10} | {'外层地址':<12} | {'内层地址':<12}")
    print("-" * 45)
    print(f"{'原始对象':<10} | {id(origin):<12} | {id(origin[1]):<12}")
    print(f"{'直接赋值':<10} | {id(assign_obj):<12} | {id(assign_obj[1]):<12}")
    print(f"{'浅拷贝':<10} | {id(shallow_obj):<12} | {id(shallow_obj[1]):<12}")
    print(f"{'深拷贝':<10} | {id(deep_obj):<12} | {id(deep_obj[1]):<12}")

if __name__ == '__main__':
    main()
