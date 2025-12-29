# 第 6 章 面向对象编程之类和对象

## 6.1 面向过程和面向对象

### 6.1.1 面向过程编程（Procedure Oriented Programming, POP）

面向过程是一种以**过程为中心**的编程思想，将问题分解为一系列步骤（函数），按顺序执行。

**特点**：
- 关注"怎么做"（How）
- 强调过程和步骤
- 使用函数来组织代码
- 数据和操作分离

**优点**：
- 简单直观，适合小型程序
- 性能高，执行效率好
- 易于理解和入门

**缺点**：
- 代码复用性差
- 维护困难
- 扩展性差
- 不适合大型项目

```python
# 面向过程示例：学生成绩管理
students = []

def add_student(name, score):
    """添加学生"""
    students.append({'name': name, 'score': score})

def get_average():
    """计算平均分"""
    if not students:
        return 0
    total = sum(s['score'] for s in students)
    return total / len(students)

def print_students():
    """打印所有学生"""
    for student in students:
        print(f"{student['name']}: {student['score']}")

# 使用
add_student('Alice', 85)
add_student('Bob', 92)
print_students()
print(f"平均分: {get_average()}")
```

### 6.1.2 面向对象编程（Object Oriented Programming, OOP）

面向对象是一种以**对象为中心**的编程思想，将数据和操作封装在对象中。

**特点**：
- 关注"是什么"（What）
- 强调对象和类
- 数据和操作封装在一起
- 符合人类的思维方式

**优点**：
- 代码复用性强
- 易于维护和扩展
- 适合大型项目
- 更接近现实世界的建模

**缺点**：
- 学习曲线陡峭
- 性能可能略低于面向过程
- 小型程序可能过度设计

```python
# 面向对象示例：学生成绩管理
class Student:
    """学生类"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        """获取等级"""
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return f"{self.name}: {self.score} ({self.get_grade()})"

class StudentManager:
    """学生管理类"""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """添加学生"""
        self.students.append(student)

    def get_average(self):
        """计算平均分"""
        if not self.students:
            return 0
        total = sum(s.score for s in self.students)
        return total / len(self.students)

    def print_students(self):
        """打印所有学生"""
        for student in self.students:
            print(student)

# 使用
manager = StudentManager()
manager.add_student(Student('Alice', 85))
manager.add_student(Student('Bob', 92))
manager.print_students()
print(f"平均分: {manager.get_average():.2f}")
```

### 6.1.3 对比总结

| 特性 | 面向过程 | 面向对象 |
|------|---------|---------|
| **核心** | 函数 | 对象 |
| **关注点** | 怎么做（过程） | 是什么（对象） |
| **数据和操作** | 分离 | 封装在一起 |
| **代码复用** | 函数复用 | 继承和多态 |
| **扩展性** | 差 | 好 |
| **维护性** | 难 | 易 |
| **适用场景** | 小型程序 | 大型项目 |

---

## 6.2 类和对象

### 6.2.1 类（Class）

**类**是对象的模板或蓝图，定义了对象的属性和方法。

**类的概念**：
- 类是抽象的概念，是对一类事物的描述
- 类定义了对象应该具有的属性和行为
- 类是创建对象的模板

**类比**：
- 汽车设计图 → 类
- 具体的汽车 → 对象

```python
# 类的定义
class Dog:
    """狗类"""

    def __init__(self, name, age):
        self.name = name  # 属性
        self.age = age

    def bark(self):  # 方法
        print(f"{self.name} 在汪汪叫！")

    def get_info(self):
        return f"{self.name} 今年 {self.age} 岁"
```

### 6.2.2 对象（Object）

**对象**是类的实例，是具体存在的事物。

**对象的概念**：
- 对象是具体的实体
- 对象是类的实例化结果
- 每个对象都有自己的属性值

```python
# 创建对象（实例化）
dog1 = Dog('旺财', 3)
dog2 = Dog('大黄', 5)

# 访问属性
print(dog1.name)  # 旺财
print(dog2.age)   # 5

# 调用方法
dog1.bark()  # 旺财 在汪汪叫！
print(dog2.get_info())  # 大黄 今年 5 岁
```

