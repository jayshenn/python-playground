"""
进程池

对应文档: 11-concurrency.md § 11.2.4
"""

from multiprocessing import Pool
import time
import os

def worker_task(n):
    print(f"进程 {os.getpid()} 正在处理数据 {n}")
    time.sleep(0.5)
    return n * n

if __name__ == '__main__':
    # 创建进程池，默认大小为 CPU 核心数
    with Pool(processes=3) as pool:
        # map 方法可以将列表中的数据分发给不同的进程处理
        results = pool.map(worker_task, range(5))
        
    print(f"所有任务处理完成，结果: {results}")
