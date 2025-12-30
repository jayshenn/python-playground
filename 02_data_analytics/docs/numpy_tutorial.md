# NumPy 科学计算

## 2.1 numpy 介绍

### 什么是 NumPy？

NumPy（Numerical Python）是 Python 科学计算的基础包，提供了：

- 强大的 N 维数组对象（ndarray）
- 广播功能（Broadcasting）
- 线性代数、傅里叶变换和随机数生成工具
- 与 C/C++ 和 Fortran 代码集成的工具

### 为什么使用 NumPy？

1. **性能优势**：NumPy 的核心是用 C 语言编写的，相比纯 Python 列表运算速度快 10-100 倍
2. **内存效率**：NumPy 数组比 Python 列表占用更少的内存空间
3. **便捷性**：提供了大量数学函数和向量化运算
4. **生态系统**：是 Pandas、Matplotlib、SciPy 等科学计算库的基础

### 安装 NumPy

```bash
# 使用 uv（推荐）
uv add numpy

# 使用 pip
pip install numpy
```

### 导入 NumPy

```python
import numpy as np  # 标准导入方式
```

---

## 2.2 ndarray

### 2.2.1 ndarray 的核心特性

ndarray（N-dimensional array）是 NumPy 的核心数据结构，具有以下特性：

1. **同质性（Homogeneous）**：数组中所有元素必须是相同的数据类型
2. **固定大小**：创建后大小固定，改变大小会创建新数组并删除原数组
3. **高效存储**：在内存中连续存储，支持向量化运算
4. **多维性**：支持任意维度的数组（1D、2D、3D...）

**核心概念**：

- **轴（axis）**：数组的维度，从 0 开始编号
  - 1D 数组：1 个轴（axis 0）
  - 2D 数组：2 个轴（axis 0 表示行，axis 1 表示列）
  - 3D 数组：3 个轴（axis 0、axis 1、axis 2）

```python
import numpy as np

# 1D 数组 - 1 个轴
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)  # [1 2 3 4 5]

# 2D 数组 - 2 个轴
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]

# 3D 数组 - 3 个轴
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d)
```

---

### 2.2.2 ndarray 的属性

#### 核心属性（必须掌握）

| 属性 | 说明 | 示例 |
|------|------|------|
| `ndim` | 数组的维度数量（轴的数量） | `arr.ndim` → 2 |
| `shape` | 数组的形状（各维度的大小），返回元组 | `arr.shape` → (3, 5) |
| `size` | 数组元素的总数量 | `arr.size` → 15 |
| `dtype` | 数组元素的数据类型 | `arr.dtype` → int64 |
| `itemsize` | 每个元素的字节大小 | `arr.itemsize` → 8 |

```python
import numpy as np

# 创建一个示例数组
a = np.arange(15).reshape(3, 5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

# 核心属性
print(f"维度数: {a.ndim}")           # 2
print(f"形状: {a.shape}")            # (3, 5)
print(f"总元素数: {a.size}")         # 15
print(f"数据类型: {a.dtype}")        # int64
print(f"每元素字节数: {a.itemsize}") # 8
print(f"总字节数: {a.nbytes}")       # 120 (15 * 8)
```

#### 进阶属性（了解即可）

| 属性 | 说明 |
|------|------|
| `nbytes` | 数组占用的总字节数（`size * itemsize`） |
| `strides` | 遍历数组时每个维度需要跨越的字节数 |
| `data` | 指向数组数据实际内存地址的缓冲区 |
| `T` | 数组的转置（仅适用于 2D 数组） |
| `real` | 复数数组的实部 |
| `imag` | 复数数组的虚部 |
| `flat` | 数组的一维迭代器 |

```python
# 进阶属性示例
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(f"strides: {arr.strides}")  # (24, 8) - 每行跨越 24 字节，每列跨越 8 字节
print(f"转置:\n{arr.T}")
# [[1 4]
#  [2 5]
#  [3 6]]
```

#### 练习题

1. 创建一个 4x6 的浮点数组，打印其所有核心属性
2. 创建一个 3x3 矩阵，计算其转置
3. 比较 int32 和 float64 数组的 itemsize 差异

---

### 2.2.3 ndarray 的创建

#### 2.2.3.1 从 Python 数据结构转换

使用 `np.array()` 从列表或元组创建数组：

```python
import numpy as np

# 从列表创建 1D 数组
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)  # [1 2 3 4 5]

# 从嵌套列表创建 2D 数组
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]

# 显式指定数据类型
arr_float = np.array([1, 2, 3], dtype=np.float64)
print(arr_float)  # [1. 2. 3.]

# 从元组创建数组
arr_tuple = np.array((10, 20, 30))
print(arr_tuple)  # [10 20 30]

# 错误示例：维度不匹配
try:
    irregular = np.array([[1, 2], [3, 4, 5]])  # 不规则嵌套列表
except ValueError as e:
    print(f"错误: {e}")
```

**注意事项**：
- 嵌套列表必须是规则的（每一行元素数量相同）
- 可以使用 `dtype` 参数显式指定数据类型
- NumPy 会自动推断最合适的数据类型

---

#### 2.2.3.2 预定义方法生成

使用占位内容创建数组，适合已知大小但内容待填充的场景：

```python
import numpy as np

# 创建全零数组
zeros = np.zeros((3, 4))
print(zeros)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 创建全一数组
ones = np.ones((2, 3, 4), dtype=np.int16)
print(ones.shape)  # (2, 3, 4)

# 创建空数组（未初始化，内容随机）
empty = np.empty((2, 3))
print(empty)  # 内容是内存中的随机值

# 创建与现有数组形状相同的数组
x = np.array([[1, 2], [3, 4]])
zeros_like = np.zeros_like(x)
ones_like = np.ones_like(x)
empty_like = np.empty_like(x)
```

