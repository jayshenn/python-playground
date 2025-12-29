"""
finally

对应文档: 08-exception-handling.md § 8.2.4
"""

# finally 块中的代码无论是否发生异常，都一定会执行
# 常用于关闭文件、断开数据库连接等收尾工作

def process_file():
    f = None
    try:
        print("正在打开文件...")
        f = open("example.txt", "w")
        f.write("Hello Python")
        # 模拟中间出现错误
        # 1 / 0 
    except Exception as e:
        print(f"处理过程中出错: {e}")
    finally:
        # 无论成功还是失败，都要确保文件被关闭
        if f:
            f.close()
            print("文件已安全关闭 (finally 块执行完毕)")

if __name__ == '__main__':
    process_file()
