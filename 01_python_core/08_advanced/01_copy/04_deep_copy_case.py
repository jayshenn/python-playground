"""
深拷贝案例

对应文档: 10-advanced-features.md § 10.1.4
"""

import copy

def main():
    original = {"data": [1, 2, 3], "status": True}
    
    # 彻底的副本
    deep = copy.deepcopy(original)
    
    # 修改原始数据
    original["data"].append(999)
    original["status"] = False
    
    print("--- 修改原始字典后 ---")
    print(f"Original: {original}")
    print(f"Deep    : {deep} (完全不受影响)")

if __name__ == '__main__':
    main()
