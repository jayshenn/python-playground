# 第 4 章 函数

## 4.1 函数的概念

函数是组织好的、可重复使用的、用来实现特定功能的代码块。函数能提高应用的模块性和代码的重复利用率。

**为什么需要函数？**
- **代码复用**：避免重复编写相同的代码
- **模块化**：将复杂问题分解为简单的子问题
- **易于维护**：修改功能只需修改函数定义
- **提高可读性**：给代码块一个有意义的名称

**Python 中的函数类型**：
1. **内置函数**：Python 提供的函数，如 `print()`、`len()`、`max()` 等
2. **标准库函数**：需要导入的函数，如 `math.sqrt()`、`random.randint()` 等
3. **第三方库函数**：安装第三方库后使用的函数
4. **自定义函数**：用户自己定义的函数

```python
# 内置函数
print("Hello")
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5
print(max(numbers))  # 5

# 标准库函数
import math
print(math.sqrt(16))  # 4.0

# 自定义函数
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

---

## 4.2 函数的定义

### 4.2.1 语法

定义函数使用 `def` 关键字。

**基本语法**：
```python
def 函数名(参数列表):
    """函数文档字符串（可选）"""
    函数体
    return 返回值（可选）
```

**语法规则**：
- 使用 `def` 关键字开始函数定义
- 函数名遵循标识符命名规则（小写字母+下划线）
- 参数列表放在括号内，可以为空
- 函数体必须缩进（通常 4 个空格）
- `return` 语句可选，用于返回值

### 4.2.2 定义一个简单的函数

```python
# 无参数、无返回值
def say_hello():
    print("Hello, World!")

say_hello()  # 调用函数

# 有参数、无返回值
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!

# 有参数、有返回值
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# 无参数、有返回值
def get_pi():
    return 3.14159

pi = get_pi()
print(pi)  # 3.14159
```

### 4.2.3 函数名

函数名是函数的标识符，命名应该遵循规范。

**命名规则**：
- 只能包含字母、数字、下划线
- 不能以数字开头
- 不能使用 Python 关键字
- 区分大小写

**命名规范**（PEP 8）：
- 使用小写字母
- 多个单词用下划线分隔（snake_case）
- 名称应该描述函数的功能（动词开头）

```python
# 好的函数名
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_even(number):
    return number % 2 == 0

def get_user_info():
    return {"name": "Alice", "age": 25}

# 不好的函数名
def calc():  # 太简短，不清楚
    pass

def MyFunction():  # 不符合规范（应该用小写）
    pass

def x():  # 无意义的名称
    pass
```

### 4.2.4 参数

参数是函数接收的输入值。

```python
# 单个参数
def square(x):
    return x ** 2

print(square(5))  # 25

# 多个参数
def add(a, b):
    return a + b

print(add(3, 5))  # 8

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!

# 可变数量参数
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15
```

### 4.2.5 函数体

函数体是函数执行的代码块，必须缩进。

```python
def process_data(data):
    # 验证数据
    if not data:
        return None

    # 处理数据
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)

    # 返回结果
    return result

numbers = [1, -2, 3, -4, 5]
processed = process_data(numbers)
print(processed)  # [2, 6, 10]
```

### 4.2.6 返回值

`return` 语句用于从函数返回值。

```python
# 返回单个值
def square(x):
    return x ** 2

# 返回多个值（元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(f"最小值: {min_val}, 最大值: {max_val}")

# 无返回值（返回 None）
def print_message(msg):
    print(msg)
    # 隐式返回 None

result = print_message("Hello")
print(result)  # None

# 条件返回
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(get_grade(85))  # B

# 提前返回
def find_item(items, target):
    for item in items:
        if item == target:
            return item  # 找到后立即返回
    return None  # 未找到
```

---

## 4.3 函数的定义和及调用

**定义函数**：
```python
def function_name(parameters):
    """函数文档"""
    # 函数体
    return value
```

**调用函数**：
```python
result = function_name(arguments)
```

**完整示例**：
```python
# 定义函数
def calculate_area(length, width):
    """
    计算矩形面积

    参数:
        length: 长度
        width: 宽度

    返回:
        矩形面积
    """
    area = length * width
    return area

