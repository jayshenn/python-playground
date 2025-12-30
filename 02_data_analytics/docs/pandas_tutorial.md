# Pandas 数据分析

## 3.1 Pandas 简介

### 3.1.1 Pandas 是什么？

**Pandas** 是 Python 中最流行的数据分析库，提供了高性能、易用的数据结构和数据分析工具。

**核心特点**：
- **高效的数据结构**：Series（一维）和 DataFrame（二维）
- **数据对齐**：自动或显式的数据对齐
- **灵活的索引**：支持标签索引和整数索引
- **强大的 IO 工具**：读写 CSV、Excel、SQL、JSON 等多种格式
- **缺失数据处理**：内置的缺失数据处理功能
- **数据聚合与分组**：类似 SQL 的 GROUP BY 功能
- **时间序列**：强大的日期和时间处理能力

**为什么使用 Pandas？**
1. **基于 NumPy 构建**：继承了 NumPy 的高性能数组计算能力
2. **类似 SQL 操作**：熟悉数据库的用户可以快速上手
3. **数据科学生态核心**：与 NumPy、Matplotlib、Scikit-learn 等库无缝集成
4. **处理真实世界数据**：擅长处理缺失值、重复值、异构类型数据

**安装 Pandas**：
```bash
# 使用 uv
uv add pandas

# 使用 pip
pip install pandas
```

**导入 Pandas**：
```python
import pandas as pd  # 标准导入方式
import numpy as np   # 通常一起使用
```

---

### 3.1.2 了解 Pandas 核心数据结构：Series 和 DataFrame

Pandas 提供两种主要的数据结构：

| 数据结构 | 维度 | 描述 | 类比 |
|---------|------|------|------|
| **Series** | 1D | 带标签的一维数组 | Excel 的一列 |
| **DataFrame** | 2D | 带标签的二维表格 | Excel 工作表 / SQL 表 |

**数据结构对比**：

```python
import pandas as pd
import numpy as np

# Series：一维数据
s = pd.Series([10, 20, 30, 40])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# DataFrame：二维数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Beijing', 'Shanghai', 'Guangzhou']
})
print(df)
#       Name  Age       City
# 0    Alice   25    Beijing
# 1      Bob   30   Shanghai
# 2  Charlie   35  Guangzhou
```

**关系**：
- DataFrame 的每一列都是一个 Series
- Series 可以看作是只有一列的 DataFrame
- 它们都具有 **索引（Index）** 和 **值（Values）**

---

## 3.2 核心数据结构：Series

### 3.2.1 创建与访问

#### 什么是 Series？

**Series** 是 Pandas 的一维数据结构，由以下两部分组成：
1. **索引（Index）**：数据的标签
2. **值（Values）**：实际的数据，存储在 NumPy 数组中

**Series 的特点**：
- 类似于带标签的 NumPy 数组
- 类似于固定长度的字典
- 支持多种数据类型（整数、浮点数、字符串、对象等）
- 索引可以是任何可哈希类型（整数、字符串、日期等）

```python
import pandas as pd

# 基本 Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)
# 0    1
# 1    3
# 2    5
# 3    7
# 4    9
# dtype: int64

# Series 的组成
print(f"索引: {s.index}")    # RangeIndex(start=0, stop=5, step=1)
print(f"值: {s.values}")      # [1 3 5 7 9]
print(f"数据类型: {s.dtype}") # int64
```

---

#### 创建 Series

**方法 1：从列表或 NumPy 数组创建**

```python
import pandas as pd
import numpy as np

# 从列表创建（默认整数索引 0, 1, 2...）
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# 从 NumPy 数组创建
arr = np.array([1.5, 2.5, 3.5])
s2 = pd.Series(arr)
print(s2)

# 自定义索引
s3 = pd.Series([85, 90, 78], index=['Math', 'English', 'Physics'])
print(s3)
# Math       85
# English    90
# Physics    78
# dtype: int64
```

**方法 2：从字典创建**

```python
# 字典的键自动成为索引
data = {'Apple': 5, 'Banana': 3, 'Orange': 7}
s = pd.Series(data)
print(s)
# Apple     5
# Banana    3
# Orange    7
# dtype: int64

# 指定索引顺序（未匹配的键会显示 NaN）
s = pd.Series(data, index=['Apple', 'Banana', 'Grape'])
print(s)
# Apple     5.0
# Banana    3.0
# Grape     NaN
# dtype: float64
```

**方法 3：从标量值创建**

```python
# 标量值会被广播到所有索引
s = pd.Series(100, index=['a', 'b', 'c', 'd'])
print(s)
# a    100
# b    100
# c    100
# d    100
# dtype: int64
```

**指定数据类型**：

```python
# 显式指定 dtype
s = pd.Series([1, 2, 3], dtype='float64')
print(s)
# 0    1.0
# 1    2.0
# 2    3.0
# dtype: float64
```

---

#### 访问 Series 数据

**方法 1：通过索引标签访问**

```python
s = pd.Series([85, 90, 78], index=['Math', 'English', 'Physics'])

# 单个值
print(s['Math'])        # 85
print(s.Math)           # 85（属性访问，仅限有效的 Python 标识符）

# 多个值
print(s[['Math', 'Physics']])
# Math       85
# Physics    78
# dtype: int64
```

**方法 2：通过位置索引访问**

```python
s = pd.Series([85, 90, 78], index=['Math', 'English', 'Physics'])

# 使用整数位置
print(s[0])          # 85（第一个元素）
print(s[-1])         # 78（最后一个元素）

# 切片
print(s[0:2])        # 前两个元素（不包含索引 2）
# Math       85
# English    90
# dtype: int64
```

**方法 3：使用 .loc 和 .iloc**

```python
s = pd.Series([85, 90, 78], index=['Math', 'English', 'Physics'])

# .loc：基于标签
print(s.loc['Math'])              # 85
print(s.loc['Math':'Physics'])    # 包含结束标签
# Math       85
# English    90
# Physics    78
# dtype: int64

# .iloc：基于整数位置
print(s.iloc[0])      # 85
print(s.iloc[0:2])    # 不包含索引 2
# Math       85
# English    90
# dtype: int64
```

**方法 4：布尔索引**

```python
s = pd.Series([85, 90, 78, 92, 88], index=['Math', 'English', 'Physics', 'Chemistry', 'Biology'])

# 筛选大于 85 的科目
print(s[s > 85])
# English      90
# Chemistry    92
# Biology      88
# dtype: int64

# 多条件筛选
print(s[(s > 80) & (s < 90)])
# Math       85
# Biology    88
# dtype: int64
```

---

#### Series 的常用属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `index` | 索引对象 | `s.index` |
| `values` | 值（NumPy 数组） | `s.values` |
| `dtype` | 数据类型 | `s.dtype` |
| `shape` | 形状（元素数量,） | `s.shape` → (5,) |
| `size` | 元素数量 | `s.size` → 5 |
| `name` | Series 的名称 | `s.name` |
| `index.name` | 索引的名称 | `s.index.name` |

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='MySeries')
s.index.name = 'Letters'

