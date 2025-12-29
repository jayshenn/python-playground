"""
辅助模块：演示模块导入

本文件仅用于被其他文件导入演示，不直接运行。
"""

# 全局变量
version = "1.0.0"
author = "Gemini AI"

# 函数
def add(a, b):
    return a + b

def info():
    print(f"模块作者: {author}, 版本: {version}")

# 类
class MyClass:
    def __init__(self):
        print("MyClass 实例已创建")

# 控制导出 (用于 05_all_variable.py)
__all__ = ['add', 'info'] 
