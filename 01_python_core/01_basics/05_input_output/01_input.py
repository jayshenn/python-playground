"""
输入

对应文档: 01-python-basics.md § 1.5.1
"""

# 使用 input() 函数从控制台接收用户输入。

def main():
    # 基本输入
    # name = input("请输入你的名字：")
    # 为了演示方便，这里模拟输入，实际运行时请取消注释上一行
    name = "User" 
    print(f"你好，{name}！")

    # input() 返回的是字符串类型
    # age_str = input("请输入你的年龄：")
    # age = int(age_str)  # 需要转换为整数
    
    # 模拟输入
    age = 25
    print(f"你的年龄是 {age} 岁")

    # 一次性输入多个值
    # data = input("请输入三个数字，用空格分隔：")
    # a, b, c = map(int, data.split())
    
    # 模拟输入
    data = "10 20 30"
    a, b, c = map(int, data.split())
    print(f"你输入的数字是：{a}, {b}, {c}")

if __name__ == "__main__":
    main()
