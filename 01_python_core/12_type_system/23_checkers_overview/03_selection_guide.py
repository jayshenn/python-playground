"""
类型检查器选择建议

对应文档: 17-type-system-checkers.md § 17.overview
"""

# 场景化的选择建议：

def scenario_based_choice():
    # 场景 A: 我使用 VS Code，想要极速反馈
    # 建议: 开启 Pylance (内部就是 pyright)
    
    # 场景 B: 我的项目使用了 Django 或 SQLAlchemy
    # 建议: 使用 mypy + 对应的插件 (django-stubs 等)
    
    # 场景 C: 我们在 CI 中需要一个权威的检查
    # 建议: mypy 是业界标准，适合作为 CI 的最终防线
    
    # 场景 D: 我们想要最严格的类型检查
    # 建议: 考虑 basedpyright
    pass

if __name__ == '__main__':
    print("推荐配置：本地开发用 pyright (实时反馈)，CI 跑 mypy (稳定权威)。")
