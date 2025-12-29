"""
通过 self 在类中调用其他方法

对应文档: 06-object-oriented-programming.md § 6.6.2
"""

class SmartHome:
    def open_door(self):
        print("门已打开")
        # 通过 self 调用内部其他方法
        self.turn_on_light()
        
    def turn_on_light(self):
        print("灯已亮起")
        self.welcome_msg()
        
    def welcome_msg(self):
        print("欢迎回家！")

if __name__ == '__main__':
    home = SmartHome()
    # 只需要调用一个入口方法，内部逻辑通过 self 串联
    home.open_door()
