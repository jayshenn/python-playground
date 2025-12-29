# 第 8 章 异常捕获与异常

在程序运行过程中，难免会出现各种错误。如果不进行处理，程序会崩溃并终止运行。Python 提供了异常处理机制，让我们能够优雅地处理错误，提高程序的健壮性。

---

## 8.1 异常介绍

**异常**（Exception）是程序运行时发生的错误事件。当 Python 检测到错误时，会抛出异常，如果不处理，程序就会终止。

### 8.1.1 语法错误

**语法错误**（Syntax Error）是代码不符合 Python 语法规则导致的错误，发生在代码执行之前（解析阶段）。

```python
# 语法错误示例

# 1. 缺少冒号
# if True
#     print("Hello")
# SyntaxError: invalid syntax

# 2. 缩进错误
# def greet():
# print("Hello")
# IndentationError: expected an indented block

# 3. 括号不匹配
# print("Hello"
# SyntaxError: unexpected EOF while parsing

# 4. 非法字符
# print("你好）
# SyntaxError: invalid character

# 5. 关键字使用错误
# class = 10
# SyntaxError: invalid syntax
```

**语法错误的特点**：
- 在代码运行之前就能发现
- 必须修改代码才能解决
- 无法通过异常处理捕获
- IDE 通常会标记语法错误

### 8.1.2 异常

**异常**（Exception）是程序运行时发生的错误，代码语法正确但执行时出现问题。

```python
# 异常示例

# 1. 除零错误
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零")

# 2. 类型错误
try:
    result = '10' + 5
except TypeError:
    print("类型不匹配")

# 3. 名称错误
try:
    print(undefined_variable)
except NameError:
    print("变量未定义")

# 4. 索引错误
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("索引超出范围")

# 5. 键错误
try:
    data = {'name': 'Alice'}
    print(data['age'])
except KeyError:
    print("键不存在")

# 6. 文件不存在错误
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")
```

**异常的特点**：
- 在代码运行时发生
- 可以通过异常处理捕获
- 不处理会导致程序崩溃
- 可以预防和处理

**语法错误 vs 异常**：

| 特性 | 语法错误 | 异常 |
|------|---------|------|
| **发生时机** | 代码解析时 | 代码运行时 |
| **能否执行** | 不能执行 | 执行到错误处才停止 |
| **是否可捕获** | 不能 | 可以 |
| **解决方法** | 修改代码 | 异常处理或修改代码 |
| **示例** | `if True print()` | `1/0` |

---

## 8.2 异常处理

异常处理允许程序在发生错误时继续运行，而不是崩溃。

### 8.2.1 try except

`try...except` 是 Python 异常处理的基本语法。

**基本语法**：
```python
try:
    # 可能发生异常的代码
    可能出错的代码
except:
    # 发生异常时执行的代码
    异常处理代码
```

**基本示例**：

```python
# 示例 1：处理除零错误
try:
    num1 = int(input("请输入被除数: "))
    num2 = int(input("请输入除数: "))
    result = num1 / num2
    print(f"结果: {result}")
except:
    print("发生了错误，无法计算")

# 示例 2：处理文件读取错误
try:
    with open('data.txt', 'r') as f:
        content = f.read()
        print(content)
except:
    print("无法读取文件")

# 示例 3：处理列表索引错误
try:
    numbers = [1, 2, 3]
    index = int(input("请输入索引: "))
    print(numbers[index])
except:
    print("索引无效")
```

**注意**：不推荐使用空的 `except`，因为它会捕获所有异常，包括系统退出信号等。

### 8.2.2 捕获指定类型的异常以及获取异常描述信息

**捕获特定异常**：

```python
# 捕获特定类型的异常
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果: {result}")
except ValueError:
    print("输入无效，请输入数字")
except ZeroDivisionError:
    print("除数不能为零")
```

**捕获多个异常**：

```python
# 方法 1：分别捕获
try:
    data = [1, 2, 3]
    index = int(input("请输入索引: "))
    print(data[index])
except ValueError:
    print("请输入整数")
except IndexError:
    print("索引超出范围")

# 方法 2：一起捕获（使用元组）
try:
    data = [1, 2, 3]
    index = int(input("请输入索引: "))
    print(data[index])
except (ValueError, IndexError):
    print("输入错误或索引超出范围")
```

