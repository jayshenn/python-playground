# 第 1 章 基础知识

## 1.1 注释

### 1.1.1 什么是注释

注释是在程序代码中添加的说明性文字，用于解释代码的功能、逻辑或其他重要信息。注释不会被 Python 解释器执行，仅供程序员阅读和理解代码。

### 1.1.2 注释的作用

- 提高代码可读性
- 帮助他人理解代码逻辑
- 方便后期维护和修改
- 记录重要的设计决策
- 临时禁用某段代码

### 1.1.3 单行注释（行注释）

Python 中使用 `#` 符号来表示单行注释。`#` 后面的内容都会被解释器忽略。

```python
# 这是单行注释
print("Hello, World!")  # 这也是单行注释

# 计算两个数的和
result = 10 + 20
```

### 1.1.4 多行注释（块注释）

Python 中可以使用三个引号（`'''` 或 `"""`）来创建多行注释。

```python
'''
这是多行注释
可以写多行内容
用于详细说明
'''

"""
这也是多行注释
通常用于文档字符串（docstring）
"""

def example_function():
    """
    这是函数的文档字符串
    用于描述函数的功能、参数和返回值
    """
    pass
```

---

## 1.2 变量

### 1.2.1 什么是变量

变量是用于存储数据的容器。在 Python 中，变量不需要提前声明类型，可以直接赋值使用。

```python
# 变量就像一个标签，指向内存中的某个值
name = "Alice"
age = 25
height = 1.68
```

### 1.2.2 变量的创建

Python 中创建变量非常简单，使用赋值运算符 `=` 即可。

```python
# 创建变量
x = 10          # 整数
y = 3.14        # 浮点数
name = "Bob"    # 字符串
is_valid = True # 布尔值

# 多重赋值
a, b, c = 1, 2, 3
x = y = z = 0
```

### 1.2.3 标识符命名规则

标识符是给变量、函数、类等命名的名称。Python 中的命名规则：

**规则**：
- 只能包含字母、数字和下划线
- 不能以数字开头
- 区分大小写
- 不能使用 Python 关键字

**推荐规范**：
- 变量名使用小写字母，多个单词用下划线分隔（snake_case）
- 常量使用全大写字母
- 类名使用首字母大写（PascalCase）
- 私有变量以下划线开头

```python
# 正确的命名
user_name = "Alice"
USER_AGE = 25
MAX_SIZE = 100

# 错误的命名
# 2name = "Bob"    # 不能以数字开头
# user-name = "C"  # 不能包含连字符
# for = 10         # 不能使用关键字
```

### 1.2.4 变量的修改

变量的值可以随时被重新赋值。

```python
x = 10
print(x)  # 输出: 10

x = 20
print(x)  # 输出: 20

# 变量的值可以改变类型
x = "Hello"
print(x)  # 输出: Hello
```

### 1.2.5 常量

Python 中没有真正的常量，通常使用全大写的变量名来表示常量，提醒开发者不要修改。

```python
# 常量（约定俗成）
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432"

# 虽然可以修改，但不建议这样做
# PI = 3.14  # 不推荐
```

---

## 1.3 类型以及转换

### 1.3.1 进制

计算机中常用的进制系统：
- **二进制（Binary）**：基数为 2，使用 0 和 1
- **八进制（Octal）**：基数为 8，使用 0-7
- **十进制（Decimal）**：基数为 10，使用 0-9
- **十六进制（Hexadecimal）**：基数为 16，使用 0-9 和 A-F

### 1.3.2 不同进制表示数字

在 Python 中，可以使用不同的前缀来表示不同进制的数字。

```python
# 十进制
decimal = 42

# 二进制（0b 或 0B 前缀）
binary = 0b101010
print(binary)  # 输出: 42

# 八进制（0o 或 0O 前缀）
octal = 0o52
print(octal)   # 输出: 42

# 十六进制（0x 或 0X 前缀）
hexadecimal = 0x2A
print(hexadecimal)  # 输出: 42
```

### 1.3.3 二进制转换成十进制

