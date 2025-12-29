"""
互斥锁

对应文档: 11-concurrency.md § 11.3.5
"""

import threading

# 共享资源
g_count = 0
# 创建锁对象
lock = threading.Lock()

def add_value():
    global g_count
    for i in range(1000000):
        # 1. 上锁：确保同一时间只有一个线程能执行后续代码
        lock.acquire()
        try:
            g_count += 1
        finally:
            # 2. 释放锁：必须释放，否则会导致死锁
            lock.release()
            
        # 也可以使用 with lock: 自动管理
        # with lock:
        #     g_count += 1

if __name__ == '__main__':
    t1 = threading.Thread(target=add_value)
    t2 = threading.Thread(target=add_value)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print(f"最终计数值: {g_count} (应该是 2000000)")
