"""
pre-commit 集成示例

对应文档: 17-type-system-checkers.md § 17.cicd
"""

# .pre-commit-config.yaml 示例：

PRE_COMMIT_CONFIG = """
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v1.8.0'
    hooks:
      - id: mypy
        additional_dependencies: [pydantic, types-requests]
        args: [--config-file=pyproject.toml]

  - repo: https://github.com/RobertCraigie/pyright-python
    rev: 'v1.1.350'
    hooks:
      - id: pyright
"""

if __name__ == '__main__':
    print("1. 安装 pre-commit: pip install pre-commit")
    print("2. 注册钩子: pre-commit install")
    print("3. 现在每次 git commit 都会自动跑类型检查。")
