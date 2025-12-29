# 第 3 章 容器型数据类型

## 3.1 序列

序列是 Python 中最基本的数据结构。序列中的每个元素都有一个位置（索引），第一个元素的索引是 0，第二个元素的索引是 1，以此类推。

Python 中常见的序列类型：
- **列表（List）**：可变序列，使用方括号 `[]`
- **元组（Tuple）**：不可变序列，使用圆括号 `()`
- **字符串（String）**：不可变的字符序列
- **范围（Range）**：不可变的数字序列

**序列的通用操作**：
```python
# 索引：访问单个元素
seq = [1, 2, 3, 4, 5]
print(seq[0])   # 第一个元素: 1
print(seq[-1])  # 最后一个元素: 5

# 切片：访问多个元素
print(seq[1:4])   # [2, 3, 4]
print(seq[:3])    # [1, 2, 3]
print(seq[2:])    # [3, 4, 5]
print(seq[::2])   # [1, 3, 5] (步长为2)

# 拼接
seq1 = [1, 2, 3]
seq2 = [4, 5, 6]
print(seq1 + seq2)  # [1, 2, 3, 4, 5, 6]

# 重复
print([1, 2] * 3)  # [1, 2, 1, 2, 1, 2]

# 长度
print(len(seq))  # 5

# 成员检查
print(3 in seq)  # True
print(10 in seq)  # False

# 最大值、最小值
print(max(seq))  # 5
print(min(seq))  # 1

# 求和
print(sum(seq))  # 15
```

---

## 3.2 列表 List

列表是 Python 中最常用的数据结构之一，是一个**可变的有序序列**，可以包含任意类型的元素。

### 3.2.1 创建列表

```python
# 空列表
empty_list = []
empty_list2 = list()

# 包含元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "hello", 3.14, True]  # 混合类型

# 使用 list() 构造函数
chars = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
range_list = list(range(5))  # [0, 1, 2, 3, 4]

# 列表推导式
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 嵌套列表（二维列表）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### 3.2.2 访问列表

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 正向索引（从 0 开始）
print(fruits[0])   # 苹果
print(fruits[2])   # 橙子

# 负向索引（从 -1 开始）
print(fruits[-1])  # 西瓜（最后一个）
print(fruits[-2])  # 葡萄（倒数第二个）

# 切片 [start:stop:step]
print(fruits[1:4])    # ['香蕉', '橙子', '葡萄']
print(fruits[:3])     # ['苹果', '香蕉', '橙子']
print(fruits[2:])     # ['橙子', '葡萄', '西瓜']
print(fruits[::2])    # ['苹果', '橙子', '西瓜'] (步长为2)
print(fruits[::-1])   # ['西瓜', '葡萄', '橙子', '香蕉', '苹果'] (反转)

# 多维列表访问
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6
```

### 3.2.3 向列表中添加元素

```python
fruits = ["苹果", "香蕉"]

# append(): 在末尾添加单个元素
fruits.append("橙子")
print(fruits)  # ['苹果', '香蕉', '橙子']

# insert(): 在指定位置插入元素
fruits.insert(1, "葡萄")  # 在索引 1 处插入
print(fruits)  # ['苹果', '葡萄', '香蕉', '橙子']

# extend(): 添加多个元素（扩展列表）
fruits.extend(["西瓜", "草莓"])
print(fruits)  # ['苹果', '葡萄', '香蕉', '橙子', '西瓜', '草莓']

# 使用 + 运算符（创建新列表）
new_fruits = fruits + ["芒果", "榴莲"]
print(new_fruits)

# 使用 += 运算符（原地修改）
fruits += ["火龙果"]
print(fruits)
```

### 3.2.4 列表删除

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# remove(): 删除指定值（第一个匹配的）
fruits.remove("橙子")
print(fruits)  # ['苹果', '香蕉', '葡萄', '西瓜']

# pop(): 删除指定索引的元素（默认最后一个）
last = fruits.pop()  # 删除并返回最后一个
print(last)  # 西瓜
print(fruits)  # ['苹果', '香蕉', '葡萄']

item = fruits.pop(0)  # 删除并返回索引 0 的元素
print(item)  # 苹果
print(fruits)  # ['香蕉', '葡萄']

# del: 删除指定索引或切片
numbers = [1, 2, 3, 4, 5]
del numbers[0]  # 删除索引 0
print(numbers)  # [2, 3, 4, 5]

del numbers[1:3]  # 删除索引 1 到 2 的元素
print(numbers)  # [2, 5]

# clear(): 清空列表
fruits = ["苹果", "香蕉", "橙子"]
fruits.clear()
print(fruits)  # []
```

### 3.2.5 列表查找

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "香蕉"]

# in / not in: 检查元素是否存在
print("苹果" in fruits)  # True
print("西瓜" in fruits)  # False
print("西瓜" not in fruits)  # True

# index(): 返回元素第一次出现的索引
print(fruits.index("橙子"))  # 2
print(fruits.index("香蕉"))  # 1（第一个香蕉）

# 如果元素不存在会报错
try:
    print(fruits.index("西瓜"))
except ValueError:
    print("元素不存在")

# 指定查找范围
print(fruits.index("香蕉", 2))  # 4（从索引 2 开始查找）

# count(): 统计元素出现的次数
print(fruits.count("香蕉"))  # 2
print(fruits.count("苹果"))  # 1
print(fruits.count("西瓜"))  # 0
```

### 3.2.6 修改列表中的元素

