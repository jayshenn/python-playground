"""
HTTP 消息结构

对应文档: 12-network-programming.md § 12.7.2
"""

def main():
    print("--- HTTP 请求报文结构 ---")
    print("1. 请求行: GET /index.html HTTP/1.1")
    print("2. 请求头: Host: www.baidu.com \\n User-Agent: Mozilla/5.0 ...")
    print("3. 空行: \\r\\n")
    print("4. 请求体: (POST 请求时提交的参数数据)")
    
    print("\n--- HTTP 响应报文结构 ---")
    print("1. 状态行: HTTP/1.1 200 OK")
    print("2. 响应头: Content-Type: text/html ...")
    print("3. 空行")
    print("4. 响应体: (网页的 HTML 源代码或其他数据)")

if __name__ == '__main__':
    main()
