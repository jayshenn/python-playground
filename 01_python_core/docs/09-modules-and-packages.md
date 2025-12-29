# 第 9 章 模块与包

随着程序规模的增大，将所有代码放在一个文件中会变得难以维护。Python 提供了**模块**和**包**的机制，让我们能够组织和复用代码。

---

## 9.1 模块概述

**模块**（Module）是包含 Python 定义和语句的文件，文件名就是模块名加上 `.py` 后缀。

### 为什么需要模块？

1. **代码复用**：避免重复编写相同的代码
2. **命名空间**：避免变量名冲突
3. **代码组织**：将相关功能组织在一起
4. **易于维护**：分模块管理，便于修改和调试

### 模块的类型

**1. 内置模块**
- Python 解释器内置的模块
- 无需安装，可直接导入
- 示例：`sys`, `os`, `math`, `random`

**2. 标准库模块**
- Python 自带的模块库
- 无需安装，但需要导入
- 示例：`datetime`, `json`, `re`, `collections`

**3. 第三方模块**
- 需要通过 pip 安装
- 由社区开发和维护
- 示例：`numpy`, `pandas`, `requests`, `flask`

**4. 自定义模块**
- 自己编写的 Python 文件
- 可以被其他模块导入使用

```python
# 查看 Python 版本和路径
import sys
print(f"Python 版本: {sys.version}")
print(f"Python 路径: {sys.executable}")

# 查看模块搜索路径
print("\n模块搜索路径:")
for path in sys.path:
    print(f"  {path}")
```

---

## 9.2 创建模块

创建模块非常简单，只需要创建一个 `.py` 文件即可。

### 示例：创建一个数学工具模块

**文件：`math_tools.py`**
```python
"""
数学工具模块

提供常用的数学计算函数
"""

# 模块级常量
PI = 3.14159
E = 2.71828

# 函数定义
def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 类定义
class Calculator:
    """计算器类"""

    def __init__(self):
        self.history = []

    def calculate(self, a, b, operation):
        """执行计算"""
        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = subtract(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            result = divide(a, b)
        else:
            raise ValueError(f"不支持的运算: {operation}")

        self.history.append(f"{a} {operation} {b} = {result}")
        return result

    def show_history(self):
        """显示历史记录"""
        for record in self.history:
            print(record)

# 模块测试代码
if __name__ == "__main__":
    # 这部分代码只在直接运行模块时执行
    print("测试数学工具模块")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"5! = {factorial(5)}")
```

**模块的最佳实践**：

1. **添加文档字符串**：说明模块的功能
2. **使用 `if __name__ == "__main__"`**：区分模块导入和直接运行
3. **遵循命名规范**：模块名使用小写字母和下划线
4. **保持单一职责**：一个模块只做一件事

---

## 9.3 导入模块

Python 提供了多种导入模块的方式。

### 9.3.1 全部导入 import

使用 `import` 导入整个模块。

**语法**：
```python
import 模块名
```

**示例**：

```python
# 导入整个模块
import math_tools

# 使用模块中的函数
result = math_tools.add(10, 5)
print(result)  # 15

# 使用模块中的常量
print(math_tools.PI)  # 3.14159

# 使用模块中的类
calc = math_tools.Calculator()
calc.calculate(10, 5, '+')
calc.show_history()
```

**导入多个模块**：

```python
import os
import sys
import math

# 或者写在一行（不推荐，PEP 8 建议分开写）
import os, sys, math
```

**使用别名**：

```python
# 给模块起别名
import math_tools as mt

result = mt.add(10, 5)
print(result)  # 15

# 常见的别名惯例
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

### 9.3.2 局部导入 from import

从模块中导入特定的成员。

**语法**：
```python
from 模块名 import 成员名
```

**示例**：

```python
# 导入特定的函数
from math_tools import add, subtract

# 直接使用函数（不需要模块前缀）
result1 = add(10, 5)
result2 = subtract(10, 5)
print(result1, result2)  # 15 5

# 导入类
from math_tools import Calculator

calc = Calculator()
calc.calculate(10, 5, '+')
```

**导入并使用别名**：

```python
from math_tools import add as addition
from math_tools import Calculator as Calc