print(s)
# Letters
# a    10
# b    20
# c    30
# Name: MySeries, dtype: int64

print(f"索引: {s.index}")        # Index(['a', 'b', 'c'], dtype='object', name='Letters')
print(f"值: {s.values}")          # [10 20 30]
print(f"数据类型: {s.dtype}")     # int64
print(f"形状: {s.shape}")         # (3,)
print(f"大小: {s.size}")          # 3
print(f"Series 名称: {s.name}")   # MySeries
```

---

### 3.2.2 Series 的运算

#### 向量化运算

Series 支持类似 NumPy 的向量化运算，比 Python 循环快得多：

```python
s = pd.Series([10, 20, 30, 40])

# 算术运算
print(s + 5)      # [15, 25, 35, 45]
print(s * 2)      # [20, 40, 60, 80]
print(s ** 2)     # [100, 400, 900, 1600]
print(s / 10)     # [1.0, 2.0, 3.0, 4.0]

# 比较运算
print(s > 25)     # [False, False, True, True]
print(s == 30)    # [False, False, True, False]
```

#### Series 之间的运算

```python
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 逐元素运算（索引对齐）
print(s1 + s2)
# a    11
# b    22
# c    33
# dtype: int64

print(s1 * s2)
# a    10
# b    40
# c    90
# dtype: int64
```

**索引自动对齐**（重要特性）：

```python
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['b', 'c', 'd'])

# 自动对齐索引，未匹配的显示 NaN
print(s1 + s2)
# a     NaN
# b    21.0
# c    32.0
# d     NaN
# dtype: float64
```

#### 数学函数

```python
import numpy as np

s = pd.Series([1, 4, 9, 16, 25])

print(np.sqrt(s))     # [1.0, 2.0, 3.0, 4.0, 5.0]
print(np.log(s))      # 自然对数
print(np.exp(s))      # e^x
```

---

### 3.2.3 常用方法与统计

#### 基本统计方法

```python
s = pd.Series([85, 90, 78, 92, 88])

print(f"均值: {s.mean()}")          # 86.6
print(f"中位数: {s.median()}")      # 88.0
print(f"标准差: {s.std()}")         # 5.5
print(f"方差: {s.var()}")           # 30.3
print(f"最小值: {s.min()}")         # 78
print(f"最大值: {s.max()}")         # 92
print(f"求和: {s.sum()}")           # 433
print(f"计数: {s.count()}")         # 5（非 NaN 值的数量）
```

#### 描述性统计

```python
s = pd.Series([85, 90, 78, 92, 88, 76, 95])

# 一次性获取多个统计指标
print(s.describe())
# count     7.000000
# mean     86.285714
# std       7.087326
# min      76.000000
# 25%      81.500000
# 50%      88.000000
# 75%      91.000000
# max      95.000000
# dtype: float64
```

#### 排序

```python
s = pd.Series([30, 10, 40, 20], index=['d', 'a', 'c', 'b'])

# 按值排序
print(s.sort_values())
# a    10
# b    20
# d    30
# c    40
# dtype: int64

# 降序排序
print(s.sort_values(ascending=False))
# c    40
# d    30
# b    20
# a    10
# dtype: int64

# 按索引排序
print(s.sort_index())
# a    10
# b    20
# c    40
# d    30
# dtype: int64
```

#### 唯一值和计数

```python
s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'D'])

# 唯一值
print(s.unique())              # ['A' 'B' 'C' 'D']

# 唯一值数量
print(s.nunique())             # 4

# 值计数（频次统计）
print(s.value_counts())
# A    3
# B    2
# C    1
# D    1
# Name: count, dtype: int64

# 按频次升序
print(s.value_counts(ascending=True))
```

#### 查找最值的索引

```python
s = pd.Series([85, 90, 78, 92, 88], index=['Math', 'English', 'Physics', 'Chemistry', 'Biology'])

print(s.idxmax())  # Chemistry（最大值的索引）
print(s.idxmin())  # Physics（最小值的索引）
```

---

### 3.2.4 统计案例

#### 案例 1：学生成绩统计

```python
import pandas as pd

# 学生成绩数据
scores = pd.Series(
    [85, 90, 78, 92, 88, 76, 95, 82, 89, 91],
    index=['张三', '李四', '王五', '赵六', '钱七',
           '孙八', '周九', '吴十', '郑一', '王二']
)

# 基本统计
print("成绩统计：")
print(scores.describe())

# 最高分和最低分
print(f"\n最高分: {scores.max()}（{scores.idxmax()}）")
print(f"最低分: {scores.min()}（{scores.idxmin()}）")

# 及格率
passing = scores >= 60
passing_rate = passing.sum() / len(scores) * 100
print(f"\n及格率: {passing_rate}%")

# 优秀学生（>= 90）
excellent = scores[scores >= 90]
print(f"\n优秀学生:\n{excellent}")

# 成绩分布
print("\n成绩分布:")
bins = [0, 60, 70, 80, 90, 100]
labels = ['不及格', '及格', '中等', '良好', '优秀']
categories = pd.cut(scores, bins=bins, labels=labels)
print(categories.value_counts().sort_index())
```

---

#### 案例 2：温度数据分析

```python
import pandas as pd

# 一周的温度数据（摄氏度）
temperatures = pd.Series(
    [22.5, 23.1, 24.8, 21.2, 25.5, 26.0, 19.8],
    index=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
)

print("一周温度数据:")
print(temperatures)

# 统计分析
print(f"\n平均温度: {temperatures.mean():.2f}°C")
print(f"最高温度: {temperatures.max():.2f}°C（{temperatures.idxmax()}）")
print(f"最低温度: {temperatures.min():.2f}°C（{temperatures.idxmin()}）")
print(f"温差: {temperatures.max() - temperatures.min():.2f}°C")

# 高于平均温度的天数
above_avg = temperatures[temperatures > temperatures.mean()]
print(f"\n高于平均温度的天数: {len(above_avg)} 天")
print(above_avg)

# 温度变化趋势（相邻日差值）
temp_diff = temperatures.diff()
print(f"\n每日温度变化:")
print(temp_diff)
```

---

#### 案例 3：股票价格分析

```python
import pandas as pd
import numpy as np

# 模拟 30 天的股票收盘价
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
prices = pd.Series(
    100 + np.cumsum(np.random.randn(30) * 2),
    index=dates,
    name='Stock Price'
)

print("股票价格数据（前 10 天）:")
print(prices.head(10))

# 统计分析
print(f"\n平均价格: {prices.mean():.2f}")
print(f"最高价: {prices.max():.2f}（{prices.idxmax().date()}）")
print(f"最低价: {prices.min():.2f}（{prices.idxmin().date()}）")
print(f"波动率（标准差）: {prices.std():.2f}")

# 每日收益率
returns = prices.pct_change()
print(f"\n平均日收益率: {returns.mean():.4f}")
print(f"最大单日涨幅: {returns.max():.2%}（{returns.idxmax().date()}）")
print(f"最大单日跌幅: {returns.min():.2%}（{returns.idxmin().date()}）")

