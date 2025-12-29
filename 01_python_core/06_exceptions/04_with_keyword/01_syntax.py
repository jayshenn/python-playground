"""
语法

对应文档: 08-exception-handling.md § 8.6.1
"""

# 使用 with 语句可以自动管理资源的开启和释放

def main():
    # 传统方式
    # f = open("test.txt", "w")
    # try:
    #     f.write("hello")
    # finally:
    #     f.close()

    # 使用 with 语句（更简洁、更安全）
    with open("with_demo.txt", "w", encoding="utf-8") as f:
        f.write("使用 with 语句写入的内容")
    
    # 代码运行到这里时，文件已经被自动关闭了
    print("文件操作完成并已自动关闭")

if __name__ == '__main__':
    main()
