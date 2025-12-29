# 第 2 章 流程控制

## 2.1 调序

程序的执行流程通常有三种基本结构：

1. **顺序结构**：代码按照从上到下的顺序依次执行
2. **分支结构**：根据条件选择不同的执行路径
3. **循环结构**：重复执行某段代码

```python
# 顺序结构示例
print("第一步")
print("第二步")
print("第三步")

# 分支结构示例
if True:
    print("条件为真")
else:
    print("条件为假")

# 循环结构示例
for i in range(3):
    print(f"第 {i+1} 次循环")
```

---

## 2.2 分支

分支结构允许程序根据条件选择不同的执行路径。Python 使用 `if`、`elif`、`else` 关键字来实现分支控制。

### 2.2.1 单分支

单分支结构只有一个 `if` 语句，当条件为真时执行代码块。

**语法**：
```python
if 条件:
    代码块
```

**示例**：
```python
# 判断年龄是否成年
age = 20
if age >= 18:
    print("你已经成年了")

# 判断成绩是否及格
score = 85
if score >= 60:
    print("恭喜你，考试及格了！")

# 判断数字是否为正数
number = 10
if number > 0:
    print(f"{number} 是正数")
```

### 2.2.2 双分支

双分支结构包含 `if` 和 `else`，当条件为真时执行 `if` 代码块，否则执行 `else` 代码块。

**语法**：
```python
if 条件:
    代码块1
else:
    代码块2
```

**示例**：
```python
# 判断奇偶数
number = 7
if number % 2 == 0:
    print(f"{number} 是偶数")
else:
    print(f"{number} 是奇数")

# 判断成绩是否及格
score = 55
if score >= 60:
    print("及格")
else:
    print("不及格")

# 判断用户年龄
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你可以观看此内容")
else:
    print("抱歉，你还未成年")
```

### 2.2.3 多分支

多分支结构使用 `if`、`elif`、`else` 组合，可以处理多个条件。

**语法**：
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
elif 条件3:
    代码块3
else:
    代码块4
```

**示例**：
```python
# 成绩等级判断
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"你的成绩等级是：{grade}")

# 季节判断
month = 5
if month in [12, 1, 2]:
    season = "冬季"
elif month in [3, 4, 5]:
    season = "春季"
elif month in [6, 7, 8]:
    season = "夏季"
elif month in [9, 10, 11]:
    season = "秋季"
else:
    season = "无效月份"
print(f"{month}月是{season}")

# BMI 指数判断
height = 1.75  # 米
weight = 70    # 千克
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "偏胖"
else:
    status = "肥胖"
print(f"你的 BMI 是 {bmi:.2f}，属于{status}")
```

### 2.2.4 嵌套分支

分支结构可以嵌套使用，即在一个分支内部再包含另一个分支。

**语法**：
```python
if 条件1:
    if 条件2:
        代码块1
    else:
        代码块2
else:
    代码块3
```

**示例**：
```python
# 用户登录验证
username = input("请输入用户名：")
if username == "admin":
    password = input("请输入密码：")
    if password == "123456":
        print("登录成功！")
    else:
        print("密码错误！")
else:
    print("用户名不存在！")

# 购票系统
age = int(input("请输入年龄："))
is_student = input("是否为学生？(y/n): ") == 'y'

if age < 18:
    print("儿童票：半价")
elif age >= 60:
    print("老年票：免费")
else:
    if is_student:
        print("学生票：8折")
    else:
        print("成人票：全价")

# 闰年判断（嵌套条件）
year = int(input("请输入年份："))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} 是闰年")
        else:
            print(f"{year} 不是闰年")
    else:
        print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
```

### 2.2.5 match case 语句

Python 3.10+ 引入了 `match case` 语句（结构模式匹配），类似于其他语言的 `switch case`。

**语法**：
```python
match 表达式:
    case 模式1:
        代码块1
    case 模式2:
        代码块2
    case _:
        默认代码块
