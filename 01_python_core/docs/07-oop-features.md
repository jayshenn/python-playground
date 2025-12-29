# 第 7 章 面向对象编程三大特性

面向对象编程有三大特性：**封装**、**继承**、**多态**。这三个特性是面向对象编程的核心，理解和掌握它们对于编写高质量的面向对象代码至关重要。

---

## 7.1 封装

**封装**（Encapsulation）是将数据和操作数据的方法绑定在一起，隐藏内部实现细节，只对外提供公共访问接口。

### 封装的核心思想

- **隐藏内部实现**：对象的内部细节对外部不可见
- **提供公共接口**：通过方法访问和修改数据
- **保护数据安全**：防止外部直接修改内部数据
- **降低耦合度**：修改内部实现不影响外部使用

### 封装的优点

1. **安全性**：防止数据被随意修改
2. **灵活性**：可以修改内部实现而不影响外部
3. **易用性**：提供简洁的接口，隐藏复杂性
4. **可维护性**：降低模块间的耦合

```python
# 不使用封装
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # 公开属性，可以随意修改

account = BankAccount(1000)
account.balance = -500  # 问题：可以设置为负数！
print(account.balance)  # -500

# 使用封装
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        """获取余额"""
        return self.__balance

account = BankAccount(1000)
# account.__balance = -500  # 无法直接访问私有属性
account.withdraw(500)  # 通过方法操作
print(account.get_balance())  # 500
```

---

### 7.1.1 私有化

在 Python 中，通过在属性或方法名前加**双下划线（`__`）**来实现私有化。

**私有化的特点**：
- 私有成员在类外部无法直接访问
- 私有成员只能在类内部使用
- Python 通过名称改编（Name Mangling）实现私有化

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 公有属性
        self.__age = age      # 私有属性

    def __private_method(self):  # 私有方法
        return "这是私有方法"

    def public_method(self):
        """公有方法可以访问私有成员"""
        return f"{self.name} 的年龄是 {self.__age}"

person = Person('Alice', 25)

# 访问公有属性
print(person.name)  # Alice

# 无法直接访问私有属性
# print(person.__age)  # AttributeError

# 通过公有方法访问
print(person.public_method())  # Alice 的年龄是 25

# 无法直接调用私有方法
# person.__private_method()  # AttributeError
```

**名称改编（Name Mangling）**：

```python
class Test:
    def __init__(self):
        self.__private = "私有属性"

obj = Test()

# Python 将 __private 改编为 _类名__private
print(obj._Test__private)  # 私有属性（不推荐这样访问）

# 但这违反了封装原则，不应该这样做
```

---

### 7.1.2 私有属性

**私有属性**是在属性名前加双下划线的属性，只能在类内部访问。

```python
class Student:
    def __init__(self, name, score):
        self.name = name        # 公有属性
        self.__score = score    # 私有属性

    def get_score(self):
        """获取成绩"""
        return self.__score

    def set_score(self, score):
        """设置成绩"""
        if 0 <= score <= 100:
            self.__score = score
            return True
        else:
            print("成绩必须在 0-100 之间")
            return False

    def get_grade(self):
        """获取等级"""
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        else:
            return 'D'

student = Student('Alice', 85)

# 无法直接访问私有属性
# print(student.__score)  # AttributeError

# 通过公有方法访问和修改
print(student.get_score())  # 85
student.set_score(95)
print(student.get_score())  # 95
print(student.get_grade())  # A

# 尝试设置无效值
student.set_score(150)  # 成绩必须在 0-100 之间
```

**私有属性的应用场景**：

```python
class CreditCard:
    """信用卡类"""

    def __init__(self, card_number, cvv, balance):
        self.__card_number = card_number  # 私有：卡号
        self.__cvv = cvv                  # 私有：安全码
        self.__balance = balance          # 私有：余额

    def make_payment(self, amount, cvv):
        """支付（需要验证安全码）"""
        if cvv != self.__cvv:
            return "安全码错误"

        if amount > self.__balance:
            return "余额不足"

        self.__balance -= amount
        return f"支付成功，剩余余额：{self.__balance}"

    def get_masked_number(self):
        """获取隐藏的卡号"""
        return f"**** **** **** {self.__card_number[-4:]}"