# 调用函数
rectangle_area = calculate_area(10, 5)
print(f"矩形面积: {rectangle_area}")  # 矩形面积: 50

# 多次调用
print(calculate_area(3, 4))   # 12
print(calculate_area(7, 8))   # 56
```

**函数调用的注意事项**：
```python
# 1. 必须先定义后调用
# greet("Alice")  # NameError: 函数未定义

def greet(name):
    return f"Hello, {name}!"

greet("Alice")  # 正确

# 2. 参数数量必须匹配
def add(a, b):
    return a + b

# add(1)  # TypeError: 缺少参数
# add(1, 2, 3)  # TypeError: 参数过多
add(1, 2)  # 正确

# 3. 函数名区分大小写
def MyFunc():
    return "Hello"

# myfunc()  # NameError
MyFunc()  # 正确
```

---

## 4.4 使用函数的好处

### 1. 代码复用

```python
# 不使用函数：重复代码
print("=" * 50)
print("欢迎使用系统")
print("=" * 50)

# ... 其他代码 ...

print("=" * 50)
print("感谢使用")
print("=" * 50)

# 使用函数：复用代码
def print_banner(message):
    print("=" * 50)
    print(message.center(50))
    print("=" * 50)

print_banner("欢迎使用系统")
# ... 其他代码 ...
print_banner("感谢使用")
```

### 2. 提高可读性

```python
# 不使用函数：不易理解
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum([x for x in data if x % 2 == 0]) / len([x for x in data if x % 2 == 0])

