"""
回调函数类型注解

对应文档: 15-type-system-stdlib.md § 15.callable
"""

from collections.abc import Callable

# 使用类型别名定义回调签名，提高代码可读性
type SuccessCallback = Callable[[str], None]
type ErrorCallback = Callable[[Exception], None]

def fetch_data(
    url: str, 
    on_success: SuccessCallback, 
    on_error: ErrorCallback
) -> None:
    """模拟异步数据抓取"""
    print(f"Fetching from {url}...")
    try:
        # 模拟成功逻辑
        if "error" in url:
            raise ConnectionError("Failed to connect")
        
        data = f"Response data from {url}"
        on_success(data)
    except Exception as e:
        on_error(e)

# 实现具体的回调
def handle_data(content: str) -> None:
    print(f"SUCCESS: Processing {content}")

def handle_failure(err: Exception) -> None:
    print(f"ERROR: {err}")

if __name__ == '__main__':
    # 模拟成功调用
    fetch_data("https://api.example.com", handle_data, handle_failure)
    
    # 模拟失败调用
    fetch_data("https://error.com", handle_data, handle_failure)