```python
fruits = ["苹果", "香蕉", "橙子"]

# 通过索引修改单个元素
fruits[1] = "葡萄"
print(fruits)  # ['苹果', '葡萄', '橙子']

# 通过切片修改多个元素
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)  # [1, 20, 30, 40, 5]

# 通过切片替换为不同数量的元素
numbers[1:4] = [100, 200]
print(numbers)  # [1, 100, 200, 5]

# 修改嵌套列表中的元素
matrix = [[1, 2], [3, 4], [5, 6]]
matrix[1][0] = 30
print(matrix)  # [[1, 2], [30, 4], [5, 6]]
```

### 3.2.7 检查某值是否在列表中存在

```python
fruits = ["苹果", "香蕉", "橙子"]

# 使用 in 运算符
if "苹果" in fruits:
    print("苹果在列表中")

if "西瓜" not in fruits:
    print("西瓜不在列表中")

# 结合条件判断
search = "葡萄"
if search in fruits:
    print(f"找到了 {search}")
else:
    print(f"没有找到 {search}")

# 在嵌套列表中查找
matrix = [[1, 2, 3], [4, 5, 6]]
if 5 in matrix[1]:
    print("5 在第二个子列表中")

# 检查多个值
targets = ["苹果", "香蕉"]
if all(item in fruits for item in targets):
    print("所有目标都在列表中")
```

### 3.2.8 求列表中的最大值、最小值、求和

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 最大值
print(max(numbers))  # 9

# 最小值
print(min(numbers))  # 1

# 求和
print(sum(numbers))  # 36

# 平均值
average = sum(numbers) / len(numbers)
print(f"平均值: {average:.2f}")  # 4.00

# 对字符串列表
fruits = ["苹果", "香蕉", "橙子"]
print(max(fruits))  # 香蕉（按字典序）
print(min(fruits))  # 橙子

# 自定义比较（使用 key 参数）
words = ["apple", "banana", "cherry", "date"]
print(max(words, key=len))  # banana（最长的）
print(min(words, key=len))  # date（最短的）

# 多维列表中的最大值
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_value = max(max(row) for row in matrix)
print(max_value)  # 9
```

### 3.2.9 求列表中某个元素的最大值、最小值、加和

```python
# 找出列表中所有偶数的最大值、最小值和总和
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤出偶数
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 偶数的最大值、最小值、求和
print(f"最大偶数: {max(evens)}")  # 10
print(f"最小偶数: {min(evens)}")  # 2
print(f"偶数之和: {sum(evens)}")  # 30

# 使用 filter() 函数
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 学生成绩统计
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 最高分学生
top_student = max(students, key=lambda s: s["score"])
print(f"最高分: {top_student['name']} - {top_student['score']}")

# 最低分
min_score = min(students, key=lambda s: s["score"])["score"]
print(f"最低分: {min_score}")

# 平均分
avg_score = sum(s["score"] for s in students) / len(students)
print(f"平均分: {avg_score:.2f}")
```

### 3.2.10 遍历列表

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 方法1: 直接遍历元素
for fruit in fruits:
    print(fruit)

# 方法2: 通过索引遍历
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 方法3: 使用 enumerate()（推荐）
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate() 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 遍历多个列表（zip）
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 遍历嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # 换行

# 使用列表推导式处理
doubled = [x * 2 for x in [1, 2, 3, 4, 5]]
print(doubled)  # [2, 4, 6, 8, 10]
```

### 3.2.11 删除列表中指定位置范围元素或者全部删除

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 删除指定范围（使用切片 + del）
del numbers[2:5]  # 删除索引 2-4 的元素
print(numbers)  # [1, 2, 6, 7, 8, 9]

# 使用切片赋值为空列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = []
print(numbers)  # [1, 2, 6, 7, 8, 9]

# 删除从开头到指定位置
numbers = [1, 2, 3, 4, 5]
del numbers[:2]
print(numbers)  # [3, 4, 5]

# 删除从指定位置到末尾
numbers = [1, 2, 3, 4, 5]
del numbers[2:]
print(numbers)  # [1, 2]

# 清空整个列表
numbers.clear()  # 方法1
print(numbers)  # []

numbers = [1, 2, 3, 4, 5]
del numbers[:]  # 方法2
print(numbers)  # []

numbers = [1, 2, 3, 4, 5]
numbers = []  # 方法3（创建新列表）
print(numbers)  # []
```

### 3.2.12 拼接列表

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 方法1: 使用 + 运算符（创建新列表）
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]

# 方法2: 使用 extend()（原地修改）
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# 方法3: 使用 += 运算符（原地修改）
list1 = [1, 2, 3]
list1 += list2
print(list1)  # [1, 2, 3, 4, 5, 6]

# 方法4: 使用 * 运算符拆包
list1 = [1, 2, 3]
result = [*list1, *list2]
print(result)  # [1, 2, 3, 4, 5, 6]

# 拼接多个列表
list3 = [7, 8, 9]
result = list1 + list2 + list3
print(result)

# 使用 sum()（不推荐，效率低）
lists = [[1, 2], [3, 4], [5, 6]]
result = sum(lists, [])
print(result)  # [1, 2, 3, 4, 5, 6]

# 使用列表推导式
result = [item for sublist in lists for item in sublist]
print(result)  # [1, 2, 3, 4, 5, 6]
```

### 3.2.13 列表推导式

列表推导式提供了一种简洁的方式来创建列表。

**语法**：`[表达式 for 变量 in 序列 if 条件]`

