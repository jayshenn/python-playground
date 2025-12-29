"""
什么是 IP

对应文档: 12-network-programming.md § 12.2.1
"""

def main():
    print("IP 地址 (Internet Protocol Address) 是网络中的身份标识。")
    print("常见的 IPv4 由 32 位二进制组成，通常写成 4 组十进制数，例如: 127.0.0.1")
    
    # 演示：本地回环地址
    localhost = "127.0.0.1"
    print(f"本地回环地址: {localhost} (指向机器自身)")

if __name__ == '__main__':
    main()