result = addition(10, 5)
calc = Calc()
```

### 9.3.3 局部导入 from import *

导入模块中的所有公开成员。

**语法**：
```python
from 模块名 import *
```

**示例**：

```python
# 导入所有公开成员
from math_tools import *

# 直接使用所有函数和类
result = add(10, 5)
print(PI)
calc = Calculator()
```

**注意**：不推荐使用 `from module import *`，因为：
1. 可能导致命名冲突
2. 不清楚导入了哪些名称
3. 影响代码可读性

```python
# 不好的做法
from math_tools import *
from string_tools import *  # 可能覆盖 math_tools 的成员

# 好的做法
from math_tools import add, subtract
from string_tools import capitalize, reverse
```

### 9.3.4 模块搜索顺序

Python 按照以下顺序搜索模块：

1. **当前目录**：首先在当前目录查找
2. **PYTHONPATH**：环境变量中指定的目录
3. **标准库目录**：Python 标准库的安装目录
4. **site-packages**：第三方库的安装目录

```python
import sys

# 查看模块搜索路径
print("模块搜索路径:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# 添加自定义搜索路径
sys.path.append('/path/to/my/modules')
```

**模块搜索示例**：

```python
# 假设有以下目录结构：
# project/
# ├── main.py
# ├── utils.py
# └── lib/
#     └── helper.py

# 在 main.py 中：
import utils        # 可以直接导入（同一目录）
# import helper     # 错误：不在搜索路径中

# 需要先添加路径
import sys
sys.path.append('./lib')
import helper       # 现在可以导入了
```

### 9.3.5 __all__

`__all__` 变量定义了 `from module import *` 时导出的成员。

**在模块中定义 __all__**：

```python
# math_tools.py
__all__ = ['add', 'subtract', 'PI']  # 只导出这些成员

PI = 3.14159
E = 2.71828  # 不会被 * 导出

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def _internal_function():  # 私有函数（以 _ 开头）
    pass
```

**使用示例**：

```python
from math_tools import *

print(add(1, 2))      # 可以使用
print(subtract(5, 3)) # 可以使用
print(PI)             # 可以使用

# print(E)              # NameError：E 不在 __all__ 中
# _internal_function()  # NameError：私有函数不导出
```

**__all__ 的好处**：
1. 明确模块的公共接口
2. 避免导出内部实现细节
3. 提高代码的可维护性

### 9.3.6 __name__

`__name__` 是模块的内置属性，表示模块的名称。

**__name__ 的值**：
- 当模块被直接运行时：`__name__` 的值为 `"__main__"`
- 当模块被导入时：`__name__` 的值为模块名

```python
# my_module.py
print(f"模块名: {__name__}")

def greet():
    print("Hello from my_module")

if __name__ == "__main__":
    # 这部分代码只在直接运行时执行
    print("模块被直接运行")
    greet()
else:
    print("模块被导入")
```

**运行结果**：

```python
# 直接运行：python my_module.py
# 输出：
# 模块名: __main__
# 模块被直接运行
# Hello from my_module

# 导入使用：
import my_module
# 输出：
# 模块名: my_module
# 模块被导入
```

**实际应用**：

```python
# utils.py
def process_data(data):
    """处理数据"""
    return [x * 2 for x in data]

def main():
    """主函数：用于测试"""
    test_data = [1, 2, 3, 4, 5]
    result = process_data(test_data)
    print(f"测试结果: {result}")

if __name__ == "__main__":
    # 只在直接运行时执行测试
    main()
```

---

## 9.4 dir()

`dir()` 函数用于列出模块中的所有成员。

**基本用法**：

```python
import math

# 查看模块的所有成员
members = dir(math)
print(members)

# 常用的数学函数
print(f"π = {math.pi}")
print(f"e = {math.e}")
print(f"sin(π/2) = {math.sin(math.pi / 2)}")
print(f"sqrt(16) = {math.sqrt(16)}")
```

**过滤私有成员**：

```python
import math

# 只显示公共成员（不以 _ 开头）
public_members = [name for name in dir(math) if not name.startswith('_')]
print(f"公共成员: {public_members}")
```

**查看自定义模块**：

```python
# 创建一个简单的模块
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass

MY_CONSTANT = 42

def my_function():
    pass

# 查看当前模块的成员
print(dir())

# 查看类的成员
print(dir(MyClass))
```

**实用技巧**：

```python
import math

# 1. 查找特定功能
print("包含 'sin' 的函数:")
for name in dir(math):
    if 'sin' in name.lower():
        print(f"  {name}")

# 2. 获取帮助信息
help(math.sqrt)

# 3. 检查是否存在某个属性
if hasattr(math, 'pi'):
    print(f"math.pi = {math.pi}")

# 4. 动态获取属性
attr_name = 'sqrt'
if hasattr(math, attr_name):
    func = getattr(math, attr_name)
    print(f"{attr_name}(16) = {func(16)}")
```

---

## 9.5 包概述

**包**（Package）是包含多个模块的目录，必须包含一个 `__init__.py` 文件。

### 为什么需要包？

1. **组织大型项目**：将相关模块组织在一起
2. **避免命名冲突**：不同包可以有同名模块
3. **层次化管理**：建立清晰的代码结构
4. **便于发布**：可以作为一个整体分发

### 包的结构

```
my_package/
├── __init__.py       # 包的初始化文件（必需）
├── module1.py        # 模块 1
├── module2.py        # 模块 2
└── subpackage/       # 子包
    ├── __init__.py   # 子包的初始化文件
    ├── module3.py    # 模块 3
    └── module4.py    # 模块 4
```

**包 vs 模块**：

| 特性 | 模块 | 包 |
|------|------|-----|
| **本质** | Python 文件 | 包含 `__init__.py` 的目录 |
| **包含内容** | 函数、类、变量 | 多个模块和子包 |
| **导入方式** | `import module` | `import package.module` |
| **用途** | 单个功能单元 | 组织多个模块 |

---

## 9.6 创建包

创建包非常简单，只需创建一个目录并添加 `__init__.py` 文件。

### 示例：创建一个工具包

**目录结构**：
```
utils/
├── __init__.py
├── string_utils.py
├── math_utils.py
└── file_utils.py
```

**1. 创建包目录**：
```bash
mkdir utils
```

**2. 创建 `__init__.py`**：

**文件：`utils/__init__.py`**
```python
"""
工具包

提供字符串、数学和文件处理工具
"""

# 包的版本信息
__version__ = '1.0.0'
__author__ = 'Your Name'

# 导入子模块，方便使用
from .string_utils import *
from .math_utils import *
from .file_utils import *

# 定义公共接口
__all__ = ['reverse_string', 'capitalize_words', 'add', 'multiply', 'read_file', 'write_file']

print(f"utils 包已加载，版本: {__version__}")
```

**3. 创建模块**：

**文件：`utils/string_utils.py`**
```python
"""字符串工具模块"""

def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def capitalize_words(s):
    """首字母大写"""
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    """统计单词数量"""
    return len(s.split())

def remove_spaces(s):
    """移除所有空格"""
    return s.replace(' ', '')
```

**文件：`utils/math_utils.py`**
```python
"""数学工具模块"""

def add(a, b):
    """加法"""
    return a + b

def multiply(a, b):
    """乘法"""
    return a * b

def power(base, exp):
    """幂运算"""
    return base ** exp

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**文件：`utils/file_utils.py`**
```python
"""文件工具模块"""

def read_file(filename):
    """读取文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def write_file(filename, content):
    """写入文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(filename, content):
    """追加到文件"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(content)

def file_exists(filename):
    """检查文件是否存在"""
    import os
    return os.path.exists(filename)
```

### 创建子包

**目录结构**：
```
utils/
├── __init__.py
├── string_utils.py
├── math_utils.py
├── file_utils.py
└── advanced/              # 子包
    ├── __init__.py
    ├── crypto_utils.py
    └── network_utils.py
```

**文件：`utils/advanced/__init__.py`**
```python
"""高级工具子包"""

from .crypto_utils import *
from .network_utils import *
```

**文件：`utils/advanced/crypto_utils.py`**
```python
"""加密工具模块"""

def simple_encrypt(text, shift=3):
    """简单的凯撒加密"""
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result.append(encrypted)
        else:
            result.append(char)
    return ''.join(result)

def simple_decrypt(text, shift=3):
    """简单的凯撒解密"""
    return simple_encrypt(text, -shift)
```

---

## 9.7 导入包

有多种方式导入和使用包。

### 9.7.1 全部导入 import

导入整个包或包中的模块。

```python
# 方式 1：导入包（执行 __init__.py）
import utils
print(f"包版本: {utils.__version__}")

# 方式 2：导入包中的模块
import utils.string_utils
result = utils.string_utils.reverse_string("Hello")
print(result)  # olleH

# 方式 3：导入子包中的模块
import utils.advanced.crypto_utils
encrypted = utils.advanced.crypto_utils.simple_encrypt("Hello")
print(encrypted)
```

### 9.7.2 局部导入模块下的成员 from import

从包中的模块导入特定成员。

```python
# 从模块导入函数
from utils.string_utils import reverse_string, capitalize_words
from utils.math_utils import add, multiply

result1 = reverse_string("Python")
result2 = capitalize_words("hello world")
result3 = add(10, 5)

print(result1)  # nohtyP
print(result2)  # Hello World
print(result3)  # 15
```

### 9.7.3 局部导入包下模块的成员 from import

从子包导入成员。

```python
# 从子包的模块导入
from utils.advanced.crypto_utils import simple_encrypt, simple_decrypt

encrypted = simple_encrypt("Secret", shift=5)
decrypted = simple_decrypt(encrypted, shift=5)

print(f"加密: {encrypted}")
print(f"解密: {decrypted}")
```

### 9.7.4 局部导入 from import * 从包中导入模块

如果 `__init__.py` 中定义了 `__all__`，可以使用 `*` 导入。

```python
# 导入 __init__.py 中定义的所有公共成员
from utils import *

# 直接使用函数
result1 = reverse_string("Hello")
result2 = add(10, 5)
result3 = read_file('test.txt')

print(result1)
print(result2)
```

**包导入的最佳实践**：

```python
# 推荐：明确导入需要的成员
from utils.string_utils import reverse_string
from utils.math_utils import add, multiply

# 可以：导入模块
import utils.string_utils as su
import utils.math_utils as mu

# 不推荐：使用 *（除非明确知道导入了什么）
from utils import *
```

---

## 9.8 常用标准库（包）

Python 标准库提供了丰富的功能。

### 常用标准库列表

#### 1. 系统和文件操作

```python
import os
import sys
import pathlib

# os：操作系统接口
print(f"当前目录: {os.getcwd()}")
print(f"目录内容: {os.listdir('.')}")

# sys：系统相关
print(f"Python 版本: {sys.version}")
print(f"命令行参数: {sys.argv}")

# pathlib：路径操作（推荐）
from pathlib import Path
path = Path('.')
print(f"绝对路径: {path.absolute()}")
```

#### 2. 日期和时间

```python
import datetime
import time

# datetime：日期时间
now = datetime.datetime.now()
print(f"当前时间: {now}")
print(f"格式化: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# time：时间相关
print(f"时间戳: {time.time()}")
time.sleep(1)  # 暂停 1 秒
```

#### 3. 数学运算

```python
import math
import random
import statistics

# math：数学函数
print(f"π = {math.pi}")
print(f"sin(π/2) = {math.sin(math.pi / 2)}")
print(f"√16 = {math.sqrt(16)}")

# random：随机数
print(f"随机整数: {random.randint(1, 10)}")
print(f"随机选择: {random.choice(['a', 'b', 'c'])}")

# statistics：统计函数
data = [1, 2, 3, 4, 5]
print(f"平均值: {statistics.mean(data)}")
print(f"中位数: {statistics.median(data)}")
```

#### 4. 文件和数据处理

```python
import json
import csv

# json：JSON 数据处理
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print(f"JSON: {json_str}")

# 解析 JSON
parsed_data = json.loads(json_str)
print(f"解析后: {parsed_data}")

# csv：CSV 文件处理
# 可以读取和写入 CSV 文件

# 注意：不推荐使用 pickle
# pickle 存在安全风险，只在信任的数据源使用
```

#### 5. 文本处理

```python
import re
import string

# re：正则表达式
pattern = r'\d+'
text = "Python 3.12 发布于 2023"
numbers = re.findall(pattern, text)
print(f"数字: {numbers}")

# string：字符串常量
print(f"字母: {string.ascii_letters}")
print(f"数字: {string.digits}")
print(f"标点: {string.punctuation}")
```

#### 6. 集合和数据结构

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter：计数器
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(f"计数: {counter}")
print(f"最常见: {counter.most_common(2)}")

# defaultdict：默认值字典
dd = defaultdict(int)
dd['count'] += 1
print(f"defaultdict: {dd}")

# namedtuple：命名元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"点: {p}, x={p.x}, y={p.y}")

# deque：双端队列
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"deque: {dq}")
```

#### 7. 网络和 Web

```python
import urllib.request
import http.server