**常用函数**：
- `np.zeros(shape, dtype=float)` - 全零数组
- `np.ones(shape, dtype=float)` - 全一数组
- `np.empty(shape, dtype=float)` - 空数组（不初始化）
- `np.full(shape, fill_value)` - 指定值填充的数组
- `np.zeros_like(arr)` - 形状相同的全零数组
- `np.ones_like(arr)` - 形状相同的全一数组

---

#### 2.2.3.3 基于数据范围生成

创建具有规律数值序列的数组：

```python
import numpy as np

# arange：类似 Python 的 range，但返回数组
arr1 = np.arange(10)
print(arr1)  # [0 1 2 3 4 5 6 7 8 9]

arr2 = np.arange(2, 10, 2)
print(arr2)  # [2 4 6 8]

arr3 = np.arange(2, 10, dtype=np.float64)
print(arr3)  # [2. 3. 4. 5. 6. 7. 8. 9.]

# linspace：生成指定数量的等间距数值
arr4 = np.linspace(0, 10, 5)
print(arr4)  # [ 0.   2.5  5.   7.5 10. ]

# logspace：生成对数等间距数值
arr5 = np.logspace(0, 2, 5)  # 10^0 到 10^2 之间的 5 个数
print(arr5)  # [  1.           3.16227766  10.          31.6227766  100.        ]
```

**函数对比**：

| 函数 | 参数 | 说明 | 适用场景 |
|------|------|------|----------|
| `arange(start, stop, step)` | 起始、结束、步长 | 类似 range，但支持浮点数 | 已知步长 |
| `linspace(start, stop, num)` | 起始、结束、数量 | 生成等间距数值（包含 stop） | 已知数量 |
| `logspace(start, stop, num)` | 起始指数、结束指数、数量 | 生成对数等间距数值 | 对数刻度 |

**最佳实践**：
- `arange` 使用整数参数避免浮点数舍入误差
- `linspace` 适合需要精确包含端点的场景
- `logspace` 适合科学计数场景

---

#### 2.2.3.4 特殊矩阵

创建常见的特殊矩阵：

```python
import numpy as np

# 单位矩阵（对角线为 1，其余为 0）
identity = np.eye(3)
print(identity)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 对角矩阵
diag = np.diag([1, 2, 3, 4])
print(diag)
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

# 从现有矩阵提取对角线
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
diagonal = np.diag(matrix)
print(diagonal)  # [1 5 9]

# 三对角矩阵（使用 diag 的 k 参数）
main_diag = np.diag([1, 2, 3], k=0)   # 主对角线
upper_diag = np.diag([4, 5], k=1)     # 上对角线
lower_diag = np.diag([6, 7], k=-1)    # 下对角线
tri_diag = main_diag + upper_diag + lower_diag
print(tri_diag)
# [[1 4 0]
#  [6 2 5]
#  [0 7 3]]
```

---

#### 2.2.3.5 随机数组

使用 NumPy 的随机数生成器创建数组：

```python
import numpy as np

# 新式 API（推荐）- 使用 Generator
rng = np.random.default_rng(seed=42)

# 均匀分布 [0, 1)
rand_uniform = rng.random((3, 4))
print(rand_uniform)

# 标准正态分布（均值 0，标准差 1）
rand_normal = rng.standard_normal((2, 3))
print(rand_normal)

# 整数随机数 [low, high)
rand_integers = rng.integers(0, 10, size=(3, 3))
print(rand_integers)

# 从数组中随机选择
choices = rng.choice([10, 20, 30, 40], size=(2, 2))
print(choices)

# 打乱数组
arr = np.arange(10)
rng.shuffle(arr)
print(arr)

# 旧式 API（不推荐，但仍常见）
np.random.seed(42)
old_rand = np.random.rand(3, 4)      # [0, 1) 均匀分布
old_randn = np.random.randn(2, 3)    # 标准正态分布
old_randint = np.random.randint(0, 10, size=(3, 3))  # 整数
```

**常用随机函数**：

| 函数 | 说明 |
|------|------|
| `random()` | [0, 1) 均匀分布 |
| `standard_normal()` | 标准正态分布 N(0, 1) |
| `normal(loc, scale, size)` | 正态分布 N(μ, σ²) |
| `integers(low, high, size)` | [low, high) 整数 |
| `choice(arr, size)` | 从数组随机选择 |
| `shuffle()` | 就地打乱数组 |
| `permutation()` | 返回打乱后的副本 |

---

#### 2.2.3.6 高级构造方法

```python
import numpy as np

# fromfunction：根据索引位置生成数组
def func(i, j):
    return i + j

arr = np.fromfunction(func, (3, 4), dtype=int)
print(arr)
# [[0 1 2 3]
#  [1 2 3 4]
#  [2 3 4 5]]

# fromiter：从可迭代对象创建
iterable = (x**2 for x in range(5))
arr_iter = np.fromiter(iterable, dtype=int)
print(arr_iter)  # [ 0  1  4  9 16]

# meshgrid：创建坐标网格
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print(X)
# [[1 2 3]
#  [1 2 3]]
print(Y)
# [[4 4 4]
#  [5 5 5]]
```

---

#### 2.2.3.7 创建方法性能对比

不同创建方法的性能对比：

```python
import numpy as np
import time

size = 1000000

# 方法 1：从列表转换（最慢）
start = time.time()
arr1 = np.array([i for i in range(size)])
print(f"从列表创建: {time.time() - start:.4f}s")

# 方法 2：arange（快）
start = time.time()
arr2 = np.arange(size)
print(f"arange 创建: {time.time() - start:.4f}s")

# 方法 3：zeros 后赋值（中等）
start = time.time()
arr3 = np.zeros(size)
for i in range(size):
    arr3[i] = i
print(f"zeros 后赋值: {time.time() - start:.4f}s")

# 方法 4：empty 后赋值（稍快）
start = time.time()
arr4 = np.empty(size)
for i in range(size):
    arr4[i] = i
print(f"empty 后赋值: {time.time() - start:.4f}s")
```

