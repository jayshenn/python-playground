"""
本地 Makefile 示例

对应文档: 17-type-system-checkers.md § 17.cicd
"""

# Makefile 示例：

MAKEFILE_CONTENT = """
.PHONY: check-types

# 运行所有类型检查
check-types:
	@echo "Running Mypy..."
	uv run mypy src/
	@echo "Running Pyright..."
	uv run pyright src/
"""

if __name__ == '__main__':
    print("使用 Makefile 可以让复杂的命令变成一个简单的词。")
    print("运行方式: make check-types")
