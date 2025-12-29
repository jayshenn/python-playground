# 第 11 章 常进程与线程

在现代编程中，为了充分利用计算机的多核处理器，提高程序的执行效率，我们需要使用并发编程技术。Python 提供了**多进程**和**多线程**两种方式来实现并发。

---

## 11.1 并发与并行

### 11.1.1 并发

**并发**（Concurrency）是指在同一时间段内处理多个任务，但不一定同时执行。

**并发的特点**：
- 任务在时间上交替执行
- 给人一种"同时进行"的错觉
- 适用于单核和多核处理器
- 通过时间片轮转实现

**并发示例**：

```python
import time

def task1():
    """任务 1"""
    for i in range(3):
        print(f"任务 1 - 步骤 {i}")
        time.sleep(0.1)

def task2():
    """任务 2"""
    for i in range(3):
        print(f"任务 2 - 步骤 {i}")
        time.sleep(0.1)

# 顺序执行（非并发）
print("=== 顺序执行 ===")
start = time.time()
task1()
task2()
print(f"总耗时: {time.time() - start:.2f} 秒\n")

# 并发执行
print("=== 并发执行 ===")
import threading

start = time.time()
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
print(f"总耗时: {time.time() - start:.2f} 秒")
```

**并发的应用场景**：
- Web 服务器处理多个客户端请求
- GUI 应用程序响应用户操作
- I/O 密集型任务（文件读写、网络请求）

### 11.1.2 并行

**并行**（Parallelism）是指在同一时刻真正同时执行多个任务。

**并行的特点**：
- 任务真正同时执行
- 需要多核处理器支持
- 充分利用硬件资源
- 适合计算密集型任务

**并发 vs 并行**：

| 特性 | 并发 | 并行 |
|------|------|------|
| **定义** | 同一时间段处理多个任务 | 同一时刻执行多个任务 |
| **硬件要求** | 单核或多核 | 必须多核 |
| **执行方式** | 时间片轮转 | 真正同时执行 |
| **适用场景** | I/O 密集型 | CPU 密集型 |
| **示例** | Web 服务器 | 科学计算 |

**形象比喻**：

```python
# 并发：一个厨师同时做多道菜（来回切换）
# 任务 A：炒菜 -> 等待（去做任务 B）-> 继续炒菜
# 任务 B：煮汤 -> 等待（去做任务 A）-> 继续煮汤

# 并行：多个厨师各做一道菜（真正同时）
# 厨师 1：炒菜
# 厨师 2：煮汤
# 厨师 3：蒸饭
```

**Python 中的并发与并行**：

```python
import multiprocessing
import os

def cpu_bound_task(n):
    """CPU 密集型任务"""
    result = sum(i * i for i in range(n))
    print(f"进程 {os.getpid()}: 计算完成")
    return result

# 并行执行（多进程）
if __name__ == '__main__':
    import time

    print("=== 顺序执行 ===")
    start = time.time()
    for _ in range(4):
        cpu_bound_task(10000000)
    print(f"耗时: {time.time() - start:.2f} 秒\n")

    print("=== 并行执行 ===")
    start = time.time()
    with multiprocessing.Pool(4) as pool:
        pool.map(cpu_bound_task, [10000000] * 4)
    print(f"耗时: {time.time() - start:.2f} 秒")
```

---

## 11.2 多进程

### 11.2.1 什么是进程

**进程**（Process）是操作系统分配资源的基本单位，是程序的一次执行过程。

**进程的特点**：
- 独立的内存空间
- 拥有独立的资源
- 进程间通信需要特殊机制
- 创建和销毁开销较大
- 真正的并行执行

```python
import os

print(f"当前进程 ID: {os.getpid()}")
print(f"父进程 ID: {os.getppid()}")
```

**进程的生命周期**：

```
创建 -> 就绪 -> 运行 -> 阻塞 -> 终止
```

### 11.2.2 使用 multiprocessing.Process 创建进程

