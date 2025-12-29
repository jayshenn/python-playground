"""
UDP 编程

对应文档: 12-network-programming.md § 12.5.2
"""

import socket

def udp_sender():
    # 1. 创建 UDP Socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. 准备数据 (必须是 bytes 类型)
    data = "你好，我是 UDP 客户端".encode('utf-8')
    
    # 3. 目标地址 (IP, Port)
    dest_addr = ("127.0.0.1", 8080)
    
    print(f"准备向 {dest_addr} 发送数据...")
    # 4. 发送数据
    # udp_socket.sendto(data, dest_addr)
    
    # 5. 关闭 Socket
    udp_socket.close()

if __name__ == '__main__':
    udp_sender()
    print("提示：在实际测试时，需要先运行一个 UDP 接收端来监听 8080 端口。")