**类与对象的关系**：
```python
# 类是模板，对象是实例
class Person:
    pass

# 创建多个对象
person1 = Person()  # 第一个实例
person2 = Person()  # 第二个实例
person3 = Person()  # 第三个实例

# 每个对象都是独立的
print(person1 is person2)  # False
print(type(person1))       # <class '__main__.Person'>
```

---

## 6.3 定义类

### 6.3.1 基本语法

```python
class 类名:
    """类的文档字符串"""

    # 类属性
    类属性 = 值

    def __init__(self, 参数):
        """构造方法"""
        self.实例属性 = 参数

    def 方法名(self, 参数):
        """实例方法"""
        方法体
```

### 6.3.2 命名规范

**类名命名规则**（PEP 8）：
- 使用大驼峰命名法（CapWords）
- 每个单词首字母大写
- 不使用下划线分隔

```python
# 好的类名
class Student:
    pass

class BankAccount:
    pass

class HttpRequest:
    pass

# 不好的类名
class student:  # 应该用大写
    pass

class bank_account:  # 应该用大驼峰
    pass

class HTTPRequest:  # 缩写词全大写不符合规范
    pass
```

### 6.3.3 简单的类定义

```python
# 1. 最简单的类
class Empty:
    """空类"""
    pass

# 2. 只有属性的类
class Point:
    """点类"""
    x = 0
    y = 0

# 3. 有方法的类
class Calculator:
    """计算器类"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# 4. 完整的类
class Rectangle:
    """矩形类"""

    def __init__(self, width, height):
        """构造方法"""
        self.width = width
        self.height = height

    def area(self):
        """计算面积"""
        return self.width * self.height

    def perimeter(self):
        """计算周长"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """字符串表示"""
        return f"Rectangle({self.width} x {self.height})"
```

### 6.3.4 类的文档字符串

```python
class Student:
    """
    学生类

    用于管理学生的基本信息和成绩。

    Attributes:
        name (str): 学生姓名
        age (int): 学生年龄
        score (float): 学生成绩

    Methods:
        get_grade(): 获取成绩等级
        is_passed(): 判断是否及格
    """

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        """获取成绩等级"""
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'

# 访问文档
print(Student.__doc__)
help(Student)
```

---

## 6.4 类的操作

### 6.4.1 创建对象（实例化）

```python
class Dog:
    def __init__(self, name):
        self.name = name

# 创建对象
dog1 = Dog('旺财')
dog2 = Dog('大黄')
dog3 = Dog('小白')

print(dog1.name)  # 旺财
print(dog2.name)  # 大黄
```

### 6.4.2 访问属性

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 25)

# 访问属性
print(person.name)  # Alice
print(person.age)   # 25

# 修改属性
person.age = 26
print(person.age)   # 26
```

### 6.4.3 调用方法

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

# 调用方法
result1 = calc.add(10, 5)
result2 = calc.multiply(10, 5)

print(result1)  # 15
print(result2)  # 50
```

### 6.4.4 删除对象

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person('Alice')
print(person.name)  # Alice

# 删除对象
del person
# print(person.name)  # NameError: name 'person' is not defined
```

---

## 6.5 __init__() 方法

### 6.5.1 构造方法的作用

`__init__()` 是类的**构造方法**（初始化方法），在创建对象时自动调用。

**作用**：
- 初始化对象的属性
- 设置对象的初始状态
- 在对象创建时执行必要的设置

```python
class Person:
    def __init__(self, name, age):
        """构造方法"""
        print("构造方法被调用")
        self.name = name
        self.age = age

# 创建对象时自动调用 __init__
person = Person('Alice', 25)
# 输出: 构造方法被调用
```

### 6.5.2 参数传递

```python
class Student:
    def __init__(self, name, age, score=60):
        """
        初始化学生对象

        Args:
            name: 姓名（必需）
            age: 年龄（必需）
            score: 成绩（可选，默认 60）
        """
        self.name = name
        self.age = age
        self.score = score

# 创建对象
student1 = Student('Alice', 20)
student2 = Student('Bob', 21, 85)

print(student1.score)  # 60（默认值）
print(student2.score)  # 85
```

### 6.5.3 注意事项

```python
# 1. __init__ 不是构造器，而是初始化器
class MyClass:
    def __init__(self):
        print("初始化对象")