# 上涨和下跌天数
up_days = (returns > 0).sum()
down_days = (returns < 0).sum()
print(f"\n上涨天数: {up_days}，下跌天数: {down_days}")
```

---

#### 案例 4：销售数据分析

```python
import pandas as pd

# 各产品销售额
sales = pd.Series({
    'iPhone': 150000,
    'iPad': 80000,
    'MacBook': 120000,
    'AirPods': 45000,
    'Apple Watch': 60000
})

print("产品销售额:")
print(sales)

# 总销售额
total_sales = sales.sum()
print(f"\n总销售额: ¥{total_sales:,.0f}")

# 销售额占比
sales_pct = sales / total_sales * 100
print("\n销售额占比:")
print(sales_pct.apply(lambda x: f"{x:.2f}%"))

# 销售排名
ranking = sales.sort_values(ascending=False)
print("\n销售排名:")
for rank, (product, amount) in enumerate(ranking.items(), 1):
    print(f"{rank}. {product}: ¥{amount:,}")

# 销售额超过 10 万的产品
high_sales = sales[sales >= 100000]
print(f"\n销售额超过 10 万的产品:")
print(high_sales)
```

---

#### 案例 5：数据合并与计算

```python
import pandas as pd

# 两个季度的销售数据
q1_sales = pd.Series({'A': 100, 'B': 150, 'C': 200}, name='Q1')
q2_sales = pd.Series({'A': 120, 'B': 130, 'C': 250, 'D': 180}, name='Q2')

print("第一季度销售:")
print(q1_sales)
print("\n第二季度销售:")
print(q2_sales)

# 增长额（自动对齐）
growth = q2_sales - q1_sales
print("\n增长额:")
print(growth)

# 增长率
growth_rate = (q2_sales - q1_sales) / q1_sales * 100
print("\n增长率:")
print(growth_rate.dropna().apply(lambda x: f"{x:.2f}%"))

# 总销售额
total = q1_sales.add(q2_sales, fill_value=0)  # 使用 fill_value 处理缺失值
print("\n总销售额:")
print(total)
```

---

## 3.3 核心数据结构：DataFrame

### 3.3.1 创建与访问

#### 什么是 DataFrame？

**DataFrame** 是 Pandas 的二维表格数据结构，由以下部分组成：
1. **行索引（Index）**：行的标签
2. **列名（Columns）**：列的标签
3. **数据（Values）**：存储在 NumPy 数组中

**DataFrame 的特点**：
- 类似于 Excel 电子表格或 SQL 表
- 每列可以是不同的数据类型
- 大小可变（可以插入和删除列）
- 自动或显式的数据对齐
- 强大的数据操作和分析能力

**DataFrame 的结构**：
```
         列名1  列名2  列名3
行索引0    值    值    值
行索引1    值    值    值
行索引2    值    值    值
```

---

#### DataFrame 的创建

**方法 1：从字典创建**

```python
import pandas as pd

# 字典的键成为列名
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'],
    'Salary': [8000, 12000, 15000, 10000]
}

df = pd.DataFrame(data)
print(df)
#       Name  Age       City  Salary
# 0    Alice   25    Beijing    8000
# 1      Bob   30   Shanghai   12000
# 2  Charlie   35  Guangzhou   15000
# 3    David   28   Shenzhen   10000

# 自定义行索引
df = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3', 'emp4'])
print(df.index)  # Index(['emp1', 'emp2', 'emp3', 'emp4'], dtype='object')
```

**方法 2：从列表的字典创建**

```python
# 每个键对应一列
data = {
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print(df)
#    col1  col2
# 0     1    10
# 1     2    20
# 2     3    30
# 3     4    40
```

**方法 3：从字典的列表创建**

```python
# 每个字典对应一行
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'Beijing'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Shanghai'},
    {'Name': 'Charlie', 'Age': 35}  # 缺失 City，会自动填充 NaN
]
df = pd.DataFrame(data)
print(df)
#       Name  Age       City
# 0    Alice   25    Beijing
# 1      Bob   30   Shanghai
# 2  Charlie   35        NaN
```

**方法 4：从 NumPy 数组创建**

```python
import numpy as np

# 2D NumPy 数组
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data,
                  columns=['A', 'B', 'C'],
                  index=['row1', 'row2', 'row3'])
print(df)
#       A  B  C
# row1  1  2  3
# row2  4  5  6
# row3  7  8  9
```

**方法 5：从 Series 字典创建**

```python
# 每个 Series 对应一列
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)
#    col1  col2
# a     1    10
# b     2    20
# c     3    30
```

**方法 6：从 CSV 文件创建**（后续详细讲解）

```python
# df = pd.read_csv('data.csv')
```

---

#### 获取 DataFrame 数据

**查看数据**：

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'Salary': [8000, 12000, 15000, 10000, 7000]
})

# 查看前几行
print(df.head())      # 默认前 5 行
print(df.head(3))     # 前 3 行

# 查看后几行
print(df.tail())      # 默认后 5 行
print(df.tail(2))     # 后 2 行

# 随机抽样
print(df.sample(3))   # 随机 3 行
```

**选择列**：

```python
# 单列（返回 Series）
print(df['Name'])
print(df.Name)  # 属性访问（仅限有效的 Python 标识符）

# 多列（返回 DataFrame）
print(df[['Name', 'Salary']])
```

**选择行**：

```python
# 使用切片
print(df[0:3])      # 前 3 行（不包含索引 3）

# 使用 .loc（基于标签）
print(df.loc[0])           # 第一行（返回 Series）
print(df.loc[0:2])         # 前 3 行（包含索引 2）
print(df.loc[[0, 2, 4]])   # 指定行

# 使用 .iloc（基于位置）
print(df.iloc[0])          # 第一行
print(df.iloc[0:3])        # 前 3 行（不包含索引 3）
print(df.iloc[-1])         # 最后一行
```

**选择行和列**：

```python
# .loc[行, 列]
print(df.loc[0, 'Name'])              # 单个值
print(df.loc[0:2, ['Name', 'Age']])   # 多行多列

# .iloc[行位置, 列位置]
print(df.iloc[0, 0])                  # 第一行第一列
print(df.iloc[0:3, 0:2])              # 前 3 行前 2 列

# .at 和 .iat（访问单个值，速度更快）
print(df.at[0, 'Name'])               # 基于标签
print(df.iat[0, 0])                   # 基于位置
```

**布尔索引**：

```python
# 筛选 Age > 25 的行
print(df[df['Age'] > 25])

# 多条件筛选
print(df[(df['Age'] > 25) & (df['Salary'] > 10000)])

# 使用 query 方法（更简洁）
print(df.query('Age > 25 and Salary > 10000'))
```

---

#### 常用属性

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [8000, 12000, 15000]
})

print(f"形状: {df.shape}")           # (3, 3) - (行数, 列数)
print(f"大小: {df.size}")            # 9 - 总元素数
print(f"维度: {df.ndim}")            # 2
print(f"行索引: {df.index}")         # RangeIndex(start=0, stop=3, step=1)
print(f"列名: {df.columns}")         # Index(['Name', 'Age', 'Salary'], dtype='object')
print(f"数据类型:\n{df.dtypes}")     # 每列的数据类型
print(f"内存使用:\n{df.memory_usage()}")  # 每列的内存占用
print(f"是否为空: {df.empty}")       # False
```

**查看数据信息**：

```python
# 简洁的概览
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64
#  2   Salary  3 non-null      int64
# dtypes: int64(2), object(1)
# memory usage: 200.0+ bytes