二进制转十进制：将每一位上的数字乘以 2 的相应次幂，然后求和。

```
例如：1010 (二进制) = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = 10 (十进制)
```

```python
# 使用内置函数转换
binary_str = "1010"
decimal_value = int(binary_str, 2)
print(decimal_value)  # 输出: 10

# 手动计算
result = 1*2**3 + 0*2**2 + 1*2**1 + 0*2**0
print(result)  # 输出: 10
```

### 1.3.4 十进制转换成二进制

十进制转二进制：使用"除2取余法"，将十进制数不断除以 2，取余数，直到商为 0。

```
例如：10 (十进制) → 1010 (二进制)
10 ÷ 2 = 5 余 0
5 ÷ 2 = 2 余 1
2 ÷ 2 = 1 余 0
1 ÷ 2 = 0 余 1
从下往上读取余数：1010
```

```python
# 使用内置函数
decimal = 10
binary_str = bin(decimal)
print(binary_str)  # 输出: 0b1010
print(binary_str[2:])  # 去掉 0b 前缀，输出: 1010
```

### 1.3.5 八进制转换成十进制

八进制转十进制：将每一位上的数字乘以 8 的相应次幂，然后求和。

```
例如：52 (八进制) = 5×8¹ + 2×8⁰ = 40 + 2 = 42 (十进制)
```

```python
# 使用内置函数转换
octal_str = "52"
decimal_value = int(octal_str, 8)
print(decimal_value)  # 输出: 42
```

### 1.3.6 十进制转换成十六进制

十进制转十六进制：使用"除16取余法"，类似于转二进制。

```python
# 使用内置函数
decimal = 255
hex_str = hex(decimal)
print(hex_str)  # 输出: 0xff
print(hex_str[2:])  # 去掉 0x 前缀，输出: ff
```

### 1.3.7 二进制转换成十六进制

二进制转十六进制：可以先转为十进制，再转为十六进制。或者将二进制数每 4 位分组，直接转换。

```
例如：11111111 (二进制)
分组：1111 1111
转换：F    F
结果：FF (十六进制)
```

```python
# 方法1：通过十进制中转
binary_str = "11111111"
decimal = int(binary_str, 2)
hex_str = hex(decimal)
print(hex_str)  # 输出: 0xff

# 方法2：直接使用格式化
binary_value = 0b11111111
print(f"{binary_value:x}")  # 输出: ff
```

### 1.3.8 十六进制转换成二进制

十六进制转二进制：每个十六进制位对应 4 个二进制位。

```
例如：FF (十六进制)
F → 1111
F → 1111
结果：11111111 (二进制)
```

```python
# 使用内置函数
hex_str = "FF"
decimal = int(hex_str, 16)
binary_str = bin(decimal)
print(binary_str)  # 输出: 0b11111111
```

---

## 1.4 数据类型

### 1.4.1 int 整数型

整数类型用于表示没有小数部分的数字。Python 3 中的整数没有大小限制。

```python
# 整数
age = 25
negative = -10
big_number = 123456789012345678901234567890

# 不同进制的整数
binary = 0b1010      # 二进制
octal = 0o12         # 八进制
hexadecimal = 0xA    # 十六进制

print(type(age))  # <class 'int'>
```

### 1.4.2 float 浮点型

浮点型用于表示带有小数部分的数字。

```python
# 浮点数
pi = 3.14159
height = 1.75
temperature = -5.5

# 科学计数法
large = 1.5e10    # 1.5 × 10^10
small = 2.5e-5    # 2.5 × 10^-5

print(type(pi))  # <class 'float'>

# 浮点数精度问题
result = 0.1 + 0.2
print(result)  # 0.30000000000000004
```

### 1.4.3 bool 布尔型

布尔型只有两个值：`True` 和 `False`，用于表示真假。

```python
# 布尔值
is_student = True
is_graduated = False

print(type(is_student))  # <class 'bool'>

# 布尔值在条件判断中的应用
if is_student:
    print("这是一名学生")

# 布尔值的数值表示
print(int(True))   # 1
print(int(False))  # 0
```