**基本用法**：

```python
from multiprocessing import Process
import os
import time

def worker(name):
    """工作进程"""
    print(f"子进程 {name} 启动，PID: {os.getpid()}")
    time.sleep(2)
    print(f"子进程 {name} 结束")

if __name__ == '__main__':
    print(f"主进程 PID: {os.getpid()}")

    # 创建进程
    p = Process(target=worker, args=('Worker-1',))

    # 启动进程
    p.start()

    # 等待进程结束
    p.join()

    print("主进程结束")
```

**创建多个进程**：

```python
from multiprocessing import Process
import time

def count_numbers(name, start, end):
    """计数任务"""
    print(f"{name} 开始计数")
    for i in range(start, end):
        print(f"{name}: {i}")
        time.sleep(0.1)
    print(f"{name} 结束")

if __name__ == '__main__':
    # 创建多个进程
    processes = []

    p1 = Process(target=count_numbers, args=('进程1', 0, 5))
    p2 = Process(target=count_numbers, args=('进程2', 5, 10))

    processes.append(p1)
    processes.append(p2)

    # 启动所有进程
    for p in processes:
        p.start()

    # 等待所有进程结束
    for p in processes:
        p.join()

    print("所有进程执行完毕")
```

**进程的属性和方法**：

```python
from multiprocessing import Process
import time

def worker():
    time.sleep(1)

if __name__ == '__main__':
    p = Process(target=worker)

    # 进程属性
    print(f"进程名称: {p.name}")
    print(f"进程是否存活: {p.is_alive()}")
    print(f"进程 PID: {p.pid}")  # 启动前为 None

    # 启动进程
    p.start()

    print(f"启动后 PID: {p.pid}")
    print(f"是否存活: {p.is_alive()}")

    # 等待进程结束
    p.join(timeout=2)  # 最多等待 2 秒

    print(f"进程退出码: {p.exitcode}")  # 0 表示正常退出
```

**传递参数**：

```python
from multiprocessing import Process

def greet(name, age):
    """问候函数"""
    print(f"Hello, {name}! You are {age} years old.")

def calculate(a, b, operation='+'):
    """计算函数"""
    if operation == '+':
        result = a + b
    elif operation == '*':
        result = a * b
    else:
        result = None
    print(f"{a} {operation} {b} = {result}")

if __name__ == '__main__':
    # 位置参数
    p1 = Process(target=greet, args=('Alice', 25))
    p1.start()
    p1.join()

    # 关键字参数
    p2 = Process(target=calculate, args=(10, 5), kwargs={'operation': '*'})
    p2.start()
    p2.join()
```

### 11.2.3 自定义 Process 子类创建进程

**继承 Process 类**：

```python
from multiprocessing import Process
import time

class MyProcess(Process):
    """自定义进程类"""

    def __init__(self, name, count):
        super().__init__()
        self.count = count
        self.name = name

    def run(self):
        """重写 run 方法"""
        print(f"{self.name} 开始执行")
        for i in range(self.count):
            print(f"{self.name}: {i}")
            time.sleep(0.5)
        print(f"{self.name} 执行完毕")

if __name__ == '__main__':
    # 创建自定义进程
    p1 = MyProcess('进程A', 3)
    p2 = MyProcess('进程B', 3)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("所有进程结束")
```

**完整示例**：

```python
from multiprocessing import Process
import os
import time

class Worker(Process):
    """工作进程"""

    def __init__(self, task_id, task_name):
        super().__init__()
        self.task_id = task_id
        self.task_name = task_name

    def run(self):
        """执行任务"""
        print(f"任务 {self.task_id}: {self.task_name} 开始")
        print(f"进程 ID: {os.getpid()}")

        # 模拟耗时任务
        for i in range(3):
            print(f"任务 {self.task_id} 进度: {i+1}/3")
            time.sleep(1)

        print(f"任务 {self.task_id}: {self.task_name} 完成")

if __name__ == '__main__':
    workers = [
        Worker(1, '数据处理'),
        Worker(2, '文件上传'),
        Worker(3, '邮件发送')
    ]

    # 启动所有工作进程
    for worker in workers:
        worker.start()

    # 等待所有进程完成
    for worker in workers:
        worker.join()

    print("所有任务完成")
```

