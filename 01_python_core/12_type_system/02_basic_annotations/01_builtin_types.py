"""
内置类型

对应文档: 14-type-system-basics.md § 14.basic
"""

# 在 Python 3.6+ 中，可以使用 变量名: 类型 = 初始值 的方式进行注解

def main():
    # 基础类型
    name: str = "Alice"
    age: int = 30
    price: float = 9.99
    is_active: bool = True
    
    print(f"{name} is {age} years old.")

if __name__ == '__main__':
    main()