```

**示例**：
```python
# 基本用法：匹配具体值
def get_weekday_name(day):
    match day:
        case 1:
            return "星期一"
        case 2:
            return "星期二"
        case 3:
            return "星期三"
        case 4:
            return "星期四"
        case 5:
            return "星期五"
        case 6:
            return "星期六"
        case 7:
            return "星期日"
        case _:
            return "无效的日期"

print(get_weekday_name(3))  # 星期三

# 匹配多个值
def check_status_code(code):
    match code:
        case 200:
            return "成功"
        case 404 | 403:  # 匹配多个值
            return "客户端错误"
        case 500 | 502 | 503:
            return "服务器错误"
        case _:
            return "未知错误"

print(check_status_code(404))  # 客户端错误

# 匹配序列
def process_command(command):
    match command:
        case ["quit"]:
            return "退出程序"
        case ["load", filename]:
            return f"加载文件：{filename}"
        case ["save", filename]:
            return f"保存文件：{filename}"
        case _:
            return "未知命令"

print(process_command(["load", "data.txt"]))  # 加载文件：data.txt

# 匹配字典
def process_user(user):
    match user:
        case {"name": name, "age": age} if age >= 18:
            return f"{name} 是成年人"
        case {"name": name, "age": age}:
            return f"{name} 是未成年人"
        case _:
            return "无效数据"

print(process_user({"name": "Alice", "age": 25}))  # Alice 是成年人
```

### 2.2.6 三目运算符

三目运算符（条件表达式）是一种简洁的条件判断方式，用于简单的 if-else 语句。

**语法**：
```python
值1 if 条件 else 值2
```

**示例**：
```python
# 基本用法
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(status)  # 成年人

# 比较传统 if-else
# 传统写法
if age >= 18:
    status = "成年人"
else:
    status = "未成年人"

# 三目运算符写法（更简洁）
status = "成年人" if age >= 18 else "未成年人"

# 求最大值
a = 10
b = 20
max_value = a if a > b else b
print(f"最大值是：{max_value}")  # 20

# 判断奇偶
number = 7
result = "奇数" if number % 2 != 0 else "偶数"
print(f"{number} 是{result}")  # 7 是奇数

# 嵌套三目运算符（不推荐，影响可读性）
score = 85
grade = 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'D'))
print(f"成绩等级：{grade}")  # B

# 实际应用：设置默认值
user_input = ""
username = user_input if user_input else "游客"
print(f"欢迎，{username}")  # 欢迎，游客

# 列表推导式中使用
numbers = [1, 2, 3, 4, 5, 6]
labels = ["奇数" if n % 2 != 0 else "偶数" for n in numbers]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数', '偶数']
```

---

## 2.3 循环

循环结构用于重复执行某段代码。Python 提供了 `while` 和 `for` 两种循环方式。

### 2.3.1 while 循环

`while` 循环会在条件为真时重复执行代码块。

**语法**：
```python
while 条件:
    代码块
```

**示例**：
```python
# 基本用法：打印 1 到 5
count = 1
while count <= 5:
    print(count)
    count += 1

# 计算 1 到 100 的和
sum_value = 0
number = 1
while number <= 100:
    sum_value += number
    number += 1
print(f"1 到 100 的和是：{sum_value}")  # 5050

# 用户输入验证
password = ""
while password != "123456":
    password = input("请输入密码：")
    if password != "123456":
        print("密码错误，请重试")
print("密码正确，登录成功！")

# 猜数字游戏
import random
target = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("请猜一个 1-100 之间的数字："))
    attempts += 1

    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print(f"恭喜你猜对了！用了 {attempts} 次")
        break

# 计算阶乘
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")  # 120

# 无限循环（需要手动中断）
# while True:
#     print("这是一个无限循环")
#     # 使用 break 退出
```

### 2.3.2 for 循环

`for` 循环用于遍历序列（如列表、元组、字符串、范围等）。

**语法**：
```python
for 变量 in 序列:
    代码块
```

**示例**：
```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 遍历字符串
word = "Python"
for char in word:
    print(char)

