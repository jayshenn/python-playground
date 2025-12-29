# 第 10 章 Python 高级语法

本章将介绍 Python 的高级特性，包括浅拷贝与深拷贝、迭代器、生成器、命名空间、作用域、闭包和装饰器。这些特性能够帮助我们编写更加优雅、高效的代码。

---

## 10.1 浅拷贝与深拷贝

在 Python 中，拷贝对象有两种方式：**浅拷贝**（Shallow Copy）和**深拷贝**（Deep Copy）。理解它们的区别对于处理可变对象非常重要。

### 10.1.1 回顾浅拷贝

**浅拷贝**创建一个新对象，但只复制对象的第一层，嵌套对象仍然是引用。

**创建浅拷贝的方法**：

```python
import copy

# 方法 1：使用切片（列表）
list1 = [1, 2, 3, 4, 5]
list2 = list1[:]
print(list1 is list2)  # False（不同对象）

# 方法 2：使用 list() 构造函数
list3 = list(list1)
print(list1 is list3)  # False

# 方法 3：使用 copy.copy()
list4 = copy.copy(list1)
print(list1 is list4)  # False

# 方法 4：使用 .copy() 方法
dict1 = {'a': 1, 'b': 2}
dict2 = dict1.copy()
print(dict1 is dict2)  # False
```

### 10.1.2 案例

**浅拷贝的问题：嵌套对象是引用**

```python
import copy

# 包含嵌套列表的情况
original = [1, 2, [3, 4, 5]]

# 浅拷贝
shallow = copy.copy(original)
# 或 shallow = original[:]
# 或 shallow = original.copy()

print(f"原始列表: {original}")
print(f"浅拷贝: {shallow}")
print(f"是同一个对象吗? {original is shallow}")  # False

# 修改第一层元素
shallow[0] = 100
print(f"修改后原始列表: {original}")  # [1, 2, [3, 4, 5]]
print(f"修改后浅拷贝: {shallow}")    # [100, 2, [3, 4, 5]]

# 修改嵌套列表（问题出现）
shallow[2][0] = 999
print(f"修改嵌套后原始列表: {original}")  # [1, 2, [999, 4, 5]]（被影响）
print(f"修改嵌套后浅拷贝: {shallow}")    # [100, 2, [999, 4, 5]]

# 验证嵌套列表是同一个对象
print(f"嵌套列表是同一个对象吗? {original[2] is shallow[2]}")  # True
```

**浅拷贝的特点**：
- 创建新的外层对象
- 嵌套对象仍然是引用（共享）
- 修改嵌套对象会影响原对象

### 10.1.3 回顾深拷贝

**深拷贝**创建一个完全独立的副本，包括所有嵌套对象。

```python
import copy

original = [1, 2, [3, 4, 5]]

# 深拷贝
deep = copy.deepcopy(original)

print(f"原始列表: {original}")
print(f"深拷贝: {deep}")
print(f"是同一个对象吗? {original is deep}")  # False

# 修改第一层元素
deep[0] = 100
print(f"修改后原始列表: {original}")  # [1, 2, [3, 4, 5]]
print(f"修改后深拷贝: {deep}")       # [100, 2, [3, 4, 5]]

# 修改嵌套列表（不影响原对象）
deep[2][0] = 999
print(f"修改嵌套后原始列表: {original}")  # [1, 2, [3, 4, 5]]（不受影响）
print(f"修改嵌套后深拷贝: {deep}")       # [100, 2, [999, 4, 5]]

# 验证嵌套列表是不同的对象
print(f"嵌套列表是同一个对象吗? {original[2] is deep[2]}")  # False
```

### 10.1.4 案例

**复杂嵌套结构的深拷贝**

```python
import copy

# 复杂的嵌套结构
original = {
    'name': 'Alice',
    'age': 25,
    'scores': [85, 90, 92],
    'address': {
        'city': 'Beijing',
        'street': ['Street A', 'Street B']
    }
}

# 浅拷贝
shallow = copy.copy(original)

# 深拷贝
deep = copy.deepcopy(original)

# 修改嵌套数据
shallow['scores'][0] = 100
deep['address']['city'] = 'Shanghai'

print("原始数据:")
print(original)
# {'name': 'Alice', 'age': 25, 'scores': [100, 90, 92], ...}
# scores 被浅拷贝影响

print("\n浅拷贝:")
print(shallow)

print("\n深拷贝:")
print(deep)
# address.city = 'Shanghai'，不影响原始数据
```

