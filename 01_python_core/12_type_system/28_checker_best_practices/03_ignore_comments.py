"""
类型忽略注释规范

对应文档: 17-type-system-checkers.md § 17.best
"""

# ❌ 不好的做法：笼统地忽略，没有任何说明
# result = call_complex_func() # type: ignore

# ✅ 好的做法：
# 1. 指定错误码 (如 [no-untyped-call])
# 2. 简要说明忽略的原因
def call_legacy_code():
    # type: ignore[no-untyped-call] # 遗留代码库，由于某些原因暂时无法添加注解
    from . import untyped_legacy
    untyped_legacy.do_something()

if __name__ == '__main__':
    print("规范：每一个 ignore 都应该有它的苦衷和解释。")
