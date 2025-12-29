"""
模块搜索顺序

对应文档: 09-modules-and-packages.md § 9.3.4
"""

# Python 导入模块时的搜索顺序：
# 1. 当前执行脚本所在的目录
# 2. PYTHONPATH 环境变量中的目录
# 3. 标准库目录
# 4. 第三方库目录 (site-packages)

import sys

if __name__ == '__main__':
    print("Python 模块搜索路径 (sys.path):")
    for path in sys.path:
        print(f" -> {path}")
    
    # 查找顺序就是这个列表的索引顺序
    print("\n注意：如果你自己定义了一个与标准库同名的文件 (如 random.py)，"
          "由于当前目录优先级最高，会导致标准库无法被正常导入。")
