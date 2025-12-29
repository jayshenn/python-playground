"""
使用 multiprocessing.Process 创建进程

对应文档: 11-concurrency.md § 11.2.2
"""

from multiprocessing import Process
import os
import time

def task(name):
    print(f"子进程 {name} (PID: {os.getpid()}) 开始工作...")
    time.sleep(1)
    print(f"子进程 {name} 工作结束")

if __name__ == '__main__':
    print(f"主进程 (PID: {os.getpid()}) 启动")
    
    # 1. 创建进程实例
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))
    
    # 2. 启动子进程
    p1.start()
    p2.start()
    
    # 3. 等待子进程结束再继续执行主进程
    p1.join()
    p2.join()
    
    print("主进程结束")
