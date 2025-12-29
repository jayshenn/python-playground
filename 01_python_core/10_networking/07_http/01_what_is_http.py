"""
什么是 HTTP

对应文档: 12-network-programming.md § 12.7.1
"""

def main():
    print("HTTP (HyperText Transfer Protocol) 超文本传输协议。")
    print("1. 简单快速: 客户端向服务器请求服务时，只需传送请求方法和路径。")
    print("2. 灵活: 允许传输任意类型的数据对象。")
    print("3. 无连接: 每次连接只处理一个请求，处理完即断开（HTTP/1.1 后支持持久连接）。")
    print("4. 无状态: 协议对于事务处理没有记忆能力（通常借由 Cookie/Session 解决）。")

if __name__ == '__main__':
    main()
