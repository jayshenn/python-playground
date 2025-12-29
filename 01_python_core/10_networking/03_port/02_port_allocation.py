"""
端口号的分配

对应文档: 12-network-programming.md § 12.3.2
"""

def main():
    print("--- 常见服务的默认端口 ---")
    print("HTTP    : 80")
    print("HTTPS   : 443")
    print("FTP     : 21")
    print("SSH     : 22")
    print("MySQL   : 3306")
    print("Redis   : 6379")
    print("MongoDB : 27017")
    
    print("\n提示：在开发阶段，我们通常选择 1024 以上的端口，以避免冲突。")

if __name__ == '__main__':
    main()
