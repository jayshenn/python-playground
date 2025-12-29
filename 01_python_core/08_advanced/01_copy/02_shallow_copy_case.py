"""
浅拷贝案例 (嵌套对象)

对应文档: 10-advanced-features.md § 10.1.2
"""

import copy

def main():
    # 嵌套列表
    original = [1, 2, [3, 4]]
    
    # 执行浅拷贝
    shallow = copy.copy(original)
    
    print(f"修改前:")
    print(f"Original: {original}")
    print(f"Shallow : {shallow}")
    
    # 修改内层的嵌套列表
    original[2][0] = "CHANGES"
    
    print(f"\n修改内层嵌套对象后:")
    print(f"Original: {original}")
    print(f"Shallow : {shallow} (浅拷贝也跟着变了！)")
    
    # 原因是：浅拷贝只拷贝了外层，内层的 [3, 4] 地址还是同一个
    print(f"\n内层地址: {id(original[2])} vs {id(shallow[2])}")

if __name__ == '__main__':
    main()
