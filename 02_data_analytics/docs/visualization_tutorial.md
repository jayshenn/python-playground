# 数据可视化

## 4.1 可视化介绍

### 什么是数据可视化？

**数据可视化**是将数据转换为图形或图像的过程，通过视觉元素（如图表、图形和地图）来展示数据中的模式、趋势和关联性。

**为什么需要数据可视化？**

1. **快速理解数据**：人脑处理视觉信息的速度远快于处理文本和数字
2. **发现模式**：可视化能够揭示数据中隐藏的模式和趋势
3. **沟通洞察**：图表比表格更容易传达数据洞察
4. **辅助决策**：可视化帮助从数据中提取有价值的信息

### Python 数据可视化生态

Python 拥有丰富的数据可视化库：

| 库 | 特点 | 适用场景 |
|---|---|---|
| **Matplotlib** | 底层库，功能强大，高度可定制 | 所有类型的静态图表 |
| **Seaborn** | 基于 Matplotlib，统计图表美观 | 统计数据可视化 |
| **Pandas** | 集成在 DataFrame 中，快速绘图 | 快速探索性分析 |
| Plotly | 交互式可视化 | 网页交互图表 |
| Bokeh | 交互式可视化 | 大数据集交互 |

**本章重点**：Matplotlib、Seaborn 和 Pandas 可视化

### 常见图表类型

| 图表类型 | 用途 | 适合数据 |
|---------|------|----------|
| **折线图** | 展示趋势、连续变化 | 时间序列数据 |
| **条形图** | 比较不同类别的数值 | 分类数据 |
| **散点图** | 展示两个变量的关系 | 数值数据（两个变量） |
| **直方图** | 展示数据分布 | 连续数值数据 |
| **箱线图** | 展示数据分布和异常值 | 数值数据 |
| **饼图** | 展示比例关系 | 分类数据（比例） |
| **热力图** | 展示数值矩阵 | 矩阵数据、相关性 |

---

## 4.2 Matplotlib 可视化

### 4.2.1 Matplotlib 简介

**Matplotlib** 是 Python 最基础、最强大的数据可视化库，由 John Hunter 于 2003 年创建。

**核心特点**：
- **功能全面**：支持几乎所有类型的 2D 图表
- **高度可定制**：可以控制图表的每个细节
- **跨平台**：支持多种输出格式（PNG、PDF、SVG 等）
- **与 NumPy 集成**：高效处理数组数据
- **生态基础**：许多其他可视化库都基于 Matplotlib

**安装**：
```bash
# 使用 uv
uv add matplotlib

# 使用 pip
pip install matplotlib
```

**导入约定**：
```python
import matplotlib.pyplot as plt
import numpy as np

# 在 Jupyter Notebook 中显示图表
%matplotlib inline
```

**基本绘图流程**：
1. 准备数据
2. 创建图表
3. 添加标题、标签、图例等
4. 显示或保存图表

---

### 4.2.2 两种画图接口

Matplotlib 提供两种不同的绘图接口：

| 接口类型 | 特点 | 适用场景 |
|---------|------|----------|
| **状态接口（pyplot）** | 类似 MATLAB，简单快捷 | 快速绘图、简单图表 |
| **面向对象接口** | 更灵活，易于管理复杂图表 | 复杂布局、多子图 |

**两种接口对比**：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 方法 1：状态接口（pyplot 接口）
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

# 方法 2：面向对象接口
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
plt.show()
```

**推荐**：
- 简单图表：使用 pyplot 接口
- 复杂图表、多子图：使用面向对象接口

---

## 状态接口（pyplot）

### 折线图

**折线图**用于展示数据随时间或有序类别的变化趋势。

#### 基本折线图

```python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.linspace(0, 10, 50)
y = np.sin(x)

# 绘制折线图
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
```

#### 多条折线

```python
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### 线条样式