# urllib：URL 处理
# response = urllib.request.urlopen('https://www.python.org')
# html = response.read()

# http.server：简单 HTTP 服务器
# python -m http.server 8000
```

### 标准库速查表

| 类别 | 模块 | 功能 |
|------|------|------|
| **系统** | os, sys, pathlib | 操作系统、路径 |
| **时间** | datetime, time | 日期时间 |
| **数学** | math, random, statistics | 数学、随机、统计 |
| **数据** | json, csv | 数据格式 |
| **文本** | re, string | 正则、字符串 |
| **集合** | collections, itertools | 数据结构、迭代器 |
| **网络** | urllib, http, socket | 网络请求、服务器 |
| **并发** | threading, multiprocessing | 多线程、多进程 |
| **测试** | unittest, doctest | 单元测试 |
| **日志** | logging | 日志记录 |

---

## 9.9 导入第三方库

第三方库需要先安装才能使用。

### 9.9.1 pip 命令方式

`pip` 是 Python 的包管理工具。

**基本命令**：

```bash
# 安装包
pip install 包名

# 安装指定版本
pip install 包名==版本号

# 升级包
pip install --upgrade 包名

# 卸载包
pip uninstall 包名

# 查看已安装的包
pip list

# 查看包信息
pip show 包名

# 搜索包
pip search 关键词

