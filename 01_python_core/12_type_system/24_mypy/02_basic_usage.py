"""
mypy 基本使用

对应文档: 17-type-system-checkers.md § 17.mypy
"""

def cli_commands():
    """
    # 检查单个文件
    mypy my_script.py
    
    # 检查整个包/目录
    mypy src/
    
    # 显示错误代码 (非常有用，用于精准忽略错误)
    mypy --show-error-codes src/
    
    # 增量检查 (默认开启，提升速度)
    mypy --incremental src/
    
    # 使用特定的配置文件
    mypy --config-file mypy.ini src/
    """
    pass

if __name__ == '__main__':
    print("运行 mypy 的最佳实践是使用命令行。")
    print("例: mypy 01_installation.py")