# 统计描述（仅数值列）
print(df.describe())
#              Age        Salary
# count   3.000000      3.000000
# mean   30.000000  11666.666667
# std     5.000000   3511.884584
# min    25.000000   8000.000000
# 25%    27.500000   10000.000000
# 50%    30.000000  12000.000000
# 75%    32.500000  13500.000000
# max    35.000000  15000.000000
```

---

### 3.3.2 常用方法与统计

#### 统计方法

```python
df = pd.DataFrame({
    'A': [10, 20, 30, 40],
    'B': [15, 25, 35, 45],
    'C': [12, 22, 32, 42]
})

# 每列的统计
print(df.mean())        # 每列平均值
print(df.sum())         # 每列求和
print(df.min())         # 每列最小值
print(df.max())         # 每列最大值
print(df.std())         # 每列标准差

# 每行的统计（axis=1）
print(df.mean(axis=1))  # 每行平均值
print(df.sum(axis=1))   # 每行求和
```

#### 排序

```python
df = pd.DataFrame({
    'Name': ['Bob', 'Alice', 'David', 'Charlie'],
    'Age': [30, 25, 28, 35],
    'Salary': [12000, 8000, 10000, 15000]
})

# 按列值排序
sorted_df = df.sort_values('Age')
print(sorted_df)
#       Name  Age  Salary
# 1    Alice   25    8000
# 2    David   28   10000
# 0      Bob   30   12000
# 3  Charlie   35   15000

# 多列排序
sorted_df = df.sort_values(['Age', 'Salary'], ascending=[True, False])

# 按索引排序
sorted_df = df.sort_index()
```

#### 添加、删除列

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# 添加新列
df['City'] = ['Beijing', 'Shanghai']
df['Salary'] = [8000, 12000]
print(df)

# 基于现有列计算新列
df['Bonus'] = df['Salary'] * 0.1

# 删除列
df = df.drop('Bonus', axis=1)    # axis=1 表示列
# 或
df = df.drop(columns=['Bonus'])

# 原地删除（不创建副本）
df.drop('City', axis=1, inplace=True)
```

#### 重命名

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# 重命名列
df = df.rename(columns={'A': 'col1', 'B': 'col2'})
print(df)
#    col1  col2
# 0     1     4
# 1     2     5
# 2     3     6

# 批量重命名
df.columns = ['X', 'Y']
```

---

### 3.3.3 运算

#### DataFrame 与标量运算

```python
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
})

# 广播运算
print(df + 10)
print(df * 2)
print(df ** 2)
```

#### DataFrame 之间运算

```python
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
})

# 逐元素运算
print(df1 + df2)
print(df1 * df2)
```

#### 处理缺失值的运算

```python
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['row1', 'row2'])

df2 = pd.DataFrame({
    'A': [10, 20],
    'C': [30, 40]
}, index=['row1', 'row3'])

# 自动对齐，未匹配的为 NaN
result = df1 + df2
print(result)
#         A   B     C
# row1  11.0 NaN   NaN
# row2   NaN NaN   NaN
# row3   NaN NaN   NaN

# 使用 fill_value 处理
result = df1.add(df2, fill_value=0)
print(result)
#         A    B     C
# row1  11.0  3.0  30.0
# row2   2.0  4.0   NaN
# row3  20.0  NaN  40.0
```

---

### 3.3.4 案例练习

#### 案例 1：学生成绩分析

```python
import pandas as pd

# 学生成绩数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [85, 90, 78, 92, 88],
    'English': [88, 85, 92, 80, 95],
    'Physics': [90, 88, 85, 95, 82]
})

print("学生成绩表:")
print(df)

# 计算每个学生的总分和平均分
df['Total'] = df[['Math', 'English', 'Physics']].sum(axis=1)
df['Average'] = df[['Math', 'English', 'Physics']].mean(axis=1)

print("\n添加总分和平均分:")
print(df)

# 每科平均分
subject_avg = df[['Math', 'English', 'Physics']].mean()
print(f"\n每科平均分:\n{subject_avg}")

# 找出总分最高的学生
top_student = df.loc[df['Total'].idxmax()]
print(f"\n总分最高的学生:\n{top_student}")

# 筛选平均分 >= 88 的学生
excellent = df[df['Average'] >= 88]
print(f"\n优秀学生（平均分 >= 88）:\n{excellent}")
```

---

#### 案例 2：销售数据分析

```python
import pandas as pd

# 销售数据
df = pd.DataFrame({
    'Product': ['iPhone', 'iPad', 'MacBook', 'AirPods', 'Watch'],
    'Q1_Sales': [1500, 800, 1200, 450, 600],
    'Q2_Sales': [1800, 750, 1300, 500, 650],
    'Q3_Sales': [2000, 900, 1400, 550, 700],
    'Q4_Sales': [2200, 950, 1500, 600, 750]
})

print("销售数据:")
print(df)

# 计算全年总销售额
df['Total'] = df[['Q1_Sales', 'Q2_Sales', 'Q3_Sales', 'Q4_Sales']].sum(axis=1)

# 计算季度平均销售额
df['Average'] = df[['Q1_Sales', 'Q2_Sales', 'Q3_Sales', 'Q4_Sales']].mean(axis=1)

print("\n添加总销售额和平均销售额:")
print(df)

# 销售额排名
ranking = df.sort_values('Total', ascending=False)
print("\n销售额排名:")
print(ranking[['Product', 'Total']])

# 计算同比增长（Q4 vs Q1）
df['Growth'] = (df['Q4_Sales'] - df['Q1_Sales']) / df['Q1_Sales'] * 100
print("\n同比增长率:")
print(df[['Product', 'Growth']])
```

---

#### 案例 3：员工考勤统计

```python
import pandas as pd

# 员工考勤数据（天数）
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Present': [22, 20, 21, 19, 22],
    'Absent': [0, 2, 1, 3, 0],
    'Late': [1, 3, 2, 4, 1]
})

print("考勤数据:")
print(df)

# 总工作日
total_days = 22

# 出勤率
df['Attendance_Rate'] = (df['Present'] / total_days * 100).round(2)

# 考勤评级
def get_rating(rate):
    if rate >= 95:
        return 'A'
    elif rate >= 85:
        return 'B'
    elif rate >= 75:
        return 'C'
    else:
        return 'D'

df['Rating'] = df['Attendance_Rate'].apply(get_rating)

print("\n添加出勤率和评级:")
print(df)

# 统计各评级人数
print("\n评级分布:")
print(df['Rating'].value_counts().sort_index())
```

---

#### 案例 4：电影评分分析

```python
import pandas as pd

# 电影评分数据
df = pd.DataFrame({
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action', 'Comedy', 'Drama', 'Action', 'Comedy'],
    'Rating': [8.5, 7.2, 9.1, 6.8, 8.0],
    'Reviews': [1500, 800, 2000, 600, 1200],
    'Revenue': [250, 120, 300, 80, 180]  # 单位：百万
})

