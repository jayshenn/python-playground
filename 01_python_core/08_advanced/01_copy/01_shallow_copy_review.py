"""
回顾浅拷贝

对应文档: 10-advanced-features.md § 10.1.1
"""

def main():
    # 1. 直接赋值 (引用传递)
    lst1 = [1, 2, 3]
    lst2 = lst1
    print(f"赋值: lst1 id={id(lst1)}, lst2 id={id(lst2)} (地址相同)")
    
    # 2. 浅拷贝 (创建了新容器)
    lst3 = lst1.copy()
    print(f"浅拷贝: lst1 id={id(lst1)}, lst3 id={id(lst3)} (地址不同)")
    
    lst3[0] = 99
    print(f"修改后: lst1={lst1}, lst3={lst3} (互不影响)")

if __name__ == '__main__':
    main()
