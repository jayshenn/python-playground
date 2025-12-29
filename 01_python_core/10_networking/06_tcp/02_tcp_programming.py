"""
TCP 编程

对应文档: 12-network-programming.md § 12.6.2
"""

import socket

def tcp_client_demo():
    # 1. 创建 TCP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. 建立连接 (假设服务端在本地 8888 端口)
    server_addr = ("127.0.0.1", 8888)
    print(f"尝试连接服务端 {server_addr}...")
    # client_socket.connect(server_addr)
    
    # 3. 发送数据
    # client_socket.send("Hello TCP".encode('utf-8'))
    
    # 4. 接收返回数据
    # data = client_socket.recv(1024)
    # print(f"收到回复: {data.decode('utf-8')}")
    
    # 5. 关闭
    client_socket.close()

if __name__ == '__main__':
    tcp_client_demo()
    print("\n提示：TCP 编程分为服务端和客户端两套逻辑。")
    print("服务端需要先 bind 地址并 listen 监听，然后 accept 接受连接。")
