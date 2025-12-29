"""
什么是进程

对应文档: 11-concurrency.md § 11.2.1
"""

import os
import multiprocessing

# 进程是系统分配资源的基本单位。
# 每个正在运行的程序都是一个进程，拥有独立的内存。

def main():
    # 获取当前进程的 ID
    print(f"当前进程 ID (PID): {os.getpid()}")
    
    # 获取父进程的 ID
    print(f"父进程 ID (PPID): {os.getppid()}")
    
    # 获取当前系统的 CPU 核心数
    print(f"CPU 核心数: {multiprocessing.cpu_count()}")

if __name__ == '__main__':
    main()