**自定义类的深拷贝**

```python
import copy

class Person:
    def __init__(self, name, age, friends=None):
        self.name = name
        self.age = age
        self.friends = friends or []

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, friends={self.friends})"

# 创建对象
alice = Person('Alice', 25, ['Bob', 'Charlie'])
bob = Person('Bob', 30)

alice.friends.append(bob)

# 浅拷贝
alice_shallow = copy.copy(alice)
alice_shallow.age = 26  # 修改简单属性
alice_shallow.friends[0] = 'David'  # 修改嵌套对象

print(f"原始对象: {alice}")
print(f"浅拷贝: {alice_shallow}")
# friends 列表被共享

# 深拷贝
alice_deep = copy.deepcopy(alice)
alice_deep.friends[0] = 'Eve'

print(f"\n原始对象: {alice}")
print(f"深拷贝: {alice_deep}")
# friends 列表完全独立
```

### 10.1.5 理想的转换情况

**何时使用浅拷贝？**
- 只需要复制第一层数据
- 嵌套对象可以共享
- 性能要求高（浅拷贝更快）

**何时使用深拷贝？**
- 需要完全独立的副本
- 嵌套对象不能共享
- 避免意外修改原数据

**对比总结**：

| 特性 | 浅拷贝 | 深拷贝 |
|------|--------|--------|
| **第一层对象** | 新对象 | 新对象 |
| **嵌套对象** | 引用（共享） | 新对象（独立） |
| **性能** | 快 | 慢 |
| **内存占用** | 少 | 多 |
| **使用场景** | 简单数据、性能要求高 | 复杂嵌套、需要独立副本 |

```python
import copy

# 性能对比
import time

data = [[1, 2, 3] for _ in range(1000)]

# 浅拷贝性能
start = time.time()
for _ in range(1000):
    shallow = copy.copy(data)
shallow_time = time.time() - start

# 深拷贝性能
start = time.time()
for _ in range(1000):
    deep = copy.deepcopy(data)
deep_time = time.time() - start

print(f"浅拷贝时间: {shallow_time:.4f} 秒")
print(f"深拷贝时间: {deep_time:.4f} 秒")
print(f"深拷贝比浅拷贝慢 {deep_time / shallow_time:.2f} 倍")
```

---

## 10.2 迭代器

**迭代器**（Iterator）是一个可以记住遍历位置的对象，用于逐个访问集合中的元素。

### 10.2.1 可迭代对象

**可迭代对象**（Iterable）是实现了 `__iter__()` 方法的对象。

```python
# 常见的可迭代对象
list_obj = [1, 2, 3, 4, 5]
tuple_obj = (1, 2, 3)
str_obj = "Hello"
dict_obj = {'a': 1, 'b': 2}
set_obj = {1, 2, 3}

# 判断是否为可迭代对象
from collections.abc import Iterable

print(isinstance(list_obj, Iterable))   # True
print(isinstance(tuple_obj, Iterable))  # True
print(isinstance(str_obj, Iterable))    # True
print(isinstance(dict_obj, Iterable))   # True
print(isinstance(123, Iterable))        # False
```

**可迭代对象 vs 迭代器**：

```python
# 可迭代对象
my_list = [1, 2, 3]

# 获取迭代器
my_iter = iter(my_list)  # 或 my_list.__iter__()

print(type(my_list))  # <class 'list'>（可迭代对象）
print(type(my_iter))  # <class 'list_iterator'>（迭代器）

# 迭代器是可迭代对象，但可迭代对象不一定是迭代器
from collections.abc import Iterator

print(isinstance(my_list, Iterable))   # True
print(isinstance(my_list, Iterator))   # False

print(isinstance(my_iter, Iterable))   # True
print(isinstance(my_iter, Iterator))   # True
```

### 10.2.2 使用迭代器

**使用 `iter()` 和 `next()`**：

```python
# 创建迭代器
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# 使用 next() 获取元素
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
print(next(my_iter))  # 5

# 迭代器耗尽后会抛出 StopIteration
try:
    print(next(my_iter))
except StopIteration:
    print("迭代器已耗尽")
```

**for 循环的本质**：

