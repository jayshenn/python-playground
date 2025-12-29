"""
__slots__ 限制实例属性与实例方法

对应文档: 06-object-oriented-programming.md § 6.9.6
"""

# __slots__ 的作用：
# 1. 限制实例只能添加指定的属性
# 2. 节省内存（不再使用 __dict__ 字典存储属性）

class Account:
    # 只有在 __slots__ 列表中的属性名才能被添加
    __slots__ = ('user', 'balance')
    
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

if __name__ == '__main__':
    acc = Account("张三", 1000)
    print(f"账户: {acc.user}, 余额: {acc.balance}")
    
    # 尝试添加不在 __slots__ 中的属性会报错
    try:
        acc.interest_rate = 0.05
    except AttributeError as e:
        print(f"限制成功: {e}")
        
    # 注意：__slots__ 仅对当前类实例起作用，对子类不起作用（除非子类也定义 __slots__）
