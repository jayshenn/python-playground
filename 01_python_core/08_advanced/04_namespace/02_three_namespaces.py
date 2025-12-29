"""
三种命名空间

对应文档: 10-advanced-features.md § 10.4.2
"""

# 1. 内置命名空间 (Built-in): 如 abs, print, len
import builtins

# 2. 全局命名空间 (Global): 模块级别的变量
global_var = "I am global"

def outer():
    # 3. 局部命名空间 (Local): 函数内部
    local_var = "I am local"
    
    print(f"访问内置: {len([1,2,3])}")
    print(f"访问全局: {global_var}")
    print(f"访问局部: {local_var}")

if __name__ == '__main__':
    outer()
    
    # 也可以手动查看内置命名空间的内容
    # print(dir(builtins))
