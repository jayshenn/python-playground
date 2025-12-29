"""
assert_never()：穷举检查

对应文档: 15-type-system-stdlib.md § 15.utils
"""

from typing import Literal, assert_never

type Status = Literal["pending", "approved", "rejected"]

def get_status_label(status: Status) -> str:
    if status == "pending":
        return "待处理"
    elif status == "approved":
        return "已通过"
    elif status == "rejected":
        return "已拒绝"
    else:
        # 1. 静态检查：如果你在 Status 中添加了新状态但这里没处理，
        # 类型检查器会在这里报错。
        # 2. 运行时检查：如果真的执行到这里，会抛出 AssertionError。
        assert_never(status)

if __name__ == '__main__':
    print(get_status_label("approved"))
    
    # 尝试传入非合法值 (绕过类型检查)
    try:
        get_status_label("unknown") # type: ignore
    except AssertionError as e:
        print(f"Caught expected error: {e}")
