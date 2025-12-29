"""
send()

对应文档: 10-advanced-features.md § 10.3.3
"""

# send() 方法可以将值传给 yield 表达式

def echo_generator():
    print("生成器启动...")
    while True:
        # yield 返回的值就是 send 发送过来的值
        received = yield
        if received == "stop":
            print("收到停止指令，退出")
            break
        print(f"生成器收到并回响: {received}")

if __name__ == '__main__':
    gen = echo_generator()
    
    # 1. 激活生成器 (必须先 next 或 send(None))
    next(gen)
    
    # 2. 发送数据
    gen.send("Hello")
    gen.send("Python")
    
    # 3. 发送停止信号
    try:
        gen.send("stop")
    except StopIteration:
        pass
