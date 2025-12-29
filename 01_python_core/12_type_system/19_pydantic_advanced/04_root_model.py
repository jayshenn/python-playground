"""
RootModel 根类型

对应文档: 16-type-system-pydantic.md § 16.advanced
"""

from pydantic import RootModel

# 1. 列表模型：用于顶层是数组的 JSON
class NameList(RootModel[list[str]]):
    pass

# 2. 键为字符串，值为整数的字典模型
class Scores(RootModel[dict[str, int]]):
    pass

if __name__ == '__main__':
    # 创建列表模型实例
    names = NameList(["Alice", "Bob", "Charlie"])
    # 访问原始数据需要使用 .root 属性
    print(f"Names root: {names.root}")
    # 支持迭代
    for name in names:
        print(f"Name: {name}")
    
    # 创建字典模型实例
    scores = Scores({"Math": 90, "English": 85})
    print(f"Math score: {scores.root['Math']}")
    
    # 导出时，RootModel 会直接导出为对应的原始类型，而不是包装后的对象
    print(f"Exported JSON: {names.model_dump_json()}") # ["Alice", "Bob", "Charlie"]