obj = MyClass()  # 对象已创建，然后调用 __init__

# 2. __init__ 必须返回 None
class Wrong:
    def __init__(self):
        # return "Hello"  # TypeError: __init__ should return None

# 3. __init__ 可以不定义
class Simple:
    pass  # 没有 __init__，使用默认的

obj = Simple()  # 可以正常创建

# 4. 父类的 __init__ 需要显式调用
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类的 __init__
        self.age = age
```

---

## 6.6 self

### 6.6.1 self 作为定义传参

`self` 代表**类的实例本身**，用于访问实例的属性和方法。

**self 的作用**：
- 引用当前对象
- 访问实例属性
- 调用实例方法
- 区分实例变量和局部变量

```python
class Person:
    def __init__(self, name, age):
        # self.name 是实例属性
        # name 是参数
        self.name = name
        self.age = age

    def introduce(self):
        # 通过 self 访问实例属性
        print(f"我是 {self.name}，今年 {self.age} 岁")

person = Person('Alice', 25)
person.introduce()  # 我是 Alice，今年 25 岁
```

**为什么需要 self？**

```python
class Counter:
    def __init__(self):
        self.count = 0  # 实例属性

    def increment(self):
        self.count += 1  # 访问实例属性

    def get_count(self):
        return self.count  # 返回实例属性

# 创建两个独立的计数器
counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()
counter2.increment()

print(counter1.get_count())  # 2
print(counter2.get_count())  # 1
# 两个对象有各自的 count 属性
```

**self 的命名**：

```python
# self 只是约定俗成的名称，可以用其他名字
class Person:
    def __init__(this, name):  # 使用 this
        this.name = name

    def greet(this):
        print(f"Hello, {this.name}")

# 但强烈建议使用 self，这是 Python 社区的标准
```

### 6.6.2 通过 self 在类中调用其他类的其他方法

```python
class MathHelper:
    """数学辅助类"""

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def add_and_multiply(self, a, b, c):
        """先相加再相乘"""
        # 通过 self 调用其他方法
        sum_result = self.add(a, b)
        return self.multiply(sum_result, c)

helper = MathHelper()
result = helper.add_and_multiply(2, 3, 4)
print(result)  # (2 + 3) * 4 = 20
```

```python
class Logger:
    """日志类"""

    def __init__(self, name):
        self.name = name

    def log(self, message):
        """记录日志"""
        print(f"[{self.name}] {message}")

    def info(self, message):
        """信息日志"""
        self.log(f"INFO: {message}")

    def error(self, message):
        """错误日志"""
        self.log(f"ERROR: {message}")

    def warning(self, message):
        """警告日志"""
        self.log(f"WARNING: {message}")

logger = Logger('MyApp')
logger.info('应用启动')
logger.warning('内存使用率较高')
logger.error('连接失败')
```

---

## 6.7 属性

### 6.7.1 类属性

**类属性**是属于类的变量，所有实例共享。

```python
class Dog:
    # 类属性
    species = '犬科'
    count = 0

    def __init__(self, name):
        self.name = name  # 实例属性
        Dog.count += 1    # 修改类属性

# 访问类属性
print(Dog.species)  # 犬科
print(Dog.count)    # 0

# 创建实例
dog1 = Dog('旺财')
dog2 = Dog('大黄')

# 所有实例共享类属性
print(dog1.species)  # 犬科
print(dog2.species)  # 犬科
print(Dog.count)     # 2
```

**类属性的特点**：
- 定义在类的内部，方法的外部
- 所有实例共享
- 通过类名或实例访问
- 通常用于存储类级别的数据

```python
class Config:
    """配置类"""
    # 类属性：所有实例共享的配置
    app_name = 'MyApp'
    version = '1.0.0'
    debug = True

    def __init__(self, user):
        self.user = user  # 实例属性：每个实例独有

# 访问类属性
print(Config.app_name)  # MyApp

# 修改类属性
Config.debug = False

# 所有实例都会受影响
config1 = Config('Alice')
config2 = Config('Bob')
print(config1.debug)  # False
print(config2.debug)  # False
```

### 6.7.2 实例属性

**实例属性**是属于对象的变量，每个实例独有。

```python
class Person:
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

