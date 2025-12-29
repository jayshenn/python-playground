"""
函数签名优先原则

对应文档: 17-type-system-checkers.md § 17.best
"""

# 类型系统的价值主要体现在函数之间的契约上

# ✅ 始终为函数签名提供完整注解
def calculate_price(unit_price: float, quantity: int, tax_rate: float) -> float:
    # 内部推断
    subtotal = unit_price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

# 这样做的好处：
# 1. 外部调用者能得到精准的 IDE 提示
# 2. 检查器能捕获调用时的参数错误
# 3. 函数体内部逻辑会自动基于参数类型获得检查

if __name__ == '__main__':
    total = calculate_price(99.9, 2, 0.1)
    print(f"Total: {total}")