### 11.2.4 进程池

**进程池**（Process Pool）用于管理多个工作进程，避免频繁创建和销毁进程。

**使用 Pool**：

```python
from multiprocessing import Pool
import os
import time

def worker(x):
    """工作函数"""
    print(f"进程 {os.getpid()} 处理 {x}")
    time.sleep(1)
    return x * x

if __name__ == '__main__':
    # 创建进程池（4 个进程）
    with Pool(processes=4) as pool:
        # 方法 1：map（阻塞）
        results = pool.map(worker, range(10))
        print(f"结果: {results}")
```

**进程池的方法**：

```python
from multiprocessing import Pool
import time

def task(x):
    """任务函数"""
    time.sleep(0.5)
    return x * 2

if __name__ == '__main__':
    with Pool(4) as pool:
        # 1. map：批量处理，返回结果列表
        results = pool.map(task, range(5))
        print(f"map 结果: {results}")

        # 2. apply：单个任务（阻塞）
        result = pool.apply(task, args=(10,))
        print(f"apply 结果: {result}")

        # 3. apply_async：单个任务（非阻塞）
        async_result = pool.apply_async(task, args=(20,))
        print(f"apply_async 结果: {async_result.get()}")

        # 4. map_async：批量处理（非阻塞）
        async_results = pool.map_async(task, range(5))
        print(f"map_async 结果: {async_results.get()}")
```

**进程池的实际应用**：

```python
from multiprocessing import Pool
import time

def process_file(filename):
    """处理文件"""
    print(f"开始处理文件: {filename}")
    time.sleep(2)  # 模拟文件处理
    return f"{filename} 处理完成"

if __name__ == '__main__':
    files = [f'file_{i}.txt' for i in range(10)]

    print("=== 使用进程池处理文件 ===")
    start = time.time()

    with Pool(4) as pool:  # 4 个工作进程
        results = pool.map(process_file, files)

    for result in results:
        print(result)

    print(f"总耗时: {time.time() - start:.2f} 秒")
```

**进程池的回调函数**：

```python
from multiprocessing import Pool

def task(x):
    """任务"""
    return x * x

def on_success(result):
    """成功回调"""
    print(f"任务成功，结果: {result}")

def on_error(error):
    """错误回调"""
    print(f"任务失败: {error}")

if __name__ == '__main__':
    with Pool(2) as pool:
        for i in range(5):
            pool.apply_async(
                task,
                args=(i,),
                callback=on_success,
                error_callback=on_error
            )

        pool.close()  # 不再接受新任务
        pool.join()   # 等待所有任务完成
```

### 11.2.5 进程间通信

**进程间通信**（IPC）是指在不同进程之间交换数据。

#### 1. Queue（队列）

```python
from multiprocessing import Process, Queue
import time

def producer(queue):
    """生产者"""
    for i in range(5):
        print(f"生产: {i}")
        queue.put(i)
        time.sleep(0.5)
    queue.put(None)  # 发送结束信号

def consumer(queue):
    """消费者"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"消费: {item}")
        time.sleep(1)

if __name__ == '__main__':
    # 创建队列
    queue = Queue()

    # 创建生产者和消费者进程
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("完成")
```

#### 2. Pipe（管道）

```python
from multiprocessing import Process, Pipe

def sender(conn):
    """发送端"""
    conn.send(['Hello', 'World'])
    conn.send({'name': 'Alice', 'age': 25})
    conn.close()

def receiver(conn):
    """接收端"""
    print(f"接收到: {conn.recv()}")
    print(f"接收到: {conn.recv()}")
    conn.close()

if __name__ == '__main__':
    # 创建管道
    parent_conn, child_conn = Pipe()

    # 创建进程
    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

#### 3. Manager（共享数据）

```python
from multiprocessing import Process, Manager