```python
x = np.linspace(0, 10, 20)

plt.figure(figsize=(12, 6))

# 不同线条样式
plt.plot(x, x, '-', label='实线')
plt.plot(x, x+1, '--', label='虚线')
plt.plot(x, x+2, '-.', label='点划线')
plt.plot(x, x+3, ':', label='点线')

# 不同标记
plt.plot(x, x+4, 'o-', label='圆形标记')
plt.plot(x, x+5, 's-', label='方形标记')
plt.plot(x, x+6, '^-', label='三角标记')
plt.plot(x, x+7, '*-', label='星形标记')

plt.legend()
plt.title('线条样式和标记')
plt.grid(True, alpha=0.3)
plt.show()
```

#### 实战案例：股票价格走势

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 模拟股票数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30)
price = 100 + np.cumsum(np.random.randn(30) * 2)

plt.figure(figsize=(12, 6))
plt.plot(dates, price, 'b-', linewidth=2, marker='o', markersize=4)
plt.title('股票价格走势图', fontsize=16, fontweight='bold')
plt.xlabel('日期', fontsize=12)
plt.ylabel('价格 (元)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

### 条形图 (Bar Chart)

**条形图**用于比较不同类别的数值大小。

#### 垂直条形图

```python
import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='steelblue', edgecolor='black', alpha=0.7)
plt.title('销售额对比', fontsize=16)
plt.xlabel('产品', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 水平条形图

```python
categories = ['产品A', '产品B', '产品C', '产品D', '产品E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(10, 6))
plt.barh(categories, values, color='coral', edgecolor='black')
plt.title('产品销售额横向对比', fontsize=16)
plt.xlabel('销售额 (万元)', fontsize=12)
plt.ylabel('产品', fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.show()
```

#### 分组条形图

```python
import numpy as np

# 数据
categories = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 18, 25, 30]

x = np.arange(len(categories))
width = 0.25

plt.figure(figsize=(12, 6))
plt.bar(x - width, product_a, width, label='产品A', color='#FF6B6B')
plt.bar(x, product_b, width, label='产品B', color='#4ECDC4')
plt.bar(x + width, product_c, width, label='产品C', color='#45B7D1')

plt.xlabel('季度', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.title('季度销售额对比', fontsize=16)
plt.xticks(x, categories)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 堆叠条形图

```python
categories = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 18, 25, 30]

plt.figure(figsize=(10, 6))
plt.bar(categories, product_a, label='产品A', color='#FF6B6B')
plt.bar(categories, product_b, bottom=product_a, label='产品B', color='#4ECDC4')
plt.bar(categories, product_c, bottom=np.array(product_a)+np.array(product_b),
        label='产品C', color='#45B7D1')

plt.xlabel('季度', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.title('季度销售额堆叠图', fontsize=16)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 实战案例：电影票房对比

```python
import matplotlib.pyplot as plt

movies = ['电影A', '电影B', '电影C', '电影D', '电影E']
box_office = [15.6, 23.4, 18.9, 31.2, 12.8]

plt.figure(figsize=(12, 6))
bars = plt.bar(movies, box_office, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'],
               edgecolor='black', linewidth=1.5)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}亿',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('2024年春节档电影票房对比', fontsize=16, fontweight='bold')
plt.xlabel('电影', fontsize=12)
plt.ylabel('票房 (亿元)', fontsize=12)
plt.ylim(0, max(box_office) * 1.15)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### 饼图 (Pie Chart)

**饼图**用于展示各部分占整体的比例关系。

#### 基本饼图

```python
import matplotlib.pyplot as plt

# 数据
labels = ['Python', 'Java', 'JavaScript', 'C++', 'Others']
sizes = [30, 25, 20, 15, 10]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, shadow=True)
plt.title('编程语言使用占比', fontsize=16)
plt.axis('equal')  # 保证饼图是圆形
plt.show()
```

#### 突出显示扇区

```python
labels = ['住房', '饮食', '交通', '娱乐', '其他']
sizes = [40, 25, 15, 12, 8]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
explode = (0.1, 0, 0, 0, 0)  # 突出显示第一个扇区

plt.figure(figsize=(10, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('家庭支出分布', fontsize=16)
plt.axis('equal')
plt.show()
```

#### 环形饼图

```python
labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 25, 20]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors,
                                    autopct='%1.1f%%', startangle=90,
                                    pctdistance=0.85)

# 创建环形效果
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('市场份额分布（环形图）', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()
```

---

### 散点图 (Scatter Plot)

**散点图**用于展示两个变量之间的关系。

#### 基本散点图

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, edgecolors='black', linewidths=0.5)
plt.title('散点图示例', fontsize=16)
plt.xlabel('X 变量', fontsize=12)
plt.ylabel('Y 变量', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 带颜色和大小映射的散点图

```python
np.random.seed(42)
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
colors = np.random.rand(n)
sizes = 1000 * np.random.rand(n)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6,
                     cmap='viridis', edgecolors='black', linewidths=0.5)
plt.colorbar(scatter, label='颜色值')
plt.title('多维散点图', fontsize=16)
plt.xlabel('X 变量', fontsize=12)
plt.ylabel('Y 变量', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 实战案例：身高体重关系

```python
import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
np.random.seed(42)
n = 100
height = np.random.normal(170, 10, n)  # 身高 (cm)
weight = 0.8 * height - 60 + np.random.normal(0, 5, n)  # 体重 (kg)
gender = np.random.choice(['男', '女'], n)

# 分性别绘制
male_mask = gender == '男'
female_mask = gender == '女'

plt.figure(figsize=(12, 8))
plt.scatter(height[male_mask], weight[male_mask], alpha=0.6,
           label='男性', color='blue', s=100, edgecolors='black')
plt.scatter(height[female_mask], weight[female_mask], alpha=0.6,
           label='女性', color='red', s=100, edgecolors='black')

plt.title('身高与体重关系散点图', fontsize=16, fontweight='bold')
plt.xlabel('身高 (cm)', fontsize=12)
plt.ylabel('体重 (kg)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### 箱线图 (Boxplot)

**箱线图**用于展示数据分布、中位数、四分位数和异常值。

#### 基本箱线图

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=['A', 'B', 'C', 'D'])
plt.title('箱线图示例', fontsize=16)
plt.xlabel('类别', fontsize=12)
plt.ylabel('数值', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 自定义样式箱线图

```python
np.random.seed(42)
data = [np.random.normal(100, 10, 200) for _ in range(5)]

plt.figure(figsize=(12, 6))
box = plt.boxplot(data, labels=['班级1', '班级2', '班级3', '班级4', '班级5'],
                  patch_artist=True,  # 填充箱体
                  showmeans=True,     # 显示均值
                  meanline=True)      # 均值用线表示

# 自定义颜色
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('各班级考试成绩分布', fontsize=16, fontweight='bold')
plt.xlabel('班级', fontsize=12)
plt.ylabel('成绩', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 实战案例：温度数据分析

```python
import matplotlib.pyplot as plt
import numpy as np

# 模拟四个季节的温度数据
np.random.seed(42)
spring = np.random.normal(18, 5, 100)
summer = np.random.normal(28, 4, 100)
autumn = np.random.normal(20, 6, 100)
winter = np.random.normal(5, 5, 100)

data = [spring, summer, autumn, winter]

plt.figure(figsize=(12, 6))
box = plt.boxplot(data, labels=['春季', '夏季', '秋季', '冬季'],
                  patch_artist=True, showmeans=True, meanline=True,
                  medianprops=dict(color='red', linewidth=2),
                  meanprops=dict(color='blue', linewidth=2))

colors = ['#98D8C8', '#FFA07A', '#FFD700', '#87CEEB']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

plt.title('四季温度分布箱线图', fontsize=16, fontweight='bold')
plt.xlabel('季节', fontsize=12)
plt.ylabel('温度 (°C)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

### 总结

**pyplot 状态接口的特点**：
- ✅ 简单快捷，适合快速绘图
- ✅ 类似 MATLAB 语法，易于上手
- ✅ 适合简单的单图绘制
- ⚠️ 复杂布局时不够灵活
- ⚠️ 多子图管理较困难

**常用 pyplot 函数总结**：

| 函数 | 功能 | 示例 |
|------|------|------|
| `plt.plot()` | 折线图 | `plt.plot(x, y)` |
| `plt.bar()` | 垂直条形图 | `plt.bar(x, height)` |
| `plt.barh()` | 水平条形图 | `plt.barh(y, width)` |
| `plt.scatter()` | 散点图 | `plt.scatter(x, y)` |
| `plt.pie()` | 饼图 | `plt.pie(sizes)` |
| `plt.boxplot()` | 箱线图 | `plt.boxplot(data)` |
| `plt.hist()` | 直方图 | `plt.hist(data)` |
| `plt.xlabel()` | X 轴标签 | `plt.xlabel('x')` |
| `plt.ylabel()` | Y 轴标签 | `plt.ylabel('y')` |
| `plt.title()` | 标题 | `plt.title('Title')` |
| `plt.legend()` | 图例 | `plt.legend()` |
| `plt.grid()` | 网格 | `plt.grid(True)` |
| `plt.show()` | 显示图表 | `plt.show()` |
| `plt.savefig()` | 保存图表 | `plt.savefig('fig.png')` |

---

## 面向对象接口

面向对象接口提供了更灵活、更强大的绘图能力，适合复杂图表和多子图布局。

### 核心概念

**Figure 和 Axes 的关系**：

```
Figure（画布）
  └─ Axes（子图1）
  └─ Axes（子图2）
  └─ Axes（子图3）
```

- **Figure**：整个图形窗口，可以包含多个 Axes
- **Axes**：具体的绘图区域，包含坐标轴、标题等

### 创建 Figure 和 Axes

```python
import matplotlib.pyplot as plt
import numpy as np

# 方法 1：创建 Figure 和单个 Axes
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
plt.show()

# 方法 2：创建 Figure 和多个 Axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# 第一个子图
ax1.plot(x, np.sin(x), 'b-')
ax1.set_title('Sine')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid(True)

# 第二个子图
ax2.plot(x, np.cos(x), 'r-')
ax2.set_title('Cosine')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid(True)

plt.tight_layout()
plt.show()
```

### 多子图布局

#### 规则网格布局

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建 2x2 网格
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x = np.linspace(0, 10, 100)

# 子图 1：折线图
axes[0, 0].plot(x, np.sin(x), 'b-')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True)

# 子图 2：条形图
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[0, 1].bar(categories, values, color='coral')
axes[0, 1].set_title('Bar Chart')
axes[0, 1].grid(axis='y')

# 子图 3：散点图
axes[1, 0].scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].grid(True)

# 子图 4：箱线图
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
axes[1, 1].boxplot(data)
axes[1, 1].set_title('Box Plot')
axes[1, 1].grid(axis='y')

plt.tight_layout()
plt.show()
```

#### 不规则网格布局（GridSpec）

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# 大子图（占据 2x2）
ax1 = fig.add_subplot(gs[0:2, 0:2])
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), 'b-', linewidth=2)
ax1.plot(x, np.cos(x), 'r-', linewidth=2)
ax1.set_title('主图：三角函数', fontsize=14, fontweight='bold')
ax1.legend(['sin(x)', 'cos(x)'])
ax1.grid(True, alpha=0.3)

# 右上子图
ax2 = fig.add_subplot(gs[0, 2])
ax2.scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
ax2.set_title('散点图')
ax2.grid(True, alpha=0.3)

# 右中子图
ax3 = fig.add_subplot(gs[1, 2])
ax3.bar(['A', 'B', 'C'], [10, 20, 15], color='steelblue')
ax3.set_title('条形图')
ax3.grid(axis='y', alpha=0.3)

# 底部子图（占据整行）
ax4 = fig.add_subplot(gs[2, :])
ax4.hist(np.random.randn(1000), bins=30, color='coral', edgecolor='black', alpha=0.7)
ax4.set_title('直方图')
ax4.grid(axis='y', alpha=0.3)

plt.suptitle('复杂布局示例', fontsize=16, fontweight='bold')
plt.show()
```

### 实战案例：综合数据仪表板

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

# 准备数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30)
sales = 1000 + np.cumsum(np.random.randn(30) * 50)
categories = ['产品A', '产品B', '产品C', '产品D']
category_sales = [2500, 3200, 2800, 3500]
regions = ['华东', '华南', '华北', '西部']
region_sales = [4000, 3500, 3000, 2500]

# 创建布局
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.3, wspace=0.3)

# 1. 销售趋势图（大图，占 2 列）
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(dates, sales, 'b-', linewidth=2, marker='o', markersize=4)
ax1.fill_between(dates, sales, alpha=0.3)
ax1.set_title('30天销售趋势', fontsize=14, fontweight='bold')
ax1.set_xlabel('日期')
ax1.set_ylabel('销售额 (元)')
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# 2. 产品销售饼图
ax2 = fig.add_subplot(gs[0, 2])
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
ax2.pie(category_sales, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('产品销售占比', fontsize=14, fontweight='bold')

# 3. 地区销售条形图
ax3 = fig.add_subplot(gs[1, 0])
bars = ax3.bar(regions, region_sales, color='#98D8C8', edgecolor='black')
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.0f}', ha='center', va='bottom', fontsize=10)
ax3.set_title('地区销售对比', fontsize=14, fontweight='bold')
ax3.set_ylabel('销售额 (元)')
ax3.grid(axis='y', alpha=0.3)

# 4. 销售额分布箱线图
ax4 = fig.add_subplot(gs[1, 1])
daily_sales = [sales[i:i+7].values for i in range(0, 28, 7)]
ax4.boxplot(daily_sales, labels=['第1周', '第2周', '第3周', '第4周'])
ax4.set_title('周销售额分布', fontsize=14, fontweight='bold')
ax4.set_ylabel('销售额 (元)')
ax4.grid(axis='y', alpha=0.3)

# 5. 统计信息文本
ax5 = fig.add_subplot(gs[1, 2])
ax5.axis('off')
stats_text = f"""
销售数据统计

总销售额: ¥{sales.sum():.0f}
平均日销额: ¥{sales.mean():.0f}
最高日销额: ¥{sales.max():.0f}
最低日销额: ¥{sales.min():.0f}

畅销产品: {categories[np.argmax(category_sales)]}
最佳地区: {regions[np.argmax(region_sales)]}
"""
ax5.text(0.1, 0.5, stats_text, fontsize=12, verticalalignment='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('销售数据仪表板', fontsize=18, fontweight='bold', y=0.98)
plt.savefig('sales_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 4.3 Seaborn 可视化

### 4.3.1 什么是 Seaborn

**Seaborn** 是基于 Matplotlib 的高级统计数据可视化库，由 Michael Waskom 创建。

**核心特点**：
- **美观的默认样式**：内置多种精美主题
- **统计图表**：专注于统计数据可视化
- **与 Pandas 集成**：直接使用 DataFrame
- **简化的接口**：用更少的代码创建复杂图表
- **自动计算**：内置统计估计和回归

**安装**：
```bash
# 使用 uv
uv add seaborn

# 使用 pip
pip install seaborn
```

**导入约定**：
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 设置 Seaborn 样式
sns.set_theme()
```

---

### 4.3.2 单变量可视化

单变量分析关注单个变量的分布特征。

#### 直方图（histplot）

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
np.random.seed(42)
data = np.random.normal(100, 15, 1000)

# 绘制直方图
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=True, color='steelblue')
plt.title('成绩分布直方图', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.ylabel('频数', fontsize=12)
plt.show()
```

#### 核密度估计图（kdeplot）

```python
plt.figure(figsize=(10, 6))
sns.kdeplot(data, fill=True, color='coral')
plt.title('成绩分布密度图', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.ylabel('密度', fontsize=12)
plt.show()
```

#### 经验累积分布函数（ecdfplot）

```python
plt.figure(figsize=(10, 6))
sns.ecdfplot(data, color='green')
plt.title('成绩累积分布图', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.ylabel('累积概率', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 地毯图（rugplot）

```python
plt.figure(figsize=(10, 6))
sns.kdeplot(data, fill=True, color='lightblue', alpha=0.5)
sns.rugplot(data, color='navy', height=0.05)
plt.title('带地毯图的密度分布', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.show()
```

---

### 4.3.3 双变量可视化

双变量分析关注两个变量之间的关系。

#### 散点图（scatterplot）

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
np.random.seed(42)
df = pd.DataFrame({
    'height': np.random.normal(170, 10, 100),
    'weight': np.random.normal(65, 10, 100),
    'gender': np.random.choice(['男', '女'], 100)
})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='height', y='weight', hue='gender',
                style='gender', s=100, alpha=0.7)
plt.title('身高与体重关系', fontsize=16)
plt.xlabel('身高 (cm)', fontsize=12)
plt.ylabel('体重 (kg)', fontsize=12)
plt.legend(title='性别')
plt.grid(True, alpha=0.3)
plt.show()
```

#### 线图（lineplot）

```python
# 时间序列数据
dates = pd.date_range('2024-01-01', periods=30)
df = pd.DataFrame({
    'date': dates,
    'sales': 1000 + np.cumsum(np.random.randn(30) * 50),
    'costs': 800 + np.cumsum(np.random.randn(30) * 30)
})

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='sales', label='销售额', linewidth=2)
sns.lineplot(data=df, x='date', y='costs', label='成本', linewidth=2)
plt.title('销售额与成本趋势', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('金额 (元)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 回归图（regplot）

```python
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
sns.regplot(x=x, y=y, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('线性回归拟合', fontsize=16)
plt.xlabel('X 变量', fontsize=12)
plt.ylabel('Y 变量', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 联合分布图（jointplot）

```python
np.random.seed(42)
x = np.random.randn(500)
y = x + np.random.randn(500) * 0.5

# 创建联合分布图
g = sns.jointplot(x=x, y=y, kind='scatter', height=8)
g.fig.suptitle('联合分布图', fontsize=16, y=1.02)
plt.show()

# 不同的 kind 参数
kinds = ['scatter', 'kde', 'hex', 'reg']
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
for ax, kind in zip(axes.flatten(), kinds):
    g = sns.jointplot(x=x, y=y, kind=kind, height=5)
    plt.close()  # 关闭单独的图
```

#### 成对关系图（pairplot）

```python
# 加载示例数据
iris = sns.load_dataset('iris')

# 绘制成对关系图
g = sns.pairplot(iris, hue='species', height=2.5)
g.fig.suptitle('鸢尾花数据集成对关系图', fontsize=16, y=1.02)
plt.show()
```

---

### 4.3.4 多变量可视化

#### 热力图（heatmap）

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 生成相关系数矩阵
np.random.seed(42)
data = np.random.randn(10, 12)
corr = np.corrcoef(data)

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('相关系数热力图', fontsize=16)
plt.tight_layout()
plt.show()
```

#### 分类散点图（catplot）

```python
# 加载示例数据
tips = sns.load_dataset('tips')

# 创建分类散点图
g = sns.catplot(data=tips, x='day', y='total_bill', hue='sex',
                col='time', kind='swarm', height=5, aspect=0.8)
g.fig.suptitle('消费金额分布', fontsize=16, y=1.02)
plt.show()
```

#### 分面网格（FacetGrid）

```python
tips = sns.load_dataset('tips')

# 创建分面网格
g = sns.FacetGrid(tips, col='time', row='smoker', height=4, aspect=1.2)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.6)
g.add_legend()
g.fig.suptitle('多维度消费分析', fontsize=16, y=1.01)
plt.show()
```

---

### 4.3.5 Seaborn 样式

Seaborn 提供了多种内置样式和颜色主题。

#### 内置样式

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 5 种内置样式
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for ax, style in zip(axes[:5], styles):
    sns.set_style(style)
    ax.plot(x, y)
    ax.set_title(f'Style: {style}', fontsize=12)
    ax.grid(True, alpha=0.3)

axes[5].axis('off')
plt.tight_layout()
plt.show()

# 恢复默认
sns.set_theme()
```

#### 调色板

```python
# 展示不同调色板
palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']

fig, axes = plt.subplots(3, 2, figsize=(12, 10))
axes = axes.flatten()

for ax, palette in zip(axes, palettes):
    sns.set_palette(palette)
    colors = sns.color_palette(palette)
    ax.bar(range(len(colors)), [1]*len(colors), color=colors)
    ax.set_title(f'Palette: {palette}', fontsize=12)
    ax.set_ylim(0, 1.2)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

#### 上下文设置

```python
# 不同上下文（影响字体大小、线宽等）
contexts = ['paper', 'notebook', 'talk', 'poster']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for ax, context in zip(axes, contexts):
    sns.set_context(context)
    ax.plot(x, y)
    ax.set_title(f'Context: {context}')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 恢复默认
sns.set_theme()
```

---

## 4.4 Pandas 可视化

Pandas 内置了基于 Matplotlib 的绘图功能，可以直接从 DataFrame 或 Series 创建图表。

### 4.4.1 单变量可视化

#### 直方图

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
df = pd.DataFrame({
    'scores': np.random.normal(75, 15, 200)
})

# 绘制直方图
df['scores'].hist(bins=30, figsize=(10, 6), edgecolor='black', alpha=0.7)
plt.title('成绩分布直方图', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.ylabel('频数', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

#### 密度图

```python
df['scores'].plot(kind='density', figsize=(10, 6), linewidth=2)
plt.title('成绩密度分布图', fontsize=16)
plt.xlabel('成绩', fontsize=12)
plt.ylabel('密度', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 箱线图

```python
# 多个变量的箱线图
df = pd.DataFrame({
    'Math': np.random.normal(80, 10, 100),
    'English': np.random.normal(75, 12, 100),
    'Physics': np.random.normal(70, 15, 100)
})

df.plot(kind='box', figsize=(10, 6))
plt.title('各科成绩箱线图', fontsize=16)
plt.ylabel('成绩', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

### 4.4.2 双变量可视化

#### 折线图

```python
# 时间序列折线图
dates = pd.date_range('2024-01-01', periods=30)
df = pd.DataFrame({
    'Sales': 1000 + np.cumsum(np.random.randn(30) * 50),
    'Costs': 800 + np.cumsum(np.random.randn(30) * 30)
}, index=dates)

df.plot(figsize=(12, 6), linewidth=2)
plt.title('销售额与成本趋势', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('金额 (元)', fontsize=12)
plt.legend(['销售额', '成本'])
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 条形图

```python
# 分组条形图
df = pd.DataFrame({
    'Q1': [20, 25, 15],
    'Q2': [35, 32, 18],
    'Q3': [30, 34, 25],
    'Q4': [35, 20, 30]
}, index=['产品A', '产品B', '产品C'])

df.plot(kind='bar', figsize=(12, 6), width=0.8)
plt.title('季度销售额对比', fontsize=16)
plt.xlabel('产品', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.legend(title='季度')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 散点图

```python
df = pd.DataFrame({
    'height': np.random.normal(170, 10, 100),
    'weight': np.random.normal(65, 10, 100)
})

df.plot(kind='scatter', x='height', y='weight',
        figsize=(10, 6), alpha=0.6, s=100)
plt.title('身高与体重关系', fontsize=16)
plt.xlabel('身高 (cm)', fontsize=12)
plt.ylabel('体重 (kg)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

#### 饼图

```python
# 市场份额饼图
data = pd.Series([30, 25, 20, 15, 10],
                 index=['公司A', '公司B', '公司C', '公司D', '其他'])

data.plot(kind='pie', figsize=(10, 8), autopct='%1.1f%%',
          startangle=90, colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
plt.title('市场份额分布', fontsize=16)
plt.ylabel('')  # 隐藏 y 轴标签
plt.show()
```

#### 面积图

```python
dates = pd.date_range('2024-01-01', periods=30)
df = pd.DataFrame({
    '产品A': np.random.randint(10, 50, 30),
    '产品B': np.random.randint(10, 50, 30),
    '产品C': np.random.randint(10, 50, 30)
}, index=dates)

df.plot(kind='area', figsize=(12, 6), alpha=0.6)
plt.title('产品销量堆叠面积图', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('销量', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 综合实战案例

### 案例 1：销售数据综合分析

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 生成模拟销售数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=365)
df = pd.DataFrame({
    'date': dates,
    'sales': 1000 + np.cumsum(np.random.randn(365) * 20),
    'visitors': np.random.randint(100, 500, 365),
    'conversion_rate': np.random.uniform(0.02, 0.08, 365)
})
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.dayofweek

# 创建综合仪表板
fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. 销售趋势（大图）
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(df['date'], df['sales'], linewidth=2, color='steelblue')
ax1.fill_between(df['date'], df['sales'], alpha=0.3)
ax1.set_title('全年销售趋势', fontsize=16, fontweight='bold')
ax1.set_xlabel('日期')
ax1.set_ylabel('销售额 (元)')
ax1.grid(True, alpha=0.3)

# 2. 月度销售箱线图
ax2 = fig.add_subplot(gs[1, 0])
monthly_data = [df[df['month']==m]['sales'].values for m in range(1, 13)]
ax2.boxplot(monthly_data, labels=range(1, 13))
ax2.set_title('月度销售分布', fontsize=14, fontweight='bold')
ax2.set_xlabel('月份')
ax2.set_ylabel('销售额 (元)')
ax2.grid(axis='y', alpha=0.3)

# 3. 访客量与转化率散点图
ax3 = fig.add_subplot(gs[1, 1])
scatter = ax3.scatter(df['visitors'], df['conversion_rate'],
                     c=df['sales'], cmap='viridis', alpha=0.6, s=50)
ax3.set_title('访客量 vs 转化率', fontsize=14, fontweight='bold')
ax3.set_xlabel('访客量')
ax3.set_ylabel('转化率')
plt.colorbar(scatter, ax=ax3, label='销售额')
ax3.grid(True, alpha=0.3)

# 4. 周销售模式
ax4 = fig.add_subplot(gs[1, 2])
weekday_sales = df.groupby('weekday')['sales'].mean()
weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
ax4.bar(weekdays, weekday_sales, color='coral', edgecolor='black')
ax4.set_title('周销售模式', fontsize=14, fontweight='bold')
ax4.set_ylabel('平均销售额 (元)')
ax4.grid(axis='y', alpha=0.3)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)

# 5. 销售额分布直方图
ax5 = fig.add_subplot(gs[2, 0])
ax5.hist(df['sales'], bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
ax5.set_title('销售额分布', fontsize=14, fontweight='bold')
ax5.set_xlabel('销售额 (元)')
ax5.set_ylabel('频数')
ax5.grid(axis='y', alpha=0.3)

# 6. 转化率趋势
ax6 = fig.add_subplot(gs[2, 1])
df_monthly = df.groupby('month').agg({
    'conversion_rate': 'mean',
    'visitors': 'sum'
}).reset_index()
ax6.plot(df_monthly['month'], df_monthly['conversion_rate'],
        marker='o', linewidth=2, markersize=8, color='purple')
ax6.set_title('月均转化率趋势', fontsize=14, fontweight='bold')
ax6.set_xlabel('月份')
ax6.set_ylabel('转化率')
ax6.grid(True, alpha=0.3)

# 7. 统计摘要
ax7 = fig.add_subplot(gs[2, 2])
ax7.axis('off')
stats_text = f"""
【数据摘要】

总销售额: ¥{df['sales'].sum():.0f}
日均销售: ¥{df['sales'].mean():.0f}
最高日销: ¥{df['sales'].max():.0f}
最低日销: ¥{df['sales'].min():.0f}

总访客数: {df['visitors'].sum():.0f}
平均转化率: {df['conversion_rate'].mean():.2%}

最佳月份: {df.groupby('month')['sales'].sum().idxmax()}月
最佳星期: 星期{df.groupby('weekday')['sales'].mean().idxmax() + 1}
"""
ax7.text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center',
        family='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('2024 年度销售数据分析仪表板', fontsize=20, fontweight='bold', y=0.98)
plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 学习建议

1. **循序渐进**：先掌握 Matplotlib 基础，再学习 Seaborn 和 Pandas 可视化
2. **多做实践**：每种图表类型都要亲手实现
3. **理解图表选择**：根据数据类型和分析目的选择合适的图表
4. **注重美化**：学会使用颜色、标签、图例等提升图表质量
5. **参考优秀案例**：多看优秀的数据可视化作品

## 参考资源

- [Matplotlib 官方文档](https://matplotlib.org/stable/index.html)
- [Matplotlib 教程](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn 官方文档](https://seaborn.pydata.org/)
- [Seaborn 教程](https://seaborn.pydata.org/tutorial.html)
- [Pandas 可视化文档](https://pandas.pydata.org/docs/user_guide/visualization.html)
- [Python Graph Gallery](https://www.python-graph-gallery.com/)
