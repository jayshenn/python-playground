"""
案例：异常情况下的资源释放

对应文档: 08-exception-handling.md § 8.6.3
"""

def test_file_safety():
    filename = "safety_test.txt"
    
    try:
        with open(filename, "w") as f:
            print("文件已打开，准备写入数据...")
            f.write("Some data")
            
            # 故意制造一个异常
            print("发生了一个意料之外的错误！")
            result = 10 / 0 
            
    except ZeroDivisionError:
        print("捕获到除零异常")
    
    # 验证文件状态
    print(f"检查文件 '{filename}' 是否已关闭: {f.closed}")

if __name__ == '__main__':
    test_file_safety()
