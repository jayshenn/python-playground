"""
综合实战：完整项目类型检查配置

对应文档: 17-type-system-checkers.md § 17.case
"""

# --- 1. 项目代码实现 ---

from pydantic import BaseModel, Field
from typing import Sequence

class User(BaseModel):
    """底层模型"""
    id: int
    name: str = Field(min_length=1)
    email: str

class UserResponse(BaseModel):
    """API 响应模型"""
    id: int
    name: str

def format_users(users: Sequence[User]) -> list[UserResponse]:
    """业务逻辑层：将 User 模型转换为响应模型"""
    return [UserResponse(id=u.id, name=u.name) for u in users]

# --- 2. 推荐的配置文件 (以注释形式) ---

PYPROJECT_TOML_CONTENT = """
[tool.mypy]
python_version = "3.12"
strict = true
plugins = ["pydantic.mypy"] # 启用 Pydantic 插件

[tool.pyright]
include = ["src"]
typeCheckingMode = "basic"
"""

# --- 3. 运行命令 ---

def run_checks():
    """
    运行类型检查的典型命令：
    
    # 运行 mypy (使用项目配置)
    uv run mypy .
    
    # 运行 pyright
    uv run pyright
    """
    pass

if __name__ == '__main__':
    # 模拟运行
    raw_users = [User(id=1, name="Alice", email="alice@msg.com")]
    formatted = format_users(raw_users)
    print(f"Formatted: {formatted}")
    
    print("\n恭喜！你已经完成了类型系统的所有学习任务。")
    print("现在，你可以自信地在你的生产代码中使用类型注解和静态检查工具了。")