card = CreditCard('1234567890123456', '123', 5000)

# 无法直接访问敏感信息
# print(card.__card_number)  # AttributeError
# print(card.__cvv)          # AttributeError

# 只能看到部分卡号
print(card.get_masked_number())  # **** **** **** 3456

# 支付需要验证
print(card.make_payment(1000, '123'))  # 支付成功，剩余余额：4000
print(card.make_payment(1000, '456'))  # 安全码错误
```

---

### 7.1.3 私有方法

**私有方法**是在方法名前加双下划线的方法，只能在类内部调用。

```python
class DataProcessor:
    """数据处理器"""

    def __init__(self, data):
        self.__data = data

    def __validate_data(self):
        """私有方法：验证数据"""
        return self.__data is not None and len(self.__data) > 0

    def __clean_data(self):
        """私有方法：清洗数据"""
        return [x for x in self.__data if x is not None]

    def __transform_data(self):
        """私有方法：转换数据"""
        return [x * 2 for x in self.__data]

    def process(self):
        """公有方法：处理数据（调用私有方法）"""
        if not self.__validate_data():
            return "数据无效"

        cleaned = self.__clean_data()
        transformed = self.__transform_data()
        return transformed

processor = DataProcessor([1, 2, None, 3, 4])

# 无法直接调用私有方法
# processor.__validate_data()  # AttributeError
# processor.__clean_data()     # AttributeError

