"""
Settings 管理 (环境变量)

对应文档: 16-type-system-pydantic.md § 16.integration
"""

# 需要安装: pip install pydantic-settings
try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("Please install pydantic-settings to run this example: pip install pydantic-settings")
    import sys
    sys.exit(0)

from pydantic import Field

class AppSettings(BaseSettings):
    """
    配置类：自动从环境变量中读取值。
    环境变量名默认与字段名一致 (不区分大小写)。
    """
    # 自动读取环境变量 APP_NAME
    app_name: str = "MyGenericApp"
    
    # 自动读取环境变量 API_KEY
    # 使用 alias 可以映射不同的环境变量名
    api_key: str = Field(..., alias="MY_APP_API_KEY")
    
    # 自动读取环境变量 DB_PORT 并转为 int
    db_port: int = 5432
    
    # 配置从 .env 文件读取
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

if __name__ == '__main__':
    # 为了演示，我们手动设置环境变量
    import os
    os.environ["MY_APP_API_KEY"] = "sk-123456"
    os.environ["DB_PORT"] = "6543"
    
    settings = AppSettings()
    
    print(f"App Name: {settings.app_name}")
    print(f"API Key: {settings.api_key}")
    print(f"DB Port: {settings.db_port} (type: {type(settings.db_port)})")
