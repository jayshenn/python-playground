"""
HTTP 请求方法

对应文档: 12-network-programming.md § 12.7.3
"""

def main():
    print(f"{'方法':<10} | {'描述'}")
    print("-" * 40)
    print(f"{'GET':<10} | {'向特定资源发出请求 (获取数据)'}")
    print(f"{'POST':<10} | {'向指定资源提交数据处理请求 (新增数据)'}")
    print(f"{'PUT':<10} | {'向指定资源位置上传其最新内容 (更新数据)'}")
    print(f"{'DELETE':<10} | {'请求服务器删除 Request-URI 所标识的资源'}")
    print(f"{'HEAD':<10} | {'只获取响应头，不获取实体主体'}")
    print(f"{'OPTIONS':<10} | {'返回服务器针对特定资源所支持的 HTTP 请求方法'}")

if __name__ == '__main__':
    main()
