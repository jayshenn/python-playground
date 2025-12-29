"""
什么是 TCP

对应文档: 12-network-programming.md § 12.6.1
"""

def main():
    print("TCP (Transmission Control Protocol) 传输控制协议。")
    print("特点：")
    print("1. 面向连接: 通信前必须先建立连接 (三次握手)。")
    print("2. 可靠传输: 超时重传、确认应答、数据排序。")
    print("3. 基于字节流: 数据没有边界，像流水一样发送。")
    print("4. 适用场景: 网页访问、文件传输、邮件发送等。")

if __name__ == '__main__':
    main()
