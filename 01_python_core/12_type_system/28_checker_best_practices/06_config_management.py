"""
类型检查配置管理

对应文档: 17-type-system-checkers.md § 17.best
"""

# 最佳实践：统一将所有工具配置集中在 pyproject.toml

PYPROJECT_CONFIG_EXAMPLE = """
[tool.mypy]
python_version = "3.12"
strict = true
show_error_codes = true
# 针对测试文件夹适当放宽限制
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[tool.pyright]
include = ["src"]
typeCheckingMode = "basic"
"""

if __name__ == '__main__':
    print("原则：保持配置的版本化，确保团队每个人的检查结果一致。")