**性能建议**：
1. **优先使用内置函数**（如 `arange`、`zeros`、`ones`）
2. **避免循环赋值**，使用向量化操作
3. `empty` 比 `zeros` 快，但内容未初始化
4. 从 Python 列表转换最慢，仅适合小数组

---

### 2.2.4 ndarray 的数据类型

NumPy 支持比 Python 更多的数值类型：

#### 常用数据类型

| 类型 | 说明 | 字节数 | 范围/精度 |
|------|------|--------|-----------|
| `int8` | 有符号 8 位整数 | 1 | -128 到 127 |
| `int16` | 有符号 16 位整数 | 2 | -32768 到 32767 |
| `int32` | 有符号 32 位整数 | 4 | -2³¹ 到 2³¹-1 |
| `int64` | 有符号 64 位整数 | 8 | -2⁶³ 到 2⁶³-1 |
| `uint8` | 无符号 8 位整数 | 1 | 0 到 255 |
| `uint16` | 无符号 16 位整数 | 2 | 0 到 65535 |
| `uint32` | 无符号 32 位整数 | 4 | 0 到 2³²-1 |
| `uint64` | 无符号 64 位整数 | 8 | 0 到 2⁶⁴-1 |
| `float16` | 半精度浮点数 | 2 | 约 ±6.5e4 |
| `float32` | 单精度浮点数 | 4 | 约 ±3.4e38 |
| `float64` | 双精度浮点数 | 8 | 约 ±1.8e308 |
| `complex64` | 复数（两个 float32） | 8 | - |
| `complex128` | 复数（两个 float64） | 16 | - |
| `bool_` | 布尔值 | 1 | True/False |
| `str_` | 字符串 | 可变 | Unicode |

```python
import numpy as np

# 创建不同类型的数组
arr_int8 = np.array([1, 2, 3], dtype=np.int8)
arr_float32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
arr_bool = np.array([True, False, True], dtype=np.bool_)

print(f"int8: {arr_int8.dtype}, itemsize={arr_int8.itemsize}")
print(f"float32: {arr_float32.dtype}, itemsize={arr_float32.itemsize}")
print(f"bool: {arr_bool.dtype}, itemsize={arr_bool.itemsize}")

# 类型转换
arr = np.array([1.7, 2.3, 3.9])
arr_int = arr.astype(np.int32)
print(arr_int)  # [1 2 3] - 注意：直接截断，不是四舍五入

# 字符串类型
arr_str = np.array(['1', '2', '3'], dtype='U10')  # Unicode 字符串，最长 10 个字符
arr_converted = arr_str.astype(np.int32)
print(arr_converted)  # [1 2 3]
```

#### 数据类型选择建议

1. **整数**：根据数值范围选择合适的位数，节省内存
2. **浮点数**：默认 float64，除非内存敏感才用 float32
3. **布尔值**：用于掩码和条件筛选
4. **复数**：科学计算中的复数运算

---

### 2.2.5 索引与切片技巧

#### 基本索引

```python
import numpy as np

# 1D 数组索引（类似 Python 列表）
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[0])      # 1 - 第一个元素
print(arr[-1])     # 10 - 最后一个元素
print(arr[2:5])    # [3 4 5] - 切片，不包含索引 5

# 2D 数组索引
arr_2d = np.array([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12]])

print(arr_2d[0, 0])      # 1 - 第一行第一列
print(arr_2d[1, 2])      # 7 - 第二行第三列
print(arr_2d[-1, -1])    # 12 - 最后一行最后一列

# 切片语法：start:stop:step
print(arr_2d[0, :])      # [1 2 3 4] - 第一行所有列
print(arr_2d[:, 1])      # [ 2  6 10] - 所有行的第二列
print(arr_2d[1:3, 1:3])  # [[ 6  7]
                          #  [10 11]] - 子矩阵
```

#### 高级索引

```python
import numpy as np

arr = np.arange(10, 20)

# 整数数组索引
indices = np.array([0, 2, 4, 6])
print(arr[indices])  # [10 12 14 16]

# 布尔索引（掩码）
mask = arr > 15
print(mask)          # [False False False False False False  True  True  True  True]
print(arr[mask])     # [16 17 18 19]

# 条件筛选
print(arr[arr % 2 == 0])  # [10 12 14 16 18] - 偶数

# 2D 数组的花式索引
arr_2d = np.arange(12).reshape(3, 4)
rows = np.array([0, 2, 2])
cols = np.array([1, 3, 0])
print(arr_2d[rows, cols])  # [ 1 11  8] - 取 (0,1), (2,3), (2,0)
```

#### 切片注意事项

**重要**：NumPy 切片返回的是**视图（view）**，不是副本！

```python
import numpy as np

arr = np.arange(10)
slice_view = arr[2:5]

# 修改切片会影响原数组
slice_view[0] = 999
print(arr)  # [  0   1 999   3   4   5   6   7   8   9]

# 如需副本，使用 copy()
arr = np.arange(10)
slice_copy = arr[2:5].copy()
slice_copy[0] = 999
print(arr)  # [0 1 2 3 4 5 6 7 8 9] - 原数组未改变
```

---

### 2.2.6 基本运算

#### 向量化运算

NumPy 支持数组间的**逐元素运算**（element-wise operations）：

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 算术运算
print(a + b)    # [11 22 33 44]
print(a - b)    # [ -9 -18 -27 -36]
print(a * b)    # [ 10  40  90 160]
print(a / b)    # [0.1  0.1  0.1  0.1 ]
print(a ** 2)   # [ 1  4  9 16]
print(a % 3)    # [1 2 0 1]

# 比较运算
print(a > 2)    # [False False  True  True]
print(a == b)   # [False False False False]