print("电影数据:")
print(df)

# 每个类型的平均评分
genre_rating = df.groupby('Genre')['Rating'].mean()
print(f"\n每个类型的平均评分:\n{genre_rating}")

# 高评分电影（>= 8.0）
high_rated = df[df['Rating'] >= 8.0]
print(f"\n高评分电影:\n{high_rated}")

# 票房与评分的相关性
correlation = df['Rating'].corr(df['Revenue'])
print(f"\n评分与票房相关系数: {correlation:.3f}")

# 按票房排序
sorted_by_revenue = df.sort_values('Revenue', ascending=False)
print(f"\n票房排名:")
print(sorted_by_revenue[['Title', 'Revenue', 'Rating']])
```

---

#### 案例 5：股票价格分析

```python
import pandas as pd
import numpy as np

# 模拟股票数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')

df = pd.DataFrame({
    'Date': dates,
    'Open': 100 + np.random.randn(30) * 5,
    'High': 105 + np.random.randn(30) * 5,
    'Low': 95 + np.random.randn(30) * 5,
    'Close': 100 + np.random.randn(30) * 5,
    'Volume': np.random.randint(1000000, 5000000, 30)
})

# 设置日期为索引
df = df.set_index('Date')

print("股票数据（前 10 天）:")
print(df.head(10))

# 计算每日涨跌幅
df['Change'] = df['Close'] - df['Open']
df['Change_Pct'] = (df['Close'] - df['Open']) / df['Open'] * 100

# 统计分析
print(f"\n平均收盘价: {df['Close'].mean():.2f}")
print(f"最高价: {df['High'].max():.2f}")
print(f"最低价: {df['Low'].min():.2f}")
print(f"平均成交量: {df['Volume'].mean():.0f}")

# 上涨和下跌天数
up_days = (df['Change'] > 0).sum()
down_days = (df['Change'] < 0).sum()
print(f"\n上涨天数: {up_days}，下跌天数: {down_days}")

# 最大涨幅和跌幅
print(f"最大涨幅: {df['Change_Pct'].max():.2f}%（{df['Change_Pct'].idxmax().date()}）")
print(f"最大跌幅: {df['Change_Pct'].min():.2f}%（{df['Change_Pct'].idxmin().date()}）")
```

---

#### 案例 6：电商用户行为分析（进阶版）

```python
import pandas as pd
import numpy as np

# 模拟用户行为数据
np.random.seed(42)
n_users = 100

df = pd.DataFrame({
    'UserID': range(1, n_users + 1),
    'Age': np.random.randint(18, 65, n_users),
    'Gender': np.random.choice(['M', 'F'], n_users),
    'City': np.random.choice(['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'], n_users),
    'PageViews': np.random.randint(1, 100, n_users),
    'TimeSpent': np.random.randint(5, 300, n_users),  # 分钟
    'Purchases': np.random.randint(0, 10, n_users),
    'Revenue': np.random.randint(0, 5000, n_users)
})

print("用户行为数据（前 10 条）:")
print(df.head(10))

# 1. 基本统计
print("\n=== 基本统计 ===")
print(df.describe())

# 2. 按性别分组统计
print("\n=== 按性别分组统计 ===")
gender_stats = df.groupby('Gender').agg({
    'PageViews': 'mean',
    'TimeSpent': 'mean',
    'Purchases': 'sum',
    'Revenue': 'sum'
}).round(2)
print(gender_stats)

# 3. 按城市分组统计
print("\n=== 按城市分组统计 ===")
city_stats = df.groupby('City').agg({
    'UserID': 'count',
    'Revenue': ['sum', 'mean']
}).round(2)
city_stats.columns = ['User_Count', 'Total_Revenue', 'Avg_Revenue']
print(city_stats)

# 4. 年龄分段分析
print("\n=== 年龄分段分析 ===")
bins = [0, 25, 35, 45, 100]
labels = ['18-25', '26-35', '36-45', '46+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
age_group_stats = df.groupby('AgeGroup')['Revenue'].mean().round(2)
print(age_group_stats)

# 5. 转化率分析
df['Converted'] = df['Purchases'] > 0
conversion_rate = df['Converted'].sum() / len(df) * 100
print(f"\n转化率: {conversion_rate:.2f}%")

# 6. 高价值用户识别（购买金额 > 2000）
high_value_users = df[df['Revenue'] > 2000]
print(f"\n高价值用户数: {len(high_value_users)}（占比 {len(high_value_users)/len(df)*100:.2f}%）")

# 7. 用户分层
def user_segment(row):
    if row['Revenue'] > 3000:
        return 'VIP'
    elif row['Revenue'] > 1000:
        return 'Premium'
    elif row['Revenue'] > 0:
        return 'Regular'
    else:
        return 'Inactive'

df['Segment'] = df.apply(user_segment, axis=1)
print("\n用户分层分布:")
print(df['Segment'].value_counts())
```

---

## 3.4 数据的输入与导出

### CSV 文件操作

```python
import pandas as pd

# 读取 CSV
df = pd.read_csv('data.csv')

# 常用参数
df = pd.read_csv(
    'data.csv',
    sep=',',              # 分隔符（默认逗号）
    header=0,             # 列名所在行（默认第一行）
    index_col=0,          # 索引列
    usecols=['A', 'B'],   # 读取指定列
    nrows=100,            # 读取前 N 行
    encoding='utf-8'      # 编码格式
)

# 写入 CSV
df.to_csv('output.csv', index=False)  # index=False 不保存索引
```

### Excel 文件操作

```python
# 读取 Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 读取多个工作表
dfs = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'Sheet2'])

# 写入 Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# 写入多个工作表
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

### 其他格式

```python
# JSON
df.to_json('data.json')
df = pd.read_json('data.json')

# SQL
import sqlite3
conn = sqlite3.connect('database.db')
df.to_sql('table_name', conn, if_exists='replace', index=False)
df = pd.read_sql('SELECT * FROM table_name', conn)

# HTML
df.to_html('table.html')

# Clipboard（剪贴板）
df.to_clipboard()
df = pd.read_clipboard()
```

---

## 3.5 数据清洗与预处理

### 1. 缺失值处理

#### 检测缺失值

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# 检测缺失值
print(df.isnull())      # 或 df.isna()
#        A      B      C
# 0  False  False  False
# 1  False   True  False
# 2   True   True  False
# 3  False  False  False

# 检测非缺失值
print(df.notnull())     # 或 df.notna()

# 统计每列缺失值数量
print(df.isnull().sum())
# A    1
# B    2
# C    0

# 统计缺失值总数
print(df.isnull().sum().sum())  # 3
```

#### 删除缺失值

```python
# 删除包含任何 NaN 的行
df_cleaned = df.dropna()
print(df_cleaned)
#      A    B   C
# 0  1.0  5.0   9
# 3  4.0  8.0  12

# 删除所有值都是 NaN 的行
df_cleaned = df.dropna(how='all')