# 创建实例
person1 = Person('Alice', 25)
person2 = Person('Bob', 30)

# 每个实例有自己的属性
print(person1.name)  # Alice
print(person2.name)  # Bob

# 修改一个实例的属性不影响其他实例
person1.age = 26
print(person1.age)  # 26
print(person2.age)  # 30（未改变）
```

**实例属性的特点**：
- 定义在 `__init__` 方法中
- 每个实例独有
- 使用 `self.属性名` 访问
- 可以动态添加和删除

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student('Alice')

# 动态添加实例属性
student.age = 20
student.score = 85

print(student.age)    # 20
print(student.score)  # 85

# 删除实例属性
del student.age
# print(student.age)  # AttributeError
```

### 6.7.3 类属性 vs 实例属性

```python
class MyClass:
    # 类属性
    class_attr = '类属性'

    def __init__(self):
        # 实例属性
        self.instance_attr = '实例属性'

# 1. 访问方式不同
print(MyClass.class_attr)  # 通过类访问类属性

obj = MyClass()
print(obj.instance_attr)   # 通过实例访问实例属性
print(obj.class_attr)      # 实例也可以访问类属性

# 2. 修改行为不同
obj.class_attr = '修改后'   # 这会创建一个同名的实例属性
print(obj.class_attr)      # 修改后（实例属性）
print(MyClass.class_attr)  # 类属性（未改变）

# 3. 共享性不同
class Counter:
    count = 0  # 类属性：共享

    def __init__(self):
        self.instance_count = 0  # 实例属性：独立

c1 = Counter()
c2 = Counter()

Counter.count = 10
print(c1.count)  # 10（共享）
print(c2.count)  # 10（共享）

c1.instance_count = 5
print(c1.instance_count)  # 5
print(c2.instance_count)  # 0（独立）
```

**对比总结**：

| 特性 | 类属性 | 实例属性 |
|------|--------|---------|
| **定义位置** | 类内部，方法外部 | `__init__` 方法中 |
| **访问方式** | `类名.属性` 或 `实例.属性` | `实例.属性` |
| **共享性** | 所有实例共享 | 每个实例独有 |
| **修改影响** | 影响所有实例 | 只影响当前实例 |
| **用途** | 类级别的常量或配置 | 对象的状态数据 |

---

## 6.8 方法

### 6.8.1 实例方法

**实例方法**是最常用的方法，第一个参数必须是 `self`。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def introduce(self):
        """自我介绍"""
        return f"我是 {self.name}，今年 {self.age} 岁"

    def have_birthday(self):
        """过生日，年龄加 1"""
        self.age += 1
        print(f"{self.name} 过生日了，现在 {self.age} 岁")

# 调用实例方法
person = Person('Alice', 25)
print(person.introduce())  # 我是 Alice，今年 25 岁
person.have_birthday()     # Alice 过生日了，现在 26 岁
```

**实例方法的特点**：
- 第一个参数必须是 `self`
- 可以访问实例属性和类属性
- 可以调用其他实例方法
- 必须通过实例调用

### 6.8.2 类方法

**类方法**使用 `@classmethod` 装饰器，第一个参数是 `cls`（类本身）。

```python
class Person:
    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        """获取创建的实例数量"""
        return cls.count

    @classmethod
    def create_anonymous(cls):
        """创建匿名用户"""
        return cls('Anonymous')

# 调用类方法
print(Person.get_count())  # 0

person1 = Person('Alice')
person2 = Person('Bob')

print(Person.get_count())  # 2