**获取异常信息**：

```python
# 使用 as 获取异常对象
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误类型: {type(e).__name__}")
    print(f"错误信息: {e}")
    print(f"错误详情: {repr(e)}")

# 输出:
# 错误类型: ZeroDivisionError
# 错误信息: division by zero
# 错误详情: ZeroDivisionError('division by zero')
```

**捕获所有异常（使用 Exception）**：

```python
try:
    # 可能发生各种异常的代码
    num = int(input("请输入数字: "))
    result = 10 / num
    data = [1, 2, 3]
    print(data[num])
except Exception as e:
    print(f"发生异常: {type(e).__name__}")
    print(f"异常信息: {e}")
```

**异常处理最佳实践**：

```python
# 好的做法：明确捕获特定异常
try:
    with open('data.txt', 'r') as f:
        data = f.read()
        value = int(data)
except FileNotFoundError:
    print("文件不存在")
except ValueError:
    print("文件内容不是有效的数字")
except PermissionError:
    print("没有权限读取文件")

# 不好的做法：捕获所有异常
try:
    with open('data.txt', 'r') as f:
        data = f.read()
        value = int(data)
except:  # 不推荐：太宽泛
    print("发生了某种错误")
```

### 8.2.3 else

`else` 子句在 `try` 块没有发生异常时执行。

**语法**：
```python
try:
    # 可能发生异常的代码
except 异常类型:
    # 处理异常
else:
    # 没有异常时执行
```

**示例**：

```python
# 示例 1：文件读取
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    else:
        print("文件读取成功")
        print(f"内容: {content}")

read_file('data.txt')

# 示例 2：除法运算
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
    except TypeError:
        print("错误：参数必须是数字")
    else:
        print(f"计算成功，结果: {result}")
        return result

divide(10, 2)   # 计算成功，结果: 5.0
divide(10, 0)   # 错误：除数不能为零
divide(10, '2') # 错误：参数必须是数字

# 示例 3：用户输入验证
def get_positive_number():
    try:
        num = int(input("请输入一个正整数: "))
        if num <= 0:
            raise ValueError("数字必须为正数")
    except ValueError as e:
        print(f"输入无效: {e}")
        return None
    else:
        print("输入有效")
        return num

result = get_positive_number()
```

**else 的优点**：
- 代码逻辑更清晰
- 区分"正常流程"和"异常处理"
- 避免在 try 块中放置过多代码

### 8.2.4 finally

`finally` 子句无论是否发生异常都会执行，通常用于清理资源。

**语法**：
```python
try:
    # 可能发生异常的代码
except 异常类型:
    # 处理异常
else:
    # 没有异常时执行
finally:
    # 无论如何都执行
```

**示例**：

```python
# 示例 1：文件操作
def process_file(filename):
    file = None
    try:
        print("打开文件")
        file = open(filename, 'r')
        content = file.read()
        print(f"文件内容: {content}")
    except FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print(f"发生错误: {e}")
    else:
        print("文件处理成功")
    finally:
        print("清理资源")
        if file:
            file.close()
            print("文件已关闭")

process_file('data.txt')

# 示例 2：数据库连接
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def connect(self):
        print(f"连接到数据库 {self.db_name}")
        self.connected = True

    def query(self, sql):
        if not self.connected:
            raise Exception("未连接到数据库")
        print(f"执行查询: {sql}")
        return "查询结果"

    def close(self):
        if self.connected:
            print("关闭数据库连接")
            self.connected = False

def database_operation():
    db = DatabaseConnection('mydb')
    try:
        db.connect()
        result = db.query("SELECT * FROM users")
        print(f"结果: {result}")
    except Exception as e:
        print(f"数据库操作失败: {e}")
    finally:
        db.close()  # 确保连接被关闭

database_operation()

# 示例 3：计数器
def process_with_counter():
    counter = 0
    try:
        counter += 1
        print(f"处理步骤 {counter}")
        result = 10 / 0  # 故意制造异常
        counter += 1
        print(f"处理步骤 {counter}")
    except ZeroDivisionError:
        print("发生除零错误")
    finally:
        print(f"总共执行了 {counter} 个步骤")
        print("清理完成")

process_with_counter()
```