### 1.4.4 String 字符串初识

字符串是用于表示文本的数据类型，使用单引号或双引号定义。

```python
# 字符串
name = "Alice"
message = 'Hello, World!'
multiline = """
这是多行
字符串
"""

print(type(name))  # <class 'str'>

# 字符串操作
greeting = "Hello"
target = "World"
full_message = greeting + " " + target  # 拼接
print(full_message)  # Hello World

# 字符串方法
print(name.upper())   # ALICE
print(name.lower())   # alice
print(len(name))      # 5
```

### 1.4.5 数据类型转换

Python 提供了多种函数来进行数据类型转换。

```python
# 转换为整数
x = int("123")      # 字符串转整数
y = int(3.14)       # 浮点数转整数（截断小数部分）
z = int(True)       # 布尔值转整数

# 转换为浮点数
a = float("3.14")   # 字符串转浮点数
b = float(10)       # 整数转浮点数
c = float(True)     # 布尔值转浮点数

# 转换为字符串
s1 = str(123)       # 整数转字符串
s2 = str(3.14)      # 浮点数转字符串
s3 = str(True)      # 布尔值转字符串

# 转换为布尔值
b1 = bool(1)        # 非零数转为 True
b2 = bool(0)        # 0 转为 False
b3 = bool("text")   # 非空字符串转为 True
b4 = bool("")       # 空字符串转为 False

print(type(x), x)  # <class 'int'> 123
```

### 1.4.6 字符的编码和解码

字符编码是将字符转换为字节序列的过程，解码是将字节序列转换回字符的过程。

```python
# 编码（字符串 → 字节）
text = "Hello, 世界"
encoded = text.encode('utf-8')
print(encoded)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# 解码（字节 → 字符串）
decoded = encoded.decode('utf-8')
print(decoded)  # Hello, 世界

# 常见编码格式
utf8_bytes = text.encode('utf-8')
gbk_bytes = text.encode('gbk')

# 获取字符的 Unicode 码点
print(ord('A'))     # 65
print(ord('中'))    # 20013

# 根据码点获取字符
print(chr(65))      # A
print(chr(20013))   # 中
```

---

## 1.5 输入与输出

### 1.5.1 输入

使用 `input()` 函数从控制台接收用户输入。

```python
# 基本输入
name = input("请输入你的名字：")
print(f"你好，{name}！")

# input() 返回的是字符串类型
age_str = input("请输入你的年龄：")
age = int(age_str)  # 需要转换为整数
print(f"你的年龄是 {age} 岁")

# 一次性输入多个值
data = input("请输入三个数字，用空格分隔：")
a, b, c = map(int, data.split())
print(f"你输入的数字是：{a}, {b}, {c}")
```

### 1.5.2 输出

使用 `print()` 函数向控制台输出内容。

```python
# 基本输出
print("Hello, World!")

# 输出多个值
name = "Alice"
age = 25
print("姓名:", name, "年龄:", age)

# 格式化输出
# 方法1：f-string（推荐）
print(f"姓名: {name}, 年龄: {age}")

# 方法2：format()
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {n}, 年龄: {a}".format(n=name, a=age))

# 方法3：% 格式化（旧式）
print("姓名: %s, 年龄: %d" % (name, age))

# 控制输出格式
print("圆周率:", 3.14159)
print(f"圆周率（保留2位小数）: {3.14159:.2f}")

# 控制输出的结束符
print("Hello", end=" ")
print("World")  # 输出: Hello World

# 控制输出的分隔符
print("apple", "banana", "orange", sep=", ")
# 输出: apple, banana, orange
```

---

## 1.6 运算符

### 1.6.1 算术运算符

用于执行基本的数学运算。

```python
a = 10
b = 3

print(a + b)   # 加法: 13
print(a - b)   # 减法: 7
print(a * b)   # 乘法: 30
print(a / b)   # 除法: 3.3333...
print(a // b)  # 整除: 3
print(a % b)   # 取余: 1
print(a ** b)  # 幂运算: 1000

# 复合赋值运算符
x = 10
x += 5   # 等价于 x = x + 5
x -= 3   # 等价于 x = x - 3
x *= 2   # 等价于 x = x * 2
x /= 4   # 等价于 x = x / 4
```