# 导出依赖列表
pip freeze > requirements.txt

# 安装依赖列表
pip install -r requirements.txt
```

**实际示例**：

```bash
# 安装 requests（HTTP 库）
pip install requests

# 安装 numpy（数值计算库）
pip install numpy

# 安装 pandas（数据分析库）
pip install pandas

# 安装多个包
pip install requests numpy pandas

# 安装指定版本
pip install django==3.2.0

# 从国内镜像安装（更快）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

**配置国内镜像（永久）**：

```bash
# 阿里云
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 清华大学
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

# 中国科技大学
pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/
```

### 9.9.2 PyCharm 中导入

**方法 1：通过设置安装**

1. 打开 PyCharm
2. File → Settings → Project → Python Interpreter
3. 点击 `+` 号
4. 搜索包名
5. 点击 Install Package

**方法 2：通过终端安装**

1. 打开 PyCharm
2. View → Tool Windows → Terminal
3. 在终端中使用 pip 命令

```bash
pip install requests
```

**方法 3：从 requirements.txt 安装**

1. 创建 `requirements.txt` 文件
2. 右键点击文件
3. 选择 "Install All Packages"

### 常用第三方库

```python
# 1. requests：HTTP 请求
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

# 2. numpy：数值计算
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(f"数组: {array}")
print(f"平均值: {array.mean()}")

# 3. pandas：数据分析
import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# 4. matplotlib：数据可视化
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('y values')
plt.xlabel('x values')
# plt.show()

# 5. flask：Web 框架
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()
```

