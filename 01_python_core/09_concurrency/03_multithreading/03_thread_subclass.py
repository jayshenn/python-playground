"""
自定义 Thread 子类创建线程

对应文档: 11-concurrency.md § 11.3.3
"""

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        """重写 run 方法"""
        print(f"线程 {self.name} 开始执行")
        time.sleep(1)
        print(f"线程 {self.name} 执行结束")

if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = MyThread()
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