# 与标量运算（广播）
print(a + 10)   # [11 12 13 14]
print(a * 2)    # [2 4 6 8]
```

#### 数组与标量运算（广播）

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 广播：标量自动扩展到数组形状
result = arr * 10
print(result)
# [[10 20 30]
#  [40 50 60]]
```

#### 数学函数

```python
import numpy as np

arr = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# 三角函数
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

# 指数和对数
x = np.array([1, 2, 3, 4])
print(np.exp(x))      # e^x
print(np.log(x))      # ln(x)
print(np.log10(x))    # log10(x)
print(np.sqrt(x))     # √x
print(np.power(x, 3)) # x^3

# 四舍五入
arr = np.array([-2.7, -1.3, 0.5, 1.8, 3.2])
print(np.floor(arr))   # [-3. -2.  0.  1.  3.] - 向下取整
print(np.ceil(arr))    # [-2. -1.  1.  2.  4.] - 向上取整
print(np.round(arr))   # [-3. -1.  0.  2.  3.] - 四舍五入
print(np.abs(arr))     # [2.7 1.3 0.5 1.8 3.2] - 绝对值
```

#### 矩阵运算

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 逐元素乘法
print(A * B)
# [[ 5 12]
#  [21 32]]

# 矩阵乘法（点积）
print(np.dot(A, B))  # 或 A @ B
# [[19 22]
#  [43 50]]

# 转置
print(A.T)
# [[1 3]
#  [2 4]]

# 行列式
det = np.linalg.det(A)
print(det)  # -2.0

# 逆矩阵
inv = np.linalg.inv(A)
print(inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
```

---

## 2.3 numpy 常用函数

### 2.3.1 统计基础

#### 基本统计量

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 基本统计函数
print(f"均值: {np.mean(data)}")        # 5.5
print(f"中位数: {np.median(data)}")    # 5.5
print(f"标准差: {np.std(data)}")       # 2.872
print(f"方差: {np.var(data)}")         # 8.25
print(f"最小值: {np.min(data)}")       # 1
print(f"最大值: {np.max(data)}")       # 10
print(f"求和: {np.sum(data)}")         # 55
print(f"乘积: {np.prod(data)}")        # 3628800
```

#### 沿轴统计

```python
import numpy as np

data_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# axis=0：沿着列（跨行）计算
col_mean = np.mean(data_2d, axis=0)
print(f"每列均值: {col_mean}")  # [4. 5. 6.]

# axis=1：沿着行（跨列）计算
row_mean = np.mean(data_2d, axis=1)
print(f"每行均值: {row_mean}")  # [2. 5. 8.]

# 其他统计函数也支持 axis 参数
print(f"每列标准差: {np.std(data_2d, axis=0)}")  # [2.449 2.449 2.449]
print(f"每行求和: {np.sum(data_2d, axis=1)}")    # [ 6 15 24]
```

#### 累积统计

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 累积求和
cumsum = np.cumsum(arr)
print(cumsum)  # [ 1  3  6 10 15]

# 累积乘积
cumprod = np.cumprod(arr)
print(cumprod)  # [  1   2   6  24 120]

# 差分（相邻元素差）
diff = np.diff(arr)
print(diff)  # [1 1 1 1]
```

#### 百分位数和分位数

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 百分位数
print(f"25% 分位数: {np.percentile(data, 25)}")  # 3.25
print(f"50% 分位数: {np.percentile(data, 50)}")  # 5.5
print(f"75% 分位数: {np.percentile(data, 75)}")  # 7.75

# 多个分位数
quantiles = np.quantile(data, [0.25, 0.5, 0.75])
print(f"四分位数: {quantiles}")  # [3.25 5.5  7.75]
```

---

### 2.3.2 基本数学函数

#### 三角函数

```python
import numpy as np

angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

print(f"sin: {np.sin(angles)}")
print(f"cos: {np.cos(angles)}")
print(f"tan: {np.tan(angles)}")

# 反三角函数
print(f"arcsin: {np.arcsin([0, 0.5, 1])}")
print(f"arccos: {np.arccos([1, 0.5, 0])}")
print(f"arctan: {np.arctan([0, 1, np.inf])}")
```

#### 指数和对数

```python
import numpy as np

x = np.array([1, 2, 3, 4])

print(f"e^x: {np.exp(x)}")           # [ 2.718  7.389 20.086 54.598]
print(f"ln(x): {np.log(x)}")         # [0.    0.693 1.099 1.386]
print(f"log10(x): {np.log10(x)}")    # [0.    0.301 0.477 0.602]
print(f"log2(x): {np.log2(x)}")      # [0. 1. 1.585 2.]

# log1p(x) = log(1 + x)，对小数值更精确
small = np.array([1e-10, 1e-5, 0.01])
print(f"log1p: {np.log1p(small)}")
```

#### 幂运算和根运算

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print(f"平方根: {np.sqrt(arr)}")           # [1. 2. 3. 4. 5.]
print(f"立方根: {np.cbrt(arr)}")           # [1.    1.587 2.08  2.52  2.924]
print(f"x^3: {np.power(arr, 3)}")         # [    1    64   729  4096 15625]
print(f"x^0.5: {np.power(arr, 0.5)}")     # [1. 2. 3. 4. 5.]
```

---

### 2.3.3 统计函数

#### 索引查找

```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# 最小值/最大值的索引
print(f"最小值索引: {np.argmin(arr)}")  # 1
print(f"最大值索引: {np.argmax(arr)}")  # 5

# 2D 数组
arr_2d = np.array([[1, 5, 3],
                   [8, 2, 9]])

# 沿轴查找
print(f"每列最小值索引: {np.argmin(arr_2d, axis=0)}")  # [0 1 0]
print(f"每行最大值索引: {np.argmax(arr_2d, axis=1)}")  # [1 2]
```

#### 相关性和协方差

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# 相关系数矩阵
correlation = np.corrcoef(x, y)
print(f"相关系数:\n{correlation}")
# [[1.    0.775]
#  [0.775 1.   ]]

# 协方差矩阵
covariance = np.cov(x, y)
print(f"协方差:\n{covariance}")
# [[2.5  1.75]
#  [1.75 1.7 ]]
```

#### NaN 处理函数

```python
import numpy as np

# 包含 NaN 的数据
data_with_nan = np.array([1, 2, np.nan, 4, 5, np.nan])

# 标准函数会返回 NaN
print(f"mean: {np.mean(data_with_nan)}")  # nan

# NaN 忽略函数
print(f"nanmean: {np.nanmean(data_with_nan)}")  # 3.0
print(f"nanstd: {np.nanstd(data_with_nan)}")    # 1.414
print(f"nansum: {np.nansum(data_with_nan)}")    # 12.0
print(f"nanmax: {np.nanmax(data_with_nan)}")    # 5.0
print(f"nanmin: {np.nanmin(data_with_nan)}")    # 1.0
```

---

### 2.3.4 比较函数

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 2, 2])