```python
# 基本用法：生成平方数
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 带条件：生成偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 处理字符串
words = ["Hello", "World", "Python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# 条件表达式
numbers = [1, 2, 3, 4, 5]
labels = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 二维列表（矩阵转置）
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4], [2, 5], [3, 6]]

# 过滤和转换
strings = ["1", "hello", "2", "world", "3"]
numbers = [int(s) for s in strings if s.isdigit()]
print(numbers)  # [1, 2, 3]

# 生成坐标对
coords = [(x, y) for x in range(3) for y in range(3)]
print(coords)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

### 3.2.14 其他操作

```python
# sort(): 排序（原地修改）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # 升序
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # 降序
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted(): 排序（返回新列表）
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 3, 4, 5, 9]
print(numbers)  # [3, 1, 4, 1, 5, 9] (原列表不变)

# 自定义排序
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # 按长度排序
print(words)  # ['date', 'apple', 'cherry', 'banana']

# reverse(): 反转列表
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed(): 返回反转迭代器
numbers = [1, 2, 3, 4, 5]
reversed_list = list(reversed(numbers))
print(reversed_list)  # [5, 4, 3, 2, 1]

# copy(): 复制列表（浅拷贝）
original = [1, 2, 3]
copied = original.copy()
copied[0] = 100
print(original)  # [1, 2, 3]
print(copied)  # [100, 2, 3]

# 深拷贝（嵌套列表）
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 100  # 影响原列表
deep[1][0] = 200     # 不影响原列表

print(original)  # [[100, 2], [3, 4]]
print(shallow)   # [[100, 2], [3, 4]]
print(deep)      # [[100, 2], [200, 4]]
```

### 3.2.15 常用函数

```python
numbers = [1, 2, 3, 4, 5]

# len(): 列表长度
print(len(numbers))  # 5

# sum(): 求和
print(sum(numbers))  # 15

# max() / min(): 最大值 / 最小值
print(max(numbers))  # 5
print(min(numbers))  # 1

# all(): 所有元素都为 True
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))  # True（非零为True）
print(all([0, 1, 2]))  # False（0为False）

# any(): 至少一个元素为 True
print(any([False, False, True]))  # True
print(any([False, False, False]))  # False
print(any([0, 0, 1]))  # True

# enumerate(): 枚举（索引和值）
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")

# zip(): 并行遍历
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} 是 {age} 岁")

# map(): 映射（应用函数）
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter(): 过滤
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce(): 累积（需要导入）
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)
```

---

## 3.3 字符串 String

字符串是不可变的字符序列，是 Python 中处理文本的基本数据类型。

### 3.3.1 创建字符串

```python
# 单引号
str1 = 'Hello'

# 双引号
str2 = "World"

# 三引号（多行字符串）
str3 = """这是
多行
字符串"""

str4 = '''这也是
多行字符串'''

# 空字符串
empty = ""
empty2 = str()

# 使用 str() 构造函数
num_str = str(123)  # "123"
bool_str = str(True)  # "True"

# 原始字符串（r前缀）
path = r"C:\Users\name\Documents"  # 不转义反斜杠
print(path)  # C:\Users\name\Documents

# f-string（格式化字符串）Python 3.6+
name = "Alice"
age = 25
greeting = f"我叫{name}，今年{age}岁"
print(greeting)  # 我叫Alice，今年25岁
```

### 3.3.2 访问字符串

```python
text = "Python Programming"

# 索引访问
print(text[0])   # P
print(text[-1])  # g

# 切片
print(text[0:6])   # Python
print(text[7:])    # Programming
print(text[:6])    # Python
print(text[::2])   # Pto rgamn（步长2）
print(text[::-1])  # gnimmargorP nohtyP（反转）

# 遍历字符串
for char in "Hello":
    print(char)

# 遍历时获取索引
for i, char in enumerate("Hello"):
    print(f"{i}: {char}")
```

### 3.3.3 字符串拼接

```python
# 方法1: 使用 + 运算符
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Hello World

# 方法2: 使用 join()（推荐，效率高）
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # Hello World Python

# 方法3: 使用 f-string
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # Hello, Alice!

# 方法4: 使用 format()
result = "{} {}".format("Hello", "World")
print(result)  # Hello World

# 方法5: 使用 % 格式化
result = "%s %s" % ("Hello", "World")
print(result)  # Hello World

# 方法6: 重复字符串
print("=" * 20)  # ====================
print("Hello " * 3)  # Hello Hello Hello

# 拼接数字和字符串
age = 25
text = "我今年" + str(age) + "岁"
# 或使用 f-string
text = f"我今年{age}岁"
```

### 3.3.4 字符串转义

```python
# 常用转义字符
print("Hello\nWorld")  # 换行
print("Hello\tWorld")  # 制表符
print("He said \"Hello\"")  # 双引号
print('It\'s OK')  # 单引号
print("C:\\Users\\name")  # 反斜杠

# 转义字符列表
# \n  换行
# \t  制表符
# \\  反斜杠
# \'  单引号
# \"  双引号
# \r  回车
# \b  退格

# 原始字符串（不转义）
path = r"C:\Users\name\Documents"
print(path)  # C:\Users\name\Documents

# Unicode 转义
print("\u4e2d\u6587")  # 中文

# 使用三引号避免转义
text = """He said "Hello" and she replied 'Hi'"""
print(text)
```

### 3.3.5 检查某值是否在字符串中存在

```python
text = "Hello, Python Programming"

# 使用 in / not in
print("Python" in text)  # True
print("Java" in text)  # False
print("Java" not in text)  # True

# find(): 返回子串第一次出现的索引（找不到返回-1）
print(text.find("Python"))  # 7
print(text.find("Java"))  # -1

# 指定查找范围
print(text.find("o", 5))  # 从索引5开始查找

