"""
使用 threading.Thread 创建线程

对应文档: 11-concurrency.md § 11.3.2
"""

import threading
import time

def sing():
    for i in range(3):
        print(f"正在唱歌... {i}")
        time.sleep(0.5)

def dance():
    for i in range(3):
        print(f"正在跳舞... {i}")
        time.sleep(0.5)

if __name__ == '__main__':
    # 创建线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    
    # 启动线程
    t1.start()
    t2.start()
    
    # 等待线程结束
    t1.join()
    t2.join()
    
    print("表演结束")
