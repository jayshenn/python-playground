# 导入模块 (Importing Modules)

本章节介绍如何在 Python 中导入和使用模块。

## 核心知识点

1. **import 语句**：导入整个模块。
2. **from ... import 语句**：导入模块中的特定成员。
3. **搜索路径**：理解 Python 如何定位模块文件（`sys.path`）。
4. **控制导出**：使用 `__all__` 变量限制 `from ... import *` 的内容。
5. **执行入口**：理解 `if __name__ == "__main__":` 的作用。

## 文件列表

- `my_module.py`: 用于演示导入的辅助模块文件。
- `01_full_import.py`: 演示使用 `import` 导入整个模块。
- `02_partial_import.py`: 演示使用 `from ... import` 导入特定成员。
- `03_import_all.py`: 介绍 `from ... import *` 及其潜在问题。
- `04_search_order.py`: 演示 Python 模块的搜索路径顺序。
- `05_all_variable.py`: 演示 `__all__` 对模块导出的控制作用。
- `06_name_variable.py`: 介绍 `__name__` 变量的妙用。
