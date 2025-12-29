"""
子网掩码

对应文档: 12-network-programming.md § 12.2.2
"""

def main():
    print("子网掩码的作用：区分 IP 地址中的网络位和主机位。")
    print("如果两个 IP 的 (IP & 子网掩码) 结果相同，说明它们在同一个子网。")
    
    # 典型示例
    ip = "192.168.1.10"
    mask = "255.255.255.0"
    print(f"IP: {ip}, 掩码: {mask}")
    print("前 24 位为网络号，最后 8 位为主机号。")

if __name__ == '__main__':
    main()
