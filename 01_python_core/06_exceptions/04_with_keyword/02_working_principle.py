"""
工作原理

对应文档: 08-exception-handling.md § 8.6.2
"""

# 实现上下文管理协议需要定义 __enter__ 和 __exit__ 方法

class MyResource:
    def __enter__(self):
        print("--- 进入上下文 (执行 __enter__) ---")
        return self  # 返回的对象会赋给 with ... as 后的变量
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- 退出上下文 (执行 __exit__) ---")
        # exc_type: 异常类型, exc_val: 异常值, exc_tb: 异常追踪信息
        if exc_type:
            print(f"检测到异常: {exc_val}")
        return True # 返回 True 表示异常已被处理，不再向上抛出

if __name__ == '__main__':
    with MyResource() as res:
        print("正在执行业务逻辑...")
        # raise ValueError("手动制造一个异常")
    
    print("程序结束")
