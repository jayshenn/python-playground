# 多进程 (Multiprocessing)

本章节介绍如何在 Python 中利用多核 CPU 资源，实现真正的并行计算。

## 核心知识点

1. **什么是进程**：操作系统分配资源的基本单位。每个进程有独立的内存空间。
2. **Process 类**：`multiprocessing` 模块的核心，用于创建和管理子进程。
3. **自定义进程类**：通过继承 `Process` 并重写 `run` 方法来实现更复杂的逻辑。
4. **进程池 (Pool)**：高效管理大量子进程，支持任务分配和结果回收。
5. **进程间通信 (IPC)**：通过 `Queue`（队列）或 `Pipe`（管道）在独立内存空间的进程间传递数据。

## 文件列表

- `01_what_is_process.py`: 介绍进程概念及如何查看进程 ID。
- `02_create_process.py`: 演示使用 `Process` 创建简单子进程。
- `03_process_subclass.py`: 演示通过继承方式创建自定义进程。
- `04_process_pool.py`: 介绍进程池的高效用法。
- `05_process_communication.py`: 演示如何利用 `Queue` 实现进程间的数据交换。