# 使用 range() 函数
# range(n): 0 到 n-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop): start 到 stop-1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step): 指定步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 倒序遍历
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

# 遍历字典
person = {"name": "Alice", "age": 25, "city": "北京"}

# 遍历键
for key in person:
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")

# 使用 enumerate() 获取索引
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 从指定索引开始
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 嵌套循环：打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行

# 列表推导式（更简洁的 for 循环）
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 条件过滤
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### 2.3.3 continue

`continue` 语句用于跳过当前循环的剩余部分，直接进入下一次循环。

**示例**：
```python
# 跳过偶数，只打印奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)  # 只打印奇数: 1, 3, 5, 7, 9

# 跳过特定值
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
for fruit in fruits:
    if fruit == "橙子":
        continue  # 跳过橙子
    print(f"我喜欢吃{fruit}")

# while 循环中使用 continue
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue  # 跳过 3 的倍数
    print(count)  # 1, 2, 4, 5, 7, 8, 10

# 实际应用：数据过滤
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_sum = 0
for num in numbers:
    if num < 0:
        continue  # 跳过负数
    positive_sum += num
print(f"正数之和：{positive_sum}")  # 25

# 跳过空字符串
words = ["hello", "", "world", "", "python"]
for word in words:
    if not word:
        continue
    print(word.upper())  # HELLO, WORLD, PYTHON
```

### 2.3.4 break

`break` 语句用于完全终止循环，跳出循环体。

**示例**：
```python
# 找到第一个偶数就退出
for i in range(1, 11):
    if i % 2 == 0:
        print(f"找到第一个偶数：{i}")
        break

# 在列表中查找元素
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
target = "橙子"
for fruit in fruits:
    if fruit == target:
        print(f"找到了：{fruit}")
        break
else:
    print(f"没有找到：{target}")

# while 循环中使用 break
count = 1
while True:
    print(count)
    if count >= 5:
        break  # 当 count 达到 5 时退出
    count += 1

# 用户输入验证（限制尝试次数）
max_attempts = 3
attempts = 0
password = "123456"

while attempts < max_attempts:
    user_input = input("请输入密码：")
    attempts += 1

    if user_input == password:
        print("密码正确，登录成功！")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"密码错误，还有 {remaining} 次机会")
        else:
            print("密码错误次数过多，账户已锁定")

# 嵌套循环中的 break（只跳出当前循环）
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break  # 只跳出内层循环
        print(f"i={i}, j={j}")
    print(f"外层循环 i={i} 结束")

# 查找质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # 找到因数，不是质数
    return True

# 找出前 10 个质数
count = 0
number = 2
while count < 10:
    if is_prime(number):
        print(number, end=" ")
        count += 1
    number += 1
# 输出: 2 3 5 7 11 13 17 19 23 29
```

### 2.3.5 pass

`pass` 是一个空语句，不执行任何操作，通常用作占位符。

**示例**：
```python
# 占位符：稍后实现的函数
def future_function():
    pass  # TODO: 稍后实现

# 空的类定义
class EmptyClass:
    pass

# 条件语句中的占位符
x = 10
if x > 5:
    pass  # 暂时不做任何处理
else:
    print("x <= 5")

# 循环中的占位符
for i in range(10):
    if i % 2 == 0:
        pass  # 偶数暂不处理
    else:
        print(i)

# 异常处理中使用
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # 忽略除零错误

# 实际应用：保留结构，稍后填充
def process_data(data):
    # 验证数据
    if not data:
        pass  # TODO: 添加错误处理

    # 处理数据
    pass  # TODO: 实现数据处理逻辑

    # 返回结果
    pass  # TODO: 返回处理结果

# 与 continue 的区别
# pass: 什么都不做，继续执行后面的代码
# continue: 跳过当前循环的剩余部分，进入下一次循环

for i in range(5):
    if i == 2:
        pass  # 什么都不做，继续执行 print
    print(i)  # 输出: 0, 1, 2, 3, 4

for i in range(5):
    if i == 2:
        continue  # 跳过 print
    print(i)  # 输出: 0, 1, 3, 4
```