# 删除包含 NaN 的列
df_cleaned = df.dropna(axis=1)

# 保留至少有 N 个非 NaN 值的行
df_cleaned = df.dropna(thresh=2)

# 原地删除
df.dropna(inplace=True)
```

#### 填充缺失值

```python
# 用指定值填充
df_filled = df.fillna(0)

# 用每列的均值填充
df_filled = df.fillna(df.mean())

# 用每列的中位数填充
df_filled = df.fillna(df.median())

# 用前一个值填充（前向填充）
df_filled = df.ffill()  # 或 df.fillna(method='ffill')

# 用后一个值填充（后向填充）
df_filled = df.bfill()  # 或 df.fillna(method='bfill')

# 按列分别填充
df_filled = df.fillna({'A': 0, 'B': df['B'].mean()})

# 插值填充
df_filled = df.interpolate()
```

---

### 2. 重复数据处理

#### 1. 检测重复行

```python
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 3],
    'B': [4, 5, 5, 6, 7]
})

# 检测重复行
print(df.duplicated())
# 0    False
# 1    False
# 2     True   # 与索引 1 重复
# 3    False
# 4    False

# 标记所有重复行（包括第一次出现）
print(df.duplicated(keep=False))
# 0    False
# 1     True
# 2     True
# 3     True
# 4    False

# 统计重复行数量
print(df.duplicated().sum())  # 1
```

#### 2. 删除重复行

```python
# 保留第一次出现，删除后续重复
df_unique = df.drop_duplicates()
print(df_unique)
#    A  B
# 0  1  4
# 1  2  5
# 3  3  6

# 保留最后一次出现
df_unique = df.drop_duplicates(keep='last')

# 删除所有重复行
df_unique = df.drop_duplicates(keep=False)
```

#### 3. 按指定列去重

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'Age': [25, 30, 26, 35],
    'City': ['Beijing', 'Shanghai', 'Beijing', 'Guangzhou']
})

# 仅根据 Name 列去重
df_unique = df.drop_duplicates(subset=['Name'])
print(df_unique)
#       Name  Age       City
# 0    Alice   25    Beijing
# 1      Bob   30   Shanghai
# 3  Charlie   35  Guangzhou

# 根据多列去重
df_unique = df.drop_duplicates(subset=['Name', 'City'])
```

#### 4. 保留最后一次出现的重复行

```python
df_unique = df.drop_duplicates(subset=['Name'], keep='last')
print(df_unique)
#       Name  Age       City
# 2    Alice   26    Beijing   # 保留 Alice 的第二次出现
# 1      Bob   30   Shanghai
# 3  Charlie   35  Guangzhou
```

#### 5. 综合案例：处理真实数据

```python
import pandas as pd

# 模拟真实数据（包含重复和缺失值）
df = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4, 5],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David', None],
    'Email': ['a@x.com', 'b@x.com', 'b@x.com', None, 'd@x.com', 'd@x.com', 'e@x.com'],
    'Age': [25, 30, 30, 35, None, 28, 22]
})

print("原始数据:")
print(df)

# 1. 删除完全重复的行
df = df.drop_duplicates()

# 2. 根据 ID 去重（保留第一次出现）
df = df.drop_duplicates(subset=['ID'], keep='first')

# 3. 删除 Name 为空的行
df = df.dropna(subset=['Name'])

# 4. 填充 Age 缺失值（用中位数）
df['Age'].fillna(df['Age'].median(), inplace=True)

# 5. 填充 Email 缺失值（用自定义值）
df['Email'].fillna('unknown@x.com', inplace=True)

print("\n清洗后的数据:")
print(df)
```

#### 注意事项

1. **先检测后处理**：使用 `duplicated()` 检查重复情况，再决定处理策略
2. **指定去重列**：根据业务逻辑选择关键字段去重
3. **保留策略**：根据需求选择保留第一次（`keep='first'`）、最后一次（`keep='last'`）或删除所有（`keep=False`）
4. **原地修改**：使用 `inplace=True` 可以节省内存，但会修改原始数据
5. **重置索引**：去重后建议重置索引 `df.reset_index(drop=True, inplace=True)`

---

### 3. 数据类型转换

#### 核心方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `astype()` | 强制类型转换 | `df['A'].astype('int')` |
| `pd.to_numeric()` | 转换为数值类型 | `pd.to_numeric(df['A'], errors='coerce')` |
| `pd.to_datetime()` | 转换为日期时间 | `pd.to_datetime(df['Date'])` |
| `pd.Categorical()` | 转换为分类类型 | `pd.Categorical(df['Category'])` |

#### 代码案例详解

**1. 查看数据类型**

```python
import pandas as pd

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': ['4.5', '5.6', '6.7'],
    'C': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'D': ['Low', 'Medium', 'High']
})

print(df.dtypes)
# A    object
# B    object
# C    object
# D    object
# dtype: object
```

**2. 强制类型转换**

```python
# 转换为整数
df['A'] = df['A'].astype('int64')

# 转换为浮点数
df['B'] = df['B'].astype('float64')

print(df.dtypes)
# A      int64
# B    float64
# C     object
# D     object
# dtype: object

# 处理转换错误
df_error = pd.DataFrame({'A': ['1', '2', 'abc']})
# df_error['A'].astype('int')  # 会报错

# 使用 pd.to_numeric 处理错误
df_error['A'] = pd.to_numeric(df_error['A'], errors='coerce')  # 无法转换的变为 NaN
print(df_error)
#      A
# 0  1.0
# 1  2.0
# 2  NaN
```

**3. 转换为日期时间**

```python
# 转换为 datetime
df['C'] = pd.to_datetime(df['C'])
print(df.dtypes)
# A             int64
# B           float64
# C    datetime64[ns]
# D            object
# dtype: object

# 指定日期格式
dates = pd.Series(['01/01/2024', '02/01/2024', '03/01/2024'])
dates = pd.to_datetime(dates, format='%d/%m/%Y')
print(dates)
```

**4. 转换为分类数据**

```python
# 转换为分类类型（节省内存，提升性能）
df['D'] = df['D'].astype('category')
print(df.dtypes)
# A             int64
# B           float64
# C    datetime64[ns]
# D          category
# dtype: object

# 查看分类信息
print(df['D'].cat.categories)  # Index(['High', 'Low', 'Medium'], dtype='object')

# 设置分类顺序
df['D'] = pd.Categorical(df['D'], categories=['Low', 'Medium', 'High'], ordered=True)
print(df['D'])
# 0       Low
# 1    Medium
# 2      High
# Name: D, dtype: category
# Categories (3, object): ['Low' < 'Medium' < 'High']
```

**5. 数据类型优化**

```python
import pandas as pd
import numpy as np

# 创建大数据集
df = pd.DataFrame({
    'A': np.random.randint(0, 100, 1000000),
    'B': np.random.choice(['A', 'B', 'C'], 1000000),
    'C': np.random.randn(1000000)
})

print("优化前内存使用:")
print(df.memory_usage(deep=True))

# 优化整数类型
df['A'] = df['A'].astype('int8')  # 0-100 范围，int8 足够

# 优化字符串为分类
df['B'] = df['B'].astype('category')

# 优化浮点数
df['C'] = df['C'].astype('float32')

print("\n优化后内存使用:")
print(df.memory_usage(deep=True))
```

