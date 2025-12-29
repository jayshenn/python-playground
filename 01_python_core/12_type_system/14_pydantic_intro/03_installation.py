"""
Pydantic 安装说明

对应文档: 16-type-system-pydantic.md § 16.intro
"""

# 提示：本文件仅作为文档参考，代码本身不执行实质操作

def installation_commands():
    """
    # 1. 基础安装
    pip install pydantic
    
    # 2. 或者使用 uv (推荐)
    uv add pydantic
    
    # 3. 安装带 email 验证支持的版本
    # (这会安装 email-validator 库)
    pip install "pydantic[email]"
    
    # 4. 安装设置管理扩展 (Pydantic V2 后拆分为独立包)
    pip install pydantic-settings
    """
    pass

if __name__ == '__main__':
    import pydantic
    print(f"Pydantic Version: {pydantic.__version__}")