def worker(shared_dict, shared_list, worker_id):
    """工作进程"""
    shared_dict[worker_id] = f"Worker {worker_id}"
    shared_list.append(worker_id)

if __name__ == '__main__':
    # 创建管理器
    with Manager() as manager:
        # 创建共享数据结构
        shared_dict = manager.dict()
        shared_list = manager.list()

        # 创建多个进程
        processes = []
        for i in range(5):
            p = Process(target=worker, args=(shared_dict, shared_list, i))
            processes.append(p)
            p.start()

        # 等待所有进程
        for p in processes:
            p.join()

        print(f"共享字典: {dict(shared_dict)}")
        print(f"共享列表: {list(shared_list)}")
```

---

## 11.3 多线程

### 11.3.1 什么是线程

**线程**（Thread）是进程中的执行单元，是 CPU 调度的基本单位。

**线程的特点**：
- 共享进程的内存空间
- 共享进程的资源
- 创建和销毁开销小
- 线程间通信简单
- 受 GIL 限制（CPython）

```python
import threading

print(f"当前线程: {threading.current_thread().name}")
print(f"活动线程数: {threading.active_count()}")
print(f"所有线程: {threading.enumerate()}")
```

**线程 vs 进程**：

| 特性 | 线程 | 进程 |
|------|------|------|
| **内存** | 共享 | 独立 |
| **通信** | 简单 | 复杂 |
| **创建开销** | 小 | 大 |
| **切换开销** | 小 | 大 |
| **并行性** | 受 GIL 限制 | 真正并行 |

### 11.3.2 使用 threading.Thread 创建线程

**基本用法**：

```python
import threading
import time

def worker(name):
    """工作线程"""
    print(f"线程 {name} 启动")
    time.sleep(2)
    print(f"线程 {name} 结束")

# 创建线程
t = threading.Thread(target=worker, args=('Worker-1',))

# 启动线程
t.start()

# 等待线程结束
t.join()

print("主线程结束")
```

**创建多个线程**：

```python
import threading
import time

def count_numbers(name, start, end):
    """计数任务"""
    print(f"{name} 开始")
    for i in range(start, end):
        print(f"{name}: {i}")
        time.sleep(0.1)
    print(f"{name} 结束")

# 创建多个线程
threads = []

t1 = threading.Thread(target=count_numbers, args=('线程1', 0, 5))
t2 = threading.Thread(target=count_numbers, args=('线程2', 5, 10))

threads.append(t1)
threads.append(t2)

# 启动所有线程
for t in threads:
    t.start()

# 等待所有线程结束
for t in threads:
    t.join()

print("所有线程执行完毕")
```

**线程的属性和方法**：

```python
import threading
import time

def worker():
    time.sleep(1)

t = threading.Thread(target=worker)

# 线程属性
print(f"线程名称: {t.name}")
print(f"线程是否存活: {t.is_alive()}")
print(f"线程是否为守护线程: {t.daemon}")

# 设置为守护线程
t.daemon = True  # 必须在 start() 之前设置

# 启动线程
t.start()

print(f"是否存活: {t.is_alive()}")

# 等待线程
t.join(timeout=2)
```

**守护线程**：

```python
import threading
import time

def daemon_thread():
    """守护线程"""
    print("守护线程启动")
    time.sleep(5)
    print("守护线程结束（可能不会打印）")

def normal_thread():
    """普通线程"""
    print("普通线程启动")
    time.sleep(1)
    print("普通线程结束")

# 守护线程
t1 = threading.Thread(target=daemon_thread)
t1.daemon = True  # 设置为守护线程
t1.start()

# 普通线程
t2 = threading.Thread(target=normal_thread)
t2.start()

t2.join()  # 等待普通线程

