"""
主流类型检查器对比

对应文档: 17-type-system-checkers.md § 17.overview
"""

# | 特性 | mypy | pyright |
# | :--- | :--- | :--- |
# | **背景** | 官方社区支持 | 微软开发 (VS Code Pylance 核心) |
# | **性能** | 中等 (Python 编写) | 极快 (Node.js/TS 编写) |
# | **严格度** | 可高度自定义 | 默认较严格 |
# | **插件** | 丰富 (如 pydantic, sqlalchemy) | 较少 |
# | **适用** | 传统项目、复杂插件需求 | 大型项目、VS Code 用户 |

def demo_diff():
    """
    某些复杂的类型推断，pyright 可能比 mypy 更聪明；
    而对于特定的第三方库，mypy 可能因为有专门的插件而更准确。
    """
    pass

if __name__ == '__main__':
    print("选择建议：")
    print("- 新项目首选 pyright (快，集成好)")
    print("- 有特殊插件需求或老项目维护选 mypy")