# 使用函数：清晰明了
def calculate_even_average(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    return sum(evens) / len(evens)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_even_average(data)
```

### 3. 模块化开发

```python
# 将复杂问题分解为小函数
def validate_input(data):
    """验证输入数据"""
    return data is not None and len(data) > 0

def process_data(data):
    """处理数据"""
    return [x * 2 for x in data if x > 0]

def format_output(data):
    """格式化输出"""
    return ", ".join(map(str, data))

def main(input_data):
    """主函数：协调各个步骤"""
    if not validate_input(input_data):
        return "无效输入"

    processed = process_data(input_data)
    output = format_output(processed)
    return output

# 调用
result = main([1, -2, 3, -4, 5])
print(result)  # 2, 6, 10
```

### 4. 易于测试和调试

```python
def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 容易测试
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(17) == True
print("所有测试通过！")
```

### 5. 便于维护

```python
# 需要修改功能时，只需修改函数定义
def calculate_discount(price):
    """计算折扣价格"""
    discount_rate = 0.1  # 10% 折扣
    return price * (1 - discount_rate)

# 如果折扣率变化，只需修改函数内部
def calculate_discount(price, customer_type="normal"):
    """根据客户类型计算折扣"""
    discount_rates = {
        "normal": 0.1,
        "vip": 0.2,
        "svip": 0.3
    }
    rate = discount_rates.get(customer_type, 0)
    return price * (1 - rate)
```

---

## 4.5 函数的参数

### 4.5.1 参数的描述

参数是函数的输入，分为**形式参数（形参）**和**实际参数（实参）**。

- **形参**：函数定义时的参数，是占位符
- **实参**：函数调用时传入的实际值

```python
def greet(name):  # name 是形参
    return f"Hello, {name}!"

greet("Alice")  # "Alice" 是实参
```

### 4.5.2 形参和实参

```python
# 形参：定义时的参数
def add(a, b):  # a, b 是形参
    return a + b

# 实参：调用时的参数
result = add(3, 5)  # 3, 5 是实参

# 形参只在函数内部有效
def multiply(x, y):
    return x * y

# print(x)  # NameError: x 未定义（x 只在函数内有效）

# 实参可以是任何表达式
num1 = 10
num2 = 20
print(add(num1, num2))  # 变量作为实参
print(add(2 + 3, 4 * 5))  # 表达式作为实参
```

### 4.5.3 函数的参数传递

Python 中参数传递是**传递对象引用**（类似于"传引用"）。

```python
# 不可变对象（整数、字符串、元组）：类似"传值"
def modify_number(x):
    x = 100  # 修改局部变量，不影响外部
    print(f"函数内: {x}")

num = 10
modify_number(num)
print(f"函数外: {num}")  # 10（未改变）

# 可变对象（列表、字典、集合）：类似"传引用"
def modify_list(lst):
    lst.append(4)  # 修改列表内容，影响外部
    print(f"函数内: {lst}")

numbers = [1, 2, 3]
modify_list(numbers)
print(f"函数外: {numbers}")  # [1, 2, 3, 4]（已改变）

# 重新赋值不影响外部
def reassign_list(lst):
    lst = [100, 200]  # 重新赋值，不影响外部
    print(f"函数内: {lst}")

numbers = [1, 2, 3]
reassign_list(numbers)
print(f"函数外: {numbers}")  # [1, 2, 3]（未改变）
```

### 4.5.4 函数有哪几种的参数形式

Python 支持多种参数形式：

#### 1. 位置参数（必需参数）

```python
def greet(name, age):
    return f"{name} 今年 {age} 岁"

# 必须按顺序传递
print(greet("Alice", 25))  # Alice 今年 25 岁
# print(greet(25, "Alice"))  # 错误：顺序不对
# print(greet("Alice"))  # TypeError: 缺少参数
```

#### 2. 默认参数（关键字参数）

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!

# 注意：默认参数必须在位置参数之后
# def invalid(a=1, b):  # SyntaxError
#     pass

def valid(a, b=1):  # 正确
    return a + b
```

#### 3. 可变位置参数（*args）

```python
def sum_all(*numbers):
    """接受任意数量的位置参数"""
    return sum(numbers)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# *args 收集为元组
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

print_args(1, 2, 3)  # (1, 2, 3)
```

#### 4. 可变关键字参数（**kwargs）

```python
def print_info(**kwargs):
    """接受任意数量的关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")
# name: Alice
# age: 25
# city: Beijing

# **kwargs 收集为字典
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

show_kwargs(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
```

#### 5. 混合使用参数

```python
def complex_function(a, b, c=3, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

complex_function(1, 2)
# a=1, b=2, c=3
# args=()
# kwargs={}

complex_function(1, 2, 4, 5, 6, x=10, y=20)
# a=1, b=2, c=4
# args=(5, 6)
# kwargs={'x': 10, 'y': 20}
```

**参数顺序规则**：
```python
# 正确的顺序：位置参数 → 默认参数 → *args → **kwargs
def func(a, b, c=3, *args, **kwargs):
    pass

# 错误的顺序
# def func(a, *args, b):  # SyntaxError
#     pass
```

### 4.5.5 解包传参

使用 `*` 和 `**` 可以解包序列和字典作为参数。

```python
# 解包列表/元组
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6（等价于 add(1, 2, 3)）

# 解包字典
def greet(name, age):
    return f"{name} 今年 {age} 岁"

person = {"name": "Alice", "age": 25}
print(greet(**person))  # Alice 今年 25 岁

# 混合使用
def func(a, b, c, d):
    return a + b + c + d

args = [1, 2]
kwargs = {"c": 3, "d": 4}
print(func(*args, **kwargs))  # 10
```

### 4.5.6 强制使用位置参数或关键字参数

Python 3.8+ 支持强制参数传递方式。

```python
# 强制位置参数（/ 之前的参数）
def func1(a, b, /, c):
    return a + b + c

print(func1(1, 2, 3))  # 正确
print(func1(1, 2, c=3))  # 正确
# print(func1(a=1, b=2, c=3))  # TypeError: a, b 必须用位置传递

# 强制关键字参数（* 之后的参数）
def func2(a, *, b, c):
    return a + b + c

print(func2(1, b=2, c=3))  # 正确
# print(func2(1, 2, 3))  # TypeError: b, c 必须用关键字传递

# 混合使用
def func3(a, b, /, c, *, d, e):
    """
    a, b: 仅限位置参数
    c: 位置或关键字参数
    d, e: 仅限关键字参数
    """
    return a + b + c + d + e

print(func3(1, 2, 3, d=4, e=5))  # 15
print(func3(1, 2, c=3, d=4, e=5))  # 15
```

### 4.5.7 防止参数修改副作用

```python
# 问题：可变参数被修改
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]（预期是 [2]）
print(add_item(3))  # [1, 2, 3]（预期是 [3]）

# 解决方案1：使用 None 作为默认值
def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_fixed(1))  # [1]
print(add_item_fixed(2))  # [2]
print(add_item_fixed(3))  # [3]

# 解决方案2：复制参数
def process_list(lst):
    lst = lst.copy()  # 创建副本
    lst.append(100)
    return lst

original = [1, 2, 3]
result = process_list(original)
print(original)  # [1, 2, 3]（未改变）
print(result)    # [1, 2, 3, 100]
```

---

## 4.6 函数说明文档

函数文档字符串（docstring）用于描述函数的功能、参数和返回值。

```python
def calculate_bmi(weight, height):
    """
    计算身体质量指数（BMI）

    参数:
        weight (float): 体重，单位：千克
        height (float): 身高，单位：米

    返回:
        float: BMI 值

    示例:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# 访问文档
print(calculate_bmi.__doc__)
help(calculate_bmi)

# Google 风格的文档字符串
def greet(name, greeting="Hello"):
    """向用户打招呼

    Args:
        name: 用户名称
        greeting: 问候语，默认为 "Hello"

    Returns:
        格式化的问候信息

    Raises:
        TypeError: 如果 name 不是字符串
    """
    if not isinstance(name, str):
        raise TypeError("name 必须是字符串")
    return f"{greeting}, {name}!"

# NumPy 风格的文档字符串
def add(a, b):
    """
    计算两个数的和

    Parameters
    ----------
    a : int or float
        第一个数
    b : int or float
        第二个数

    Returns
    -------
    int or float
        两数之和

    Examples
    --------
    >>> add(2, 3)
    5
    """
    return a + b
```

---

## 4.7 返回值

### 返回单个值

```python
def square(x):
    return x ** 2

result = square(5)
print(result)  # 25
```

### 返回多个值（元组）

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])
print(f"最小: {min_val}, 最大: {max_val}, 平均: {avg}")
```

### 返回列表或字典

```python
def get_even_odd(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    return {"evens": evens, "odds": odds}

result = get_even_odd([1, 2, 3, 4, 5])
print(result)  # {'evens': [2, 4], 'odds': [1, 3, 5]}
```

### 条件返回

```python
def check_sign(number):
    if number > 0:
        return "正数"
    elif number < 0:
        return "负数"
    else:
        return "零"
```

### 无返回值（None）

```python
def print_message(msg):
    print(msg)
    # 没有 return，隐式返回 None

result = print_message("Hello")
print(result)  # None
```

---

## 4.8 函数嵌套调用

函数可以调用其他函数。

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b, c):
    """计算 (a + b) * c"""
    sum_result = add(a, b)
    final_result = multiply(sum_result, c)
    return final_result

print(calculate(2, 3, 4))  # (2 + 3) * 4 = 20

# 实际应用：数据处理管道
def validate_data(data):
    return data is not None and len(data) > 0

def clean_data(data):
    return [x.strip() for x in data if x.strip()]

def process_data(data):
    return [x.upper() for x in data]

def pipeline(raw_data):
    if not validate_data(raw_data):
        return []
    cleaned = clean_data(raw_data)
    processed = process_data(cleaned)
    return processed

data = ["  hello  ", "world", "  ", "python  "]
result = pipeline(data)
print(result)  # ['HELLO', 'WORLD', 'PYTHON']
```

---

## 4.9 变量的作用域

### 4.9.1 全局变量和局部变量

```python
# 全局变量
global_var = 100

def func():
    # 局部变量
    local_var = 50
    print(f"局部变量: {local_var}")
    print(f"全局变量: {global_var}")

func()
print(f"全局变量: {global_var}")
# print(local_var)  # NameError: 局部变量在函数外不可见

# 变量查找顺序：LEGB
# L (Local): 局部作用域
# E (Enclosing): 嵌套函数的外层函数作用域
# G (Global): 全局作用域
# B (Built-in): 内置作用域

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local

    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

### 4.9.2 global 关键字

使用 `global` 在函数内修改全局变量。

```python
count = 0

def increment():
    global count  # 声明使用全局变量
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2

# 不使用 global（错误）
def increment_wrong():
    # count += 1  # UnboundLocalError: 局部变量在赋值前被引用
    pass

# 实际应用：计数器
total = 0

def add_score(score):
    global total
    total += score
    return total

print(add_score(10))  # 10
print(add_score(20))  # 30
print(add_score(15))  # 45
```

### 4.9.3 nonlocal 关键字

使用 `nonlocal` 在嵌套函数中修改外层函数的变量。

```python
def outer():
    x = 10

    def inner():
        nonlocal x  # 声明使用外层函数的变量
        x += 5
        print(f"内层函数: x = {x}")

    inner()
    print(f"外层函数: x = {x}")

outer()
# 内层函数: x = 15
# 外层函数: x = 15

# 实际应用：闭包计数器
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

---

## 4.10 递归

### 4.10.1 概念

递归是函数调用自身的编程技巧。

**递归的两个要素**：
1. **基线条件（Base Case）**：递归终止的条件
2. **递归条件（Recursive Case）**：函数调用自身

### 4.10.2 本质

递归将大问题分解为相似的小问题，直到问题简单到可以直接解决。

```python
# 递归示例：计算阶乘
def factorial(n):
    # 基线条件
    if n == 0 or n == 1:
        return 1
    # 递归条件
    return n * factorial(n - 1)

print(factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120
```

### 4.10.3 在定义递归函数的时候，主要确定两点

1. **确定基线条件**：什么时候停止递归
2. **确定递归关系**：如何将问题分解为子问题

```python
# 示例：斐波那契数列
def fibonacci(n):
    # 基线条件
    if n <= 1:
        return n
    # 递归关系
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
# F(6) = F(5) + F(4) = 5 + 3 = 8
```

### 4.10.4 递归案例，求一个整数 n 的阶乘

```python
def factorial(n):
    """
    计算 n 的阶乘

    n! = n × (n-1)!
    0! = 1
    """
    # 基线条件
    if n == 0 or n == 1:
        return 1

    # 递归条件
    return n * factorial(n - 1)

# 测试
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(10))  # 3628800
```

### 4.10.5 递归执行流程分析

```python
# 计算 factorial(5) 的执行流程
"""
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
"""

# 递归深度限制
import sys
print(sys.getrecursionlimit())  # 默认 1000

# 超过递归深度会报错
# factorial(1001)  # RecursionError

# 可以修改递归深度限制（不推荐）
# sys.setrecursionlimit(2000)

# 更多递归示例
def sum_list(numbers):
    """递归求和"""
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15

def reverse_string(s):
    """递归反转字符串"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # olleh

# 递归 vs 迭代
# 递归实现
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 迭代实现（通常更高效）
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
```

---

## 4.11 匿名函数

### 4.11.1 语法

匿名函数使用 `lambda` 关键字定义。

**语法**：
```python
lambda 参数: 表达式
```

**特点**：
- 只能包含一个表达式
- 不需要 `return`，表达式的结果就是返回值
- 可以有多个参数，但只能有一个表达式
- 通常用于简单的、一次性的函数

### 4.11.2 使用普通函数替代参数

```python
# 普通函数
def square(x):
    return x ** 2

print(square(5))  # 25

# 使用普通函数作为参数
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### 4.11.3 使用匿名函数替代参数

```python
# 匿名函数
square = lambda x: x ** 2
print(square(5))  # 25

# 使用匿名函数作为参数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 常见应用场景
# 1. 排序
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(sorted_students)

# 2. 过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# 3. 映射
words = ["hello", "world", "python"]
upper_words = list(map(lambda s: s.upper(), words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 4.11.4 匿名函数体内只能有有效的参数

```python
# 正确：单个表达式
add = lambda a, b: a + b
print(add(3, 5))  # 8

# 正确：多个参数
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # 24

# 正确：条件表达式
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))  # 20

# 错误：不能包含多条语句
# invalid = lambda x:
#     y = x + 1  # SyntaxError
#     return y

# 错误：不能包含复杂逻辑
# 如果逻辑复杂，应该使用普通函数

# Lambda 的限制
# 1. 只能是单个表达式
# 2. 不能包含语句（如 print、赋值等）
# 3. 不能包含注解
# 4. 不便于调试

# 何时使用 lambda
# 1. 简单的一次性函数
# 2. 作为参数传递给高阶函数
# 3. 函数体只有一行

# 何时使用普通函数
# 1. 复杂的逻辑
# 2. 需要文档字符串
# 3. 需要多次调用
# 4. 需要调试
```

---

## 4.12 函数的注释（了解）

### 类型注解（Type Hints）

Python 3.5+ 支持类型注解，帮助提高代码可读性和类型检查。

```python
# 基本类型注解
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# 复杂类型注解
from typing import List, Dict, Tuple, Optional, Union

def process_numbers(numbers: List[int]) -> Dict[str, int]:
    return {
        "sum": sum(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

def get_user(user_id: int) -> Optional[Dict[str, str]]:
    """返回用户信息，如果不存在返回 None"""
    # ...
    return None

def convert(value: Union[int, str]) -> str:
    """接受整数或字符串，返回字符串"""
    return str(value)

# 函数类型注解
from typing import Callable

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    """
    应用操作函数到两个数

    Args:
        x: 第一个数
        y: 第二个数
        op: 操作函数，接受两个 int，返回 int
    """
    return op(x, y)

result = apply_operation(10, 5, lambda a, b: a + b)
print(result)  # 15

# 注意：类型注解不强制类型检查
# Python 仍然是动态类型语言
# 类型注解主要用于：
# 1. 提高代码可读性
# 2. IDE 自动补全
# 3. 使用 mypy 等工具进行静态类型检查
```

---

## 综合示例

### 示例 1：学生成绩管理

```python
def add_student(students: Dict[str, Dict], name: str, score: int) -> None:
    """添加学生"""
    students[name] = {"score": score}

def get_average(students: Dict[str, Dict]) -> float:
    """计算平均分"""
    if not students:
        return 0
    total = sum(s["score"] for s in students.values())
    return total / len(students)

def get_top_students(students: Dict[str, Dict], n: int = 3) -> List[Tuple[str, int]]:
    """获取前 n 名学生"""
    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )
    return [(name, info["score"]) for name, info in sorted_students[:n]]

# 使用
students = {}
add_student(students, "Alice", 85)
add_student(students, "Bob", 92)
add_student(students, "Charlie", 78)
add_student(students, "David", 95)

print(f"平均分: {get_average(students):.2f}")
print(f"前 3 名: {get_top_students(students)}")
```

### 示例 2：递归遍历目录

```python
import os

def list_files(path: str, indent: int = 0) -> None:
    """递归列出目录中的所有文件"""
    try:
        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            print("  " * indent + item)
            if os.path.isdir(full_path):
                list_files(full_path, indent + 1)
    except PermissionError:
        print("  " * indent + "[无权限访问]")

# list_files(".")
```

### 示例 3：装饰器函数

```python
def timer(func):
    """计时装饰器"""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result

    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "完成"

# slow_function()  # slow_function 耗时: 1.0001 秒
```

---

## 总结

本章介绍了 Python 函数的核心概念：

1. **函数的概念**：代码复用、模块化的基本单元
2. **函数定义**：语法、参数、函数体、返回值
3. **函数调用**：先定义后调用、参数匹配
4. **参数类型**：位置参数、默认参数、*args、**kwargs
5. **参数传递**：传递对象引用、解包传参
6. **作用域**：局部变量、全局变量、global、nonlocal
7. **递归**：基线条件、递归关系
8. **匿名函数**：lambda 表达式
9. **文档和注解**：docstring、类型注解

掌握函数是编写高质量 Python 代码的关键。

---

## 练习题

1. 编写函数，判断一个数是否为质数
2. 编写函数，计算列表中所有偶数的和
3. 使用递归实现二分查找算法
4. 编写函数，接受任意数量的参数，返回最大值和最小值
5. 实现一个简单的计算器函数，支持加减乘除
6. 编写递归函数，计算斐波那契数列的第 n 项
7. 使用 lambda 函数对字典列表进行排序
8. 编写装饰器函数，记录函数的调用次数
