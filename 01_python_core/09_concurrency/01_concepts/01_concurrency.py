"""
并发

对应文档: 11-concurrency.md § 11.1.1
"""

import time

# 并发：在一段时间内处理多个任务。
# 比如：一个人同时在烧水和洗菜。虽然他只有一双手（一个核心），
# 但可以在水还没烧开的时候去洗菜，水开了去关火，然后再洗菜。

def boil_water():
    print("开始烧水...")
    # 模拟 IO 等待
    # time.sleep(3) 
    print("水烧开了！")

def wash_vegetables():
    print("开始洗菜...")
    # 模拟洗菜过程
    # time.sleep(2)
    print("菜洗好了！")

if __name__ == '__main__':
    print("--- 串行执行 ---")
    boil_water()
    wash_vegetables()
    
    print("\n并发的本质是通过切换任务，利用 CPU 在等待过程中的空闲时间。")