### 1.6.2 赋值运算符

用于给变量赋值。

```python
# 简单赋值
x = 10

# 复合赋值
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2

# 多重赋值
a = b = c = 0
x, y, z = 1, 2, 3

# 交换变量
a, b = b, a
```

### 1.6.3 比较运算符

用于比较两个值，返回布尔值。

```python
a = 10
b = 5

print(a == b)  # 等于: False
print(a != b)  # 不等于: True
print(a > b)   # 大于: True
print(a < b)   # 小于: False
print(a >= b)  # 大于等于: True
print(a <= b)  # 小于等于: False

# 链式比较
x = 5
print(1 < x < 10)  # True
print(0 <= x <= 100)  # True
```

### 1.6.4 逻辑运算符

用于组合多个条件判断。

```python
# and（与）：所有条件都为 True 时返回 True
print(True and True)    # True
print(True and False)   # False

# or（或）：至少一个条件为 True 时返回 True
print(True or False)    # True
print(False or False)   # False

# not（非）：取反
print(not True)   # False
print(not False)  # True

# 实际应用
age = 25
is_student = True
if age >= 18 and is_student:
    print("成年学生")

# 短路运算
x = 0
y = 10
result = x != 0 and y / x  # x == 0，不会执行 y / x
```

### 1.6.5 位运算符

用于对二进制位进行操作。

```python
a = 60  # 二进制: 0011 1100
b = 13  # 二进制: 0000 1101

print(a & b)   # 按位与: 12 (0000 1100)
print(a | b)   # 按位或: 61 (0011 1101)
print(a ^ b)   # 按位异或: 49 (0011 0001)
print(~a)      # 按位取反: -61
print(a << 2)  # 左移: 240 (1111 0000)
print(a >> 2)  # 右移: 15 (0000 1111)

# 实际应用：快速计算
# 左移1位相当于乘以2
print(5 << 1)  # 10

# 右移1位相当于除以2
print(10 >> 1)  # 5
```

### 1.6.6 成员运算符

用于检查一个值是否在序列中。

```python
# in：存在于序列中
# not in：不存在于序列中

# 字符串
text = "Hello, World!"
print('H' in text)       # True
print('h' in text)       # False
print('Python' not in text)  # True

# 列表
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(10 not in numbers) # True

# 字典
person = {'name': 'Alice', 'age': 25}
print('name' in person)  # True（检查键）
print('Alice' in person) # False（不检查值）
```

### 1.6.7 身份运算符

用于比较两个对象的内存地址是否相同。

```python
# is：两个对象是否相同（内存地址相同）
# is not：两个对象是否不同

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True（值相等）
print(a is b)   # False（不是同一个对象）
print(a is c)   # True（是同一个对象）

# 特殊情况：小整数和短字符串会被缓存
x = 10
y = 10
print(x is y)  # True

# 与 None 比较时，应该使用 is
value = None
if value is None:
    print("value 是 None")
```

### 1.6.8 运算符优先级

运算符优先级从高到低：

1. **括号**：`()`
2. **幂运算**：`**`
3. **正负号**：`+x`, `-x`, `~x`
4. **乘除取余**：`*`, `/`, `//`, `%`
5. **加减**：`+`, `-`
6. **位移**：`<<`, `>>`
7. **按位与**：`&`
8. **按位异或**：`^`
9. **按位或**：`|`
10. **比较运算**：`<`, `<=`, `>`, `>=`, `==`, `!=`
11. **身份运算**：`is`, `is not`
12. **成员运算**：`in`, `not in`
13. **逻辑非**：`not`
14. **逻辑与**：`and`
15. **逻辑或**：`or`

```python
# 优先级示例
result = 2 + 3 * 4  # 先乘后加: 14
result = (2 + 3) * 4  # 括号优先: 20

# 建议使用括号提高可读性
result = (a > b) and (c < d)
```

---

## 1.7 Python 编程规范

