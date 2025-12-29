"""
pyright 忽略检查

对应文档: 17-type-system-checkers.md § 17.pyright
"""

# 1. 忽略当前行所有报错
x = "string"
y = x + 10 # pyright: ignore

# 2. 忽略特定错误码 (更推荐)
z = x + 20 # pyright: ignore[reportGeneralTypeIssues]

# 3. 在文件顶部通过配置注释忽略整个文件的某类错误
# pyright: reportUnusedVariable=false

if __name__ == '__main__':
    print("注意：pyright 的 ignore 语法与 mypy (# type: ignore) 不同。")
    print("不过为了兼容，pyright 通常也能识别 # type: ignore。")