# 通过公有方法间接使用私有方法
result = processor.process()
print(result)  # [2, 4, 6, 8]
```

**私有方法的优点**：

```python
class Calculator:
    """计算器类"""

    def __init__(self):
        self.__history = []

    def __log_operation(self, operation, result):
        """私有方法：记录操作历史"""
        self.__history.append(f"{operation} = {result}")

    def __validate_numbers(self, a, b):
        """私有方法：验证输入"""
        return isinstance(a, (int, float)) and isinstance(b, (int, float))

    def add(self, a, b):
        """加法"""
        if not self.__validate_numbers(a, b):
            return "输入无效"

        result = a + b
        self.__log_operation(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        """减法"""
        if not self.__validate_numbers(a, b):
            return "输入无效"

        result = a - b
        self.__log_operation(f"{a} - {b}", result)
        return result

    def get_history(self):
        """获取操作历史"""
        return self.__history

calc = Calculator()
calc.add(10, 5)
calc.subtract(10, 3)
print(calc.get_history())  # ['10 + 5 = 15', '10 - 3 = 7']
```

---

### 7.1.4 property

`property` 是 Python 的内置装饰器，用于将方法转换为属性访问方式，实现更优雅的封装。

#### 使用 property 装饰器

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        """获取年龄（getter）"""
        return self.__age

    @age.setter
    def age(self, value):
        """设置年龄（setter）"""
        if 0 < value < 150:
            self.__age = value
        else:
            raise ValueError("年龄必须在 0-150 之间")

    @age.deleter
    def age(self):
        """删除年龄（deleter）"""
        print("删除年龄属性")
        del self.__age

person = Person('Alice', 25)

# 像访问属性一样使用（实际调用的是方法）
print(person.age)  # 25（调用 getter）

# 像设置属性一样使用（实际调用 setter）
person.age = 26    # 调用 setter
print(person.age)  # 26

# 尝试设置无效值
try:
    person.age = 200  # 会抛出异常
except ValueError as e:
    print(e)  # 年龄必须在 0-150 之间

# 删除属性
del person.age  # 调用 deleter
```

#### property 的优点

```python
# 不使用 property
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if value > 0:
            self.__width = value

    def get_area(self):
        return self.__width * self.__height

rect = Rectangle(10, 5)
print(rect.get_width())  # 需要调用方法
rect.set_width(20)
print(rect.get_area())

# 使用 property（推荐）
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value

    @property
    def area(self):
        """只读属性"""
        return self.__width * self.__height

rect = Rectangle(10, 5)
print(rect.width)   # 像访问属性一样
rect.width = 20     # 像设置属性一样
print(rect.area)    # 只读属性
# rect.area = 100   # AttributeError: 没有 setter
```

#### property 的应用场景

```python
class Temperature:
    """温度类（支持摄氏度和华氏度转换）"""

    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        """摄氏度（getter）"""
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        """摄氏度（setter）"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self.__celsius = value

    @property
    def fahrenheit(self):
        """华氏度（getter）"""
        return self.__celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """华氏度（setter）"""
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self.__celsius = celsius

    @property
    def kelvin(self):
        """开尔文（getter，只读）"""
        return self.__celsius + 273.15

temp = Temperature(25)

# 摄氏度
print(f"摄氏度: {temp.celsius}°C")  # 25°C

# 自动转换为华氏度
print(f"华氏度: {temp.fahrenheit}°F")  # 77°F

# 设置华氏度，自动转换为摄氏度
temp.fahrenheit = 86
print(f"摄氏度: {temp.celsius}°C")  # 30°C

# 开尔文（只读）
print(f"开尔文: {temp.kelvin}K")  # 303.15K
```

#### 使用 property() 函数

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("半径必须大于 0")

    def del_radius(self):
        del self.__radius

    # 使用 property() 函数
    radius = property(get_radius, set_radius, del_radius, "圆的半径")

circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10
print(circle.radius)  # 10
```

---

## 7.2 继承

**继承**（Inheritance）是指一个类可以继承另一个类的属性和方法，实现代码复用。

### 继承的核心思想

- **代码复用**：子类继承父类的属性和方法
- **扩展功能**：子类可以添加新的属性和方法
- **覆盖行为**：子类可以重写父类的方法
- **is-a 关系**：子类是父类的一种特殊类型

### 继承的优点

1. **代码复用**：避免重复编写相同的代码
2. **易于维护**：修改父类会影响所有子类
3. **层次结构**：建立清晰的类层次关系
4. **多态性**：支持多态特性

```python
# 不使用继承
class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西")

class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西")

# 使用继承
class Animal:
    """动物类（父类）"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西")

class Dog(Animal):
    """狗类（子类）"""
    def bark(self):
        print(f"{self.name} 在汪汪叫")

class Cat(Animal):
    """猫类（子类）"""
    def meow(self):
        print(f"{self.name} 在喵喵叫")

dog = Dog('旺财')
dog.eat()   # 继承自父类
dog.bark()  # 子类自己的方法

cat = Cat('咪咪')
cat.eat()   # 继承自父类
cat.meow()  # 子类自己的方法
```

---

### 7.2.1 单继承

**单继承**是指一个子类只继承一个父类。

```python
class Parent:
    """父类"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    """子类"""
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类的 __init__
        self.age = age

    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

child = Child('Alice', 10)
print(child.greet())      # Hello, I'm Alice（继承自父类）
print(child.introduce())  # I'm Alice, 10 years old（子类自己的）
```

**单继承示例**：

```python
class Vehicle:
    """交通工具（父类）"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        """启动"""
        self.is_running = True
        print(f"{self.brand} {self.model} 启动了")

    def stop(self):
        """停止"""
        self.is_running = False
        print(f"{self.brand} {self.model} 停止了")

class Car(Vehicle):
    """汽车（子类）"""

    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def open_trunk(self):
        """打开后备箱"""
        print("后备箱已打开")

class Motorcycle(Vehicle):
    """摩托车（子类）"""

    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        """翘头"""
        if self.is_running:
            print("摩托车翘头中...")
        else:
            print("请先启动摩托车")

# 使用
car = Car('Tesla', 'Model 3', 4)
car.start()        # 继承自父类
car.open_trunk()   # 子类自己的方法
car.stop()         # 继承自父类

motorcycle = Motorcycle('Harley', 'Sportster', False)
motorcycle.start()
motorcycle.wheelie()
```

---

### 7.2.2 多继承

**多继承**是指一个子类可以继承多个父类。

```python
class Father:
    def __init__(self):
        self.father_name = 'Father'

    def drive(self):
        print("开车技能来自父亲")

class Mother:
    def __init__(self):
        self.mother_name = 'Mother'

    def cook(self):
        print("做饭技能来自母亲")

class Child(Father, Mother):
    """子类继承多个父类"""
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = 'Child'

child = Child()
child.drive()  # 来自 Father
child.cook()   # 来自 Mother
print(child.father_name)  # Father
print(child.mother_name)  # Mother
```

**多继承的应用**：

```python
class Flyable:
    """可飞行的"""
    def fly(self):
        print("我可以飞")

class Swimmable:
    """可游泳的"""
    def swim(self):
        print("我可以游泳")

class Walkable:
    """可行走的"""
    def walk(self):
        print("我可以走路")

class Duck(Flyable, Swimmable, Walkable):
    """鸭子：可以飞、游泳、走路"""
    pass

class Fish(Swimmable):
    """鱼：只能游泳"""
    pass

class Bird(Flyable, Walkable):
    """鸟：可以飞、走路"""
    pass

# 使用
duck = Duck()
duck.fly()   # 我可以飞
duck.swim()  # 我可以游泳
duck.walk()  # 我可以走路

fish = Fish()
fish.swim()  # 我可以游泳

bird = Bird()
bird.fly()   # 我可以飞
bird.walk()  # 我可以走路
```

**多继承的方法解析顺序（MRO）**：

```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

# 方法解析顺序
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # B.method（按照 MRO 查找）
```

---

### 7.2.3 复用父类方法

子类可以通过 `super()` 或直接调用父类名来复用父类的方法。

#### 使用 super()（推荐）

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "动物发出声音"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的 __init__
        self.breed = breed

    def speak(self):
        # 调用父类的方法并扩展
        parent_speak = super().speak()
        return f"{parent_speak}，{self.name} 汪汪叫"

dog = Dog('旺财', '金毛')
print(dog.speak())  # 动物发出声音，旺财 汪汪叫
```

#### 直接调用父类

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)  # 直接调用父类
        self.age = age

    def greet(self):
        parent_greeting = Parent.greet(self)  # 直接调用父类方法
        return f"{parent_greeting}, age {self.age}"

child = Child('Alice', 10)
print(child.greet())  # Hello from Alice, age 10
```

#### super() vs 直接调用

```python
class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()  # 推荐：使用 super()

class C(A):
    def __init__(self):
        print("C.__init__")
        A.__init__(self)  # 可行但不推荐

b = B()
# B.__init__
# A.__init__

c = C()
# C.__init__
# A.__init__
```

**super() 的优点**：
- 自动处理多继承的 MRO
- 代码更简洁
- 更易于维护

---

### 7.2.4 方法重写和重载

#### 方法重写（Override）

子类重新定义父类的方法。

```python
class Animal:
    def speak(self):
        return "动物发出声音"

class Dog(Animal):
    def speak(self):
        """重写父类的 speak 方法"""
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        """重写父类的 speak 方法"""
        return "喵喵喵"

dog = Dog()
cat = Cat()

print(dog.speak())  # 汪汪汪（使用子类的方法）
print(cat.speak())  # 喵喵喵（使用子类的方法）
```

**方法重写的应用**：

```python
class Shape:
    """形状基类"""

    def __init__(self, name):
        self.name = name

    def area(self):
        """计算面积（子类必须重写）"""
        raise NotImplementedError("子类必须实现 area 方法")

    def perimeter(self):
        """计算周长（子类必须重写）"""
        raise NotImplementedError("子类必须实现 perimeter 方法")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('矩形')
        self.width = width
        self.height = height

    def area(self):
        """重写 area 方法"""
        return self.width * self.height

    def perimeter(self):
        """重写 perimeter 方法"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('圆形')
        self.radius = radius

    def area(self):
        """重写 area 方法"""
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        """重写 perimeter 方法"""
        import math
        return 2 * math.pi * self.radius

# 使用
rect = Rectangle(10, 5)
print(f"{rect.name} 面积: {rect.area()}")        # 矩形 面积: 50
print(f"{rect.name} 周长: {rect.perimeter()}")  # 矩形 周长: 30

circle = Circle(5)
print(f"{circle.name} 面积: {circle.area():.2f}")        # 圆形 面积: 78.54
print(f"{circle.name} 周长: {circle.perimeter():.2f}")  # 圆形 周长: 31.42
```

#### 方法重载（Overload）

**注意**：Python 不支持传统意义上的方法重载（同名方法不同参数）。

```python
# Python 不支持这种重载
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):  # 会覆盖上面的 add
        return a + b + c

