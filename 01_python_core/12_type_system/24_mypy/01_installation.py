"""
mypy 安装说明

对应文档: 17-type-system-checkers.md § 17.mypy
"""

def install_mypy():
    """
    # 1. 使用 pip 安装
    pip install mypy
    
    # 2. 使用 uv 安装 (推荐)
    uv add --dev mypy
    
    # 3. 安装常用插件
    uv add --dev types-requests  # requests 库的类型定义
    uv add --dev types-redis     # redis 库的类型定义
    """
    pass

if __name__ == '__main__':
    try:
        import mypy
        print(f"mypy is installed. Version is accessible via CLI.")
    except ImportError:
        print("mypy not found. Please follow the installation steps.")
