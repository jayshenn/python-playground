"""
HTTP 状态码

对应文档: 12-network-programming.md § 12.7.4
"""

def main():
    print("--- 常用 HTTP 状态码 ---")
    
    print("\n1xx (信息性): 接收的请求正在处理")
    
    print("\n2xx (成功):")
    print("  - 200 OK: 请求成功")
    print("  - 201 Created: 已创建")
    
    print("\n3xx (重定向):")
    print("  - 301 Moved Permanently: 永久重定向")
    print("  - 302 Found: 临时重定向")
    
    print("\n4xx (客户端错误):")
    print("  - 400 Bad Request: 语法错误")
    print("  - 401 Unauthorized: 未授权")
    print("  - 403 Forbidden: 禁止访问")
    print("  - 404 Not Found: 资源不存在")
    
    print("\n5xx (服务器错误):")
    print("  - 500 Internal Server Error: 服务器内部错误")
    print("  - 503 Service Unavailable: 服务不可用")

if __name__ == '__main__':
    main()