calc = Calculator()
# calc.add(1, 2)  # TypeError: 缺少参数

# Python 的替代方案：使用默认参数
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(1, 2))      # 3
print(calc.add(1, 2, 3))   # 6

# 或使用可变参数
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         # 3
print(calc.add(1, 2, 3))      # 6
print(calc.add(1, 2, 3, 4))   # 10
```

---

### 7.2.5 方法搜索

Python 使用 **MRO（Method Resolution Order）** 来确定方法的搜索顺序。

```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

# 查看 MRO
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # B.method（按照 MRO: D -> B -> C -> A）
```

**MRO 的规则**：
1. 子类优先于父类
2. 多继承时，按照继承顺序
3. 使用 C3 线性化算法

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)

d = D()
d.show()  # C（MRO: D -> B -> C -> A，在 C 中找到）
```

**super() 与 MRO**：

```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()  # 调用 MRO 中的下一个类

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)

d = D()
d.method()
# 输出:
# D.method
# B.method
# C.method
# A.method
```

---

## 7.3 多态

**多态**（Polymorphism）是指不同的对象对同一消息做出不同的响应。

### 多态的核心思想

- **同一接口，不同实现**：相同的方法名，不同的行为
- **运行时决定**：在运行时确定调用哪个方法
- **增强灵活性**：可以用统一的方式处理不同类型的对象

