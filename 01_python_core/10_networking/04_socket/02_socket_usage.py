"""
socket 的使用

对应文档: 12-network-programming.md § 12.4.2
"""

import socket

def create_demo_socket():
    # 1. 创建 TCP Socket
    # AF_INET: 使用 IPv4 地址族
    # SOCK_STREAM: 使用流式传输 (TCP 协议)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("TCP Socket 已创建")
    
    # 2. 创建 UDP Socket
    # SOCK_DGRAM: 使用数据报传输 (UDP 协议)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP Socket 已创建")
    
    # 3. 关闭 Socket
    tcp_socket.close()
    udp_socket.close()

if __name__ == '__main__':
    create_demo_socket()
