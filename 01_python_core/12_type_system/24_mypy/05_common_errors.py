"""
mypy 常见错误与解决

对应文档: 17-type-system-checkers.md § 17.mypy
"""

# 错误 1: 缺少注解 (Missing type annotation)
# 错误: def add(a, b):
def add(a: int, b: int) -> int: # 修复: 添加注解
    return a + b

# 错误 2: 返回类型不匹配 (Incompatible return value type)
def get_name() -> str:
    # return 123 # 错误: 返回了 int
    return "Alice" # 修复

# 错误 3: 可选值未处理 (Item "None" has no attribute)
def find_user(id: int) -> str | None:
    return "User" if id > 0 else None

def process_user():
    name = find_user(1)
    # print(name.upper()) # 错误: name 可能是 None
    
    if name is not None:
        print(name.upper()) # 修复: 增加判空保护

# 错误 4: 缺少导入定义 (Ignore missing imports)
# import some_weird_lib # 错误: 找不到该库的类型信息
# 解决: 安装 types-xxx 包，或者在配置中忽略