### 多态的优点

1. **灵活性**：可以处理多种类型的对象
2. **可扩展性**：添加新类型不需要修改现有代码
3. **代码复用**：使用统一的接口
4. **降低耦合**：依赖抽象而不是具体实现

```python
class Animal:
    """动物基类"""
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

class Duck(Animal):
    def speak(self):
        return "嘎嘎嘎"

# 多态：统一的接口，不同的实现
def make_animal_speak(animal):
    """让动物发出声音（多态）"""
    print(animal.speak())

# 使用
dog = Dog()
cat = Cat()
duck = Duck()

make_animal_speak(dog)   # 汪汪汪
make_animal_speak(cat)   # 喵喵喵
make_animal_speak(duck)  # 嘎嘎嘎
```

### 多态的应用

#### 示例 1：支付系统

```python
class Payment:
    """支付基类"""

    def pay(self, amount):
        """支付方法（子类必须实现）"""
        raise NotImplementedError("子类必须实现 pay 方法")

class CreditCardPayment(Payment):
    """信用卡支付"""

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"使用信用卡 {self.card_number[-4:]} 支付 {amount} 元"

class AlipayPayment(Payment):
    """支付宝支付"""

    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        return f"使用支付宝账户 {self.account} 支付 {amount} 元"

class WeChatPayment(Payment):
    """微信支付"""

    def __init__(self, phone):
        self.phone = phone

    def pay(self, amount):
        return f"使用微信账户 {self.phone} 支付 {amount} 元"

# 多态：统一的支付接口
def process_payment(payment: Payment, amount: float):
    """处理支付（多态）"""
    print(payment.pay(amount))

# 使用不同的支付方式
credit_card = CreditCardPayment('1234567890123456')
alipay = AlipayPayment('user@example.com')
wechat = WeChatPayment('13800138000')

process_payment(credit_card, 100)  # 使用信用卡 3456 支付 100 元
process_payment(alipay, 200)       # 使用支付宝账户 user@example.com 支付 200 元
process_payment(wechat, 300)       # 使用微信账户 13800138000 支付 300 元
```

#### 示例 2：图形绘制系统

```python
class Shape:
    """形状基类"""

    def draw(self):
        """绘制形状（子类必须实现）"""
        raise NotImplementedError("子类必须实现 draw 方法")

    def area(self):
        """计算面积（子类必须实现）"""
        raise NotImplementedError("子类必须实现 area 方法")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"绘制半径为 {self.radius} 的圆形"

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"绘制 {self.width}x{self.height} 的矩形"

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        return f"绘制底边 {self.base}、高 {self.height} 的三角形"

    def area(self):
        return 0.5 * self.base * self.height

# 多态：统一处理所有形状
def render_shapes(shapes):
    """渲染形状列表（多态）"""
    for shape in shapes:
        print(shape.draw())
        print(f"面积: {shape.area():.2f}")
        print("-" * 40)

# 使用
shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(8, 6)
]

render_shapes(shapes)
```