```python
# for 循环自动处理迭代器
my_list = [1, 2, 3, 4, 5]

# 实际上 for 循环做了这些事：
# 1. 调用 iter() 获取迭代器
# 2. 循环调用 next()
# 3. 捕获 StopIteration 异常

# 等价的手动实现
my_iter = iter(my_list)
while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break
```

**迭代器的特点**：

```python
my_list = [1, 2, 3]
my_iter = iter(my_list)

# 1. 迭代器只能前进，不能后退
print(next(my_iter))  # 1
print(next(my_iter))  # 2
# 无法回到 1

# 2. 迭代器是一次性的
for item in my_iter:
    print(item)  # 只会打印 3

# 再次迭代，什么也不输出
for item in my_iter:
    print(item)  # 无输出

# 3. 节省内存（惰性求值）
import sys

my_list = list(range(1000000))
my_iter = iter(my_list)

print(f"列表大小: {sys.getsizeof(my_list)} 字节")
print(f"迭代器大小: {sys.getsizeof(my_iter)} 字节")
```

### 10.2.3 自定义迭代器

**实现迭代器协议**：

实现 `__iter__()` 和 `__next__()` 方法。

```python
class MyRange:
    """自定义的 range 迭代器"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """返回迭代器对象本身"""
        return self

    def __next__(self):
        """返回下一个值"""
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# 使用自定义迭代器
my_range = MyRange(1, 5)

for num in my_range:
    print(num)  # 1 2 3 4

# 手动使用
my_range2 = MyRange(10, 13)
print(next(my_range2))  # 10
print(next(my_range2))  # 11
print(next(my_range2))  # 12
# print(next(my_range2))  # StopIteration
```

**斐波那契数列迭代器**：

```python
class Fibonacci:
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """生成前 n 个斐波那契数"""
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            if self.current == 1:
                return self.a
            elif self.current == 2:
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                return self.b
        else:
            raise StopIteration

# 使用
fib = Fibonacci(10)
for num in fib:
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34
```

**可迭代对象（容器类）**：

```python
class MyList:
    """自定义的可迭代列表"""

    def __init__(self):
        self.items = []

    def add(self, item):
        """添加元素"""
        self.items.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        return MyListIterator(self.items)

class MyListIterator:
    """MyList 的迭代器"""

    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            value = self.items[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# 使用
my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

for item in my_list:
    print(item)  # 1 2 3

# 可以多次迭代
for item in my_list:
    print(item)  # 1 2 3
```

---

## 10.3 生成器

**生成器**（Generator）是一种特殊的迭代器，使用更简洁的语法创建。

### 10.3.1 什么是生成器

生成器是使用 `yield` 关键字的函数，每次产生一个值。

**生成器的优点**：
- 语法简洁（相比自定义迭代器）
- 节省内存（惰性求值）
- 状态自动保存

```python
# 普通函数 vs 生成器函数
def normal_function():
    """普通函数：一次返回所有值"""
    result = []
    for i in range(5):
        result.append(i)
    return result

def generator_function():
    """生成器函数：每次产生一个值"""
    for i in range(5):
        yield i

# 使用普通函数
print(normal_function())  # [0, 1, 2, 3, 4]

# 使用生成器
gen = generator_function()
print(gen)  # <generator object>
print(list(gen))  # [0, 1, 2, 3, 4]
```

### 10.3.2 创建生成器

**方法 1：生成器函数**

```python
def count_up_to(n):
    """生成 0 到 n-1 的数字"""
    count = 0
    while count < n:
        yield count
        count += 1

# 使用生成器
gen = count_up_to(5)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# 或使用 for 循环
for num in count_up_to(5):
    print(num)  # 0 1 2 3 4
```

**方法 2：生成器表达式**

```python
# 列表推导式
list_comp = [x ** 2 for x in range(5)]
print(list_comp)  # [0, 1, 4, 9, 16]

# 生成器表达式（使用圆括号）
gen_exp = (x ** 2 for x in range(5))
print(gen_exp)  # <generator object>

# 逐个获取值
print(next(gen_exp))  # 0
print(next(gen_exp))  # 1

# 或转换为列表
gen_exp2 = (x ** 2 for x in range(5))
print(list(gen_exp2))  # [0, 1, 4, 9, 16]
```

**生成器的应用**：

