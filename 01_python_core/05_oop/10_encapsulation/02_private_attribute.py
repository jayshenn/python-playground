"""
私有属性

对应文档: 07-oop-features.md § 7.1.2
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性，防止被外部直接修改金额
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功，当前余额: {self.__balance}")
            
    def get_balance(self):
        return self.__balance

if __name__ == '__main__':
    account = BankAccount(1000)
    
    # 外部只能通过提供的接口操作
    account.deposit(500)
    print(f"查询余额: {account.get_balance()}")
    
    # 不能 account.__balance = 999999
