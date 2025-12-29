"""
mypy 严格模式选项

对应文档: 17-type-system-checkers.md § 17.mypy
"""

# [mypy]
# strict = True  # 这会开启下面所有的严格选项

# 核心严格选项说明：

# 1. disallow_untyped_defs = True
#    要求所有函数必须有类型注解 (包括参数和返回值)

# 2. disallow_any_generics = True
#    禁止使用不带参数的泛型，如 list，必须写成 list[str]

# 3. check_untyped_defs = True
#    即使函数本身没有注解，也会检查其内部逻辑

# 4. no_implicit_optional = True
#    禁止 arg: str = None，必须显式写为 arg: str | None = None

# 5. warn_unused_ignores = True
#    如果某行不再报错，但你还留着 # type: ignore，检查器会警告你

if __name__ == '__main__':
    print("新项目建议开启 strict = True 以保证最高质量。")