```python
# 1. 斐波那契数列生成器
def fibonacci(n):
    """生成前 n 个斐波那契数"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(10):
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34

# 2. 读取大文件
def read_large_file(file_path):
    """逐行读取大文件"""
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# for line in read_large_file('large.txt'):
#     process(line)

# 3. 无限序列
def infinite_sequence():
    """生成无限序列"""
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

**生成器的状态保存**：

```python
def demo_generator():
    """演示生成器状态保存"""
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("再继续")
    yield 3
    print("结束")

gen = demo_generator()

print("第一次 next:")
print(next(gen))  # 开始 -> 1

print("\n第二次 next:")
print(next(gen))  # 继续 -> 2

print("\n第三次 next:")
print(next(gen))  # 再继续 -> 3

print("\n第四次 next:")
try:
    print(next(gen))  # 结束 -> StopIteration
except StopIteration:
    print("生成器已耗尽")
```

### 10.3.3 send()

`send()` 方法可以向生成器发送值，并恢复执行。

```python
def echo_generator():
    """接收并回显值的生成器"""
    print("生成器启动")

    while True:
        # 接收通过 send() 发送的值
        value = yield
        if value is not None:
            print(f"接收到: {value}")

gen = echo_generator()

# 必须先启动生成器
next(gen)  # 或 gen.send(None)

# 发送值
gen.send('Hello')    # 接收到: Hello
gen.send('World')    # 接收到: World
gen.send(123)        # 接收到: 123
```

**send() 的高级用法**：

```python
def running_average():
    """计算移动平均值"""
    total = 0
    count = 0

    while True:
        value = yield total / count if count > 0 else 0
        total += value
        count += 1

avg_gen = running_average()
next(avg_gen)  # 启动生成器

print(avg_gen.send(10))   # 10.0
print(avg_gen.send(20))   # 15.0
print(avg_gen.send(30))   # 20.0
print(avg_gen.send(40))   # 25.0
```

**生成器的双向通信**：

```python
def two_way_generator():
    """双向通信的生成器"""
    print("生成器准备就绪")

    received = yield "准备接收"

    while True:
        print(f"收到: {received}")
        received = yield f"处理了 {received}"

gen = two_way_generator()

# 启动
print(next(gen))  # 准备接收

# 发送并接收
print(gen.send("数据1"))  # 收到: 数据1 -> 处理了 数据1
print(gen.send("数据2"))  # 收到: 数据2 -> 处理了 数据2
```

---

## 10.4 命名空间

**命名空间**（Namespace）是名称到对象的映射，用于避免命名冲突。

### 10.4.1 什么是命名空间

命名空间是存储变量名和对象映射关系的字典。

```python
# 查看命名空间
x = 10
y = 20

# locals()：查看局部命名空间
print(locals())

# globals()：查看全局命名空间
print(globals())

# 命名空间是字典
print(type(locals()))  # <class 'dict'>
```

**命名空间的作用**：

```python
# 避免命名冲突
def function1():
    x = 10
    print(f"function1 中的 x: {x}")

def function2():
    x = 20
    print(f"function2 中的 x: {x}")

function1()  # function1 中的 x: 10
function2()  # function2 中的 x: 20

# 两个函数的 x 互不影响（不同的命名空间）
```

### 10.4.2 三种命名空间

Python 有三种命名空间：

**1. 内置命名空间（Built-in）**
- Python 启动时创建
- 包含内置函数和异常
- 一直存在，直到解释器退出

```python
# 查看内置命名空间
import builtins
print(dir(builtins))

# 内置函数示例
print(len([1, 2, 3]))  # len 在内置命名空间
print(max([1, 2, 3]))  # max 在内置命名空间
```

**2. 全局命名空间（Global）**
- 模块被导入时创建
- 包含模块级别的变量和函数
- 模块存在期间一直存在

```python
# 全局变量
global_var = "我是全局变量"

def my_function():
    print(global_var)  # 可以访问全局变量

my_function()

# 查看全局命名空间
print('global_var' in globals())  # True
```

**3. 局部命名空间（Local）**
- 函数被调用时创建
- 包含函数的参数和局部变量
- 函数返回时销毁

```python
def my_function(param):
    local_var = "我是局部变量"
    print(locals())  # {'param': ..., 'local_var': ...}

my_function("参数值")

# 函数外无法访问局部变量
# print(local_var)  # NameError
```

**命名空间的生命周期**：

```python
# 内置命名空间
print(len)  # 始终可用