# 通过类方法创建对象
anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous
print(Person.get_count())  # 3
```

**类方法的特点**：
- 使用 `@classmethod` 装饰器
- 第一个参数是 `cls`（类本身）
- 可以访问类属性，但不能访问实例属性
- 可以通过类或实例调用
- 常用于工厂方法

**类方法的应用**：

```python
from datetime import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """从字符串创建日期对象"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """创建今天的日期"""
        now = datetime.now()
        return cls(now.year, now.month, now.day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# 使用类方法创建对象
date1 = Date(2024, 1, 1)
date2 = Date.from_string('2024-12-25')
date3 = Date.today()

print(date1)  # 2024-01-01
print(date2)  # 2024-12-25
print(date3)  # 当前日期
```

### 6.8.3 静态方法

**静态方法**使用 `@staticmethod` 装饰器，不需要 `self` 或 `cls` 参数。

```python
class MathUtils:
    """数学工具类"""

    @staticmethod
    def add(a, b):
        """加法"""
        return a + b

    @staticmethod
    def is_even(n):
        """判断是否为偶数"""
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# 调用静态方法
print(MathUtils.add(10, 5))        # 15
print(MathUtils.is_even(4))        # True
print(MathUtils.factorial(5))      # 120

# 也可以通过实例调用
utils = MathUtils()
print(utils.add(3, 7))  # 10
```

**静态方法的特点**：
- 使用 `@staticmethod` 装饰器
- 不需要 `self` 或 `cls` 参数
- 不能访问实例属性或类属性
- 与类和实例无关，只是逻辑上属于类
- 可以通过类或实例调用

### 6.8.4 在类外定义方法

可以在类外定义函数，然后将其绑定到类。

```python
# 在类外定义函数
def greet(self):
    return f"Hello, {self.name}!"

class Person:
    def __init__(self, name):
        self.name = name

# 将函数绑定到类
Person.greet = greet

# 使用
person = Person('Alice')
print(person.greet())  # Hello, Alice!
```

### 6.8.5 特殊方法（魔法方法）

特殊方法以双下划线开头和结尾，用于实现特定的功能。

#### 常用特殊方法

```python
class Point:
    """点类"""

    def __init__(self, x, y):
        """构造方法"""
        self.x = x
        self.y = y

    def __str__(self):
        """字符串表示（用于 print）"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """官方字符串表示（用于调试）"""
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """相等性比较"""
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """加法运算符重载"""
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        """长度（距离原点）"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# 使用特殊方法
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)           # Point(1, 2) - 调用 __str__
print(repr(p2))     # Point(3, 4) - 调用 __repr__
print(p1 == p2)     # False - 调用 __eq__
p3 = p1 + p2        # 调用 __add__
print(p3)           # Point(4, 6)
print(len(p1))      # 2 - 调用 __len__
```

#### 更多特殊方法

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"《{self.title}》"

    def __len__(self):
        """返回页数"""
        return self.pages

    def __getitem__(self, index):
        """支持索引访问"""
        if index == 0:
            return self.title
        elif index == 1:
            return self.author
        else:
            raise IndexError("索引超出范围")

    def __contains__(self, keyword):
        """支持 in 操作"""
        return keyword in self.title

    def __call__(self):
        """使对象可调用"""
        return f"{self.title} by {self.author}"

book = Book('Python 编程', '张三', 500)

print(len(book))      # 500
print(book[0])        # Python 编程
print('Python' in book)  # True
print(book())         # Python 编程 by 张三
```

### 6.8.6 方法对比总结

| 方法类型 | 装饰器 | 第一个参数 | 访问实例属性 | 访问类属性 | 调用方式 |
|---------|--------|-----------|------------|-----------|---------|
| **实例方法** | 无 | `self` | ✓ | ✓ | `实例.方法()` |
| **类方法** | `@classmethod` | `cls` | ✗ | ✓ | `类.方法()` 或 `实例.方法()` |
| **静态方法** | `@staticmethod` | 无 | ✗ | ✗ | `类.方法()` 或 `实例.方法()` |

```python
class Demo:
    class_attr = '类属性'

    def __init__(self):
        self.instance_attr = '实例属性'

    # 实例方法
    def instance_method(self):
        print(f"实例方法: {self.instance_attr}")
        print(f"类属性: {self.class_attr}")

    # 类方法
    @classmethod
    def class_method(cls):
        print(f"类方法: {cls.class_attr}")
        # print(self.instance_attr)  # 错误：无法访问实例属性

    # 静态方法
    @staticmethod
    def static_method():
        print("静态方法：不访问实例和类属性")
        # print(self.instance_attr)  # 错误
        # print(cls.class_attr)      # 错误

# 调用演示
obj = Demo()
obj.instance_method()   # 实例调用实例方法
Demo.class_method()     # 类调用类方法
Demo.static_method()    # 类调用静态方法
```

---

## 6.9 添加和删除属性与方法

