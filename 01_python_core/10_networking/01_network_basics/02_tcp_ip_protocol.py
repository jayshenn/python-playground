"""
TCP/IP 协议族

对应文档: 12-network-programming.md § 12.1.2
"""

def main():
    print("--- TCP/IP 四层参考模型 ---")
    
    # 应用层: HTTP, FTP, DNS (负责应用程序间的沟通)
    # 传输层: TCP, UDP (负责端到端的数据传输)
    # 网络层: IP (负责寻址和路由)
    # 链路层: 以太网 (负责物理层面的传输)
    
    print("Python 的网络编程主要工作在 [应用层] 和 [传输层]。")

if __name__ == '__main__':
    main()