# 全局命名空间
global_var = 100

def outer():
    # 外层函数的局部命名空间
    outer_var = 200

    def inner():
        # 内层函数的局部命名空间
        inner_var = 300
        print(f"可以访问: {global_var}, {outer_var}, {inner_var}")

    inner()
    # print(inner_var)  # NameError：inner_var 已销毁

outer()
# print(outer_var)  # NameError：outer_var 已销毁
```

---

## 10.5 作用域

**作用域**（Scope）是程序中变量可访问的范围。

### 10.5.1 什么是作用域

作用域决定了在代码的哪些部分可以访问某个变量。

```python
x = "global"

def outer():
    y = "outer"

    def inner():
        z = "inner"
        print(f"inner 可以访问: {x}, {y}, {z}")

    inner()
    print(f"outer 可以访问: {x}, {y}")
    # print(z)  # NameError：z 不在 outer 作用域

outer()
print(f"global 可以访问: {x}")
# print(y)  # NameError：y 不在全局作用域
```

### 10.5.2 四种作用域（LEGB 规则）

Python 按照 **LEGB** 顺序查找变量：

**L（Local）**：局部作用域
- 函数内部定义的变量

**E（Enclosing）**：嵌套作用域
- 外层函数的局部作用域

**G（Global）**：全局作用域
- 模块级别的变量

**B（Built-in）**：内置作用域
- Python 内置的名称

```python
# B（Built-in）
print(len)  # 内置函数

# G（Global）
x = "global x"

def outer():
    # E（Enclosing）
    x = "enclosing x"

    def inner():
        # L（Local）
        x = "local x"
        print(x)  # local x（优先使用局部）

    inner()
    print(x)  # enclosing x

outer()
print(x)  # global x
```

**LEGB 查找顺序示例**：

```python
x = "global"

def test():
    # x = "local"  # 如果注释掉，会向上查找

    def inner():
        print(x)  # 按 LEGB 顺序查找

    inner()

test()  # global（如果 test 中没有 x，使用全局的）
```

**global 关键字**：

```python
count = 0

def increment():
    global count  # 声明使用全局变量
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2
```

**nonlocal 关键字**：

```python
def outer():
    count = 0

    def inner():
        nonlocal count  # 声明使用外层函数的变量
        count += 1
        print(f"inner: count = {count}")

    inner()  # inner: count = 1
    inner()  # inner: count = 2
    print(f"outer: count = {count}")  # outer: count = 2

outer()
```

**作用域陷阱**：

```python
# 陷阱 1：后期绑定
funcs = []
for i in range(3):
    funcs.append(lambda: i)  # i 是后期绑定

for func in funcs:
    print(func())  # 2 2 2（都是最后的 i 值）

# 解决方案：立即绑定
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)  # 使用默认参数立即绑定

for func in funcs:
    print(func())  # 0 1 2

# 陷阱 2：global 的影响
x = 10

def modify():
    global x
    x = 20  # 修改全局变量

modify()
print(x)  # 20（全局变量被修改）
```

---

## 10.6 闭包

**闭包**（Closure）是一个函数以及其相关的引用环境的组合。

### 10.6.1 什么是闭包

闭包是指：
1. 嵌套函数
2. 内层函数引用外层函数的变量
3. 外层函数返回内层函数

```python
def outer(x):
    """外层函数"""
    def inner(y):
        """内层函数（闭包）"""
        return x + y  # 引用外层函数的 x
    return inner

# 创建闭包
closure = outer(10)
print(closure(5))   # 15
print(closure(20))  # 30

# closure 记住了 x=10
```

**闭包的特点**：

```python
def make_counter():
    """计数器闭包"""
    count = 0  # 自由变量

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# 创建两个独立的计数器
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 1（独立的计数器）
print(counter2())  # 2
```

### 10.6.2 使用闭包

**示例 1：记住配置**

```python
def make_multiplier(factor):
    """创建乘法器"""
    def multiply(x):
        return x * factor
    return multiply

# 创建不同的乘法器
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

**示例 2：数据隐藏**

