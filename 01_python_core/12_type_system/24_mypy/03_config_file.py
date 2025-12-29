"""
mypy 配置文件示例

对应文档: 17-type-system-checkers.md § 17.mypy
"""

# 方式 A: mypy.ini (传统方式)
MYPY_INI_TEMPLATE = """
[mypy]
python_version = 3.12
warn_return_any = True
show_error_codes = True
pretty = True

# 针对特定模块的配置
[mypy-pandas.*]
ignore_missing_imports = True
"""

# 方式 B: pyproject.toml (现代推荐方式)
PYPROJECT_TOML_TEMPLATE = """
[tool.mypy]
python_version = "3.12"
strict = true
show_error_codes = true

[[tool.mypy.overrides]]
module = "numpy.*"
ignore_missing_imports = true
"""

if __name__ == '__main__':
    print("建议将配置放在 pyproject.toml 中以保持项目整洁。")