#### 示例 3：文件处理系统

```python
class FileProcessor:
    """文件处理基类"""

    def process(self, content):
        """处理文件（子类必须实现）"""
        raise NotImplementedError("子类必须实现 process 方法")

class TextProcessor(FileProcessor):
    """文本文件处理"""

    def process(self, content):
        return f"处理文本文件，内容长度: {len(content)}"

class ImageProcessor(FileProcessor):
    """图片文件处理"""

    def process(self, content):
        return f"处理图片文件，大小: {len(content)} 字节"

class VideoProcessor(FileProcessor):
    """视频文件处理"""

    def process(self, content):
        return f"处理视频文件，时长: {len(content)} 秒"

# 多态：统一的文件处理接口
def handle_file(processor: FileProcessor, content):
    """处理文件（多态）"""
    print(processor.process(content))

# 使用
text_proc = TextProcessor()
image_proc = ImageProcessor()
video_proc = VideoProcessor()

handle_file(text_proc, "Hello, World!")  # 处理文本文件，内容长度: 13
handle_file(image_proc, b'\x00' * 1024)  # 处理图片文件，大小: 1024 字节
handle_file(video_proc, [1, 2, 3])       # 处理视频文件，时长: 3 秒
```

### 鸭子类型（Duck Typing）

Python 是动态类型语言，支持鸭子类型："如果它走起来像鸭子，叫起来像鸭子，那么它就是鸭子。"

```python
# 不需要显式继承，只要有相同的方法就行
class Dog:
    def speak(self):
        return "汪汪汪"

class Robot:
    def speak(self):
        return "01010101"

class Person:
    def speak(self):
        return "你好"

# 多态：只要有 speak 方法就可以调用
def make_it_speak(obj):
    print(obj.speak())

dog = Dog()
robot = Robot()
person = Person()

make_it_speak(dog)    # 汪汪汪
make_it_speak(robot)  # 01010101
make_it_speak(person) # 你好
```

---

## 综合示例

### 示例 1：员工管理系统

```python
class Employee:
    """员工基类"""

    def __init__(self, name, id):
        self.__name = name      # 私有属性：封装
        self.__id = id
        self.__salary = 0

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value

    def calculate_salary(self):
        """计算工资（多态：子类重写）"""
        raise NotImplementedError("子类必须实现 calculate_salary 方法")

    def __str__(self):
        return f"{self.name} ({self.id})"

class FullTimeEmployee(Employee):
    """全职员工（继承）"""

    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        """重写：计算月工资"""
        self.salary = self.monthly_salary
        return self.salary

class PartTimeEmployee(Employee):
    """兼职员工（继承）"""

    def __init__(self, name, id, hourly_rate):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours(self, hours):
        """添加工作小时数"""
        self.hours_worked += hours

    def calculate_salary(self):
        """重写：计算时薪工资"""
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

class Manager(FullTimeEmployee):
    """经理（继承全职员工）"""

    def __init__(self, name, id, monthly_salary, bonus_rate):
        super().__init__(name, id, monthly_salary)
        self.bonus_rate = bonus_rate

    def calculate_salary(self):
        """重写：计算工资（含奖金）"""
        base_salary = super().calculate_salary()
        bonus = base_salary * self.bonus_rate
        self.salary = base_salary + bonus
        return self.salary

# 多态：统一处理不同类型的员工
def process_payroll(employees):
    """处理工资（多态）"""
    total = 0
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.name}: ¥{salary:.2f}")
        total += salary
    print(f"总工资: ¥{total:.2f}")

# 使用
employees = [
    FullTimeEmployee('Alice', 'E001', 8000),
    PartTimeEmployee('Bob', 'E002', 100),
    Manager('Charlie', 'E003', 15000, 0.2)
]

# 兼职员工添加工作小时
employees[1].add_hours(80)

# 处理工资
process_payroll(employees)
```

### 示例 2：动物园管理系统

