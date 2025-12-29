"""
什么是线程

对应文档: 11-concurrency.md § 11.3.1
"""

import threading
import time

# 线程是进程内的一个执行单元，是 CPU 调度的最小单位。
# 同一个进程内的所有线程共享该进程的资源（内存、全局变量等）。

def main():
    # 查看当前活动的线程列表
    print(f"当前活动线程数: {threading.active_count()}")
    print(f"当前线程对象: {threading.current_thread().name}")

if __name__ == '__main__':
    main()
