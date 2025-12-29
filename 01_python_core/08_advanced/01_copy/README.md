# 浅拷贝与深拷贝 (Shallow Copy vs Deep Copy)

本章节介绍 Python 中对象的复制机制，特别是针对列表、字典等容器在包含嵌套对象时的行为差异。

## 核心知识点

1. **直接赋值**：只是引用的传递，两个变量指向同一个内存地址。
2. **浅拷贝 (Shallow Copy)**：创建一个新对象，但其内部的子对象仍然是引用。使用 `list.copy()` 或 `copy.copy()`。
3. **深拷贝 (Deep Copy)**：递归地创建所有子对象的副本。使用 `copy.deepcopy()`。
4. **内存分析**：理解 `id()` 函数在验证拷贝效果时的作用。

## 文件列表

- `01_shallow_copy_review.py`: 回顾浅拷贝的基本概念。
- `02_shallow_copy_case.py`: 演示浅拷贝在处理嵌套对象时的局限性。
- `03_deep_copy_review.py`: 介绍深拷贝的概念及优势。
- `04_deep_copy_case.py`: 演示深拷贝如何解决嵌套对象的修改问题。
- `05_ideal_conversion.py`: 综合对比几种复制方式的内存地址差异。
