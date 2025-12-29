"""
pyright 配置文件示例

对应文档: 17-type-system-checkers.md § 17.pyright
"""

# pyrightconfig.json 示例
PYRIGHT_CONFIG = """
{
  "include": ["src"],
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    ".venv"
  ],
  "pythonVersion": "3.12",
  "typeCheckingMode": "basic",
  "reportMissingImports": true,
  "reportUnusedVariable": "warning"
}
"""

if __name__ == '__main__':
    print("你也可以将配置放在 pyproject.toml 中的 [tool.pyright] 节。")