```python
def create_account(initial_balance):
    """创建银行账户（使用闭包隐藏余额）"""
    balance = initial_balance  # 私有变量

    def deposit(amount):
        """存款"""
        nonlocal balance
        if amount > 0:
            balance += amount
            return balance
        return None

    def withdraw(amount):
        """取款"""
        nonlocal balance
        if 0 < amount <= balance:
            balance -= amount
            return balance
        return None

    def get_balance():
        """查询余额"""
        return balance

    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'get_balance': get_balance
    }

# 使用
account = create_account(1000)
print(account['get_balance']())  # 1000
account['deposit'](500)
print(account['get_balance']())  # 1500
account['withdraw'](200)
print(account['get_balance']())  # 1300

# 无法直接访问 balance
```

**示例 3：延迟计算**

```python
def lazy_sum(*args):
    """延迟求和"""
    def calculate():
        return sum(args)
    return calculate

# 创建闭包（不立即计算）
f = lazy_sum(1, 2, 3, 4, 5)
print(f)  # <function>

# 需要时才计算
print(f())  # 15
```

### 10.6.3 查看闭包中的值

使用 `__closure__` 属性查看闭包捕获的变量。

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)

# 查看闭包
print(closure.__closure__)  # (<cell at 0x...: int object at 0x...>,)

# 查看闭包中的值
if closure.__closure__:
    for cell in closure.__closure__:
        print(cell.cell_contents)  # 10

# 查看闭包函数的自由变量名
print(closure.__code__.co_freevars)  # ('x',)
```

**复杂闭包示例**：

```python
def create_functions():
    """创建多个闭包函数"""
    functions = []

    for i in range(3):
        def func(x, val=i):  # 使用默认参数捕获值
            return x + val
        functions.append(func)

    return functions

funcs = create_functions()
print(funcs[0](10))  # 10
print(funcs[1](10))  # 11
print(funcs[2](10))  # 12
```

---

## 10.7 装饰器

**装饰器**（Decorator）是一个返回函数的函数，用于在不修改原函数代码的情况下增强函数功能。

### 10.7.1 什么是装饰器

装饰器本质是一个闭包，用于包装另一个函数。

```python
# 不使用装饰器
def say_hello():
    print("Hello!")

def wrapper(func):
    def inner():
        print("函数执行前")
        func()
        print("函数执行后")
    return inner

say_hello = wrapper(say_hello)
say_hello()
# 函数执行前
# Hello!
# 函数执行后

# 使用装饰器（语法糖）
def wrapper(func):
    def inner():
        print("函数执行前")
        func()
        print("函数执行后")
    return inner

@wrapper  # 等价于 say_hello = wrapper(say_hello)
def say_hello():
    print("Hello!")

say_hello()
```

### 10.7.2 函数装饰器

**基本装饰器**：

```python
def my_decorator(func):
    """简单的装饰器"""
    def wrapper():
        print("--- 装饰器开始 ---")
        func()
        print("--- 装饰器结束 ---")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()
# --- 装饰器开始 ---
# Hello, World!
# --- 装饰器结束 ---
```

**带参数的函数装饰器**：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 5)
# 调用函数: add
# 参数: args=(3, 5), kwargs={}
# 返回值: 8
```

**保留函数元信息**：

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        """wrapper 的文档"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """向某人打招呼"""
    return f"Hello, {name}!"

print(greet.__name__)  # greet（而不是 wrapper）
print(greet.__doc__)   # 向某人打招呼
```

**实用装饰器示例**：

```python
import time
from functools import wraps

# 1. 计时装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"

result = slow_function()

# 2. 日志装饰器
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回 {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

# 3. 缓存装饰器
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 快速计算（使用缓存）
```

### 10.7.3 多层装饰器

可以对一个函数应用多个装饰器。

```python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello!")

greet()
# Decorator 1
# Decorator 2
# Hello!

# 等价于：greet = decorator1(decorator2(greet))
```

**装饰器执行顺序**：

```python
def dec1(func):
    print("执行 dec1")
    def wrapper():
        print("dec1 before")
        func()
        print("dec1 after")
    return wrapper

def dec2(func):
    print("执行 dec2")
    def wrapper():
        print("dec2 before")
        func()
        print("dec2 after")
    return wrapper

@dec1
@dec2
def test():
    print("test 函数")

# 输出（定义时）：
# 执行 dec2
# 执行 dec1

print("\n调用函数:")
test()
# dec1 before
# dec2 before
# test 函数
# dec2 after
# dec1 after
```

### 10.7.4 带参数的装饰器

装饰器本身也可以接受参数。

```python
def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

**带参数装饰器的结构**：

```python
def decorator_with_args(arg1, arg2):
    """带参数的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"装饰器参数: {arg1}, {arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args("参数1", "参数2")
