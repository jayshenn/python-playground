"""
忽略类型检查

对应文档: 17-type-system-checkers.md § 17.mypy
"""

# 1. 忽略整行 (不推荐，太笼统)
x = "string"
y = x + 10 # type: ignore

# 2. 忽略特定错误码 (推荐，更精确)
# 这里的 [operator] 告诉 mypy 只忽略操作符不匹配错误
z = x + 20 # type: ignore[operator]

# 3. 忽略整个文件的错误
# 在文件顶部添加： # mypy: ignore-errors

# 4. 忽略某个函数
def legacy_function(): # type: ignore
    pass

if __name__ == '__main__':
    print("原则：尽可能修复错误，只有在第三方库问题或极端特殊情况才使用 ignore。")
