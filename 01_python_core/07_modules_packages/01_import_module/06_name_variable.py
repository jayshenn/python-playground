"""
__name__

对应文档: 09-modules-and-packages.md § 9.3.6
"""

# __name__ 是 Python 中的内置变量
# 1. 如果文件是直接运行的，__name__ 的值是 "__main__"
# 2. 如果文件是被导入的，__name__ 的值是 模块名

def main():
    print("这是一段核心业务逻辑，只有在直接运行本文件时才执行。")

# 习惯用法：程序入口检查
if __name__ == '__main__':
    print(f"当前文件的 __name__ 是: {__name__}")
    main()
else:
    print(f"文件被导入了，__name__ 是: {__name__}")