def test():
    print("test 函数")

test()
# 装饰器参数: 参数1, 参数2
# test 函数
```

**实用示例：权限检查装饰器**：

```python
def require_role(role):
    """要求特定角色才能执行"""
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') == role:
                return func(user, *args, **kwargs)
            else:
                raise PermissionError(f"需要 {role} 权限")
        return wrapper
    return decorator

@require_role('admin')
def delete_user(user, user_id):
    print(f"删除用户 {user_id}")

# 测试
admin_user = {'name': 'Alice', 'role': 'admin'}
normal_user = {'name': 'Bob', 'role': 'user'}

delete_user(admin_user, 123)  # 成功
try:
    delete_user(normal_user, 456)  # PermissionError
except PermissionError as e:
    print(e)
```

### 10.7.5 类装饰器

使用类实现装饰器。

```python
class Counter:
    """计数装饰器"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@Counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # greet 被调用了 1 次
greet("Bob")    # greet 被调用了 2 次
greet("Charlie")  # greet 被调用了 3 次
```

**带参数的类装饰器**：

```python
class Repeat:
    """重复执行装饰器（类实现）"""

    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!
# Hello!
```

**完整的类装饰器示例**：

```python
class Logger:
    """日志装饰器（类实现）"""

    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{self.level}] 调用 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{self.level}] {func.__name__} 返回 {result}")
            return result
        return wrapper

@Logger(level='DEBUG')
def add(a, b):
    return a + b

add(3, 5)
# [DEBUG] 调用 add
# [DEBUG] add 返回 8
```

---

## 综合示例

### 示例 1：完整的装饰器系统

```python
from functools import wraps
import time

def timer(func):
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时 {end - start:.4f} 秒")
        return result
    return wrapper

def logger(func):
    """日志装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回 {result}")
        return result
    return wrapper

def validate(func):
    """参数验证装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(x, (int, float)) for x in args):
            raise TypeError("所有参数必须是数字")
        return func(*args, **kwargs)
    return wrapper

@timer
@logger
@validate
def calculate(a, b, c):
    """复杂计算"""
    time.sleep(0.1)  # 模拟耗时操作
    return (a + b) * c

# 使用
result = calculate(10, 20, 3)
```

### 示例 2：迭代器和生成器的应用

```python
class DataStream:
    """数据流处理（迭代器）"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

def process_stream(stream):
    """使用生成器处理数据流"""
    for item in stream:
        if item > 0:
            yield item * 2

# 使用
data = [1, -2, 3, -4, 5, -6, 7]
stream = DataStream(data)
processed = process_stream(stream)

for value in processed:
    print(value)  # 2, 6, 10, 14
```

---

## 总结

本章介绍了 Python 的高级语法特性：

### 10.1 浅拷贝与深拷贝
- **浅拷贝**：复制第一层，嵌套对象共享
- **深拷贝**：完全独立的副本

### 10.2 迭代器
- **可迭代对象**：实现 `__iter__()`
- **迭代器**：实现 `__iter__()` 和 `__next__()`
- **自定义迭代器**：创建自己的迭代逻辑

### 10.3 生成器
- **生成器函数**：使用 `yield`
- **生成器表达式**：惰性求值
- **send()**：双向通信

### 10.4 命名空间
- **内置**、**全局**、**局部**三种命名空间

### 10.5 作用域
- **LEGB** 规则：Local → Enclosing → Global → Built-in

### 10.6 闭包
- **定义**：内层函数 + 外层变量
- **应用**：数据隐藏、延迟计算

### 10.7 装饰器
- **函数装饰器**：增强函数功能
- **类装饰器**：使用类实现
- **带参数装饰器**：更灵活的配置

掌握这些高级特性是编写优雅 Python 代码的关键。

---

## 练习题

1. 实现一个深拷贝函数，处理嵌套的字典和列表
2. 创建一个迭代器，生成质数序列
3. 使用生成器实现文件逐行读取（节省内存）
4. 编写一个装饰器，限制函数的调用次数
5. 实现一个缓存装饰器，优化递归函数性能
6. 创建一个闭包，实现简单的状态机
7. 使用生成器实现无限的斐波那契数列
8. 编写一个装饰器类，实现函数调用统计