# 逐元素比较
print(f"大于: {np.greater(a, b)}")       # [False False  True  True]
print(f"大于等于: {np.greater_equal(a, b)}")  # [False  True  True  True]
print(f"小于: {np.less(a, b)}")          # [ True False False False]
print(f"等于: {np.equal(a, b)}")         # [False  True False False]
print(f"不等于: {np.not_equal(a, b)}")   # [ True False  True  True]

# 等价的运算符形式（推荐）
print(a > b)    # [False False  True  True]
print(a >= b)   # [False  True  True  True]
print(a < b)    # [ True False False False]
print(a == b)   # [False  True False False]
print(a != b)   # [ True False  True  True]

# 逻辑运算
x = np.array([True, True, False, False])
y = np.array([True, False, True, False])
print(f"与: {np.logical_and(x, y)}")   # [ True False False False]
print(f"或: {np.logical_or(x, y)}")    # [ True  True  True False]
print(f"非: {np.logical_not(x)}")      # [False False  True  True]
```

---

### 2.3.5 排序函数

```python
import numpy as np

# 基本排序
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr = np.sort(arr)
print(f"排序后: {sorted_arr}")  # [1 1 2 3 4 5 6 9]

# 原地排序
arr_inplace = np.array([3, 1, 4, 1, 5, 9, 2, 6])
arr_inplace.sort()
print(f"原地排序: {arr_inplace}")  # [1 1 2 3 4 5 6 9]

# argsort：返回排序后的索引
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
indices = np.argsort(arr)
print(f"排序索引: {indices}")        # [1 3 6 0 2 4 7 5]
print(f"使用索引排序: {arr[indices]}")  # [1 1 2 3 4 5 6 9]

# 2D 数组排序
arr_2d = np.array([[3, 2, 1],
                   [6, 5, 4]])

# 沿行排序（每行独立排序）
sorted_rows = np.sort(arr_2d, axis=1)
print(f"每行排序:\n{sorted_rows}")
# [[1 2 3]
#  [4 5 6]]

# 沿列排序（每列独立排序）
sorted_cols = np.sort(arr_2d, axis=0)
print(f"每列排序:\n{sorted_cols}")
# [[3 2 1]
#  [6 5 4]]

# 降序排序（使用负号索引技巧）
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
descending = np.sort(arr)[::-1]
print(f"降序: {descending}")  # [9 6 5 4 3 2 1 1]
```

---

### 2.3.6 去重函数

```python
import numpy as np

# 基本去重
arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])
unique = np.unique(arr)
print(f"去重: {unique}")  # [1 2 3 4 5]

# 返回计数
unique, counts = np.unique(arr, return_counts=True)
print(f"唯一值: {unique}")    # [1 2 3 4 5]
print(f"出现次数: {counts}")  # [1 2 3 1 2]

# 返回索引
unique, indices = np.unique(arr, return_index=True)
print(f"首次出现索引: {indices}")  # [0 1 3 6 7]

# 返回逆索引（重建原数组）
unique, inverse = np.unique(arr, return_inverse=True)
print(f"逆索引: {inverse}")  # [0 1 1 2 2 2 3 4 4]
print(f"重建原数组: {unique[inverse]}")  # [1 2 2 3 3 3 4 5 5]
```

---

### 2.3.7 其他实用函数

#### 数组拼接

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 一维拼接
concat = np.concatenate([a, b])
print(concat)  # [1 2 3 4 5 6]

# 二维拼接
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 垂直拼接（沿 axis=0，增加行）
vstack = np.vstack([arr1, arr2])
print(vstack)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 水平拼接（沿 axis=1，增加列）
hstack = np.hstack([arr1, arr2])
print(hstack)
# [[1 2 5 6]
#  [3 4 7 8]]
```

#### 数组分割

```python
import numpy as np

arr = np.arange(12)

# 均匀分割
split = np.split(arr, 4)
print(split)  # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8]), array([ 9, 10, 11])]

# 指定位置分割
split_at = np.split(arr, [3, 7])
print(split_at)  # [array([0, 1, 2]), array([3, 4, 5, 6]), array([ 7,  8,  9, 10, 11])]

# 2D 数组分割
arr_2d = np.arange(12).reshape(3, 4)
hsplit = np.hsplit(arr_2d, 2)  # 水平分割（分列）
vsplit = np.vsplit(arr_2d, 3)  # 垂直分割（分行）
```

#### 数组形状变换

```python
import numpy as np

arr = np.arange(12)

# reshape：改变形状
reshaped = arr.reshape(3, 4)
print(reshaped)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# ravel：展平为一维（返回视图）
flattened = reshaped.ravel()
print(flattened)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# flatten：展平为一维（返回副本）
flattened_copy = reshaped.flatten()

# transpose：转置
transposed = reshaped.T
print(transposed)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

# swapaxes：交换轴
swapped = reshaped.swapaxes(0, 1)
print(swapped)  # 等价于 transpose
```

