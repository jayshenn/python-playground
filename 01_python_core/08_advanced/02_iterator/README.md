# 迭代器 (Iterators)

本章节介绍 Python 中的迭代协议，理解 `for` 循环的工作原理。

## 核心知识点

1. **可迭代对象 (Iterable)**：实现了 `__iter__` 方法的对象（如列表、元组、字符串）。
2. **迭代器 (Iterator)**：实现了 `__iter__` 和 `__next__` 方法的对象。迭代器记录了遍历的位置。
3. **迭代过程**：通过 `iter()` 获取迭代器，通过 `next()` 获取下一个值，直到抛出 `StopIteration` 异常。
4. **自定义迭代器**：通过编写包含 `__iter__` 和 `__next__` 的类来创建自己的迭代逻辑。

## 文件列表

- `01_iterable_object.py`: 介绍如何判断一个对象是否可迭代。
- `02_use_iterator.py`: 演示迭代器的基本用法（iter 和 next）。
- `03_custom_iterator.py`: 演示如何实现一个自定义的迭代器类。
