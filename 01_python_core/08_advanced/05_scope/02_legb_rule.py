"""
四种作用域 (LEGB 规则)

对应文档: 10-advanced-features.md § 10.5.2
"""

# B - Built-in (如 str, len)
# G - Global (全局)
# E - Enclosing (嵌套)
# L - Local (局部)

v = "Global V"

def outer():
    # v = "Enclosing V" # 如果注释掉这一行，会向上找 Global
    
    def inner():
        # v = "Local V" # 如果注释掉这一行，会向上找 Enclosing
        print(f"当前访问的 v 是: {v}")
    
    inner()

if __name__ == '__main__':
    outer()
    
    # 查找顺序：L -> E -> G -> B
    print(f"内置函数名 str 在内置作用域中: {str}")
