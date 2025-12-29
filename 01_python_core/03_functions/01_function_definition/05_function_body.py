"""
函数体

对应文档: 04-functions.md § 4.2.5
"""

# 函数体是函数执行的代码块，必须缩进。

def process_data(data):
    # 验证数据
    if not data:
        return None

    # 处理数据
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)

    # 返回结果
    return result

numbers = [1, -2, 3, -4, 5]
processed = process_data(numbers)
print(f"Original: {numbers}")
print(f"Processed (positive * 2): {processed}")

# 空数据测试
print(f"Empty input: {process_data([])}")