print("主线程结束（守护线程也会结束）")
```

### 11.3.3 自定义 Thread 子类创建线程

**继承 Thread 类**：

```python
import threading
import time

class MyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count

    def run(self):
        """重写 run 方法"""
        print(f"{self.name} 开始执行")
        for i in range(self.count):
            print(f"{self.name}: {i}")
            time.sleep(0.5)
        print(f"{self.name} 执行完毕")

# 创建线程
t1 = MyThread('线程A', 3)
t2 = MyThread('线程B', 3)

t1.start()
t2.start()

t1.join()
t2.join()

print("所有线程结束")
```

**完整示例**：

```python
import threading
import time

class Worker(threading.Thread):
    """工作线程"""

    def __init__(self, task_id, task_name):
        super().__init__()
        self.task_id = task_id
        self.task_name = task_name

    def run(self):
        """执行任务"""
        print(f"任务 {self.task_id}: {self.task_name} 开始")

        # 模拟耗时任务
        for i in range(3):
            print(f"任务 {self.task_id} 进度: {i+1}/3")
            time.sleep(1)

        print(f"任务 {self.task_id}: {self.task_name} 完成")

# 创建工作线程
workers = [
    Worker(1, '数据处理'),
    Worker(2, '文件上传'),
    Worker(3, '邮件发送')
]

# 启动所有线程
for worker in workers:
    worker.start()

# 等待所有线程完成
for worker in workers:
    worker.join()

print("所有任务完成")
```

### 11.3.4 线程池

**使用 ThreadPoolExecutor**：

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(x):
    """任务函数"""
    print(f"处理 {x}")
    time.sleep(1)
    return x * 2

# 使用线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    # 方法 1：map
    results = executor.map(task, range(5))
    print(f"结果: {list(results)}")

    # 方法 2：submit
    future = executor.submit(task, 10)
    print(f"Future 结果: {future.result()}")
```

**线程池的回调函数**：

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(x):
    """任务"""
    time.sleep(1)
    return x * x

def on_done(future):
    """完成回调"""
    print(f"任务完成，结果: {future.result()}")

with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(5):
        future = executor.submit(task, i)
        future.add_done_callback(on_done)
```

### 11.3.5 互斥锁

**互斥锁**（Mutex Lock）用于保护共享资源，避免竞态条件。

**不使用锁的问题**：

```python
import threading

# 共享变量
count = 0

def increment():
    """增加计数"""
    global count
    for _ in range(100000):
        count += 1

# 创建多个线程
threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

# 等待所有线程
for t in threads:
    t.join()

print(f"最终计数: {count}")  # 可能不是 1000000（竞态条件）
```

**使用锁**：

```python
import threading

count = 0
lock = threading.Lock()  # 创建锁

def increment():
    """增加计数（使用锁）"""
    global count
    for _ in range(100000):
        with lock:  # 获取锁
            count += 1
        # 自动释放锁

# 创建多个线程
threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

# 等待所有线程
for t in threads:
    t.join()

print(f"最终计数: {count}")  # 正确：1000000
```

**锁的手动管理**：

```python
import threading

lock = threading.Lock()

# 方法 1：with 语句（推荐）
with lock:
    # 临界区代码
    print("受保护的代码")

# 方法 2：手动加锁和解锁
lock.acquire()
try:
    # 临界区代码
    print("受保护的代码")
finally:
    lock.release()
```

**死锁问题**：

```python
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    """任务 1"""
    with lock1:
        print("任务 1 获得锁 1")
        time.sleep(0.1)
        with lock2:  # 等待锁 2
            print("任务 1 获得锁 2")

def task2():
    """任务 2"""
    with lock2:
        print("任务 2 获得锁 2")
        time.sleep(0.1)
        with lock1:  # 等待锁 1（可能死锁）
            print("任务 2 获得锁 1")

# 可能导致死锁
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
```

**使用 RLock（可重入锁）**：

```python
import threading

lock = threading.RLock()  # 可重入锁