### 1.7.1 缩进

Python 使用缩进来表示代码块，而不是使用大括号。

```python
# 正确的缩进
if True:
    print("缩进正确")
    if True:
        print("嵌套缩进")

# 错误的缩进会导致语法错误
# if True:
# print("这是错误的")  # IndentationError

# 推荐使用 4 个空格作为缩进
def example():
    x = 10
    if x > 0:
        print("正数")
```

### 1.7.2 行长

每行代码不应该超过 79 个字符（PEP 8 规范）。

```python
# 过长的行应该折行
long_string = (
    "这是一个很长的字符串，"
    "为了保持代码的可读性，"
    "我们将它分成多行"
)

# 函数调用可以这样折行
result = some_function(
    argument1,
    argument2,
    argument3
)

# 列表、字典等也可以折行
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
```

### 1.7.3 空行

使用空行来分隔代码的逻辑部分，提高可读性。

```python
# 顶级函数和类之间空两行
def function1():
    pass


def function2():
    pass


class MyClass:
    pass


# 类中的方法之间空一行
class Example:
    def method1(self):
        pass

    def method2(self):
        pass


# 函数内部可以使用空行分隔逻辑段
def complex_function():
    # 第一部分
    x = 10
    y = 20

    # 第二部分
    result = x + y
    return result
```

### 1.7.4 一行显示多条语句

虽然 Python 允许在一行中写多条语句，但不推荐这样做。

```python
# 不推荐：一行多条语句
x = 10; y = 20; z = 30

# 推荐：每行一条语句
x = 10
y = 20
z = 30

# 简单的条件语句可以写在一行
if x > 0: print("正数")

# 但建议还是分行写
if x > 0:
    print("正数")
```

### 1.7.5 分号

Python 中不需要使用分号来结束语句（除非在一行中写多条语句）。

```python
# 正确：不使用分号
print("Hello")
x = 10

# 虽然允许，但不推荐
print("Hello");
x = 10;

# 一行多条语句时使用分号（不推荐）
x = 10; y = 20
```

### 1.7.6 逗号(,)编码

在使用逗号时，应该注意格式。

```python
# 函数参数
def example(a, b, c):
    pass

# 列表、元组等
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)

# 多行时，最后一项可以加逗号（推荐）
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing',  # 最后一项也加逗号，方便以后添加新项
}

# 函数调用
result = some_function(
    arg1,
    arg2,
    arg3,  # 最后一项也可以加逗号
)
```

### 1.7.7 代码格式统一—行代码

保持代码格式统一，提高可读性。

```python
# 运算符两边加空格
x = 10
y = x + 5

# 函数定义
def add(a, b):
    return a + b

# 函数调用
result = add(10, 20)

# 列表索引和切片不加空格
my_list[0]
my_list[1:5]

# 字典
person = {'name': 'Alice', 'age': 25}

# 命名规范
# 变量和函数：小写+下划线
user_name = "Alice"

def get_user_info():
    pass

# 类名：大驼峰
class UserProfile:
    pass

# 常量：全大写+下划线
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30
```

---

## 总结

本章介绍了 Python 编程的基础知识，包括：

1. **注释**：单行注释和多行注释的使用
2. **变量**：变量的创建、命名规则和修改
3. **类型转换**：进制转换和数据类型转换
4. **数据类型**：整数、浮点数、布尔值、字符串及其操作
5. **输入输出**：使用 `input()` 和 `print()` 进行交互
6. **运算符**：算术、比较、逻辑、位、成员、身份运算符及其优先级
7. **编程规范**：缩进、行长、空行、代码格式等

掌握这些基础知识是学习 Python 的重要起点。建议通过大量的练习来巩固这些概念。

---

## 练习题

1. 编写一个程序，输入两个数字，输出它们的和、差、积、商
2. 实现一个简单的计算器，支持加减乘除运算
3. 编写程序，将十进制数转换为二进制、八进制和十六进制
4. 使用逻辑运算符判断一个年份是否为闰年
5. 编写一个程序，输入字符串，统计其中的字母、数字和空格的数量