**完整的异常处理流程**：

```python
def complete_example():
    """完整的异常处理示例"""
    try:
        print("1. 开始执行 try 块")
        num = int(input("请输入数字: "))
        result = 10 / num
        print(f"2. 计算结果: {result}")
    except ValueError:
        print("3a. 捕获 ValueError：输入不是数字")
    except ZeroDivisionError:
        print("3b. 捕获 ZeroDivisionError：除数为零")
    else:
        print("4. 没有异常，执行 else 块")
    finally:
        print("5. 无论如何都执行 finally 块")

complete_example()

# 输入 5 时的输出:
# 1. 开始执行 try 块
# 2. 计算结果: 2.0
# 4. 没有异常，执行 else 块
# 5. 无论如何都执行 finally 块

# 输入 0 时的输出:
# 1. 开始执行 try 块
# 3b. 捕获 ZeroDivisionError：除数为零
# 5. 无论如何都执行 finally 块

# 输入 abc 时的输出:
# 1. 开始执行 try 块
# 3a. 捕获 ValueError：输入不是数字
# 5. 无论如何都执行 finally 块
```

**finally 的应用场景**：
- 关闭文件
- 释放数据库连接
- 释放网络连接
- 清理临时资源
- 记录日志

---

## 8.3 抛出异常

除了处理异常，我们也可以主动抛出异常。

### 8.3.1 raise

使用 `raise` 语句可以主动抛出异常。

**基本语法**：
```python
raise 异常类型("异常信息")
```

**示例**：

```python
# 示例 1：检查年龄
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过 150")
    print(f"年龄设置为: {age}")

try:
    set_age(200)
except ValueError as e:
    print(f"错误: {e}")

# 示例 2：检查用户权限
def delete_user(user_id, current_user_role):
    if current_user_role != 'admin':
        raise PermissionError("只有管理员可以删除用户")
    print(f"删除用户 {user_id}")

try:
    delete_user(123, 'user')
except PermissionError as e:
    print(f"权限错误: {e}")

# 示例 3：检查文件类型
def process_image(filename):
    if not filename.endswith(('.jpg', '.png', '.gif')):
        raise TypeError(f"不支持的文件类型: {filename}")
    print(f"处理图片: {filename}")

try:
    process_image('document.pdf')
except TypeError as e:
    print(f"类型错误: {e}")
```

**重新抛出异常**：

```python
def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError as e:
        print(f"数据转换失败: {e}")
        raise  # 重新抛出当前异常

try:
    process_data("abc")
except ValueError:
    print("在外层捕获到重新抛出的异常")
```

**抛出不同的异常**：

```python
def read_config(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        # 将 FileNotFoundError 转换为自定义异常
        raise RuntimeError(f"配置文件缺失: {filename}")

try:
    read_config('config.ini')
except RuntimeError as e:
    print(f"运行时错误: {e}")
```

### 8.3.2 assert 断言

`assert` 用于在开发阶段检查条件是否满足，不满足则抛出 `AssertionError`。

**基本语法**：
```python
assert 条件, "错误信息"
```

**示例**：

```python
# 示例 1：检查参数
def calculate_average(numbers):
    assert len(numbers) > 0, "列表不能为空"
    assert all(isinstance(n, (int, float)) for n in numbers), "所有元素必须是数字"
    return sum(numbers) / len(numbers)

try:
    print(calculate_average([1, 2, 3]))  # 2.0
    print(calculate_average([]))         # AssertionError: 列表不能为空
except AssertionError as e:
    print(f"断言错误: {e}")

# 示例 2：检查状态
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        assert amount > 0, "取款金额必须大于 0"
        assert amount <= self.balance, "余额不足"
        self.balance -= amount
        return self.balance

account = BankAccount(1000)
try:
    account.withdraw(500)   # 成功
    account.withdraw(-100)  # AssertionError: 取款金额必须大于 0
except AssertionError as e:
    print(f"断言错误: {e}")

# 示例 3：检查数据完整性
def process_user_data(user):
    assert 'name' in user, "用户数据缺少 name 字段"
    assert 'email' in user, "用户数据缺少 email 字段"
    assert '@' in user['email'], "邮箱格式无效"
    print(f"处理用户: {user['name']}")

try:
    process_user_data({'name': 'Alice', 'email': 'alice@example.com'})  # 成功
    process_user_data({'name': 'Bob'})  # AssertionError: 用户数据缺少 email 字段
except AssertionError as e:
    print(f"数据验证失败: {e}")
```

