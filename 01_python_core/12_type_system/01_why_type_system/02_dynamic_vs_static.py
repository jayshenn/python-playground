"""
Python 动态类型 vs 静态类型提示

对应文档: 14-type-system-basics.md § 14.why
"""

# 动态类型的风险
def process_data(data):
    # 如果 data 是 None，这里会抛出 AttributeError
    # 如果没有类型提示，开发者可能忘记处理 None 的情况
    return data.strip().upper()

# 静态类型提示的预防
def process_data_safe(data: str) -> str:
    return data.strip().upper()

if __name__ == '__main__':
    # 动态类型允许传入任何值，直到报错那一刻
    try:
        process_data(None)
    except Exception as e:
        print(f"运行时错误: {e}")
    
    print("\n引入静态检查后，我们在写代码阶段就能通过工具发现传入 None 是不合法的。")
