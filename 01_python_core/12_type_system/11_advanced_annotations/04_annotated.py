"""
Annotated：带元数据的类型

对应文档: 15-type-system-stdlib.md § 15.advanced
"""

from typing import Annotated

# 1. 为类型附加语义元数据
# 这些元数据不影响 Python 运行时，但可以被工具读取
type PositiveInt = Annotated[int, "Value must be > 0"]
type Username = Annotated[str, "Min length: 3", "Max length: 20"]

def create_user(user_id: PositiveInt, name: Username) -> None:
    print(f"User {name} (ID: {user_id}) created.")

# 2. 实际应用场景：模拟与框架集成 (如数据库字段定义)
type PrimaryKey = Annotated[int, "AUTO_INCREMENT", "PRIMARY KEY"]

class DatabaseModel:
    id: PrimaryKey = 0

if __name__ == '__main__':
    create_user(101, "alice")
    
    # 获取元数据
    from typing import get_type_hints
    hints = get_type_hints(create_user, include_extras=True)
    print(f"Type hints with extras: {hints}")
    
    # 打印 user_id 的元数据
    print(f"Metadata for user_id: {hints['user_id'].__metadata__}")