def recursive_function(n):
    """递归函数"""
    with lock:
        if n > 0:
            print(n)
            recursive_function(n - 1)  # 可以重复获取锁

recursive_function(5)
```

### 11.3.6 GIL

**GIL（Global Interpreter Lock，全局解释器锁）**是 CPython 的一个特性，限制了同一时刻只有一个线程执行 Python 字节码。

**GIL 的影响**：

```python
import threading
import time

def cpu_bound():
    """CPU 密集型任务"""
    count = 0
    for _ in range(50000000):
        count += 1

# 单线程
start = time.time()
cpu_bound()
cpu_bound()
print(f"单线程耗时: {time.time() - start:.2f} 秒")

# 多线程（受 GIL 限制，不会更快）
start = time.time()
t1 = threading.Thread(target=cpu_bound)
t2 = threading.Thread(target=cpu_bound)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"多线程耗时: {time.time() - start:.2f} 秒")
```

**GIL 的特点**：
- 保护 CPython 的内存管理
- 限制了多线程的并行性
- CPU 密集型任务不适合多线程
- I/O 密集型任务影响较小
- 可以使用多进程绕过 GIL

**何时受 GIL 影响**：

```python
# CPU 密集型：受 GIL 影响（推荐多进程）
def cpu_task():
    return sum(i * i for i in range(10000000))

# I/O 密集型：受 GIL 影响较小（推荐多线程）
def io_task():
    import time
    time.sleep(1)  # I/O 等待时会释放 GIL
    return "完成"
```

---

## 11.4 进程和线程对比

### 11.4.1 区别

| 特性 | 进程 | 线程 |
|------|------|------|
| **定义** | 资源分配的基本单位 | CPU 调度的基本单位 |
| **内存空间** | 独立 | 共享 |
| **资源开销** | 大（创建、切换） | 小 |
| **通信方式** | IPC（Queue、Pipe） | 共享变量（需要锁） |
| **数据隔离** | 完全隔离 | 共享数据 |
| **并行性** | 真正并行 | 受 GIL 限制 |
| **稳定性** | 一个进程崩溃不影响其他 | 一个线程崩溃可能影响整个进程 |
| **适用场景** | CPU 密集型 | I/O 密集型 |

**对比示例**：

```python
import multiprocessing
import threading
import time

# 测试数据
data = list(range(1000000))

# CPU 密集型任务
def cpu_task(numbers):
    return sum(i * i for i in numbers)