#### 数组重复

```python
import numpy as np

arr = np.array([1, 2, 3])

# repeat：重复元素
repeated = np.repeat(arr, 3)
print(repeated)  # [1 1 1 2 2 2 3 3 3]

# tile：平铺数组
tiled = np.tile(arr, 3)
print(tiled)  # [1 2 3 1 2 3 1 2 3]

# 2D 平铺
arr_2d = np.array([[1, 2], [3, 4]])
tiled_2d = np.tile(arr_2d, (2, 3))
print(tiled_2d)
# [[1 2 1 2 1 2]
#  [3 4 3 4 3 4]
#  [1 2 1 2 1 2]
#  [3 4 3 4 3 4]]
```

---

### 2.3.8 常用小结

#### 统计函数速查表

| 函数 | 功能 | 示例 |
|------|------|------|
| `np.mean()` | 平均值 | `np.mean(arr)` |
| `np.median()` | 中位数 | `np.median(arr)` |
| `np.std()` | 标准差 | `np.std(arr)` |
| `np.var()` | 方差 | `np.var(arr)` |
| `np.min()` / `np.max()` | 最小/最大值 | `np.min(arr)` |
| `np.sum()` / `np.prod()` | 求和/求积 | `np.sum(arr)` |
| `np.argmin()` / `np.argmax()` | 最小/最大值索引 | `np.argmin(arr)` |
| `np.percentile()` | 百分位数 | `np.percentile(arr, 50)` |
| `np.corrcoef()` | 相关系数 | `np.corrcoef(x, y)` |

#### 数学函数速查表

| 函数 | 功能 | 示例 |
|------|------|------|
| `np.sin()` / `np.cos()` / `np.tan()` | 三角函数 | `np.sin(arr)` |
| `np.exp()` | e^x | `np.exp(arr)` |
| `np.log()` / `np.log10()` / `np.log2()` | 对数 | `np.log(arr)` |
| `np.sqrt()` / `np.cbrt()` | 平方根/立方根 | `np.sqrt(arr)` |
| `np.power()` | 幂运算 | `np.power(arr, 3)` |
| `np.abs()` | 绝对值 | `np.abs(arr)` |
| `np.floor()` / `np.ceil()` / `np.round()` | 取整 | `np.round(arr)` |

#### 数组操作速查表

| 函数 | 功能 | 示例 |
|------|------|------|
| `np.sort()` | 排序 | `np.sort(arr)` |
| `np.argsort()` | 排序索引 | `np.argsort(arr)` |
| `np.unique()` | 去重 | `np.unique(arr)` |
| `np.concatenate()` | 拼接 | `np.concatenate([a, b])` |
| `np.split()` | 分割 | `np.split(arr, 3)` |
| `np.reshape()` | 改变形状 | `arr.reshape(3, 4)` |
| `np.ravel()` / `np.flatten()` | 展平 | `arr.ravel()` |

---

## 2.4 综合练习

### 题目 1：温度数据分析

**任务**：分析一周的温度数据，计算统计信息并找出异常值。

```python
import numpy as np

# 一周的温度数据（摄氏度）
temperatures = np.array([22.5, 23.1, 24.8, 21.2, 25.5, 26.0, 19.8])

# TODO:
# 1. 计算平均温度、最高温度、最低温度
# 2. 计算温度的标准差
# 3. 找出高于平均温度的天数
# 4. 找出温度异常的天数（偏离均值超过 2 个标准差）
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

temperatures = np.array([22.5, 23.1, 24.8, 21.2, 25.5, 26.0, 19.8])

# 1. 基本统计
mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print(f"平均温度: {mean_temp:.2f}°C")
print(f"最高温度: {max_temp:.2f}°C")
print(f"最低温度: {min_temp:.2f}°C")

# 2. 标准差
std_temp = np.std(temperatures)
print(f"标准差: {std_temp:.2f}°C")

# 3. 高于平均温度的天数
above_mean = temperatures > mean_temp
days_above = np.sum(above_mean)
print(f"高于平均温度的天数: {days_above}")

# 4. 异常温度（偏离均值超过 2 个标准差）
lower_bound = mean_temp - 2 * std_temp
upper_bound = mean_temp + 2 * std_temp
outliers = (temperatures < lower_bound) | (temperatures > upper_bound)
print(f"异常温度的天数: {np.sum(outliers)}")
print(f"异常温度值: {temperatures[outliers]}")
```
</details>

---

### 题目 2：学生成绩统计

**任务**：分析班级学生的考试成绩。

```python
import numpy as np

# 5 个学生在 3 门课程的成绩（行=学生，列=课程）
scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [78, 85, 80],
                   [90, 92, 88],
                   [88, 76, 85]])

# TODO:
# 1. 计算每个学生的平均分
# 2. 计算每门课程的平均分
# 3. 找出总分最高的学生
# 4. 找出每门课程的最高分和最低分
# 5. 统计每门课程及格（>=60）和不及格的人数
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [78, 85, 80],
                   [90, 92, 88],
                   [88, 76, 85]])

# 1. 每个学生的平均分
student_avg = np.mean(scores, axis=1)
print(f"每个学生的平均分:\n{student_avg}")

# 2. 每门课程的平均分
course_avg = np.mean(scores, axis=0)
print(f"每门课程的平均分:\n{course_avg}")

# 3. 总分最高的学生
total_scores = np.sum(scores, axis=1)
top_student = np.argmax(total_scores)
print(f"总分最高的学生: 学生 {top_student + 1}，总分: {total_scores[top_student]}")

# 4. 每门课程的最高分和最低分
course_max = np.max(scores, axis=0)
course_min = np.min(scores, axis=0)
print(f"每门课程最高分: {course_max}")
print(f"每门课程最低分: {course_min}")

# 5. 及格/不及格统计
passing = scores >= 60
passing_count = np.sum(passing, axis=0)
failing_count = np.sum(~passing, axis=0)
print(f"每门课程及格人数: {passing_count}")
print(f"每门课程不及格人数: {failing_count}")
```
</details>

