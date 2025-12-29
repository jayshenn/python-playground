# 动态操作 (Dynamic Operations)

本章节介绍 Python 面向对象编程中的动态特性，即在程序运行时动态地添加或修改属性和方法，以及如何通过 `__slots__` 机制进行限制。

## 核心知识点

1. **动态属性**：可以在运行时随时为对象或类添加新的属性。
2. **动态方法**：可以将外部定义的函数绑定到对象（需使用 `types.MethodType`）或类上。
3. **删除操作**：使用 `delattr()` 或 `del` 动态删除成员。
4. **属性限制**：使用 `__slots__` 变量限制实例能添加的属性名称，起到节省内存和规范代码的作用。

## 文件列表

- `01_add_instance_attribute.py`: 演示动态为单个对象添加属性。
- `02_add_class_attribute.py`: 演示动态为整个类添加属性。
- `03_add_instance_method.py`: 演示动态为单个对象绑定方法。
- `04_add_class_method.py`: 演示动态为类绑定方法（所有实例受益）。
- `05_delete_attr_method.py`: 演示动态删除属性和方法。
- `06_slots.py`: 介绍 `__slots__` 的作用和限制。