---

## 循环控制语句对比

| 语句 | 作用 | 使用场景 |
|------|------|----------|
| `break` | 终止整个循环 | 找到目标后提前退出 |
| `continue` | 跳过当前迭代，进入下一次循环 | 跳过某些不需要处理的情况 |
| `pass` | 什么都不做，占位符 | 保留代码结构，稍后实现 |

**示例对比**：
```python
# break: 找到 5 就停止
for i in range(10):
    if i == 5:
        break
    print(i)  # 输出: 0, 1, 2, 3, 4

# continue: 跳过 5
for i in range(10):
    if i == 5:
        continue
    print(i)  # 输出: 0, 1, 2, 3, 4, 6, 7, 8, 9

# pass: 遇到 5 也打印
for i in range(10):
    if i == 5:
        pass
    print(i)  # 输出: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

## for-else 和 while-else

Python 的循环结构支持 `else` 子句，当循环正常结束（没有被 `break` 中断）时执行。

**示例**：
```python
# for-else
for i in range(5):
    print(i)
else:
    print("循环正常结束")
# 输出: 0, 1, 2, 3, 4, 循环正常结束

# 使用 break 时不执行 else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("循环正常结束")  # 不会执行
# 输出: 0, 1, 2

# 实际应用：查找元素
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"找到了 {target}")
        break
else:
    print(f"没有找到 {target}")
# 输出: 没有找到 6

# while-else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("while 循环正常结束")
# 输出: 0, 1, 2, 3, 4, while 循环正常结束
```

---

## 综合示例

### 示例 1：打印图形
```python
# 直角三角形
n = 5
for i in range(1, n + 1):
    print('*' * i)

# 输出:
# *
# **
# ***
# ****
# *****

# 等腰三角形
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 输出:
#     *
#    ***
#   *****
#  *******
# *********
```

### 示例 2：菲波那契数列
```python
# 打印前 10 个菲波那契数
n = 10
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
# 输出: 0 1 1 2 3 5 8 13 21 34
```

### 示例 3：简易 ATM 系统
```python
balance = 1000  # 初始余额

while True:
    print("\n=== ATM 系统 ===")
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")

    choice = input("请选择操作（1-4）：")

    if choice == '1':
        print(f"当前余额：{balance} 元")

    elif choice == '2':
        amount = float(input("请输入存款金额："))
        if amount > 0:
            balance += amount
            print(f"存款成功！当前余额：{balance} 元")
        else:
            print("金额无效！")

    elif choice == '3':
        amount = float(input("请输入取款金额："))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"取款成功！当前余额：{balance} 元")
            else:
                print("余额不足！")
        else:
            print("金额无效！")

    elif choice == '4':
        print("谢谢使用，再见！")
        break

    else:
        print("无效的选择，请重试！")
```

---

## 总结

本章介绍了 Python 的流程控制，包括：

1. **顺序结构**：代码按顺序执行
2. **分支结构**：
   - 单分支（if）
   - 双分支（if-else）
   - 多分支（if-elif-else）
   - 嵌套分支
   - match-case 语句（Python 3.10+）
   - 三目运算符
3. **循环结构**：
   - while 循环：条件循环
   - for 循环：遍历序列
4. **循环控制**：
   - break：终止循环
   - continue：跳过当前迭代
   - pass：占位符
5. **循环的 else 子句**

掌握流程控制是编程的基础，通过合理使用分支和循环，可以实现复杂的程序逻辑。

---

## 练习题

1. 编写程序判断一个数是否为质数
2. 打印 99 乘法表
3. 编写猜数字游戏（1-100，给出提示"太大"或"太小"）
4. 计算 1! + 2! + 3! + ... + n!
5. 使用循环实现字符串反转
6. 编写简单的学生成绩管理系统（可以添加、查询、统计成绩）
7. 打印杨辉三角的前 n 行
8. 找出 100 以内的所有完数（完数等于其所有因子之和）
