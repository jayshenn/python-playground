"""
自定义 Process 子类创建进程

对应文档: 11-concurrency.md § 11.2.3
"""

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, name):
        # 必须调用父类的构造方法
        super().__init__()
        self.name = name

    def run(self):
        """重写 run 方法，定义子进程要执行的逻辑"""
        print(f"自定义进程 {self.name} 正在运行...")
        time.sleep(1)
        print(f"自定义进程 {self.name} 运行结束")

if __name__ == '__main__':
    p = MyProcess("Sub-Class-Process")
    p.start() # 调用 start() 时会自动执行 run()
    p.join()
