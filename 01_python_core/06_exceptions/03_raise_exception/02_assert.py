"""
assert 断言

对应文档: 08-exception-handling.md § 8.3.2
"""

# assert 语法: assert condition, message
# 如果 condition 为 False，则抛出 AssertionError 并输出 message

def calculate_average(scores):
    # 断言：列表不能为空
    assert len(scores) > 0, "成绩列表不能为空"
    return sum(scores) / len(scores)

if __name__ == '__main__':
    print(f"平均分: {calculate_average([90, 80, 70])}")
    
    try:
        calculate_average([]) # 触发断言
    except AssertionError as e:
        print(f"断言失败: {e}")

# 注意：assert 通常用于调试阶段，在生产环境中可以通过 python -O 禁用
