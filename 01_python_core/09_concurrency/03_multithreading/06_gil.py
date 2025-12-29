"""
GIL (Global Interpreter Lock)

对应文档: 11-concurrency.md § 11.3.6
"""

# GIL 是 Python 解释器层面的全局锁，它使得同一时刻只有一个线程能运行 Python 字节码。

def main():
    print("--- GIL 的核心结论 ---")
    print("1. 计算密集型任务：多线程由于 GIL 的存在，不仅没变快，反而可能因为频繁切换变慢。"
          "解决方案：使用多进程 (multiprocessing)。")
    print("2. IO 密集型任务：线程在等待 IO 时会释放 GIL，因此多线程能显著提升效率。"
          "解决方案：使用多线程 (threading) 或 协程 (asyncio)。")

if __name__ == '__main__':
    main()
