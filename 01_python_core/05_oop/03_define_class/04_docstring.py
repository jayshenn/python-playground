"""
类的文档字符串

对应文档: 06-object-oriented-programming.md § 6.3.4
"""

class Robot:
    """
    这是一个机器人模型类。
    
    用于演示如何编写类的文档字符串（Docstring）。
    文档字符串应该紧跟在类定义的第一行。
    """
    
    def work(self):
        """机器人开始工作的描述"""
        print("机器人正在工作...")

if __name__ == '__main__':
    # 1. 访问类的文档字符串
    print("--- 类的文档内容 ---")
    print(Robot.__doc__)
    
    # 2. 访问方法的文档字符串
    print("\n--- 方法的文档内容 ---")
    print(Robot.work.__doc__)
    
    # 3. 使用 help() 函数查看
    # help(Robot)
