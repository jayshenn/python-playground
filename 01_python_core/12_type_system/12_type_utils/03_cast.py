"""
cast()：类型转换提示

对应文档: 15-type-system-stdlib.md § 15.utils
"""

from typing import cast

def get_data_from_legacy_api() -> object:
    """模拟一个返回 object 类型的旧接口"""
    return {"id": 1, "role": "admin"}

def process_admin(data: dict[str, str | int]):
    print(f"Processing admin {data['id']}")

if __name__ == '__main__':
    raw_data = get_data_from_legacy_api()
    
    # 类型检查器此时只知道 raw_data 是 object
    # process_admin(raw_data) # 警告：object 不匹配 dict
    
    # 1. 使用 cast 显式告诉检查器：这就是我要的类型
    # 注意：cast 在运行时没有任何效果，它只是返回原对象
    clean_data = cast(dict[str, str | int], raw_data)
    
    process_admin(clean_data) # 现在检查器满意了
    
    # 2. 危险：cast 不做运行时验证
    # 即使强制转换为 int，它运行时还是个字典
    fake_int = cast(int, {"not": "an int"})
    print(f"Type: {type(fake_int)}") # 依然是 <class 'dict'>
