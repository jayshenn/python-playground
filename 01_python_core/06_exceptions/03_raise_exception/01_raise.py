"""
raise

对应文档: 08-exception-handling.md § 8.3.1
"""

def set_age(age):
    if age < 0 or age > 150:
        # 当发现逻辑不符合要求时，主动抛出异常
        raise ValueError(f"年龄超出范围: {age}")
    print(f"设置年龄成功: {age}")

if __name__ == '__main__':
    try:
        set_age(200)
    except ValueError as e:
        print(f"捕获到手动抛出的异常: {e}")
