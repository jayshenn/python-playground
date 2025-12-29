# 继承 (Inheritance)

本章节介绍面向对象编程中的继承特性，实现代码的复用和层级结构的构建。

## 核心知识点

1. **单继承**：子类继承自一个父类，获得父类的属性和方法。
2. **多继承**：子类可以同时继承多个父类，具备多个父类的特征。
3. **super()**：用于调用父类的方法，特别是在重写（Override）父类方法时实现逻辑扩展。
4. **方法重写**：子类定义与父类同名的方法，以覆盖或修改父类的行为。
5. **MRO (Method Resolution Order)**：Python 的方法搜索顺序，解决多继承下的命名冲突。

## 文件列表

- `01_single_inheritance.py`: 演示最基础的单继承用法。
- `02_multiple_inheritance.py`: 演示 Python 支持的多继承特性。
- `03_reuse_parent_method.py`: 演示如何使用 `super()` 复用和扩展父类逻辑。
- `04_override_overload.py`: 介绍方法重写，以及 Python 中关于重载的说明。
- `05_method_search.py`: 演示 Python 的 MRO 方法搜索顺序。
