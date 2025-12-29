"""
线程池

对应文档: 11-concurrency.md § 11.3.4
"""

from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(url):
    print(f"正在从 {url} 获取数据...")
    time.sleep(1)
    return f"来自 {url} 的结果"

if __name__ == '__main__':
    urls = ["baidu.com", "google.com", "github.com", "python.org"]
    
    # 创建包含 2 个线程的线程池
    with ThreadPoolExecutor(max_workers=2) as executor:
        # map 会阻塞直到所有结果返回
        results = executor.map(fetch_data, urls)
        
    for res in results:
        print(f"处理完成: {res}")
