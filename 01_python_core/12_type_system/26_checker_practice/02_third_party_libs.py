"""
处理缺少类型信息的第三方库

对应文档: 17-type-system-checkers.md § 17.practice
"""

# 方法 1: 安装 Stub 包 (最推荐)
# 例如：pip install types-requests types-redis pandas-stubs

# 方法 2: 配置文件忽略 (适用于大量导入该库的情况)
# mypy.ini:
# [mypy-some_lib.*]
# ignore_missing_imports = True

# 方法 3: 代码中单行忽略
try:
    import legacy_untyped_lib # type: ignore
except ImportError:
    pass

# 方法 4: 使用 cast 强制赋予类型
from typing import Any, cast

def get_external_data() -> Any:
    # 假设该库返回 Any
    return {"key": "value"}

data = cast(dict[str, str], get_external_data())
# 现在你可以安全地使用 data["key"].upper() 了

if __name__ == '__main__':
    print("原则：查一下是否有现成的 types- 包，没有再考虑 ignore 或 cast。")
