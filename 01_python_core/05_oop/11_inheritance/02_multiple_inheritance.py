"""
多继承

对应文档: 07-oop-features.md § 7.2.2
"""

class Camera:
    def take_photo(self):
        print("拍照中...")

class Phone:
    def make_call(self):
        print("拨打电话中...")

# 智能手机继承了相机和手机的功能
class SmartPhone(Camera, Phone):
    pass

if __name__ == '__main__':
    iphone = SmartPhone()
    iphone.take_photo() # 来自 Camera
    iphone.make_call()  # 来自 Phone
