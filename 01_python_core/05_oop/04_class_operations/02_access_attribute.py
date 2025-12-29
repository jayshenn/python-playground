"""
访问属性

对应文档: 06-object-oriented-programming.md § 6.4.2
"""

class Phone:
    brand = "Apple"
    color = "White"

if __name__ == '__main__':
    my_phone = Phone()
    
    # 1. 访问属性
    print(f"品牌: {my_phone.brand}")
    print(f"颜色: {my_phone.color}")
    
    # 2. 修改属性
    my_phone.color = "Space Gray"
    print(f"修改后的颜色: {my_phone.color}")
    
    # 3. 动态添加属性 (Python 的特性，但不推荐在类外部频繁这样操作)
    my_phone.price = 7999
    print(f"新增的价格属性: {my_phone.price}")
