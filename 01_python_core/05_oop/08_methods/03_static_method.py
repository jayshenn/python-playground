"""
静态方法

对应文档: 06-object-oriented-programming.md § 6.8.3
"""

# 静态方法：逻辑上属于类，但不访问实例属性(self)也不访问类属性(cls)
# 使用 @staticmethod 装饰，没有默认的第一个参数

class Validator:
    @staticmethod
    def is_valid_email(email):
        # 只是一个普通的逻辑判断，不需要类或实例的信息
        return "@" in email and "." in email

if __name__ == '__main__':
    # 通过类名直接调用
    result = Validator.is_valid_email("test@example.com")
    print(f"邮件格式是否正确: {result}")
    
    # 常用于工具类或不依赖状态的逻辑封装