### 6.9.1 动态给对象添加属性

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person('Alice')
print(person.name)  # Alice

# 动态添加实例属性
person.age = 25
person.city = 'Beijing'

print(person.age)   # 25
print(person.city)  # Beijing

# 只影响当前实例
person2 = Person('Bob')
# print(person2.age)  # AttributeError: 没有 age 属性
```

### 6.9.2 动态给类添加属性

```python
class Dog:
    def __init__(self, name):
        self.name = name

# 动态给类添加属性
Dog.species = '犬科'
Dog.count = 0

# 所有实例都可以访问
dog1 = Dog('旺财')
dog2 = Dog('大黄')

print(dog1.species)  # 犬科
print(dog2.species)  # 犬科
```

### 6.9.3 动态给对象添加方法

```python
class Person:
    def __init__(self, name):
        self.name = name

def greet(self):
    return f"Hello, {self.name}!"

person = Person('Alice')

# 给实例添加方法（需要使用 types.MethodType）
import types
person.greet = types.MethodType(greet, person)

print(person.greet())  # Hello, Alice!

# 只影响当前实例
person2 = Person('Bob')
# person2.greet()  # AttributeError
```

### 6.9.4 动态给类添加方法

```python
class Person:
    def __init__(self, name):
        self.name = name

# 定义方法
def introduce(self):
    return f"我是 {self.name}"

def greet(self):
    return f"Hello, {self.name}!"

# 给类添加方法
Person.introduce = introduce
Person.greet = greet

# 所有实例都可以使用
person1 = Person('Alice')
person2 = Person('Bob')

print(person1.introduce())  # 我是 Alice
print(person2.greet())      # Hello, Bob!
```

### 6.9.5 动态删除属性与方法

```python
class Person:
    species = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

person = Person('Alice', 25)

# 删除实例属性
del person.age
# print(person.age)  # AttributeError

# 删除类属性
del Person.species
# print(person.species)  # AttributeError

# 删除方法
del Person.greet
# person.greet()  # AttributeError

# 使用 delattr()
person.city = 'Beijing'
delattr(person, 'city')
# print(person.city)  # AttributeError
```

### 6.9.6 __slots__ 限制实例属性与实例方法

`__slots__` 用于限制实例可以拥有的属性，提高内存效率。

```python
class Person:
    # 只允许这些属性
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 25)

# 允许的属性
person.name = 'Bob'
person.age = 30

# 不允许添加其他属性
try:
    person.city = 'Beijing'  # AttributeError
except AttributeError as e:
    print(f"错误: {e}")
```

**__slots__ 的优点**：

```python
# 1. 节省内存
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# WithSlots 实例占用更少的内存

# 2. 防止属性拼写错误
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 25)
# person.agee = 30  # AttributeError: 拼写错误会立即发现
```

**__slots__ 的限制**：

```python
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 25)

# 1. 不能动态添加属性
# person.city = 'Beijing'  # AttributeError

# 2. 没有 __dict__ 属性
# print(person.__dict__)  # AttributeError

# 3. 不能使用默认的 __weakref__
# import weakref
# weakref.ref(person)  # TypeError（除非在 __slots__ 中添加 '__weakref__'）
```

**__slots__ 的继承**：

```python
class Parent:
    __slots__ = ['name']

class Child(Parent):
    __slots__ = ['age']  # 子类的 __slots__ 会与父类合并

