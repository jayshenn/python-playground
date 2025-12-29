# 导入包 (Importing Packages)

本章节介绍 Python 中包（Package）的概念及导入方法。

## 核心知识点

1. **什么是包**：包含 `__init__.py` 文件的目录。
2. **点号语法**：使用 `包名.模块名` 的形式进行层级访问。
3. **导入粒度**：
    - 导入整个包。
    - 导入包下的特定模块。
    - 导入模块中的具体成员。
4. **__init__.py**：包的初始化文件及其在导入中的作用。

## 文件列表

- `my_package/`: 演示用的包目录。
- `01_full_import.py`: 演示如何导入包下的完整模块。
- `02_import_module_member.py`: 演示直接从包中导入模块成员。
- `03_import_package_member.py`: 演示从包下的特定模块导入成员。
- `04_import_all.py`: 演示从包中全量导入（配合 `__init__.py`）。