**assert vs raise**：

| 特性 | assert | raise |
|------|--------|-------|
| **用途** | 开发时调试 | 生产环境错误处理 |
| **可禁用** | 可以（`python -O`） | 不能 |
| **异常类型** | 总是 AssertionError | 可以指定任何异常 |
| **使用场景** | 检查内部逻辑 | 处理外部输入 |

```python
# assert：开发调试
def divide(a, b):
    assert b != 0, "除数不能为零（内部检查）"
    return a / b

# raise：生产环境
def safe_divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
```

**注意**：不要在生产代码中依赖 `assert` 进行错误检查，因为 assert 可以被禁用。

---

## 8.4 自定义异常

可以通过继承 `Exception` 类来创建自定义异常。

**基本语法**：
```python
class 自定义异常名(Exception):
    pass
```

**简单示例**：

```python
# 示例 1：自定义异常
class InvalidAgeError(Exception):
    """年龄无效异常"""
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"年龄必须在 0-150 之间，当前值: {age}")
    print(f"年龄设置为: {age}")

try:
    set_age(200)
except InvalidAgeError as e:
    print(f"自定义异常: {e}")
```

**带额外信息的自定义异常**：

```python
class ValidationError(Exception):
    """数据验证异常"""

    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        self.message = message
        super().__init__(f"{field} 验证失败: {message} (值: {value})")

def validate_email(email):
    if '@' not in email:
        raise ValidationError('email', email, '缺少 @ 符号')
    if '.' not in email.split('@')[1]:
        raise ValidationError('email', email, '域名格式无效')
    return True

try:
    validate_email('invalid-email')
except ValidationError as e:
    print(f"字段: {e.field}")
    print(f"值: {e.value}")
    print(f"错误: {e.message}")
```

**自定义异常层次**：

```python
# 异常基类
class AppError(Exception):
    """应用程序异常基类"""
    pass

# 具体异常
class DatabaseError(AppError):
    """数据库异常"""
    pass

class NetworkError(AppError):
    """网络异常"""
    pass

class AuthenticationError(AppError):
    """认证异常"""
    pass

class PermissionDeniedError(AppError):
    """权限拒绝异常"""
    pass

# 使用
def connect_database(host, port):
    if not host:
        raise DatabaseError("数据库主机未指定")
    print(f"连接到 {host}:{port}")

def authenticate_user(username, password):
    if not username or not password:
        raise AuthenticationError("用户名或密码为空")
    if username != 'admin':
        raise PermissionDeniedError(f"用户 {username} 没有权限")
    print("认证成功")

# 捕获所有应用异常
try:
    connect_database('', 3306)
    authenticate_user('guest', '123')
except AppError as e:
    print(f"应用错误: {type(e).__name__} - {e}")
```

**实际应用示例**：

```python
class InsufficientFundsError(Exception):
    """余额不足异常"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"余额不足: 当前余额 {balance}，需要 {amount}"
        super().__init__(message)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self.balance += amount
        return self.balance

# 使用
account = BankAccount('Alice', 1000)

try:
    account.withdraw(500)   # 成功
    account.withdraw(1000)  # 余额不足
except InsufficientFundsError as e:
    print(f"错误: {e}")
    print(f"当前余额: {e.balance}")
    print(f"尝试取款: {e.amount}")
    print(f"差额: {e.amount - e.balance}")
```

---

## 8.5 异常的传递

异常会沿着调用栈向上传递，直到被捕获或导致程序终止。

**基本示例**：

```python
def func1():
    print("func1 开始")
    func2()
    print("func1 结束")  # 不会执行

def func2():
    print("func2 开始")
    func3()
    print("func2 结束")  # 不会执行

def func3():
    print("func3 开始")
    result = 10 / 0  # 抛出异常
    print("func3 结束")  # 不会执行

try:
    func1()
except ZeroDivisionError:
    print("在最外层捕获异常")

# 输出:
# func1 开始
# func2 开始
# func3 开始
# 在最外层捕获异常
```