child = Child()
child.name = 'Alice'  # 允许（来自父类）
child.age = 25        # 允许（来自子类）
# child.city = 'Beijing'  # AttributeError
```

---

## 综合示例

### 示例 1：银行账户系统

```python
class BankAccount:
    """银行账户类"""

    # 类属性：利率
    interest_rate = 0.03

    # 类属性：账户总数
    account_count = 0

    def __init__(self, owner, balance=0):
        """
        初始化账户

        Args:
            owner: 账户持有人
            balance: 初始余额
        """
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
        BankAccount.account_count += 1

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"存款: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"取款: -{amount}")
            return True
        return False

    def add_interest(self):
        """添加利息"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"利息: +{interest:.2f}")

    def get_balance(self):
        """获取余额"""
        return self.balance

    def print_history(self):
        """打印交易历史"""
        print(f"账户持有人: {self.owner}")
        print("交易历史:")
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print(f"当前余额: {self.balance:.2f}")

    @classmethod
    def get_account_count(cls):
        """获取账户总数"""
        return cls.account_count

    @classmethod
    def set_interest_rate(cls, rate):
        """设置利率"""
        cls.interest_rate = rate

    def __str__(self):
        return f"账户({self.owner}): {self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

# 使用示例
account1 = BankAccount('Alice', 1000)
account2 = BankAccount('Bob', 500)

# 存取款
account1.deposit(500)
account1.withdraw(200)
account1.add_interest()

# 打印信息
print(account1)
account1.print_history()

# 类方法
print(f"账户总数: {BankAccount.get_account_count()}")
BankAccount.set_interest_rate(0.05)
```

### 示例 2：学生成绩管理系统

```python
class Student:
    """学生类"""

    # 类属性：学生总数
    student_count = 0

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {}
        Student.student_count += 1

    def add_score(self, subject, score):
        """添加成绩"""
        if 0 <= score <= 100:
            self.scores[subject] = score
            return True
        return False

    def get_average(self):
        """计算平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_grade(self):
        """获取等级"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def print_report(self):
        """打印成绩单"""
        print(f"学生: {self.name} ({self.student_id})")
        print("成绩:")
        for subject, score in self.scores.items():
            print(f"  {subject}: {score}")
        print(f"平均分: {self.get_average():.2f}")
        print(f"等级: {self.get_grade()}")

    @classmethod
    def get_student_count(cls):
        """获取学生总数"""
        return cls.student_count

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def __eq__(self, other):
        """比较学生（根据学号）"""
        return self.student_id == other.student_id

class StudentManager:
    """学生管理类"""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """添加学生"""
        if student not in self.students:
            self.students.append(student)
            return True
        return False

    def find_student(self, student_id):
        """查找学生"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_top_students(self, n=3):
        """获取成绩最好的 n 个学生"""
        sorted_students = sorted(
            self.students,
            key=lambda s: s.get_average(),
            reverse=True
        )
        return sorted_students[:n]

    def print_all_students(self):
        """打印所有学生"""
        for student in self.students:
            student.print_report()
            print("-" * 40)

# 使用示例
manager = StudentManager()

# 创建学生
student1 = Student('Alice', 'S001')
student1.add_score('数学', 95)
student1.add_score('英语', 88)
student1.add_score('物理', 92)

student2 = Student('Bob', 'S002')
student2.add_score('数学', 78)
student2.add_score('英语', 85)
student2.add_score('物理', 80)

# 添加到管理器
manager.add_student(student1)
manager.add_student(student2)

# 打印成绩
manager.print_all_students()

# 获取优秀学生
top_students = manager.get_top_students(1)
print(f"最优秀的学生: {top_students[0]}")
```

---

## 总结

本章介绍了 Python 面向对象编程的核心概念：

1. **面向过程 vs 面向对象**：两种编程范式的对比
2. **类和对象**：类是模板，对象是实例
3. **定义类**：类的语法、命名规范、文档字符串
4. **类的操作**：创建对象、访问属性、调用方法
5. **__init__ 方法**：构造方法的作用和使用
6. **self 参数**：引用当前实例，访问属性和方法
7. **属性**：类属性和实例属性的区别
8. **方法**：实例方法、类方法、静态方法、特殊方法
9. **动态操作**：动态添加/删除属性和方法、__slots__ 限制

面向对象编程是 Python 的重要特性，掌握这些概念是编写高质量代码的基础。

---

## 练习题

1. 创建一个 `Car` 类，包含品牌、型号、价格等属性，以及启动、停止等方法
2. 实现一个 `Rectangle` 类，计算面积和周长，并重载比较运算符
3. 创建一个 `Library` 类和 `Book` 类，实现图书管理系统
4. 实现一个 `ShoppingCart` 类，支持添加、删除商品，计算总价
5. 创建一个 `Employee` 类，使用类方法统计员工总数
6. 实现一个 `Counter` 类，使用 `__call__` 方法使对象可调用
7. 创建一个 `Point` 类，重载加法、减法、相等性比较等运算符
8. 使用 `__slots__` 优化一个包含大量实例的类
