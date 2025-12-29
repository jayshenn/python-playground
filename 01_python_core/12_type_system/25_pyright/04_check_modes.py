"""
pyright 类型检查模式

对应文档: 17-type-system-checkers.md § 17.pyright
"""

# Pyright 提供了四种预设的检查强度：

# 1. "off"
#    几乎不检查，仅报告语法错误。适用于极其庞大的老旧项目。

# 2. "basic" (默认)
#    提供平衡的类型检查，适合大多数生产项目。

# 3. "standard"
#    比 basic 更严格，会报告更多潜在的类型不确定性。

# 4. "strict"
#    最严格模式。禁止隐式的 Any，要求完整的类型标注。
#    类似于 mypy --strict。

if __name__ == '__main__':
    print("推荐新项目开启 'standard' 或 'strict' 模式以获得最佳安全性。")