---

## 9.10 打包自己的库并发布

可以将自己的代码打包并发布到 PyPI。

### 创建可发布的包

**目录结构**：
```
my_project/
├── setup.py              # 安装配置
├── README.md             # 项目说明
├── LICENSE               # 许可证
├── requirements.txt      # 依赖列表
└── my_package/           # 包代码
    ├── __init__.py
    ├── module1.py
    └── module2.py
```

### 编写 setup.py

```python
from setuptools import setup, find_packages

setup(
    name='my_package',              # 包名
    version='1.0.0',                # 版本
    author='Your Name',             # 作者
    author_email='your@email.com',  # 邮箱
    description='A short description',  # 简短描述
    long_description=open('README.md').read(),  # 详细描述
    long_description_content_type='text/markdown',
    url='https://github.com/username/my_package',  # 项目主页
    packages=find_packages(),       # 自动查找包
    classifiers=[                   # 分类信息
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',        # Python 版本要求
    install_requires=[              # 依赖包
        'requests>=2.25.0',
        'numpy>=1.19.0',
    ],
)
```

### 打包和发布

```bash
# 1. 安装打包工具
pip install setuptools wheel twine

# 2. 构建包
python setup.py sdist bdist_wheel

# 3. 上传到 PyPI
twine upload dist/*

# 4. 安装自己的包
pip install my_package
```