# 多进程
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(4) as pool:
        pool.map(cpu_task, [data] * 4)
    print(f"多进程耗时: {time.time() - start:.2f} 秒")

    # 多线程
    start = time.time()
    threads = []
    for _ in range(4):
        t = threading.Thread(target=cpu_task, args=(data,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"多线程耗时: {time.time() - start:.2f} 秒")
```

### 11.4.2 使用场景

**使用多进程的场景**：
- CPU 密集型任务（计算、数据处理）
- 需要真正的并行执行
- 任务之间独立，通信较少
- 对稳定性要求高

**使用多线程的场景**：
- I/O 密集型任务（网络请求、文件读写）
- 需要共享大量数据
- 对响应速度要求高
- GUI 应用程序

**实际应用示例**：

```python
# 示例 1：网络爬虫（I/O 密集型，使用多线程）
import threading
import requests

def fetch_url(url):
    """获取网页"""
    response = requests.get(url)
    print(f"{url}: {len(response.content)} 字节")

urls = ['https://www.python.org'] * 10

threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# 示例 2：图像处理（CPU 密集型，使用多进程）
from multiprocessing import Pool

def process_image(image_path):
    """处理图像"""
    # 模拟图像处理
    result = sum(i * i for i in range(1000000))
    return f"{image_path} 处理完成"

if __name__ == '__main__':
    images = [f'image_{i}.jpg' for i in range(10)]

    with Pool(4) as pool:
        results = pool.map(process_image, images)

    for result in results:
        print(result)
```

**选择建议**：

```python
# 决策树
"""
是 CPU 密集型任务？
├─ 是 → 使用多进程（multiprocessing）
└─ 否 → 是 I/O 密集型任务？
    ├─ 是 → 使用多线程（threading）
    └─ 否 → 考虑异步 I/O（asyncio）
"""
```

---

## 综合示例

### 示例 1：Web 服务器（多线程）

```python
import threading
import socket

def handle_client(client_socket):
    """处理客户端请求"""
    request = client_socket.recv(1024).decode()
    print(f"收到请求:\n{request}")

    # 发送响应
    response = "HTTP/1.1 200 OK\r\n\r\nHello, World!"
    client_socket.send(response.encode())
    client_socket.close()

def start_server(host='localhost', port=8080):
    """启动服务器"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"服务器启动: {host}:{port}")

    while True:
        client, addr = server.accept()
        print(f"客户端连接: {addr}")

        # 为每个客户端创建线程
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# start_server()  # 启动服务器
```

### 示例 2：数据处理（多进程）

```python
from multiprocessing import Pool
import time

def process_chunk(chunk):
    """处理数据块"""
    # 模拟数据处理
    result = sum(x * x for x in chunk)
    return result

def process_large_dataset(data, num_workers=4):
    """处理大数据集"""
    # 分块
    chunk_size = len(data) // num_workers
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # 使用进程池处理
    with Pool(num_workers) as pool:
        results = pool.map(process_chunk, chunks)

    return sum(results)

if __name__ == '__main__':
    # 生成大数据集
    data = list(range(10000000))

    start = time.time()
    result = process_large_dataset(data)
    print(f"结果: {result}")
    print(f"耗时: {time.time() - start:.2f} 秒")
```

### 示例 3：生产者-消费者模式

```python
import threading
import queue
import time
import random

def producer(q, name):
    """生产者"""
    for i in range(5):
        item = f"{name}-{i}"
        q.put(item)
        print(f"{name} 生产: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(q, name):
    """消费者"""
    while True:
        try:
            item = q.get(timeout=1)
            print(f"{name} 消费: {item}")
            time.sleep(random.uniform(0.2, 0.8))
            q.task_done()
        except queue.Empty:
            break

# 创建队列
q = queue.Queue()

# 创建生产者线程
producers = [
    threading.Thread(target=producer, args=(q, f'生产者{i}'))
    for i in range(2)
]

# 创建消费者线程
consumers = [
    threading.Thread(target=consumer, args=(q, f'消费者{i}'))
    for i in range(3)
]

# 启动所有线程
for p in producers:
    p.start()
for c in consumers:
    c.start()

# 等待所有线程
for p in producers:
    p.join()
for c in consumers:
    c.join()

print("所有任务完成")
```

---

## 总结

本章介绍了 Python 的并发编程：

### 11.1 并发与并行
- **并发**：同一时间段处理多个任务
- **并行**：同一时刻执行多个任务

### 11.2 多进程
- **创建进程**：Process 类、自定义进程类
- **进程池**：Pool 管理多个进程
- **进程间通信**：Queue、Pipe、Manager

### 11.3 多线程
- **创建线程**：Thread 类、自定义线程类
- **线程池**：ThreadPoolExecutor
- **互斥锁**：保护共享资源
- **GIL**：限制了 CPU 密集型任务的并行

### 11.4 进程和线程对比
- **进程**：适合 CPU 密集型任务
- **线程**：适合 I/O 密集型任务

掌握并发编程能够充分利用计算机资源，提高程序性能。

---

## 练习题

1. 使用多进程计算大量数据的平方和
2. 使用多线程实现文件下载器
3. 实现一个线程安全的计数器类
4. 使用进程池处理图像批量转换
5. 实现生产者-消费者模式（多线程）
6. 对比多进程和多线程处理 CPU 密集型任务的性能
7. 使用 Queue 实现进程间的数据传递
8. 编写一个多线程的网络爬虫
