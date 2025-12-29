"""
IPv4 与 IPv6

对应文档: 12-network-programming.md § 12.2.5
"""

def main():
    print("--- IPv4 vs IPv6 ---")
    
    print("\n[IPv4]")
    print("- 地址长度: 32 位")
    print("- 地址数量: 约 43 亿")
    print("- 表示方式: 点分十进制 (如 192.168.1.1)")
    
    print("\n[IPv6]")
    print("- 地址长度: 128 位")
    print("- 地址数量: 理论上可为地球上每一粒沙子分配一个 IP")
    print("- 表示方式: 冒号十六进制 (如 2001:0db8:85a3:0000:0000:8a2e:0370:7334)")

if __name__ == '__main__':
    main()
