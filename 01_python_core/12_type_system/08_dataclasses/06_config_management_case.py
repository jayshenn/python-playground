"""
实战案例：配置管理系统

对应文档: 15-type-system-stdlib.md § 15.dataclasses
"""

from dataclasses import dataclass, field
from typing import Literal

@dataclass(frozen=True)
class DBConfig:
    host: str = "localhost"
    port: int = 5432
    db_name: str = "production"

@dataclass(frozen=True)
class APIConfig:
    base_url: str
    timeout: int = 30
    retries: int = 3

@dataclass(frozen=True)
class AppSettings:
    env: Literal["dev", "prod", "test"]
    # 嵌套数据类，使用 default_factory
    db: DBConfig = field(default_factory=DBConfig)
    api: APIConfig = field(default_factory=lambda: APIConfig(base_url="https://api.v1.com"))
    
    debug: bool = False

if __name__ == '__main__':
    # 1. 默认配置
    dev_settings = AppSettings(env="dev", debug=True)
    print(f"Dev settings: {dev_settings}")
    
    # 2. 自定义嵌套配置
    prod_settings = AppSettings(
        env="prod",
        db=DBConfig(host="db.real.com", db_name="real_data"),
        api=APIConfig(base_url="https://api.real.com", timeout=60)
    )
    
    print("\n--- Production Config ---")
    print(f"Environment: {prod_settings.env}")
    print(f"DB Host: {prod_settings.db.host}")
    print(f"API URL: {prod_settings.api.base_url}")
    
    # 3. 由于设置了 frozen=True，配置是只读的
    # prod_settings.debug = True # type: ignore (运行时会报错)