**异常传递流程**：

```python
def level1():
    """第一层：抛出异常"""
    print("Level 1: 开始")
    raise ValueError("在 level1 发生错误")
    print("Level 1: 结束")  # 不会执行

def level2():
    """第二层：不处理异常，继续传递"""
    print("Level 2: 开始")
    level1()
    print("Level 2: 结束")  # 不会执行

def level3():
    """第三层：捕获并处理异常"""
    print("Level 3: 开始")
    try:
        level2()
    except ValueError as e:
        print(f"Level 3: 捕获异常 - {e}")
    print("Level 3: 结束")

level3()

# 输出:
# Level 3: 开始
# Level 2: 开始
# Level 1: 开始
# Level 3: 捕获异常 - 在 level1 发生错误
# Level 3: 结束
```

**部分处理异常**：

```python
def read_data():
    """读取数据"""
    raise IOError("无法读取数据")

def process_data():
    """处理数据"""
    try:
        data = read_data()
    except IOError as e:
        print(f"处理层捕获: {e}")
        raise  # 重新抛出异常

def main():
    """主函数"""
    try:
        process_data()
    except IOError:
        print("主函数捕获异常")

main()

# 输出:
# 处理层捕获: 无法读取数据
# 主函数捕获异常
```

**异常传递的应用**：

```python
class DataProcessor:
    """数据处理器"""

    def validate(self, data):
        """验证数据"""
        if not data:
            raise ValueError("数据不能为空")
        if not isinstance(data, list):
            raise TypeError("数据必须是列表")

    def transform(self, data):
        """转换数据"""
        self.validate(data)  # 可能抛出异常
        return [x * 2 for x in data]

    def save(self, data):
        """保存数据"""
        transformed = self.transform(data)  # 可能抛出异常
        print(f"保存数据: {transformed}")

    def process(self, data):
        """处理数据（入口）"""
        try:
            self.save(data)
        except ValueError as e:
            print(f"验证错误: {e}")
        except TypeError as e:
            print(f"类型错误: {e}")
        except Exception as e:
            print(f"未知错误: {e}")

processor = DataProcessor()
processor.process([1, 2, 3])  # 成功
processor.process(None)       # 验证错误
processor.process("abc")      # 类型错误
```

---

## 8.6 with 关键字

`with` 语句用于自动管理资源（如文件、网络连接），确保资源正确释放。

### 8.6.1 语法

**基本语法**：
```python
with 表达式 as 变量:
    # 使用资源的代码块
```

**示例**：

```python
# 传统方式（不推荐）
file = open('data.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()

# 使用 with（推荐）
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# 自动关闭文件
```

### 8.6.2 工作原理

`with` 语句使用**上下文管理器**（Context Manager）来管理资源。

**上下文管理器的方法**：
- `__enter__()`: 进入 with 块时调用
- `__exit__()`: 离开 with 块时调用

```python
class MyContext:
    """自定义上下文管理器"""

    def __enter__(self):
        print("进入 with 块")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("离开 with 块")
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")
        return False  # 不抑制异常

    def do_something(self):
        print("执行操作")

# 使用
with MyContext() as ctx:
    ctx.do_something()

# 输出:
# 进入 with 块
# 执行操作
# 离开 with 块
```

**带异常处理的上下文管理器**：

```python
class FileManager:
    """文件管理器"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"关闭文件: {self.filename}")
            self.file.close()

        if exc_type:
            print(f"发生异常: {exc_val}")
            return False  # 不抑制异常
        return True

# 使用
try:
    with FileManager('test.txt', 'w') as f:
        f.write('Hello, World!')
        raise ValueError("测试异常")
except ValueError:
    print("外层捕获异常")

# 输出:
# 打开文件: test.txt
# 关闭文件: test.txt
# 发生异常: 测试异常
# 外层捕获异常
```

**使用 contextlib 简化**：

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    """简化的上下文管理器"""
    print("进入上下文")
    try:
        yield "资源对象"
    finally:
        print("离开上下文")

