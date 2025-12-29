# 多线程 (Multithreading)

本章节介绍 Python 中的多线程编程，它是处理 IO 密集型任务（如网络请求、磁盘读写）的理想选择。

## 核心知识点

1. **什么是线程**：操作系统调度的最小单位。同一进程内的线程共享内存空间。
2. **Thread 类**：使用 `threading.Thread` 创建和启动线程。
3. **互斥锁 (Lock)**：防止多个线程同时修改同一数据导致的数据混乱（竞态条件）。
4. **线程池 (ThreadPoolExecutor)**：管理线程生命周期，提高资源利用率。
5. **GIL (全局解释器锁)**：理解为什么 Python 多线程在计算密集型任务上无法发挥多核性能。

## 文件列表

- `01_what_is_thread.py`: 介绍线程概念。
- `02_create_thread.py`: 演示创建简单的线程。
- `03_thread_subclass.py`: 演示自定义线程类。
- `04_thread_pool.py`: 介绍线程池的用法。
- `05_mutex_lock.py`: 演示如何使用锁保护共享数据。
- `06_gil.py`: 介绍 GIL 的影响及应对方案。
