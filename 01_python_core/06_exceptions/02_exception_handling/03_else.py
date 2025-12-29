"""
else

对应文档: 08-exception-handling.md § 8.2.3
"""

# else 块中的代码只有在 try 块没有抛出任何异常时才会执行

def check_even():
    try:
        n = int(input("请输入一个偶数: "))
        if n % 2 != 0:
             raise ValueError("这不是偶数")
    except ValueError as e:
        print(f"验证失败: {e}")
    else:
        # 成功通过 try 且没报错
        print("恭喜！验证通过，这是一个偶数。")

if __name__ == '__main__':
    check_even()