# rfind(): 从右往左查找
print(text.rfind("o"))  # 最后一个 o 的位置

# index(): 类似 find()，但找不到会报错
try:
    print(text.index("Java"))
except ValueError:
    print("子串不存在")

# count(): 统计子串出现次数
print(text.count("o"))  # 3

# startswith() / endswith()
print(text.startswith("Hello"))  # True
print(text.endswith("Programming"))  # True
print(text.startswith("Python", 7))  # 从索引7开始检查
```

### 3.3.6 删除字符串

```python
# 字符串是不可变的，不能直接删除，只能创建新字符串

text = "Hello, World!"

# 方法1: 使用切片
new_text = text[:5] + text[7:]
print(new_text)  # Hello World!

# 方法2: 使用 replace()
new_text = text.replace(",", "")
print(new_text)  # Hello World!

# 删除指定字符
text = "Hello, Python!"
new_text = text.replace("o", "")
print(new_text)  # Hell, Pythn!

# 删除空白字符
text = "  Hello  World  "
print(text.strip())   # 删除两端空白: "Hello  World"
print(text.lstrip())  # 删除左侧空白: "Hello  World  "
print(text.rstrip())  # 删除右侧空白: "  Hello  World"

# 删除指定字符
text = "***Hello***"
print(text.strip("*"))  # "Hello"

# 使用 filter()
text = "Hello123World456"
letters_only = ''.join(filter(str.isalpha, text))
print(letters_only)  # HelloWorld
```

### 3.3.7 常用函数

```python
text = "Hello, Python Programming"

# 长度
print(len(text))  # 25

# 大小写转换
print(text.upper())  # HELLO, PYTHON PROGRAMMING
print(text.lower())  # hello, python programming
print(text.capitalize())  # Hello, python programming
print(text.title())  # Hello, Python Programming
print("HELLO".swapcase())  # hello（大小写互换）

# 判断类型
print("123".isdigit())  # True（是否为数字）
print("abc".isalpha())  # True（是否为字母）
print("abc123".isalnum())  # True（是否为字母或数字）
print("   ".isspace())  # True（是否为空白）
print("Hello".islower())  # False
print("HELLO".isupper())  # True
print("Hello World".istitle())  # True

# 字符串分割
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

# 按行分割
text = "line1\nline2\nline3"
lines = text.splitlines()
print(lines)  # ['line1', 'line2', 'line3']

# 分割次数限制
text = "a-b-c-d"
print(text.split("-", 2))  # ['a', 'b', 'c-d']

# 字符串连接
words = ["Hello", "World"]
print(" ".join(words))  # Hello World
print("-".join(words))  # Hello-World

# 替换
text = "Hello, World"
print(text.replace("World", "Python"))  # Hello, Python
print(text.replace("o", "0", 1))  # Hell0, World（只替换第一个）

# 对齐
print("Hello".center(20))  # "       Hello        "
print("Hello".ljust(20, "*"))  # "Hello***************"
print("Hello".rjust(20, "*"))  # "***************Hello"
print("42".zfill(5))  # "00042"（数字补零）

# 查找和替换
text = "Python is awesome. Python is powerful."
print(text.find("Python"))  # 0
print(text.rfind("Python"))  # 19（从右查找）
print(text.count("Python"))  # 2
```

### 3.3.8 其他操作

```python
# 字符串格式化
name = "Alice"
age = 25
score = 95.5

# f-string（推荐）Python 3.6+
print(f"{name} 今年 {age} 岁，得分 {score:.1f}")

# format() 方法
print("{} 今年 {} 岁".format(name, age))
print("{name} 今年 {age} 岁".format(name=name, age=age))
print("{0} 今年 {1} 岁，{0} 很聪明".format(name, age))

# % 格式化（旧式）
print("%s 今年 %d 岁" % (name, age))
print("得分: %.2f" % score)  # 保留2位小数

# 进制转换
num = 255
print(f"十进制: {num}")
print(f"二进制: {bin(num)}")  # 0b11111111
print(f"八进制: {oct(num)}")  # 0o377
print(f"十六进制: {hex(num)}")  # 0xff

# 编码和解码
text = "你好，世界"
encoded = text.encode('utf-8')  # 编码为字节
print(encoded)  # b'\xe4\xbd\xa0\xe5\xa5\xbd...'

decoded = encoded.decode('utf-8')  # 解码为字符串
print(decoded)  # 你好，世界

# 字符和 ASCII 码
print(ord('A'))  # 65（字符转ASCII）
print(chr(65))  # A（ASCII转字符）
print(ord('中'))  # 20013

# 字符串模板
from string import Template
t = Template("$name 今年 $age 岁")
print(t.substitute(name="Alice", age=25))

# 正则表达式
import re
text = "联系电话：138-1234-5678"
phone = re.search(r'\d{3}-\d{4}-\d{4}', text)
if phone:
    print(phone.group())  # 138-1234-5678
```

---

## 3.4 元组 Tuple

元组是**不可变的有序序列**，一旦创建就不能修改。元组使用圆括号 `()` 定义。

### 3.4.1 创建元组

```python
# 空元组
empty_tuple = ()
empty_tuple2 = tuple()

# 包含元素的元组
numbers = (1, 2, 3, 4, 5)
fruits = ("苹果", "香蕉", "橙子")
mixed = (1, "hello", 3.14, True)

# 单元素元组（必须有逗号）
single = (42,)  # 正确
not_tuple = (42)  # 这是整数，不是元组
print(type(single))  # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# 不使用括号（元组打包）
coords = 10, 20
print(type(coords))  # <class 'tuple'>