with my_context() as resource:
    print(f"使用资源: {resource}")

# 输出:
# 进入上下文
# 使用资源: 资源对象
# 离开上下文
```

### 8.6.3 案例：打开一个文件并且其中的内容，验证出现异常时文件是否正常关闭

```python
# 不使用 with：需要手动关闭
def read_file_without_with(filename):
    """不使用 with（不推荐）"""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        # 故意制造异常
        result = 10 / 0
        return content
    except ZeroDivisionError:
        print("发生除零错误")
    finally:
        if file:
            file.close()
            print("文件已关闭（手动）")

# 使用 with：自动关闭
def read_file_with_with(filename):
    """使用 with（推荐）"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # 故意制造异常
            result = 10 / 0
            return content
    except ZeroDivisionError:
        print("发生除零错误")
    # 文件自动关闭

# 创建测试文件
with open('test.txt', 'w') as f:
    f.write('测试内容')

# 测试
print("=== 不使用 with ===")
read_file_without_with('test.txt')

print("\n=== 使用 with ===")
read_file_with_with('test.txt')
```

**验证文件是否关闭**：

```python
def test_file_closure():
    """验证文件是否正确关闭"""

    # 测试 1：正常情况
    print("测试 1: 正常情况")
    with open('test.txt', 'w') as f:
        print(f"文件打开: {not f.closed}")
    print(f"with 块外，文件关闭: {f.closed}")

    # 测试 2：异常情况
    print("\n测试 2: 发生异常")
    try:
        with open('test.txt', 'w') as f:
            print(f"文件打开: {not f.closed}")
            raise ValueError("测试异常")
    except ValueError:
        print(f"异常发生后，文件关闭: {f.closed}")

    # 测试 3：多个文件
    print("\n测试 3: 同时打开多个文件")
    with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
        print(f"文件1打开: {not f1.closed}, 文件2打开: {not f2.closed}")
    print(f"with 块外，文件1关闭: {f1.closed}, 文件2关闭: {f2.closed}")

test_file_closure()
```

---

## 8.7 Python 常见异常

### 8.7.1 异常基类

Python 的所有异常都继承自 `BaseException`。

**异常层次结构**：
```
BaseException
├── SystemExit          # sys.exit() 调用
├── KeyboardInterrupt   # Ctrl+C 中断
├── GeneratorExit       # 生成器关闭
└── Exception           # 所有常规异常的基类
    ├── StopIteration   # 迭代器结束
    ├── ArithmeticError # 算术错误
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError  # assert 失败
    ├── AttributeError  # 属性不存在
    ├── EOFError        # input() 到达文件末尾
    ├── ImportError     # 导入失败
    ├── LookupError     # 查找错误
    │   ├── IndexError  # 索引超出范围
    │   └── KeyError    # 键不存在
    ├── NameError       # 变量未定义
    ├── OSError         # 操作系统错误
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── ...
    ├── RuntimeError    # 运行时错误
    ├── SyntaxError     # 语法错误
    ├── TypeError       # 类型错误
    ├── ValueError      # 值错误
    └── ...
```

### 8.7.2 具体异常

#### 常见异常类型

```python
# 1. ZeroDivisionError：除零错误
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")

# 2. TypeError：类型错误
try:
    result = '10' + 5
except TypeError as e:
    print(f"类型错误: {e}")

# 3. ValueError：值错误
try:
    num = int('abc')
except ValueError as e:
    print(f"值错误: {e}")

# 4. NameError：名称错误
try:
    print(undefined_variable)
except NameError as e:
    print(f"名称错误: {e}")

# 5. IndexError：索引错误
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"索引错误: {e}")

# 6. KeyError：键错误
try:
    data = {'name': 'Alice'}
    print(data['age'])
except KeyError as e:
    print(f"键错误: {e}")

# 7. AttributeError：属性错误
try:
    value = None
    value.append(1)
except AttributeError as e:
    print(f"属性错误: {e}")

# 8. FileNotFoundError：文件不存在
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"文件不存在: {e}")

# 9. PermissionError：权限错误
try:
    with open('/root/protected.txt', 'w') as f:
        f.write('test')
except PermissionError as e:
    print(f"权限错误: {e}")

# 10. ImportError / ModuleNotFoundError：导入错误
try:
    import nonexistent_module
except ModuleNotFoundError as e:
    print(f"模块不存在: {e}")

# 11. StopIteration：迭代结束
try:
    it = iter([1, 2, 3])
    next(it)
    next(it)
    next(it)
    next(it)  # 超出范围
except StopIteration:
    print("迭代结束")

# 12. AssertionError：断言失败
try:
    assert 1 == 2, "1 不等于 2"
except AssertionError as e:
    print(f"断言错误: {e}")

# 13. RuntimeError：运行时错误
class MyClass:
    def __init__(self):
        self.__init__()  # 递归深度超限

try:
    obj = MyClass()
except RecursionError as e:
    print(f"递归错误: {e}")

# 14. UnicodeError：编码错误
try:
    text = b'\x80abc'
    text.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"解码错误: {e}")
```

**异常速查表**：

| 异常类型 | 说明 | 示例 |
|---------|------|------|
| **ZeroDivisionError** | 除数为零 | `10 / 0` |
| **TypeError** | 类型不匹配 | `'10' + 5` |
| **ValueError** | 值错误 | `int('abc')` |
| **NameError** | 变量未定义 | `print(x)` |
| **IndexError** | 索引超出范围 | `[1, 2][10]` |
| **KeyError** | 字典键不存在 | `{'a': 1}['b']` |
| **AttributeError** | 属性不存在 | `None.append(1)` |
| **FileNotFoundError** | 文件不存在 | `open('x.txt')` |
| **PermissionError** | 权限不足 | 读写受保护文件 |
| **ImportError** | 导入失败 | `import xxx` |
| **AssertionError** | 断言失败 | `assert False` |
| **RuntimeError** | 运行时错误 | 递归深度超限 |

---

## 综合示例

### 示例 1：文件处理系统

```python
class FileProcessor:
    """文件处理器"""

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """读取文件"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return content
        except FileNotFoundError:
            print(f"错误：文件 {self.filename} 不存在")
            return None
        except PermissionError:
            print(f"错误：没有权限读取文件 {self.filename}")
            return None
        except UnicodeDecodeError:
            print(f"错误：文件编码格式错误")
            return None
        except Exception as e:
            print(f"未知错误: {e}")
            return None

    def write_file(self, content):
        """写入文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"成功写入文件: {self.filename}")
                return True
        except PermissionError:
            print(f"错误：没有权限写入文件 {self.filename}")
            return False
        except Exception as e:
            print(f"写入失败: {e}")
            return False
        finally:
            print("文件操作完成")

    def append_file(self, content):
        """追加到文件"""
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(content)
                print(f"成功追加到文件: {self.filename}")
                return True
        except Exception as e:
            print(f"追加失败: {e}")
            return False

# 使用
processor = FileProcessor('test.txt')
processor.write_file('第一行\n')
processor.append_file('第二行\n')
content = processor.read_file()
print(content)
```

### 示例 2：用户注册系统

```python
class RegistrationError(Exception):
    """注册异常基类"""
    pass

class InvalidUsernameError(RegistrationError):
    """用户名无效"""
    pass

class InvalidPasswordError(RegistrationError):
    """密码无效"""
    pass

class UserExistsError(RegistrationError):
    """用户已存在"""
    pass

class UserRegistration:
    """用户注册"""

    def __init__(self):
        self.users = set()

    def validate_username(self, username):
        """验证用户名"""
        if not username:
            raise InvalidUsernameError("用户名不能为空")
        if len(username) < 3:
            raise InvalidUsernameError("用户名至少 3 个字符")
        if not username.isalnum():
            raise InvalidUsernameError("用户名只能包含字母和数字")
        return True

    def validate_password(self, password):
        """验证密码"""
        if not password:
            raise InvalidPasswordError("密码不能为空")
        if len(password) < 6:
            raise InvalidPasswordError("密码至少 6 个字符")
        if not any(c.isdigit() for c in password):
            raise InvalidPasswordError("密码必须包含数字")
        if not any(c.isalpha() for c in password):
            raise InvalidPasswordError("密码必须包含字母")
        return True

    def register(self, username, password):
        """注册用户"""
        try:
            # 验证用户名
            self.validate_username(username)

            # 验证密码
            self.validate_password(password)

            # 检查用户是否已存在
            if username in self.users:
                raise UserExistsError(f"用户 {username} 已存在")

            # 注册成功
            self.users.add(username)
            print(f"用户 {username} 注册成功")
            return True

        except InvalidUsernameError as e:
            print(f"用户名错误: {e}")
            return False
        except InvalidPasswordError as e:
            print(f"密码错误: {e}")
            return False
        except UserExistsError as e:
            print(f"注册失败: {e}")
            return False
        except Exception as e:
            print(f"未知错误: {e}")
            return False

# 使用
registration = UserRegistration()

# 测试各种情况
registration.register('alice', 'pass123')    # 成功
registration.register('ab', 'pass123')       # 用户名太短
registration.register('alice', 'pass123')    # 用户已存在
registration.register('bob', '123')          # 密码太短
registration.register('charlie', '123456')   # 密码没有字母
registration.register('david', 'abcdef')     # 密码没有数字
registration.register('bob', 'pass456')      # 成功
```

### 示例 3：数据库连接管理

```python
class DatabaseError(Exception):
    """数据库异常"""
    pass

class ConnectionError(DatabaseError):
    """连接异常"""
    pass

class QueryError(DatabaseError):
    """查询异常"""
    pass

class Database:
    """数据库连接"""

    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.connected = False

    def __enter__(self):
        """进入上下文"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开上下文"""
        self.disconnect()
        return False

    def connect(self):
        """连接数据库"""
        try:
            print(f"连接到数据库 {self.database} @ {self.host}:{self.port}")
            # 模拟连接
            if not self.host:
                raise ConnectionError("主机地址无效")
            self.connected = True
            print("连接成功")
        except ConnectionError as e:
            print(f"连接失败: {e}")
            raise

    def disconnect(self):
        """断开连接"""
        if self.connected:
            print("断开数据库连接")
            self.connected = False

    def query(self, sql):
        """执行查询"""
        try:
            if not self.connected:
                raise ConnectionError("未连接到数据库")

            print(f"执行查询: {sql}")

            # 模拟查询
            if 'error' in sql.lower():
                raise QueryError("查询语法错误")

            return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

        except QueryError as e:
            print(f"查询失败: {e}")
            raise

