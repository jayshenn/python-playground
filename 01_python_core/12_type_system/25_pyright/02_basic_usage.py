"""
pyright 基本使用

对应文档: 17-type-system-checkers.md § 17.pyright
"""

def cli_usage():
    """
    # 检查当前目录
    pyright
    
    # 检查特定路径
    pyright src/
    
    # 持续监听模式 (监视文件变化并实时检查)
    pyright --watch
    
    # 指定虚拟环境路径 (这对正确寻找第三方库很重要)
    pyright --venv-path . --venv .venv
    """
    pass

if __name__ == '__main__':
    print("Pyright 命令行工具对于在 CI/CD 中进行检查非常有用。")