```python
class Animal:
    """动物基类"""

    def __init__(self, name, age):
        self._name = name        # 受保护属性
        self._age = age
        self.__health = 100      # 私有属性

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def health(self):
        return self.__health

    def eat(self):
        """吃东西（多态）"""
        raise NotImplementedError("子类必须实现 eat 方法")

    def make_sound(self):
        """发出声音（多态）"""
        raise NotImplementedError("子类必须实现 make_sound 方法")

    def get_info(self):
        """获取信息"""
        return f"{self.name} ({self.age}岁，健康度: {self.health})"

class Mammal(Animal):
    """哺乳动物"""

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

class Bird(Animal):
    """鸟类"""

    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

class Lion(Mammal):
    """狮子"""

    def __init__(self, name, age):
        super().__init__(name, age, '黄色')

    def eat(self):
        return f"{self.name} 正在吃肉"

    def make_sound(self):
        return "吼~"

    def hunt(self):
        return f"{self.name} 正在狩猎"

class Elephant(Mammal):
    """大象"""

    def __init__(self, name, age):
        super().__init__(name, age, '灰色')

    def eat(self):
        return f"{self.name} 正在吃草"

    def make_sound(self):
        return "嗷~"

class Parrot(Bird):
    """鹦鹉"""

    def __init__(self, name, age):
        super().__init__(name, age, True)

    def eat(self):
        return f"{self.name} 正在吃种子"

    def make_sound(self):
        return "你好！"

    def speak(self, words):
        return f"{self.name} 说: {words}"

class Zoo:
    """动物园"""

    def __init__(self, name):
        self.name = name
        self.__animals = []  # 私有属性

    def add_animal(self, animal):
        """添加动物"""
        self.__animals.append(animal)
        print(f"添加 {animal.name} 到 {self.name}")

    def feed_all(self):
        """喂养所有动物（多态）"""
        print(f"\n在 {self.name} 喂养动物:")
        for animal in self.__animals:
            print(f"  {animal.eat()}")

    def make_all_sound(self):
        """让所有动物发出声音（多态）"""
        print(f"\n{self.name} 的动物发出声音:")
        for animal in self.__animals:
            print(f"  {animal.name}: {animal.make_sound()}")

    def show_animals(self):
        """显示所有动物"""
        print(f"\n{self.name} 的动物:")
        for animal in self.__animals:
            print(f"  {animal.get_info()}")

# 使用
zoo = Zoo('北京动物园')

# 添加动物
lion = Lion('辛巴', 5)
elephant = Elephant('大力', 10)
parrot = Parrot('波利', 2)

zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(parrot)

# 展示动物
zoo.show_animals()

# 喂养（多态）
zoo.feed_all()

# 发出声音（多态）
zoo.make_all_sound()

# 特有方法
print(f"\n{lion.name} 的特殊技能: {lion.hunt()}")
print(f"{parrot.name} 的特殊技能: {parrot.speak('Python很有趣！')}")
```

---

## 总结

本章介绍了面向对象编程的三大特性：

### 7.1 封装
- **私有化**：使用双下划线实现私有属性和方法
- **私有属性**：隐藏内部数据，提供安全性
- **私有方法**：隐藏实现细节
- **property**：优雅的属性访问方式

### 7.2 继承
- **单继承**：一个子类继承一个父类
- **多继承**：一个子类继承多个父类
- **复用父类方法**：使用 super() 调用父类方法
- **方法重写**：子类重新定义父类方法
- **方法搜索**：MRO 确定方法查找顺序

### 7.3 多态
- **统一接口**：相同方法名，不同实现
- **灵活处理**：用统一方式处理不同对象
- **鸭子类型**：Python 的动态特性

这三大特性是面向对象编程的核心，掌握它们能够编写出更加灵活、可维护和可扩展的代码。

---

## 练习题

1. 创建一个银行账户类，使用封装保护账户余额
2. 实现一个形状类层次（继承），包括矩形、圆形、三角形
3. 创建一个交通工具类层次，实现多态的移动方法
4. 使用 property 实现温度类（支持摄氏度和华氏度转换）
5. 实现一个员工管理系统，使用继承和多态
6. 创建一个游戏角色类层次，包含不同类型的角色
7. 实现一个文件处理系统，支持不同类型的文件（多态）
8. 创建一个图书馆管理系统，使用封装、继承和多态
