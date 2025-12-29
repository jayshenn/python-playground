"""
GitHub Actions CI 配置示例

对应文档: 17-type-system-checkers.md § 17.cicd
"""

# .github/workflows/type-check.yml 示例：

YAML_CONFIG = """
name: Type Check

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install uv
        run: pip install uv
      - name: Install dependencies
        run: uv sync
      - name: Run mypy
        run: uv run mypy src/
      - name: Run pyright
        run: uv run pyright src/
"""

if __name__ == '__main__':
    print("将上面的 YAML 内容保存到项目根目录的 .github/workflows/ 目录下即可生效。")
