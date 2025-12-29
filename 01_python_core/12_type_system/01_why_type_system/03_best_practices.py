"""
现代项目中的最佳实践

对应文档: 14-type-system-basics.md § 14.why
"""

def main():
    print("--- 类型系统最佳实践 ---")
    print("1. 核心业务逻辑必须添加类型提示。")
    print("2. 公开的 API 和库函数必须提供完整的类型注解。")
    print("3. 使用 mypy 或 pyright 作为 CI/CD 流程中的强制检查环节。")
    print("4. 不要过度追求 100% 的覆盖，允许在极少数极端动态场景下使用 Any。")
    print("5. 结合 Pydantic 进行运行时数据验证。")

if __name__ == '__main__':
    main()