---

### 题目 3：矩阵运算

**任务**：进行矩阵运算和线性代数操作。

```python
import numpy as np

A = np.array([[2, 1],
              [1, 3]])
B = np.array([[1, 0],
              [0, 2]])

# TODO:
# 1. 计算 A + B 和 A - B
# 2. 计算 A 和 B 的逐元素乘法和矩阵乘法
# 3. 计算 A 的转置、行列式、逆矩阵
# 4. 求解线性方程组 Ax = b，其中 b = [5, 7]
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

A = np.array([[2, 1],
              [1, 3]])
B = np.array([[1, 0],
              [0, 2]])

# 1. 加减法
print(f"A + B:\n{A + B}")
print(f"A - B:\n{A - B}")

# 2. 乘法
print(f"逐元素乘法:\n{A * B}")
print(f"矩阵乘法:\n{A @ B}")

# 3. 转置、行列式、逆矩阵
print(f"A 的转置:\n{A.T}")
print(f"A 的行列式: {np.linalg.det(A)}")
print(f"A 的逆矩阵:\n{np.linalg.inv(A)}")

# 4. 求解线性方程组 Ax = b
b = np.array([5, 7])
x = np.linalg.solve(A, b)
print(f"方程组的解: {x}")

# 验证
print(f"验证 Ax: {A @ x}")  # 应该等于 b
```
</details>

---

### 题目 4：随机数据生成

**任务**：使用随机数生成器创建模拟数据。

```python
import numpy as np

# TODO:
# 1. 生成 100 个服从标准正态分布的随机数
# 2. 生成 50 个 [10, 100) 之间的随机整数
# 3. 从 ['A', 'B', 'C', 'D'] 中随机选择 20 个元素（可重复）
# 4. 生成一个 5x5 的随机矩阵，元素在 [0, 1) 之间
# 5. 打乱数组 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

rng = np.random.default_rng(seed=42)

# 1. 标准正态分布
normal_data = rng.standard_normal(100)
print(f"正态分布数据（前 10 个）: {normal_data[:10]}")

# 2. 随机整数
random_ints = rng.integers(10, 100, size=50)
print(f"随机整数（前 10 个）: {random_ints[:10]}")

# 3. 随机选择
choices = rng.choice(['A', 'B', 'C', 'D'], size=20)
print(f"随机选择: {choices}")

# 4. 随机矩阵
random_matrix = rng.random((5, 5))
print(f"随机矩阵:\n{random_matrix}")

# 5. 打乱数组
arr = np.arange(1, 11)
rng.shuffle(arr)
print(f"打乱后的数组: {arr}")
```
</details>

---

### 题目 5：数组变形

**任务**：练习数组形状的变换操作。

```python
import numpy as np

arr = np.arange(1, 25)

# TODO:
# 1. 将 arr 变形为 4x6 矩阵
# 2. 将 arr 变形为 2x3x4 的三维数组
# 3. 将二维数组展平为一维
# 4. 转置二维数组
# 5. 交换三维数组的第 0 轴和第 2 轴
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

arr = np.arange(1, 25)

# 1. 变形为 4x6
arr_2d = arr.reshape(4, 6)
print(f"4x6 矩阵:\n{arr_2d}")

# 2. 变形为 2x3x4
arr_3d = arr.reshape(2, 3, 4)
print(f"2x3x4 三维数组:\n{arr_3d}")

# 3. 展平
flattened = arr_2d.ravel()
print(f"展平: {flattened}")

# 4. 转置
transposed = arr_2d.T
print(f"转置:\n{transposed}")

# 5. 交换轴
swapped = arr_3d.swapaxes(0, 2)
print(f"交换轴后形状: {swapped.shape}")  # (4, 3, 2)
```
</details>

---

### 题目 6：布尔索引

**任务**：使用布尔索引进行数据筛选。

```python
import numpy as np

data = np.array([12, 35, 8, 23, 50, 17, 42, 29, 6, 31])

# TODO:
# 1. 筛选出大于 20 的元素
# 2. 筛选出在 10 到 30 之间的元素
# 3. 筛选出能被 5 整除的元素
# 4. 将所有小于 10 的元素替换为 0
# 5. 统计满足条件 (x > 15 且 x < 40) 的元素数量
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

data = np.array([12, 35, 8, 23, 50, 17, 42, 29, 6, 31])

# 1. 大于 20
print(f"大于 20: {data[data > 20]}")

# 2. 在 10 到 30 之间
mask = (data >= 10) & (data <= 30)
print(f"10-30 之间: {data[mask]}")

# 3. 能被 5 整除
print(f"能被 5 整除: {data[data % 5 == 0]}")

# 4. 替换小于 10 的元素
data_copy = data.copy()
data_copy[data_copy < 10] = 0
print(f"替换后: {data_copy}")

# 5. 统计满足条件的元素
count = np.sum((data > 15) & (data < 40))
print(f"满足 15 < x < 40 的元素数量: {count}")
```
</details>

---

### 题目 7：统计函数应用

**任务**：综合应用统计函数分析数据。