# 使用 tuple() 构造函数
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)  # (1, 2, 3)

string_tuple = tuple("Hello")
print(string_tuple)  # ('H', 'e', 'l', 'l', 'o')

# 嵌套元组
nested = ((1, 2), (3, 4), (5, 6))
```

### 3.4.2 访问元组

```python
fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")

# 索引访问
print(fruits[0])   # 苹果
print(fruits[-1])  # 西瓜

# 切片
print(fruits[1:4])   # ('香蕉', '橙子', '葡萄')
print(fruits[:3])    # ('苹果', '香蕉', '橙子')
print(fruits[2:])    # ('橙子', '葡萄', '西瓜')
print(fruits[::2])   # ('苹果', '橙子', '西瓜')
print(fruits[::-1])  # ('西瓜', '葡萄', '橙子', '香蕉', '苹果')

# 元组解包
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# 交换变量
a, b = 10, 20
a, b = b, a  # 使用元组解包交换
print(a, b)  # 20 10

# 多个返回值
def get_user_info():
    return "Alice", 25, "Beijing"

name, age, city = get_user_info()
print(name, age, city)

# 嵌套元组访问
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])     # (3, 4)
print(nested[1][0])  # 3
```

### 3.4.3 元组相加

```python
# 使用 + 运算符（创建新元组）
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4, 5, 6)

# 使用 * 运算符（重复）
tuple1 = (1, 2, 3)
result = tuple1 * 3
print(result)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 拼接多个元组
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5, 6)
result = tuple1 + tuple2 + tuple3
print(result)  # (1, 2, 3, 4, 5, 6)

# 注意：元组是不可变的，不能使用 append、extend 等方法
# 如果需要修改，只能创建新元组
```

### 3.4.4 元组查找

```python
fruits = ("苹果", "香蕉", "橙子", "葡萄", "香蕉")

# in / not in
print("苹果" in fruits)  # True
print("西瓜" in fruits)  # False

# index(): 返回元素第一次出现的索引
print(fruits.index("橙子"))  # 2
print(fruits.index("香蕉"))  # 1

# 指定查找范围
print(fruits.index("香蕉", 2))  # 4（从索引2开始查找）

# count(): 统计元素出现次数
print(fruits.count("香蕉"))  # 2
print(fruits.count("西瓜"))  # 0

# 查找不存在的元素会报错
try:
    print(fruits.index("西瓜"))
except ValueError:
    print("元素不存在")
```

### 3.4.5 检查某值是否在元组中存在

```python
fruits = ("苹果", "香蕉", "橙子")

# 使用 in 运算符
if "苹果" in fruits:
    print("苹果在元组中")

if "西瓜" not in fruits:
    print("西瓜不在元组中")

# 结合条件判断
search = "葡萄"
if search in fruits:
    print(f"找到了 {search}")
else:
    print(f"没有找到 {search}")

# 嵌套元组中查找
nested = ((1, 2, 3), (4, 5, 6))
if 5 in nested[1]:
    print("5 在第二个子元组中")

# 检查多个值
targets = ("苹果", "香蕉")
if all(item in fruits for item in targets):
    print("所有目标都在元组中")
```

### 3.4.6 获取元组长度

```python
fruits = ("苹果", "香蕉", "橙子", "葡萄")

# len(): 获取元组长度
print(len(fruits))  # 4

# 空元组
empty = ()
print(len(empty))  # 0

# 单元素元组
single = (42,)
print(len(single))  # 1

# 嵌套元组
nested = ((1, 2), (3, 4), (5, 6))
print(len(nested))  # 3（外层元组的长度）
print(len(nested[0]))  # 2（子元组的长度）
```

### 3.4.7 求元组中的最大值、最小值、加和

```python
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5)

# 最大值
print(max(numbers))  # 9

# 最小值
print(min(numbers))  # 1

# 求和
print(sum(numbers))  # 36

# 平均值
average = sum(numbers) / len(numbers)
print(f"平均值: {average:.2f}")

# 对字符串元组
fruits = ("苹果", "香蕉", "橙子")
print(max(fruits))  # 香蕉（按字典序）
print(min(fruits))  # 橙子

# 自定义比较
words = ("apple", "banana", "cherry", "date")
print(max(words, key=len))  # banana（最长的）
print(min(words, key=len))  # date（最短的）
```

### 3.4.8 遍历元组

```python
fruits = ("苹果", "香蕉", "橙子", "葡萄")

# 直接遍历元素
for fruit in fruits:
    print(fruit)

# 通过索引遍历
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 使用 enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate() 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 遍历多个元组（zip）
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)

for name, age in zip(names, ages):
    print(f"{name}: {age}")

# 嵌套元组遍历
nested = ((1, 2), (3, 4), (5, 6))
for sub_tuple in nested:
    for item in sub_tuple:
        print(item, end=" ")
    print()
```

### 3.4.9 元组的不可变

```python
# 元组是不可变的
fruits = ("苹果", "香蕉", "橙子")

# 不能修改元素（会报错）
# fruits[0] = "葡萄"  # TypeError

# 不能删除元素（会报错）
# del fruits[0]  # TypeError

# 不能使用 append、extend 等方法
# fruits.append("西瓜")  # AttributeError

# 但是可以删除整个元组
del fruits
# print(fruits)  # NameError: 元组已被删除

# 如果元组包含可变对象，可变对象的内容可以修改
data = ([1, 2, 3], [4, 5, 6])
data[0].append(4)  # 修改列表内容（允许）
print(data)  # ([1, 2, 3, 4], [4, 5, 6])