### 本地安装（开发模式）

```bash
# 在包目录下执行
pip install -e .

# 或
python setup.py develop
```

---

## 综合示例

### 示例 1：创建一个完整的工具包

**目录结构**：
```
mytools/
├── __init__.py
├── string_tools.py
├── math_tools.py
├── file_tools.py
└── validators/
    ├── __init__.py
    └── email_validator.py
```

**文件：`mytools/__init__.py`**
```python
"""
MyTools 工具包

提供字符串、数学、文件处理和验证工具
"""

__version__ = '1.0.0'
__all__ = ['string_tools', 'math_tools', 'file_tools', 'validators']

from . import string_tools
from . import math_tools
from . import file_tools
from . import validators

print(f"MyTools {__version__} 已加载")
```

**文件：`mytools/validators/email_validator.py`**
```python
"""邮箱验证器"""

import re

def is_valid_email(email):
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_email(email):
    """验证邮箱（抛出异常）"""
    if not is_valid_email(email):
        raise ValueError(f"无效的邮箱地址: {email}")
    return True
```

**使用示例**：

```python
# 导入包
import mytools

# 使用字符串工具
from mytools.string_tools import reverse_string
print(reverse_string("Python"))

# 使用数学工具
from mytools.math_tools import factorial
print(factorial(5))

# 使用验证器
from mytools.validators.email_validator import is_valid_email
print(is_valid_email("test@example.com"))
```

### 示例 2：项目结构最佳实践

```
my_project/
├── README.md
├── requirements.txt
├── setup.py
├── tests/                  # 测试代码
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── docs/                   # 文档
│   └── guide.md
└── src/                    # 源代码
    └── my_package/
        ├── __init__.py
        ├── core/
        │   ├── __init__.py
        │   └── engine.py
        └── utils/
            ├── __init__.py
            └── helpers.py
```

---

## 总结

本章介绍了 Python 模块和包的核心内容：

### 9.1-9.4 模块
- **模块概述**：代码复用的基本单元
- **创建模块**：编写 `.py` 文件
- **导入模块**：import、from import、import *
- **dir()**：查看模块成员

### 9.5-9.7 包
- **包概述**：组织多个模块
- **创建包**：包含 `__init__.py` 的目录
- **导入包**：多种导入方式

### 9.8-9.10 库管理
- **标准库**：Python 自带的丰富功能
- **第三方库**：使用 pip 安装
- **打包发布**：分享自己的代码

掌握模块和包的使用是编写大型 Python 项目的基础。

---

## 练习题

1. 创建一个数学工具模块，包含常用数学函数
2. 创建一个包，包含字符串、数学和文件处理模块
3. 使用标准库 `datetime` 创建一个日期计算工具
4. 使用 `json` 模块实现配置文件的读写
5. 创建一个子包，实现不同的验证器（邮箱、手机号等）
6. 使用 `pathlib` 实现文件和目录操作
7. 编写 `setup.py`，打包自己的工具库
8. 使用 `collections` 模块实现数据统计功能