#### 常见问题与技巧

**问题 1：字符串转数值时包含非数值字符**
```python
# 使用 errors='coerce' 将无法转换的设为 NaN
df['col'] = pd.to_numeric(df['col'], errors='coerce')
```

**问题 2：日期格式不统一**
```python
# 使用 infer_datetime_format=True 自动推断
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
```

**问题 3：批量转换多列**
```python
# 批量转换
cols_to_convert = ['A', 'B', 'C']
df[cols_to_convert] = df[cols_to_convert].astype('float64')
```

#### 实战案例：处理 penguins.csv

```python
import pandas as pd

# 读取数据
df = pd.read_csv('penguins.csv')

print("原始数据类型:")
print(df.dtypes)

# 1. 转换分类变量
categorical_cols = ['species', 'island', 'sex']
for col in categorical_cols:
    df[col] = df[col].astype('category')

# 2. 转换数值变量（优化内存）
df['bill_length_mm'] = df['bill_length_mm'].astype('float32')
df['bill_depth_mm'] = df['bill_depth_mm'].astype('float32')
df['flipper_length_mm'] = df['flipper_length_mm'].astype('int16')
df['body_mass_g'] = df['body_mass_g'].astype('int16')

# 3. 转换年份为整数
df['year'] = df['year'].astype('int16')

print("\n优化后数据类型:")
print(df.dtypes)

print("\n内存使用对比:")
print(f"原始: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
```

---

### 4. 数据重塑与变形

#### 1. 行列转置（df.T）

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'English': [88, 85, 92]
})

# 转置
df_transposed = df.T
print(df_transposed)
#             0      1        2
# Name    Alice    Bob  Charlie
# Math       85     90       78
# English    88     85       92
```

#### 2. 宽表转长表（pd.melt()）

```python
# 宽表
df_wide = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Math': [85, 90],
    'English': [88, 85]
})

# 转换为长表
df_long = pd.melt(df_wide, id_vars=['Name'],
                  value_vars=['Math', 'English'],
                  var_name='Subject',
                  value_name='Score')
print(df_long)
#      Name  Subject  Score
# 0   Alice     Math     85
# 1     Bob     Math     90
# 2   Alice  English     88
# 3     Bob  English     85
```

#### 3. 长表转宽表（df.pivot()）

```python
# 长表
df_long = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob'],
    'Subject': ['Math', 'English', 'Math', 'English'],
    'Score': [85, 88, 90, 85]
})

# 转换为宽表
df_wide = df_long.pivot(index='Name', columns='Subject', values='Score')
print(df_wide)
# Subject  English  Math
# Name
# Alice         88    85
# Bob           85    90
```

#### 4. 分列操作（str.split()）

```python
df = pd.DataFrame({
    'Name': ['Alice_25', 'Bob_30', 'Charlie_35']
})

# 分列
df[['Name', 'Age']] = df['Name'].str.split('_', expand=True)
print(df)
#       Name Age
# 0    Alice  25
# 1      Bob  30
# 2  Charlie  35

# 转换 Age 为整数
df['Age'] = df['Age'].astype('int')
```

#### 注意事项

1. **pivot() 要求索引唯一**：如果索引重复，使用 `pivot_table()` 并指定聚合函数
2. **melt() 适合数据分析**：将宽表转为长表更适合 groupby 操作
3. **内存占用**：转置和重塑会创建新的 DataFrame，注意内存使用

---

### 5. 文本数据处理

Pandas 提供了强大的字符串处理方法（`.str` 访问器）：

#### 1. 字符串小写转换

```python
df = pd.DataFrame({
    'Name': ['ALICE', 'BOB', 'CHARLIE']
})

df['Name'] = df['Name'].str.lower()
print(df)
#       Name
# 0    alice
# 1      bob
# 2  charlie

# 其他转换
df['Name'].str.upper()      # 大写
df['Name'].str.title()      # 首字母大写
df['Name'].str.capitalize() # 句首大写
```

#### 2. 去除空格

```python
df = pd.DataFrame({
    'Name': ['  Alice  ', ' Bob ', 'Charlie  ']
})

df['Name'] = df['Name'].str.strip()   # 去除两端空格
# df['Name'].str.lstrip()  # 去除左侧空格
# df['Name'].str.rstrip()  # 去除右侧空格
print(df)
```

#### 3. 字符串替换

```python
df = pd.DataFrame({
    'Text': ['Hello World', 'Python Programming', 'Data Science']
})

# 简单替换
df['Text'] = df['Text'].str.replace('o', '0')
print(df)
#                    Text
# 0          Hell0 W0rld
# 1  Pyth0n Pr0gramming
# 2         Data Science

# 正则替换
df['Text'] = df['Text'].str.replace(r'\d', 'X', regex=True)  # 数字替换为 X
```

#### 4. 正则表达式提取

```python
df = pd.DataFrame({
    'Email': ['alice@example.com', 'bob@test.org', 'charlie@demo.net']
})

# 提取用户名（@ 之前的部分）
df['Username'] = df['Email'].str.extract(r'(.+)@')
print(df)
#                 Email Username
# 0  alice@example.com    alice
# 1       bob@test.org      bob
# 2  charlie@demo.net  charlie

# 提取域名（@ 之后的部分）
df['Domain'] = df['Email'].str.extract(r'@(.+)')
print(df)
```

#### 5. 字符串包含检测

```python
df = pd.DataFrame({
    'Text': ['apple', 'banana', 'cherry', 'date']
})

# 检测包含 'a'
mask = df['Text'].str.contains('a')
print(df[mask])
#      Text
# 0   apple
# 1  banana
# 3    date

# 正则匹配
mask = df['Text'].str.contains(r'^c')  # 以 c 开头
print(df[mask])
```

#### 实战案例：处理 employees.csv

```python
import pandas as pd

# 模拟员工数据
df = pd.DataFrame({
    'Name': ['  ALICE WANG  ', ' bob chen ', 'CHARLIE LI'],
    'Email': ['alice@company.com', 'bob@company.com', 'charlie@company.com'],
    'Phone': ['138-1234-5678', '139-8765-4321', '136-5555-6666']
})

print("原始数据:")
print(df)

# 1. 清理姓名（去空格、标准化大小写）
df['Name'] = df['Name'].str.strip().str.title()

# 2. 提取邮箱用户名
df['Username'] = df['Email'].str.extract(r'(.+)@')[0]

# 3. 格式化电话号码（去除连字符）
df['Phone'] = df['Phone'].str.replace('-', '')

# 4. 检测特定域名的邮箱
df['IsCompanyEmail'] = df['Email'].str.contains('@company.com')

print("\n清洗后的数据:")
print(df)
```

---

#### 6. 数据分箱与离散化

将连续数值转换为分类区间：

```python
df = pd.DataFrame({
    'Age': [22, 25, 35, 45, 55, 65]
})