# 但不能替换列表对象本身
# data[0] = [10, 20]  # TypeError

# 如果需要修改，可以转换为列表
fruits = ("苹果", "香蕉", "橙子")
fruits_list = list(fruits)
fruits_list[0] = "葡萄"
fruits = tuple(fruits_list)
print(fruits)  # ('葡萄', '香蕉', '橙子')
```

---

## 3.5 集合 Set

集合是**无序的、不重复的**元素集。集合使用花括号 `{}` 定义。

### 3.5.1 创建集合

```python
# 使用花括号
numbers = {1, 2, 3, 4, 5}
fruits = {"苹果", "香蕉", "橙子"}

# 空集合（必须使用 set()）
empty_set = set()  # 正确
# empty = {}  # 这是空字典，不是空集合

# 使用 set() 构造函数
list_data = [1, 2, 3, 2, 1]  # 有重复元素
set_data = set(list_data)
print(set_data)  # {1, 2, 3}（自动去重）

string_set = set("Hello")
print(string_set)  # {'H', 'e', 'l', 'o'}（自动去重）

# 集合推导式
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# 注意：集合是无序的
fruits = {"苹果", "香蕉", "橙子"}
print(fruits)  # 顺序可能不同
```

### 3.5.2 向集合中添加元素

```python
fruits = {"苹果", "香蕉"}

# add(): 添加单个元素
fruits.add("橙子")
print(fruits)  # {'苹果', '香蕉', '橙子'}

# 添加已存在的元素（无效果）
fruits.add("苹果")
print(fruits)  # {'苹果', '香蕉', '橙子'}（无变化）

# update(): 添加多个元素
fruits.update(["葡萄", "西瓜"])
print(fruits)  # {'苹果', '香蕉', '橙子', '葡萄', '西瓜'}

# update() 可以接受多个可迭代对象
fruits.update(["草莓"], {"芒果"})
print(fruits)

# 使用 | 运算符（创建新集合）
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5}
```

### 3.5.3 从集合中删除元素

```python
fruits = {"苹果", "香蕉", "橙子", "葡萄", "西瓜"}

# remove(): 删除指定元素（不存在会报错）
fruits.remove("橙子")
print(fruits)  # {'苹果', '香蕉', '葡萄', '西瓜'}

try:
    fruits.remove("榴莲")  # KeyError
except KeyError:
    print("元素不存在")

# discard(): 删除指定元素（不存在不报错）
fruits.discard("葡萄")
print(fruits)  # {'苹果', '香蕉', '西瓜'}

fruits.discard("榴莲")  # 不报错
print(fruits)  # {'苹果', '香蕉', '西瓜'}

# pop(): 随机删除并返回一个元素
item = fruits.pop()
print(f"删除了: {item}")
print(fruits)

# clear(): 清空集合
fruits.clear()
print(fruits)  # set()
```

### 3.5.4 检查某值是否在集合中存在

```python
fruits = {"苹果", "香蕉", "橙子"}

# 使用 in / not in
print("苹果" in fruits)  # True
print("西瓜" in fruits)  # False
print("西瓜" not in fruits)  # True

# 结合条件判断
if "香蕉" in fruits:
    print("香蕉在集合中")

# 检查子集
set1 = {1, 2, 3}
set2 = {1, 2}
print(set2.issubset(set1))  # True（set2 是 set1 的子集）
print(set1.issuperset(set2))  # True（set1 是 set2 的超集）

# 检查是否有交集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.isdisjoint(set2))  # False（有交集）

set3 = {6, 7, 8}
print(set1.isdisjoint(set3))  # True（无交集）
```

### 3.5.5 获取集合长度

```python
fruits = {"苹果", "香蕉", "橙子", "葡萄"}

# len(): 获取集合长度
print(len(fruits))  # 4

# 空集合
empty = set()
print(len(empty))  # 0

# 集合自动去重
numbers = {1, 2, 3, 2, 1}
print(len(numbers))  # 3（去重后）
```

### 3.5.6 求集合中的最大值、最小值、加和

```python
numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5}  # 集合会自动去重

# 最大值
print(max(numbers))  # 9

# 最小值
print(min(numbers))  # 1

# 求和
print(sum(numbers))  # 31（去重后的和）

# 平均值
average = sum(numbers) / len(numbers)
print(f"平均值: {average:.2f}")

# 对字符串集合
fruits = {"苹果", "香蕉", "橙子"}
print(max(fruits))  # 香蕉（按字典序）
print(min(fruits))  # 橙子
```

### 3.5.7 遍历集合

```python
fruits = {"苹果", "香蕉", "橙子", "葡萄"}

# 直接遍历（顺序不确定）
for fruit in fruits:
    print(fruit)

# 转换为列表后遍历（可以排序）
for fruit in sorted(fruits):
    print(fruit)

# 使用 enumerate()（顺序不确定）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 集合推导式
numbers = {1, 2, 3, 4, 5}
squares = {x**2 for x in numbers}
print(squares)  # {1, 4, 9, 16, 25}
```

### 3.5.8 集合运算

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 并集（所有元素）
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))  # 同上

# 交集（共同元素）
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # 同上

# 差集（在 set1 但不在 set2 中）
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))  # 同上

# 对称差集（不同时在两个集合中）
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # 同上

# 实际应用：去重
list_data = [1, 2, 3, 2, 1, 4, 5, 4]
unique = list(set(list_data))
print(unique)  # [1, 2, 3, 4, 5]

# 找出两个列表的共同元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)  # [4, 5]

# 找出只在第一个列表中的元素
only_in_list1 = list(set(list1) - set(list2))
print(only_in_list1)  # [1, 2, 3]
```

