"""
类方法

对应文档: 06-object-oriented-programming.md § 6.8.2
"""

# 类方法：属于类本身，使用 @classmethod 装饰
# 第一个参数通常命名为 cls，代表类本身

class Shop:
    total_sales = 0  # 类属性：总销量

    @classmethod
    def record_sale(cls, amount):
        # cls 此时指向 Shop 类
        cls.total_sales += amount
        print(f"记录一笔销量: {amount}, 总销量: {cls.total_sales}")

if __name__ == '__main__':
    # 不需要实例化，直接通过类名调用
    Shop.record_sale(100)
    Shop.record_sale(250)
    
    # 也可以通过实例调用（不推荐，但可行）
    s = Shop()
    s.record_sale(50)
