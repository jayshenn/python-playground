"""
get_type_hints() 运行时获取类型

对应文档: 15-type-system-stdlib.md § 15.utils
"""

from typing import get_type_hints

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"

class User:
    id: int
    username: str

if __name__ == '__main__':
    # 1. 获取函数的类型提示
    func_hints = get_type_hints(greet)
    print(f"Function hints: {func_hints}")
    # 输出: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
    
    # 2. 获取类的类型提示
    class_hints = get_type_hints(User)
    print(f"Class hints: {class_hints}")
    # 输出: {'id': <class 'int'>, 'username': <class 'str'>}
    
    # 3. 实际用途：简单的运行时类型验证
    def validate_call(func, **kwargs):
        hints = get_type_hints(func)
        for arg_name, expected_type in hints.items():
            if arg_name == 'return': continue
            val = kwargs.get(arg_name)
            if not isinstance(val, expected_type):
                print(f"Warning: {arg_name} expected {expected_type}, got {type(val)}")
        return func(**kwargs)

    validate_call(greet, name="Alice", age="30") # 故意传入错误的 age 类型