# 分箱
bins = [0, 30, 40, 50, 100]
labels = ['Youth', 'Adult', 'Middle', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df)
#    Age AgeGroup
# 0   22    Youth
# 1   25    Youth
# 2   35    Adult
# 3   45   Middle
# 4   55   Senior
# 5   65   Senior

# 等频分箱（每个箱子包含相似数量的样本）
df['AgeQcut'] = pd.qcut(df['Age'], q=3, labels=['Low', 'Medium', 'High'])
```

---

#### 7. 其他常用转换

```python
# 应用自定义函数
df['NewCol'] = df['OldCol'].apply(lambda x: x * 2)

# 映射字典
mapping = {'A': 1, 'B': 2, 'C': 3}
df['Mapped'] = df['Category'].map(mapping)

# 替换值
df['Col'].replace({'old': 'new', 'foo': 'bar'})

# 重命名列
df = df.rename(columns={'OldName': 'NewName'})

# 设置索引
df = df.set_index('ID')

# 重置索引
df = df.reset_index(drop=True)
```

---

## 3.6 时间数据的处理

### 1. 时间戳 timestamp

```python
import pandas as pd
import numpy as np

# 创建时间戳
ts = pd.Timestamp('2024-01-01 12:30:00')
print(ts)  # 2024-01-01 12:30:00

# 当前时间
now = pd.Timestamp.now()
print(now)

# 时间戳属性
print(ts.year)        # 2024
print(ts.month)       # 1
print(ts.day)         # 1
print(ts.hour)        # 12
print(ts.minute)      # 30
print(ts.dayofweek)   # 0（周一）
print(ts.dayofyear)   # 1
```

### 2. 日期数据转换

```python
# 字符串转日期
dates = pd.Series(['2024-01-01', '2024-01-02', '2024-01-03'])
dates = pd.to_datetime(dates)
print(dates)

# 多种格式自动识别
dates = pd.to_datetime(['2024-01-01', '01/02/2024', 'Jan 3, 2024'])
print(dates)

# 指定格式
dates = pd.to_datetime(['20240101', '20240102'], format='%Y%m%d')
print(dates)
```

### 3. 设置日期数据作为索引

```python
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=5, freq='D'),
    'Sales': [100, 120, 110, 130, 140]
})

# 设置日期为索引
df = df.set_index('Date')
print(df)
#             Sales
# Date
# 2024-01-01    100
# 2024-01-02    120
# 2024-01-03    110
# 2024-01-04    130
# 2024-01-05    140

# 使用日期索引选择数据
print(df.loc['2024-01-03'])      # 单日
print(df.loc['2024-01-02':'2024-01-04'])  # 日期范围
```

### 4. 时间间隔 timedelta

```python
# 创建时间间隔
delta = pd.Timedelta('2 days 3 hours')
print(delta)  # 2 days 03:00:00

# 时间运算
start = pd.Timestamp('2024-01-01')
end = start + pd.Timedelta('7 days')
print(end)  # 2024-01-08

# 计算时间差
df['Date1'] = pd.to_datetime(['2024-01-01', '2024-01-05'])
df['Date2'] = pd.to_datetime(['2024-01-10', '2024-01-15'])
df['Diff'] = df['Date2'] - df['Date1']
print(df['Diff'])
# 0   9 days
# 1  10 days
```

### 5. 时间序列

```python
# 生成日期范围
dates = pd.date_range('2024-01-01', periods=10, freq='D')
print(dates)

# 不同频率
dates_hour = pd.date_range('2024-01-01', periods=24, freq='H')   # 小时
dates_month = pd.date_range('2024-01-01', periods=12, freq='M')  # 月末
dates_week = pd.date_range('2024-01-01', periods=4, freq='W')    # 周

# 提取时间特征
df = pd.DataFrame({'Date': dates, 'Value': np.random.randn(10)})
df = df.set_index('Date')

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
df['Weekday'] = df.index.dayofweek
df['Quarter'] = df.index.quarter
```

### 6. 重新采样

```python
# 创建时间序列数据
dates = pd.date_range('2024-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randint(0, 100, len(dates)), index=dates)

# 降采样：日数据 -> 周数据
weekly = ts.resample('W').sum()    # 每周求和
print(weekly.head())

# 升采样：日数据 -> 小时数据（会产生 NaN）
hourly = ts.resample('H').mean()

# 不同的聚合方式
monthly_stats = ts.resample('M').agg(['sum', 'mean', 'max', 'min'])
print(monthly_stats)
```

---

## 3.7 数据分析与统计

### 1. 常用聚合函数

```python
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# 单个聚合
print(df['A'].sum())      # 15
print(df['A'].mean())     # 3.0
print(df['A'].median())   # 3.0
print(df['A'].std())      # 标准差
print(df['A'].var())      # 方差
print(df['A'].min())      # 1
print(df['A'].max())      # 5
print(df['A'].count())    # 5

# 多个聚合
print(df.agg(['sum', 'mean', 'max']))
```

### 2. 分组聚合

#### DataFrameGroupBy 对象

```python
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 30, 40, 50]
})

# 分组
grouped = df.groupby('Category')

# 查看分组
for name, group in grouped:
    print(f"Group {name}:")
    print(group)

# 分组聚合
print(grouped['Value'].sum())
# Category
# A    90
# B    60

print(grouped['Value'].mean())
# Category
# A    30.0
# B    30.0
```

### 3. 一次计算多个统计值

```python
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 250, 180],
    'Quantity': [10, 20, 15, 25, 18]
})

# 多列多聚合
result = df.groupby('Category').agg({
    'Sales': ['sum', 'mean', 'max'],
    'Quantity': ['sum', 'mean']
})
print(result)
```

### 4. 分组转换

```python
# 计算每组内的标准化值
df['Normalized'] = df.groupby('Category')['Sales'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

### 5. 分组过滤

```python
# 只保留组内均值 > 150 的组
filtered = df.groupby('Category').filter(lambda x: x['Sales'].mean() > 150)
print(filtered)
```

---

## 3.8 案例详解

由于案例已经在前面章节中详细展示，这里总结关键要点：

**数据分析流程**：
1. **数据导入**：`pd.read_csv()`, `pd.read_excel()`
2. **数据探索**：`df.head()`, `df.info()`, `df.describe()`
3. **数据清洗**：处理缺失值、重复值、异常值
4. **数据转换**：类型转换、数据重塑、特征工程
5. **数据分析**：分组聚合、统计分析
6. **数据可视化**：配合 Matplotlib/Seaborn
7. **结果导出**：`df.to_csv()`, `df.to_excel()`

---

## 学习建议

1. **循序渐进**：先掌握 Series 和 DataFrame 基础，再学习高级功能
2. **多做练习**：每个知识点都配有案例，务必动手实践
3. **查阅文档**：遇到问题查阅 [Pandas 官方文档](https://pandas.pydata.org/docs/)
4. **真实数据**：使用 Kaggle 等平台的真实数据集练习
5. **组合使用**：Pandas 通常与 NumPy、Matplotlib 配合使用

## 参考资源

- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [Pandas 快速入门](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas API 参考](https://pandas.pydata.org/docs/reference/index.html)
- [Pandas 用户指南](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