---

## 3.6 字典 Dictionary

字典是**无序的键值对集合**，使用花括号 `{}` 定义，键必须唯一且不可变。

### 3.6.1 创建字典

```python
# 空字典
empty_dict = {}
empty_dict2 = dict()

# 包含元素的字典
person = {
    "name": "Alice",
    "age": 25,
    "city": "北京"
}

# 使用 dict() 构造函数
person = dict(name="Alice", age=25, city="北京")

# 从元组列表创建
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)

# 使用 zip() 创建
keys = ["name", "age", "city"]
values = ["Alice", 25, "北京"]
person = dict(zip(keys, values))

# 字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 使用 fromkeys() 创建（所有键共享同一个值）
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # {'a': 0, 'b': 0, 'c': 0}

# 嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
```

### 3.6.2 访问字典

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# 通过键访问值
print(person["name"])  # Alice
print(person["age"])   # 25

# 键不存在会报错
# print(person["email"])  # KeyError

# 使用 get() 方法（推荐）
print(person.get("name"))  # Alice
print(person.get("email"))  # None（不报错）
print(person.get("email", "未提供"))  # 未提供（提供默认值）

# 访问嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(users["user1"]["name"])  # Alice

# 获取所有键
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# 获取所有值
print(person.values())  # dict_values(['Alice', 25, '北京'])

# 获取所有键值对
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', '北京')])
```

### 3.6.3 向字典中添加元素

```python
person = {"name": "Alice", "age": 25}

# 直接赋值添加
person["city"] = "北京"
print(person)  # {'name': 'Alice', 'age': 25, 'city': '北京'}

# update(): 添加多个键值对
person.update({"email": "alice@example.com", "phone": "123-4567"})
print(person)

# update() 也可以接受关键字参数
person.update(job="工程师", salary=10000)
print(person)

# setdefault(): 如果键不存在则添加，存在则返回值
person.setdefault("country", "中国")
print(person)  # 添加了 country

person.setdefault("name", "Bob")  # name 已存在，不修改
print(person["name"])  # Alice
```

### 3.6.4 修改字典中的元素

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# 直接通过键修改
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': '北京'}

# 使用 update() 修改
person.update({"age": 27, "city": "上海"})
print(person)  # {'name': 'Alice', 'age': 27, 'city': '上海'}

# 修改嵌套字典
users = {
    "user1": {"name": "Alice", "age": 25}
}
users["user1"]["age"] = 26
print(users)  # {'user1': {'name': 'Alice', 'age': 26}}

# 如果键不存在，直接赋值会创建新键值对
person["email"] = "alice@example.com"
print(person)
```

### 3.6.5 检查某值是否在字典中的 key

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# 使用 in / not in（检查键）
print("name" in person)  # True
print("email" in person)  # False
print("email" not in person)  # True

# 检查值（需要使用 values()）
print("Alice" in person.values())  # True
print("Bob" in person.values())  # False

# 结合条件判断
if "email" in person:
    print(f"邮箱: {person['email']}")
else:
    print("没有邮箱信息")

# 使用 get() 更安全
email = person.get("email")
if email:
    print(f"邮箱: {email}")
else:
    print("没有邮箱信息")
```

### 3.6.6 获取字典长度

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# len(): 获取键值对数量
print(len(person))  # 3

# 空字典
empty = {}
print(len(empty))  # 0

# 嵌套字典（只计算外层）
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(len(users))  # 2（外层只有2个键）
print(len(users["user1"]))  # 2（user1 内部有2个键）
```

### 3.6.7 遍历字典

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# 遍历键
for key in person:
    print(key)

# 或显式使用 keys()
for key in person.keys():
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对（推荐）
for key, value in person.items():
    print(f"{key}: {value}")

# 使用 enumerate()
for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")

# 嵌套字典遍历
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}

