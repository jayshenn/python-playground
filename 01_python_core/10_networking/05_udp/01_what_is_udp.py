"""
什么是 UDP

对应文档: 12-network-programming.md § 12.5.1
"""

def main():
    print("UDP (User Datagram Protocol) 用户数据报协议。")
    print("特点：")
    print("1. 无连接: 不需要像电话那样先拨通。")
    print("2. 不可靠: 发出去就不管了，丢了也不补发。")
    print("3. 效率高: 头部开销小，传输速度快。")
    print("4. 支持一对一、一对多、多对多通信。")

if __name__ == '__main__':
    main()