# 使用
try:
    with Database('localhost', 3306, 'mydb') as db:
        result = db.query("SELECT * FROM users")
        print(f"查询结果: {result}")

        # 故意制造错误
        result = db.query("SELECT error FROM users")

except DatabaseError as e:
    print(f"数据库操作失败: {e}")
```

---

## 总结

本章介绍了 Python 异常处理的核心内容：

### 8.1 异常介绍
- **语法错误**：代码解析时发生，必须修改代码
- **异常**：运行时发生，可以捕获和处理

### 8.2 异常处理
- **try...except**：捕获和处理异常
- **捕获特定异常**：提供更精确的错误处理
- **else**：没有异常时执行
- **finally**：无论如何都执行

### 8.3 抛出异常
- **raise**：主动抛出异常
- **assert**：断言检查（开发调试）

### 8.4 自定义异常
- 继承 `Exception` 类创建自定义异常
- 提供更清晰的错误信息

### 8.5 异常的传递
- 异常沿调用栈向上传递
- 可以在不同层次捕获和处理

### 8.6 with 关键字
- 自动管理资源
- 确保资源正确释放

### 8.7 常见异常
- 了解 Python 内置异常类型
- 正确选择和使用异常

掌握异常处理是编写健壮程序的关键技能。

---

## 练习题

1. 编写一个安全的除法函数，处理所有可能的异常
2. 实现一个文件复制程序，包含完整的异常处理
3. 创建一个自定义异常类，用于表单验证
4. 编写一个函数，演示异常的传递过程
5. 实现一个上下文管理器，管理数据库连接
6. 创建一个登录系统，使用自定义异常处理各种错误
7. 编写一个配置文件读取器，处理各种文件异常
8. 实现一个网络请求包装器，使用 with 语句管理连接