for user_id, user_info in users.items():
    print(f"{user_id}:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 过滤字典
person = {"name": "Alice", "age": 25, "city": "北京", "email": "alice@example.com"}
filtered = {k: v for k, v in person.items() if isinstance(v, str)}
print(filtered)  # {'name': 'Alice', 'city': '北京', 'email': 'alice@example.com'}
```

### 3.6.8 删除字典元素

```python
person = {"name": "Alice", "age": 25, "city": "北京", "email": "alice@example.com"}

# pop(): 删除指定键并返回值
age = person.pop("age")
print(age)  # 25
print(person)  # {'name': 'Alice', 'city': '北京', 'email': 'alice@example.com'}

# pop() 提供默认值（键不存在时不报错）
phone = person.pop("phone", "未提供")
print(phone)  # 未提供

# popitem(): 删除并返回最后一个键值对（Python 3.7+）
item = person.popitem()
print(item)  # ('email', 'alice@example.com')
print(person)  # {'name': 'Alice', 'city': '北京'}

# del: 删除指定键
del person["city"]
print(person)  # {'name': 'Alice'}

# 删除不存在的键会报错
# del person["age"]  # KeyError

# clear(): 清空字典
person.clear()
print(person)  # {}
```

### 3.6.9 常用函数

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# len(): 字典长度
print(len(person))  # 3

# keys(): 获取所有键
print(list(person.keys()))  # ['name', 'age', 'city']

# values(): 获取所有值
print(list(person.values()))  # ['Alice', 25, '北京']

# items(): 获取所有键值对
print(list(person.items()))  # [('name', 'Alice'), ('age', 25), ('city', '北京')]

# get(): 安全获取值
print(person.get("name"))  # Alice
print(person.get("email", "无"))  # 无

# copy(): 浅拷贝
person_copy = person.copy()
person_copy["age"] = 26
print(person["age"])  # 25（原字典不变）

# 深拷贝（嵌套字典）
import copy
users = {"user1": {"name": "Alice", "age": 25}}
shallow = users.copy()
deep = copy.deepcopy(users)

shallow["user1"]["age"] = 26  # 影响原字典
deep["user1"]["age"] = 27     # 不影响原字典

print(users)  # {'user1': {'name': 'Alice', 'age': 26}}

# 合并字典（Python 3.9+）
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}

# 或使用 update()
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# sorted(): 按键排序
person = {"name": "Alice", "city": "北京", "age": 25}
sorted_keys = sorted(person.keys())
print(sorted_keys)  # ['age', 'city', 'name']

# 按值排序
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

---

## 3.7 列表、元组、字典和集合的区别

| 特性 | 列表 (List) | 元组 (Tuple) | 字典 (Dictionary) | 集合 (Set) |
|------|------------|-------------|------------------|-----------|
| **定义符号** | `[]` | `()` | `{}` | `{}` 或 `set()` |
| **是否有序** | 有序 | 有序 | 无序（Python 3.7+ 保持插入顺序） | 无序 |
| **是否可变** | 可变 | 不可变 | 可变 | 可变 |
| **元素唯一性** | 可重复 | 可重复 | 键唯一 | 元素唯一 |
| **访问方式** | 索引 | 索引 | 键 | 不支持索引 |
| **存储内容** | 任意类型 | 任意类型 | 键值对 | 不可变类型 |
| **典型用途** | 动态数据集合 | 不可变数据、函数返回值 | 映射关系、配置 | 去重、集合运算 |

### 详细对比

```python
# 列表：可变、有序、可重复
my_list = [1, 2, 3, 2, 1]
my_list[0] = 10  # 可以修改
my_list.append(4)  # 可以添加
print(my_list)  # [10, 2, 3, 2, 1, 4]

# 元组：不可变、有序、可重复
my_tuple = (1, 2, 3, 2, 1)
# my_tuple[0] = 10  # TypeError: 不能修改
print(my_tuple[0])  # 可以通过索引访问

# 字典：可变、无序（3.7+有序）、键唯一
my_dict = {"a": 1, "b": 2, "a": 3}  # 重复键会覆盖
my_dict["c"] = 4  # 可以添加
print(my_dict)  # {'a': 3, 'b': 2, 'c': 4}

# 集合：可变、无序、元素唯一
my_set = {1, 2, 3, 2, 1}  # 自动去重
my_set.add(4)  # 可以添加
print(my_set)  # {1, 2, 3, 4}
# print(my_set[0])  # TypeError: 不支持索引
```

### 使用场景

```python
# 列表：适合需要频繁修改、保持顺序的数据
shopping_list = ["苹果", "香蕉", "橙子"]
shopping_list.append("葡萄")

# 元组：适合不可变的数据、函数返回多个值
coordinates = (10, 20)
def get_user():
    return "Alice", 25, "Beijing"

# 字典：适合键值映射、配置数据
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# 集合：适合去重、集合运算
# 去重
numbers = [1, 2, 3, 2, 1]
unique = list(set(numbers))  # [1, 2, 3]

# 找交集
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))  # [3, 4]
```

### 性能对比

```python
# 列表：O(1) 索引访问，O(n) 查找
my_list = [1, 2, 3, 4, 5]
print(my_list[2])  # O(1)
print(3 in my_list)  # O(n)

# 元组：与列表类似，但更轻量
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])  # O(1)

# 字典：O(1) 键访问（哈希表）
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["b"])  # O(1)
print("b" in my_dict)  # O(1)

# 集合：O(1) 成员检查（哈希表）
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # O(1)
```

### 相互转换

```python
# 列表、元组、集合之间的转换
my_list = [1, 2, 3, 2, 1]

# 列表 → 元组
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 2, 1)

# 列表 → 集合（去重）
my_set = set(my_list)
print(my_set)  # {1, 2, 3}

# 元组 → 列表
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3, 2, 1]

# 集合 → 列表
my_list = list(my_set)
print(my_list)  # [1, 2, 3]

# 字典 → 列表
my_dict = {"a": 1, "b": 2, "c": 3}
keys = list(my_dict.keys())
values = list(my_dict.values())
items = list(my_dict.items())
print(keys)  # ['a', 'b', 'c']
print(values)  # [1, 2, 3]
print(items)  # [('a', 1), ('b', 2), ('c', 3)]

# 列表 → 字典
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
```

---

## 总结

本章介绍了 Python 的容器型数据类型：

1. **序列**：有序的元素集合，支持索引和切片
2. **列表**：可变、有序、可重复，最常用的数据结构
3. **字符串**：不可变的字符序列，丰富的文本处理方法
4. **元组**：不可变、有序、可重复，适合固定数据
5. **集合**：无序、元素唯一，支持集合运算
6. **字典**：键值对映射，快速查找

掌握这些数据结构的特点和使用方法，是编写高效 Python 程序的基础。

---

## 练习题

1. 编写程序统计列表中每个元素出现的次数（使用字典）
2. 实现两个列表的合并并去重
3. 编写函数，输入学生成绩字典，返回平均分最高的班级
4. 使用集合运算找出两个列表的交集、并集、差集
5. 编写程序，将嵌套列表展平为一维列表
6. 实现一个简单的学生管理系统（使用字典存储学生信息）
7. 编写函数，反转字典的键和值
8. 使用列表推导式生成 1-100 内所有质数的列表