```python
import numpy as np

# 模拟 30 天的股票价格
np.random.seed(42)
stock_prices = 100 + np.random.randn(30) * 5

# TODO:
# 1. 计算股价的均值、中位数、标准差
# 2. 找出最高价和最低价出现的日期（索引）
# 3. 计算每日涨跌幅（今日价格 - 昨日价格）
# 4. 统计上涨天数和下跌天数
# 5. 计算 25%、50%、75% 分位数
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

np.random.seed(42)
stock_prices = 100 + np.random.randn(30) * 5

# 1. 基本统计
print(f"均值: {np.mean(stock_prices):.2f}")
print(f"中位数: {np.median(stock_prices):.2f}")
print(f"标准差: {np.std(stock_prices):.2f}")

# 2. 最高价和最低价的日期
max_day = np.argmax(stock_prices)
min_day = np.argmin(stock_prices)
print(f"最高价出现在第 {max_day + 1} 天: {stock_prices[max_day]:.2f}")
print(f"最低价出现在第 {min_day + 1} 天: {stock_prices[min_day]:.2f}")

# 3. 每日涨跌幅
daily_change = np.diff(stock_prices)
print(f"每日涨跌幅（前 5 天）: {daily_change[:5]}")

# 4. 上涨和下跌天数
up_days = np.sum(daily_change > 0)
down_days = np.sum(daily_change < 0)
print(f"上涨天数: {up_days}，下跌天数: {down_days}")

# 5. 分位数
quartiles = np.percentile(stock_prices, [25, 50, 75])
print(f"25% 分位数: {quartiles[0]:.2f}")
print(f"50% 分位数: {quartiles[1]:.2f}")
print(f"75% 分位数: {quartiles[2]:.2f}")
```
</details>

---

### 题目 8：数组拼接

**任务**：练习数组的拼接和堆叠操作。

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([10, 20])

# TODO:
# 1. 垂直拼接 a 和 b
# 2. 水平拼接 a 和 b
# 3. 将 c 作为新行添加到 a 的下方
# 4. 将三个数组 [a, b, a] 沿深度方向（第 3 维）堆叠
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([10, 20])

# 1. 垂直拼接
vertical = np.vstack([a, b])
print(f"垂直拼接:\n{vertical}")

# 2. 水平拼接
horizontal = np.hstack([a, b])
print(f"水平拼接:\n{horizontal}")

# 3. 添加新行
with_new_row = np.vstack([a, c])
print(f"添加新行:\n{with_new_row}")

# 4. 深度堆叠
depth_stacked = np.dstack([a, b, a])
print(f"深度堆叠形状: {depth_stacked.shape}")  # (2, 2, 3)
print(f"深度堆叠:\n{depth_stacked}")
```
</details>

---

### 题目 9：唯一值与排序

**任务**：处理数组中的唯一值和排序操作。

```python
import numpy as np

data = np.array([5, 2, 8, 2, 9, 5, 1, 8, 5, 3])

# TODO:
# 1. 找出唯一值并排序
# 2. 统计每个唯一值出现的次数
# 3. 找出出现次数最多的值
# 4. 对数组降序排序
# 5. 找出排序后的索引（argsort）
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

data = np.array([5, 2, 8, 2, 9, 5, 1, 8, 5, 3])

# 1. 唯一值
unique_values = np.unique(data)
print(f"唯一值: {unique_values}")

# 2. 统计出现次数
unique, counts = np.unique(data, return_counts=True)
print(f"值: {unique}")
print(f"次数: {counts}")

# 3. 出现次数最多的值
most_common_idx = np.argmax(counts)
most_common = unique[most_common_idx]
print(f"出现最多的值: {most_common}（{counts[most_common_idx]} 次）")

# 4. 降序排序
descending = np.sort(data)[::-1]
print(f"降序排序: {descending}")

# 5. 排序索引
sort_indices = np.argsort(data)
print(f"升序索引: {sort_indices}")
print(f"使用索引排序: {data[sort_indices]}")

# 降序索引
descending_indices = np.argsort(data)[::-1]
print(f"降序索引: {descending_indices}")
```
</details>

---

### 题目 10：缺失值处理

**任务**：处理包含 NaN 的数据。

```python
import numpy as np

data = np.array([1.5, 2.3, np.nan, 4.1, np.nan, 5.7, 3.2, np.nan, 6.8])

# TODO:
# 1. 统计 NaN 的数量
# 2. 找出 NaN 的位置（索引）
# 3. 计算非 NaN 值的均值和标准差
# 4. 用均值填充 NaN
# 5. 删除所有 NaN 值
```

<details>
<summary>参考答案</summary>

```python
import numpy as np

data = np.array([1.5, 2.3, np.nan, 4.1, np.nan, 5.7, 3.2, np.nan, 6.8])

# 1. 统计 NaN 数量
nan_count = np.sum(np.isnan(data))
print(f"NaN 数量: {nan_count}")

# 2. NaN 的位置
nan_indices = np.where(np.isnan(data))[0]
print(f"NaN 位置: {nan_indices}")

# 3. 非 NaN 值的统计
mean_value = np.nanmean(data)
std_value = np.nanstd(data)
print(f"均值: {mean_value:.2f}")
print(f"标准差: {std_value:.2f}")

# 4. 用均值填充 NaN
data_filled = data.copy()
data_filled[np.isnan(data_filled)] = mean_value
print(f"填充后: {data_filled}")

# 5. 删除 NaN
data_cleaned = data[~np.isnan(data)]
print(f"删除 NaN 后: {data_cleaned}")
```
</details>

---

## 学习建议

1. **循序渐进**：从基础的数组创建和属性开始，逐步学习索引、运算和函数
2. **多做练习**：理论结合实践，完成每个章节的练习题
3. **查阅文档**：遇到不熟悉的函数，及时查阅 [NumPy 官方文档](https://numpy.org/doc/)
4. **性能意识**：优先使用向量化操作，避免 Python 循环
5. **实际应用**：将 NumPy 应用到数据分析、机器学习等实际项目中

## 参考资源

- [NumPy 官方文档](https://numpy.org/doc/)
- [NumPy 快速入门](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy API 参考](https://numpy.org/doc/stable/reference/)
- [NumPy 用户指南](https://numpy.org/doc/stable/user/index.html)
