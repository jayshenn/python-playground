"""
进程间通信

对应文档: 11-concurrency.md § 11.2.5
"""

from multiprocessing import Process, Queue
import time

# 进程间内存不共享，必须使用 Queue, Pipe 等机制通信

def producer(q):
    for i in range(3):
        print(f"生产者: 生产了消息 {i}")
        q.put(f"消息_{i}")
        time.sleep(0.5)

def consumer(q):
    while True:
        msg = q.get() # 阻塞式等待
        print(f"消费者: 接收到了 {msg}")
        if "结束" in msg:
            break

if __name__ == '__main__':
    q = Queue()
    
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    # 告诉消费者可以结束了
    q.put("结束信号")
    p2.join()
