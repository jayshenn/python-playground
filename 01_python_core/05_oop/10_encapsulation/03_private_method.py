"""
私有方法

对应文档: 07-oop-features.md § 7.1.3
"""

class ATM:
    def withdraw(self):
        # 1. 内部调用私有方法进行身份验证
        if self.__verify_card():
            print("取款成功")
        else:
            print("取款失败")

    def __verify_card(self):
        """私有方法：验证卡片逻辑，不希望外部直接调用"""
        print("正在进行安全验证...")
        return True

if __name__ == '__main__':
    atm = ATM()
    atm.withdraw()
    
    # atm.__verify_card() # 外部无法直接验证
