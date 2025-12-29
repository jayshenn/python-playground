# 第 13 章 正则表达式

正则表达式（Regular Expression，简称 regex 或 regexp）是一种强大的文本处理工具，用于匹配、搜索、替换和验证字符串。本章将介绍 Python 中正则表达式的使用方法。

## 13.1 什么是正则表达式

正则表达式是一种描述字符串模式的语言，可以用来：
- **匹配**：检查字符串是否符合某种模式
- **搜索**：在文本中查找符合模式的内容
- **替换**：将符合模式的内容替换为其他内容
- **分割**：按照某种模式分割字符串
- **验证**：验证用户输入（如邮箱、手机号等）

### 正则表达式的组成

正则表达式由以下部分组成：
1. **普通字符**：直接匹配的字符（如 `a`、`1`、`@`）
2. **元字符**：具有特殊含义的字符（如 `.`、`*`、`+`、`?`）
3. **字符类**：匹配一组字符（如 `[abc]`、`\d`、`\w`）
4. **量词**：指定匹配次数（如 `*`、`+`、`{n}`）
5. **边界**：指定匹配位置（如 `^`、`$`、`\b`）
6. **分组**：将多个字符组合（如 `(abc)`）

### 为什么需要正则表达式

```python
# 不使用正则表达式：验证邮箱格式（复杂且容易出错）
def validate_email_without_regex(email):
    """不使用正则表达式验证邮箱"""
    if '@' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    username, domain = parts
    if not username or not domain:
        return False

    if '.' not in domain:
        return False

    # 还需要更多检查...
    return True

# 使用正则表达式：简洁明了
import re

def validate_email_with_regex(email):
    """使用正则表达式验证邮箱"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 测试
emails = ['user@example.com', 'invalid.email', 'test@domain']
for email in emails:
    result = validate_email_with_regex(email)
    print(f"{email:20s} -> {'有效' if result else '无效'}")
```

### 正则表达式的应用场景

| 场景 | 示例 |
|------|------|
| 数据验证 | 验证邮箱、手机号、身份证号 |
| 数据提取 | 从日志中提取 IP 地址、时间戳 |
| 数据清洗 | 删除多余空格、统一格式 |
| 文本搜索 | 搜索文档中的特定内容 |
| 文本替换 | 批量替换文本内容 |
| 网页爬虫 | 提取网页中的链接、图片 |

## 13.2 re 模块

Python 通过内置的 `re` 模块提供正则表达式支持。

### re 模块常用方法

| 方法 | 说明 | 返回值 |
|------|------|--------|
| `match()` | 从字符串开头匹配 | Match 对象或 None |
| `search()` | 在字符串中搜索第一个匹配 | Match 对象或 None |
| `findall()` | 查找所有匹配 | 列表 |
| `finditer()` | 查找所有匹配 | 迭代器 |
| `sub()` | 替换匹配的内容 | 新字符串 |
| `split()` | 按模式分割字符串 | 列表 |
| `compile()` | 编译正则表达式 | Pattern 对象 |

```python
import re

text = "Python is great. Python is powerful."

# 基本使用示例
print("原始文本:", text)

# match - 从开头匹配
result = re.match(r'Python', text)
print(f"match: {result.group() if result else 'None'}")

# search - 搜索第一个匹配
result = re.search(r'great', text)
print(f"search: {result.group() if result else 'None'}")

# findall - 查找所有匹配
results = re.findall(r'Python', text)
print(f"findall: {results}")

# sub - 替换
new_text = re.sub(r'Python', 'Java', text)
print(f"sub: {new_text}")

# split - 分割
parts = re.split(r'\. ', text)
print(f"split: {parts}")
```

### 13.2.1 search

`search()` 方法在字符串中搜索第一个匹配的位置。

**语法**：
```python
re.search(pattern, string, flags=0)
```

**参数**：
- `pattern`：正则表达式模式
- `string`：要搜索的字符串
- `flags`：可选标志

```python
import re

text = "我的手机号是 13812345678，邮箱是 user@example.com"

# 搜索手机号
result = re.search(r'1[3-9]\d{9}', text)
if result:
    print(f"找到手机号: {result.group()}")
    print(f"起始位置: {result.start()}")
    print(f"结束位置: {result.end()}")
    print(f"位置范围: {result.span()}")

# 搜索邮箱
result = re.search(r'[\w.-]+@[\w.-]+\.\w+', text)
if result:
    print(f"\n找到邮箱: {result.group()}")

# 搜索不存在的内容
result = re.search(r'QQ号', text)
print(f"\n搜索 QQ号: {result}")  # None

# 使用 group 分组
text = "价格：100元"
result = re.search(r'价格：(\d+)元', text)
if result:
    print(f"\n完整匹配: {result.group(0)}")  # 价格：100元
    print(f"第一组: {result.group(1)}")      # 100
```

### 13.2.2 match

`match()` 方法从字符串的**开头**开始匹配。

**语法**：
```python
re.match(pattern, string, flags=0)
```

```python
import re

# match 从开头匹配
text = "Python is great"

# 成功匹配（从开头）
result = re.match(r'Python', text)
print(f"match 'Python': {result.group() if result else 'None'}")

# 失败（不是从开头）
result = re.match(r'great', text)
print(f"match 'great': {result.group() if result else 'None'}")

# search 可以匹配任意位置
result = re.search(r'great', text)
print(f"search 'great': {result.group() if result else 'None'}")

# match vs search 对比
text = "  Python"

print("\n空格开头的字符串:")
print(f"match: {re.match(r'Python', text)}")      # None
print(f"search: {re.search(r'Python', text)}")    # <Match object>
```

### 13.2.3 findall

`findall()` 方法查找字符串中所有匹配的内容，返回列表。

**语法**：
```python
re.findall(pattern, string, flags=0)
```

```python
import re

text = "我的手机号是 13812345678，备用号码是 13987654321，座机 010-12345678"

# 查找所有手机号
phones = re.findall(r'1[3-9]\d{9}', text)
print(f"所有手机号: {phones}")

# 查找所有数字
numbers = re.findall(r'\d+', text)
print(f"所有数字: {numbers}")

# 带分组的 findall
text = "张三:90分, 李四:85分, 王五:95分"
results = re.findall(r'(\w+):(\d+)分', text)
print(f"\n成绩列表: {results}")  # [('张三', '90'), ('李四', '85'), ('王五', '95')]

# 遍历结果
for name, score in results:
    print(f"  {name}: {score}分")

# findall vs finditer
text = "Python is great. Python is powerful."
print("\nfindall 返回列表:")
results = re.findall(r'Python', text)
print(f"  {results}")

print("\nfinditer 返回迭代器:")
results = re.finditer(r'Python', text)
for match in results:
    print(f"  {match.group()} at position {match.span()}")
```

### 13.2.4 sub

`sub()` 方法替换字符串中匹配的内容。

**语法**：
```python
re.sub(pattern, repl, string, count=0, flags=0)
```

**参数**：
- `pattern`：正则表达式模式
- `repl`：替换字符串或函数
- `string`：原始字符串
- `count`：最多替换次数（0 表示全部替换）

```python
import re

# 简单替换
text = "我爱Python，Python真好！"
new_text = re.sub(r'Python', 'Java', text)
print(f"替换后: {new_text}")

# 限制替换次数
text = "Python Python Python"
new_text = re.sub(r'Python', 'Java', text, count=2)
print(f"替换 2 次: {new_text}")

# 删除多余空格
text = "这是    一段   有很多   空格的    文本"
new_text = re.sub(r'\s+', ' ', text)
print(f"\n删除多余空格: {new_text}")

# 使用函数替换
def double_number(match):
    """将数字翻倍"""
    num = int(match.group())
    return str(num * 2)

text = "价格：50元，数量：10个"
new_text = re.sub(r'\d+', double_number, text)
print(f"\n数字翻倍: {new_text}")

# 使用分组替换
text = "张三：男，李四：女，王五：男"
new_text = re.sub(r'(\w+)：(男|女)', r'\1是\2生', text)
print(f"\n分组替换: {new_text}")

# 隐藏手机号中间4位
text = "联系方式：13812345678"
new_text = re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', text)
print(f"\n隐藏手机号: {new_text}")
```

### 13.2.5 split

`split()` 方法按照正则表达式模式分割字符串。

**语法**：
```python
re.split(pattern, string, maxsplit=0, flags=0)
```

```python
import re

# 按空格分割
text = "Python Java C++ JavaScript"
parts = re.split(r'\s+', text)
print(f"按空格分割: {parts}")

# 按多种分隔符分割
text = "apple,banana;orange|grape"
parts = re.split(r'[,;|]', text)
print(f"按多种分隔符分割: {parts}")

# 按标点符号分割
text = "你好！这是一个测试。包含多种标点？"
parts = re.split(r'[！。？]', text)
print(f"按标点分割: {parts}")

# 限制分割次数
text = "a-b-c-d-e"
parts = re.split(r'-', text, maxsplit=2)
print(f"限制分割次数: {parts}")

# 保留分隔符（使用分组）
text = "one,two;three|four"
parts = re.split(r'([,;|])', text)
print(f"保留分隔符: {parts}")

# 按数字分割
text = "abc123def456ghi"
parts = re.split(r'\d+', text)
print(f"按数字分割: {parts}")
```

### compile - 编译正则表达式

对于重复使用的正则表达式，可以先编译成 Pattern 对象，提高效率。

```python
import re

# 编译正则表达式
pattern = re.compile(r'\d{3}-\d{4}-\d{4}')

# 使用编译后的对象
text1 = "电话：010-1234-5678"
text2 = "手机：138-1234-5678"

result1 = pattern.search(text1)
result2 = pattern.search(text2)

print(f"文本1: {result1.group() if result1 else 'None'}")
print(f"文本2: {result2.group() if result2 else 'None'}")

# 编译时指定标志
pattern = re.compile(r'python', re.IGNORECASE)  # 忽略大小写

texts = ['Python', 'python', 'PYTHON']
for text in texts:
    result = pattern.search(text)
    print(f"{text}: {'匹配' if result else '不匹配'}")
```

### re 模块常用标志

| 标志 | 说明 |
|------|------|
| `re.IGNORECASE` 或 `re.I` | 忽略大小写 |
| `re.MULTILINE` 或 `re.M` | 多行模式，`^` 和 `$` 匹配每行 |
| `re.DOTALL` 或 `re.S` | `.` 匹配包括换行符在内的所有字符 |
| `re.VERBOSE` 或 `re.X` | 详细模式，可以添加注释 |
| `re.ASCII` 或 `re.A` | 只匹配 ASCII 字符 |

```python
import re

# IGNORECASE - 忽略大小写
text = "Python PYTHON python"
results = re.findall(r'python', text, re.IGNORECASE)
print(f"忽略大小写: {results}")

# MULTILINE - 多行模式
text = """第一行
第二行
第三行"""
results = re.findall(r'^第', text, re.MULTILINE)
print(f"\n多行模式: {results}")

# DOTALL - . 匹配所有字符包括换行
text = "第一行\n第二行"
result = re.search(r'第一.*第二', text, re.DOTALL)
print(f"\nDOTALL: {result.group() if result else 'None'}")

# VERBOSE - 详细模式（可读性更好）
pattern = re.compile(r'''
    \d{3}     # 区号 3 位
    -         # 分隔符
    \d{4}     # 前 4 位
    -         # 分隔符
    \d{4}     # 后 4 位
''', re.VERBOSE)

text = "电话：010-1234-5678"
result = pattern.search(text)
print(f"\nVERBOSE: {result.group() if result else 'None'}")
```

## 13.3 表示字符

正则表达式提供了多种方式来表示和匹配字符。

### 普通字符

普通字符直接匹配自身：

```python
import re

text = "Hello World"

# 匹配普通字符
print(re.search(r'Hello', text).group())  # Hello
print(re.search(r'World', text).group())  # World
print(re.search(r'o', text).group())      # o (第一个)
```

### 元字符

元字符具有特殊含义，需要转义才能匹配字面值：

| 元字符 | 说明 | 示例 |
|--------|------|------|
| `.` | 匹配任意字符（除换行符） | `a.c` 匹配 "abc"、"a1c" |
| `^` | 匹配字符串开头 | `^Hello` |
| `$` | 匹配字符串结尾 | `end$` |
| `*` | 匹配 0 次或多次 | `ab*` 匹配 "a"、"ab"、"abb" |
| `+` | 匹配 1 次或多次 | `ab+` 匹配 "ab"、"abb" |
| `?` | 匹配 0 次或 1 次 | `ab?` 匹配 "a"、"ab" |
| `\` | 转义字符 | `\.` 匹配字面点号 |
| `\|` | 或运算符 | `cat\|dog` 匹配 "cat" 或 "dog" |
| `[]` | 字符类 | `[abc]` 匹配 a、b 或 c |
| `()` | 分组 | `(ab)+` 匹配 "ab"、"abab" |

```python
import re

# . 匹配任意字符
print(re.findall(r'a.c', "abc a1c a@c"))  # ['abc', 'a1c', 'a@c']

# 转义元字符
text = "文件名: test.txt"
print(re.search(r'\.txt', text).group())  # .txt

# | 或运算
text = "I have a cat and a dog"
print(re.findall(r'cat|dog', text))  # ['cat', 'dog']

# [] 字符类
print(re.findall(r'[aeiou]', "hello"))  # ['e', 'o']
```

### 预定义字符类

| 字符类 | 等价形式 | 说明 |
|--------|----------|------|
| `\d` | `[0-9]` | 数字 |
| `\D` | `[^0-9]` | 非数字 |
| `\w` | `[a-zA-Z0-9_]` | 字母、数字、下划线 |
| `\W` | `[^a-zA-Z0-9_]` | 非字母、数字、下划线 |
| `\s` | `[ \t\n\r\f\v]` | 空白字符 |
| `\S` | `[^ \t\n\r\f\v]` | 非空白字符 |

```python
import re

text = "用户名: user123, 密码: pass@456"

# \d 匹配数字
print(f"所有数字: {re.findall(r'\d', text)}")          # ['1', '2', '3', '4', '5', '6']
print(f"连续数字: {re.findall(r'\d+', text)}")         # ['123', '456']

# \w 匹配字母数字下划线
print(f"单词字符: {re.findall(r'\w+', text)}")         # ['user123', 'pass', '456']

# \s 匹配空白
print(f"空白字符数量: {len(re.findall(r'\s', text))}")  # 3

# \D 匹配非数字
print(f"非数字: {re.findall(r'\D+', text)}")           # ['用户名: user', ', 密码: pass@']

# 组合使用
text = "邮箱: test_123@example.com"
email = re.search(r'[\w.]+@[\w.]+', text)
print(f"\n提取邮箱: {email.group()}")
```

### 字符类和范围

```python
import re

text = "Hello123World456"

# 字符类 - 匹配列表中的任意字符
print(re.findall(r'[aeiou]', text))      # ['e', 'o', 'o']
print(re.findall(r'[HW]', text))         # ['H', 'W']

# 范围
print(re.findall(r'[a-z]', text))        # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
print(re.findall(r'[A-Z]', text))        # ['H', 'W']
print(re.findall(r'[0-9]', text))        # ['1', '2', '3', '4', '5', '6']

# 组合范围
print(re.findall(r'[a-zA-Z]', text))     # 所有字母
print(re.findall(r'[a-zA-Z0-9]', text))  # 所有字母和数字

# 取反 [^...] - 匹配不在列表中的字符
print(re.findall(r'[^0-9]', text))       # 所有非数字

# 特殊字符在 [] 中
text = "file-name_123.txt"
print(re.findall(r'[a-z_-]+', text))     # ['file-name_', 'txt']
```

### 转义特殊字符

```python
import re

# 需要转义的特殊字符
special_chars = r'. ^ $ * + ? { } [ ] \ | ( )'

# 匹配点号
text = "文件：test.txt"
print(re.search(r'\.txt', text).group())  # .txt

# 匹配括号
text = "价格：(100元)"
print(re.search(r'\(.*?\)', text).group())  # (100元)

# 匹配反斜杠
text = r"路径：C:\Users\test"
print(re.search(r'\\Users\\', text).group())  # \Users\

# 匹配特殊符号
text = "价格：$100"
print(re.search(r'\$\d+', text).group())  # $100

# 匹配加号
text = "1+2=3"
print(re.search(r'\d+\+\d+', text).group())  # 1+2

# re.escape() 自动转义所有特殊字符
special_text = "What? Yes! (Maybe)"
pattern = re.escape("(Maybe)")
print(re.search(pattern, special_text).group())  # (Maybe)
```

## 13.4 表示数量

量词用于指定字符或分组出现的次数。

### 基本量词

| 量词 | 说明 | 示例 |
|------|------|------|
| `*` | 0 次或多次 | `a*` 匹配 ""、"a"、"aa" |
| `+` | 1 次或多次 | `a+` 匹配 "a"、"aa"、"aaa" |
| `?` | 0 次或 1 次 | `a?` 匹配 ""、"a" |
| `{n}` | 恰好 n 次 | `a{3}` 匹配 "aaa" |
| `{n,}` | 至少 n 次 | `a{2,}` 匹配 "aa"、"aaa" |
| `{n,m}` | n 到 m 次 | `a{2,4}` 匹配 "aa"、"aaa"、"aaaa" |

```python
import re

# * - 0 次或多次
print(re.findall(r'ab*', "a ab abb abbb"))    # ['a', 'ab', 'abb', 'abbb']

# + - 1 次或多次
print(re.findall(r'ab+', "a ab abb abbb"))    # ['ab', 'abb', 'abbb']

# ? - 0 次或 1 次
print(re.findall(r'ab?', "a ab abb abbb"))    # ['a', 'ab', 'ab', 'ab']

# {n} - 恰好 n 次
print(re.findall(r'a{3}', "aa aaa aaaa"))     # ['aaa', 'aaa']

# {n,} - 至少 n 次
print(re.findall(r'a{2,}', "a aa aaa aaaa"))  # ['aa', 'aaa', 'aaaa']

# {n,m} - n 到 m 次
print(re.findall(r'a{2,3}', "a aa aaa aaaa")) # ['aa', 'aaa', 'aaa']

# 实际应用：匹配手机号（11 位数字）
text = "联系方式：13812345678"
phone = re.search(r'1[3-9]\d{9}', text)
print(f"\n手机号: {phone.group() if phone else 'None'}")

# 匹配邮政编码（6 位数字）
text = "地址：北京市 100000"
zipcode = re.search(r'\d{6}', text)
print(f"邮政编码: {zipcode.group() if zipcode else 'None'}")

# 匹配 QQ 号（5-11 位数字）
text = "我的QQ是 12345678"
qq = re.search(r'\d{5,11}', text)
print(f"QQ号: {qq.group() if qq else 'None'}")
```

### 量词的实际应用

```python
import re

# 匹配 HTML 标签
html = "<div>Hello</div><p>World</p>"
tags = re.findall(r'<\w+>', html)
print(f"HTML 标签: {tags}")

# 匹配整数和小数
text = "价格：100 或 99.99 元"
numbers = re.findall(r'\d+\.?\d*', text)
print(f"数字: {numbers}")

# 匹配 IP 地址
text = "服务器 IP：192.168.1.100"
ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
print(f"IP 地址: {ip.group() if ip else 'None'}")

# 匹配连续重复的字符
text = "哈哈哈哈，呵呵呵"
laughs = re.findall(r'哈{2,}|呵{2,}', text)
print(f"笑声: {laughs}")

# 匹配日期格式
dates = [
    "2024-01-01",
    "2024-1-1",
    "2024/12/31"
]
pattern = r'\d{4}[-/]\d{1,2}[-/]\d{1,2}'
for date in dates:
    if re.match(pattern, date):
        print(f"{date} 格式正确")
```

## 13.5 表示边界

边界符用于指定匹配的位置。

### 边界符号

| 符号 | 说明 | 示例 |
|------|------|------|
| `^` | 字符串开头 | `^Hello` 匹配以 "Hello" 开头 |
| `$` | 字符串结尾 | `end$` 匹配以 "end" 结尾 |
| `\b` | 单词边界 | `\bword\b` 匹配完整单词 |
| `\B` | 非单词边界 | `\Bword\B` |
| `\A` | 字符串开头（同 `^`） | 多行模式下只匹配整个字符串开头 |
| `\Z` | 字符串结尾（同 `$`） | 多行模式下只匹配整个字符串结尾 |

```python
import re

# ^ 和 $ - 匹配开头和结尾
text = "Hello World"
print(re.search(r'^Hello', text))      # 匹配
print(re.search(r'^World', text))      # 不匹配
print(re.search(r'World$', text))      # 匹配
print(re.search(r'Hello$', text))      # 不匹配

# 同时使用 ^ 和 $ 匹配整个字符串
pattern = r'^\d{11}$'  # 恰好 11 位数字
print(re.match(pattern, '13812345678'))   # 匹配
print(re.match(pattern, '138123456789'))  # 不匹配（12 位）
print(re.match(pattern, 'a13812345678'))  # 不匹配（有字母）

# \b 单词边界
text = "The word is wonderful"
print(re.findall(r'\bword', text))     # ['word']（匹配独立的 word）
print(re.findall(r'word\b', text))     # ['word']
print(re.findall(r'\bword\b', text))   # ['word']（完整单词）

# \B 非单词边界
text = "The word is wonderful"
print(re.findall(r'\Bword', text))     # []（word 前面是边界）
print(re.findall(r'word\B', text))     # []（word 后面是边界）

text = "password and sword"
print(re.findall(r'\Bword', text))     # ['word', 'word']（都不在边界）
```

### 边界的实际应用

```python
import re

# 匹配完整单词
text = "I love Python programming. Python is great!"

# 不使用边界 - 可能匹配到部分
print(re.findall(r'is', text))         # ['is', 'is']（包括 This 中的 is）

# 使用边界 - 只匹配完整单词
print(re.findall(r'\bis\b', text))     # ['is', 'is']（只有独立的 is）

# 验证用户名（只能包含字母数字下划线，3-16位）
def validate_username(username):
    pattern = r'^\w{3,16}$'
    return re.match(pattern, username) is not None

usernames = ['user123', 'ab', 'user@123', 'valid_user_name']
for username in usernames:
    result = validate_username(username)
    print(f"{username:20s} -> {'有效' if result else '无效'}")

# 验证密码（8-16位，包含字母和数字）
def validate_password(password):
    # 必须包含字母和数字
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{8,16}$'
    return re.match(pattern, password) is not None

passwords = ['12345678', 'abcdefgh', 'pass123', 'ValidPass123']
print("\n密码验证:")
for pwd in passwords:
    result = validate_password(pwd)
    print(f"{pwd:20s} -> {'有效' if result else '无效'}")

# 多行模式中的 ^ 和 $
text = """第一行内容
第二行内容
第三行内容"""

# 不使用多行模式
print("\n不使用 MULTILINE:")
print(re.findall(r'^第', text))          # ['第']（只匹配整个字符串开头）

# 使用多行模式
print("\n使用 MULTILINE:")
print(re.findall(r'^第', text, re.MULTILINE))  # ['第', '第', '第']（每行开头）
```

### 零宽断言

零宽断言用于指定匹配位置，但不包含在结果中：

| 断言 | 说明 | 示例 |
|------|------|------|
| `(?=...)` | 正向先行断言 | `\d(?=元)` 匹配后面是"元"的数字 |
| `(?!...)` | 负向先行断言 | `\d(?!元)` 匹配后面不是"元"的数字 |
| `(?<=...)` | 正向后行断言 | `(?<=\$)\d+` 匹配前面是"$"的数字 |
| `(?<!...)` | 负向后行断言 | `(?<!\$)\d+` 匹配前面不是"$"的数字 |

```python
import re

# 正向先行断言 (?=...)
text = "100元，200美元，300日元"
# 匹配后面是"元"的数字
results = re.findall(r'\d+(?=元)', text)
print(f"后面是'元'的数字: {results}")  # ['100', '300']

# 负向先行断言 (?!...)
# 匹配后面不是"元"的数字
results = re.findall(r'\d+(?!元)', text)
print(f"后面不是'元'的数字: {results}")  # ['10', '200', '30']（注意部分匹配）

# 正向后行断言 (?<=...)
text = "$100，￥200，€300"
# 匹配前面是"$"的数字
results = re.findall(r'(?<=\$)\d+', text)
print(f"前面是'$'的数字: {results}")    # ['100']

# 负向后行断言 (?<!...)
# 匹配前面不是"$"的数字
results = re.findall(r'(?<!\$)\d+', text)
print(f"前面不是'$'的数字: {results}")  # ['00', '200', '300']

# 实际应用：提取价格（只要数字，不要货币符号）
text = "价格：$100，¥200，€300"
prices = re.findall(r'(?<=[$¥€])\d+', text)
print(f"\n所有价格: {prices}")

# 密码强度验证（必须包含大小写字母和数字）
def strong_password(password):
    # 至少8位，包含大写、小写、数字
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(pattern, password) is not None

passwords = ['password', 'Password', 'Pass123', 'ValidPass123']
print("\n密码强度验证:")
for pwd in passwords:
    result = strong_password(pwd)
    print(f"{pwd:20s} -> {'强' if result else '弱'}")
```

## 13.6 匹配分组

分组允许我们提取匹配内容的特定部分，或者将多个字符作为一个整体。

### 基本分组 ()

```python
import re

# 基本分组
text = "我的生日是 1990-05-15"
result = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)

if result:
    print(f"完整匹配: {result.group(0)}")  # 1990-05-15
    print(f"年份: {result.group(1)}")      # 1990
    print(f"月份: {result.group(2)}")      # 05
    print(f"日期: {result.group(3)}")      # 15
    print(f"所有分组: {result.groups()}")   # ('1990', '05', '15')

# 分组与 findall
text = "张三:90分, 李四:85分, 王五:95分"
results = re.findall(r'(\w+):(\d+)分', text)
print(f"\n成绩列表:")
for name, score in results:
    print(f"  {name}: {score}分")

# 分组引用（在替换中使用）
text = "姓名：张三，年龄：25"
new_text = re.sub(r'(\w+)：(\w+)', r'\1是\2', text)
print(f"\n替换后: {new_text}")
```

### 命名分组 (?P<name>...)

```python
import re

# 命名分组
text = "联系方式：姓名：张三，电话：13812345678"
pattern = r'姓名：(?P<name>\w+)，电话：(?P<phone>\d{11})'
result = re.search(pattern, text)

if result:
    print(f"姓名: {result.group('name')}")
    print(f"电话: {result.group('phone')}")
    print(f"所有分组: {result.groupdict()}")

# 命名分组在替换中使用
text = "出生日期：1990-05-15"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
new_text = re.sub(pattern, r'\g<year>年\g<month>月\g<day>日', text)
print(f"\n替换后: {new_text}")

# 提取邮箱的用户名和域名
text = "邮箱：user@example.com"
pattern = r'(?P<username>[\w.]+)@(?P<domain>[\w.]+)'
result = re.search(pattern, text)

if result:
    print(f"\n用户名: {result.group('username')}")
    print(f"域名: {result.group('domain')}")
```

### 非捕获分组 (?:...)

非捕获分组用于分组但不保存到结果中，可以提高性能。

```python
import re

# 普通分组（捕获）
text = "http://www.example.com"
result = re.search(r'(http|https)://([\w.]+)', text)
print(f"捕获分组: {result.groups()}")  # ('http', 'www.example.com')

# 非捕获分组
result = re.search(r'(?:http|https)://([\w.]+)', text)
print(f"非捕获分组: {result.groups()}")  # ('www.example.com',)

# 实际应用：匹配电话号码（区号可选）
text1 = "010-12345678"
text2 = "12345678"

pattern = r'(?:\d{3}-)?(\d{8})'
print(f"\n{text1}: {re.search(pattern, text1).group(1)}")  # 12345678
print(f"{text2}: {re.search(pattern, text2).group(1)}")    # 12345678
```

### 反向引用 \1, \2

反向引用可以匹配之前捕获的分组内容。

```python
import re

# 匹配重复的单词
text = "这是一个一个重复的例子"
result = re.search(r'(\w+)\1', text)
print(f"重复的词: {result.group() if result else 'None'}")

# 匹配 HTML 标签
html = "<div>内容</div>"
result = re.search(r'<(\w+)>.*?</\1>', html)
print(f"匹配的标签: {result.group() if result else 'None'}")

# 查找重复的字符
text = "hello"
results = re.findall(r'(\w)\1', text)
print(f"\n重复字符: {results}")  # ['l']

# 匹配回文词（简单版）
text = "level, hello, noon"
palindromes = re.findall(r'\b(\w)(\w)\2\1\b', text)
print(f"四字母回文: {palindromes}")

# 替换重复的空格
text = "这是    一个   有很多    空格的文本"
new_text = re.sub(r'(\s)\1+', r'\1', text)
print(f"\n删除重复空格: {new_text}")
```

### 分组的实际应用

```python
import re

# 解析 URL
def parse_url(url):
    """解析 URL 各个部分"""
    pattern = r'''
        (?P<protocol>https?://)?      # 协议（可选）
        (?P<domain>[\w.-]+)           # 域名
        (?::(?P<port>\d+))?           # 端口（可选）
        (?P<path>/[\w/.-]*)?          # 路径（可选）
        (?:\?(?P<query>[\w=&]*))?     # 查询参数（可选）
    '''

    result = re.search(pattern, url, re.VERBOSE)
    if result:
        return result.groupdict()
    return None

urls = [
    "https://www.example.com:8080/path/to/page?id=123",
    "example.com/page",
    "http://api.example.com"
]

for url in urls:
    parts = parse_url(url)
    print(f"\nURL: {url}")
    for key, value in parts.items():
        if value:
            print(f"  {key}: {value}")

# 解析日志
def parse_log(log_line):
    """解析日志行"""
    pattern = r'\[(?P<time>.*?)\] (?P<level>\w+): (?P<message>.*)'
    result = re.search(pattern, log_line)
    if result:
        return result.groupdict()
    return None

log = "[2024-01-01 10:00:00] ERROR: Connection failed"
info = parse_log(log)
print(f"\n日志解析:")
for key, value in info.items():
    print(f"  {key}: {value}")
```

## 13.7 贪婪字符串

正则表达式默认是**贪婪模式**，会匹配尽可能多的字符。

### 贪婪 vs 非贪婪

| 量词 | 贪婪模式 | 非贪婪模式 | 说明 |
|------|----------|------------|------|
| `*` | `*` | `*?` | 0 次或多次 |
| `+` | `+` | `+?` | 1 次或多次 |
| `?` | `?` | `??` | 0 次或 1 次 |
| `{n,}` | `{n,}` | `{n,}?` | 至少 n 次 |
| `{n,m}` | `{n,m}` | `{n,m}?` | n 到 m 次 |

```python
import re

# 贪婪模式（默认）
text = "<div>Hello</div><div>World</div>"

# 贪婪匹配 - 匹配尽可能多
result = re.search(r'<div>.*</div>', text)
print(f"贪婪模式: {result.group()}")
# 输出: <div>Hello</div><div>World</div>

# 非贪婪模式
result = re.search(r'<div>.*?</div>', text)
print(f"非贪婪模式: {result.group()}")
# 输出: <div>Hello</div>

# 更多示例
text = "aaaa"

print("\n贪婪 vs 非贪婪:")
print(f"a* (贪婪): {re.match(r'a*', text).group()}")      # aaaa
print(f"a*? (非贪婪): {re.match(r'a*?', text).group()}")  # (空字符串)

print(f"a+ (贪婪): {re.match(r'a+', text).group()}")      # aaaa
print(f"a+? (非贪婪): {re.match(r'a+?', text).group()}")  # a

print(f"a{{2,}} (贪婪): {re.match(r'a{2,}', text).group()}")    # aaaa
print(f"a{{2,}}? (非贪婪): {re.match(r'a{2,}?', text).group()}")  # aa
```

### 贪婪模式的问题

```python
import re

# 问题1：提取引号中的内容
text = 'He said "Hello" and "Goodbye"'

# 贪婪模式（错误）
result = re.search(r'".*"', text)
print(f"贪婪: {result.group()}")  # "Hello" and "Goodbye"

# 非贪婪模式（正确）
results = re.findall(r'".*?"', text)
print(f"非贪婪: {results}")       # ['"Hello"', '"Goodbye"']

# 问题2：提取 HTML 标签内容
html = "<p>段落1</p><p>段落2</p>"

# 贪婪模式（错误）
result = re.search(r'<p>.*</p>', html)
print(f"\n贪婪: {result.group()}")  # <p>段落1</p><p>段落2</p>

# 非贪婪模式（正确）
results = re.findall(r'<p>.*?</p>', html)
print(f"非贪婪: {results}")         # ['<p>段落1</p>', '<p>段落2</p>']

# 问题3：提取数字
text = "价格：100-200元"

# 贪婪模式
result = re.search(r'\d+', text)
print(f"\n第一个数字: {result.group()}")  # 100

# 如果想匹配最少的数字
result = re.search(r'\d+?', text)
print(f"非贪婪: {result.group()}")        # 1（只匹配一个数字）
```

### 实际应用

**示例1：提取 HTML 标签内容**

```python
import re

def extract_html_tags(html):
    """提取 HTML 标签内容"""
    pattern = r'<(\w+)>(.*?)</\1>'
    matches = re.findall(pattern, html)
    return {tag: content for tag, content in matches}

html = """
<h1>标题</h1>
<p>段落1</p>
<p>段落2</p>
<div>内容</div>
"""

tags = extract_html_tags(html)
print("HTML 标签内容:")
for tag, content in tags.items():
    print(f"  <{tag}>: {content}")
```

**示例2:提取 Markdown 代码块**

````python
import re

def extract_code_blocks(text):
    """提取 Markdown 代码块"""
    pattern = r'```(\w+)?\n(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

markdown = """
这是文本

```python
print("Hello")
```

继续文本

```javascript
console.log("World");
```
"""

blocks = extract_code_blocks(markdown)
print("代码块:")
for lang, code in blocks:
    print(f"  语言: {lang if lang else '未指定'}")
    print(f"  代码: {code.strip()}\n")
````

**示例3:提取 JSON 字符串**

```python
import re

def extract_json_strings(text):
    """提取 JSON 中的字符串值"""
    pattern = r'"(\w+)":\s*"(.*?)"'
    matches = re.findall(pattern, text)
    return dict(matches)

json_text = '{"name": "张三", "age": "25", "city": "北京"}'
data = extract_json_strings(json_text)
print("JSON 数据:")
for key, value in data.items():
    print(f"  {key}: {value}")
```

## 13.8 案例

### 13.8.1 匹配电话号码

```python
import re

def validate_phone(phone):
    """验证各种电话号码格式"""
    patterns = {
        '手机号': r'^1[3-9]\d{9}$',
        '固定电话': r'^0\d{2,3}-?\d{7,8}$',
        '400电话': r'^400-?\d{3}-?\d{4}$',
        '800电话': r'^800-?\d{3}-?\d{4}$'
    }

    for phone_type, pattern in patterns.items():
        if re.match(pattern, phone):
            return phone_type

    return None

# 测试
phones = [
    '13812345678',      # 手机号
    '010-12345678',     # 固定电话
    '02112345678',      # 固定电话（无横线）
    '400-123-4567',     # 400电话
    '8001234567',       # 800电话
    '12345678901',      # 无效
]

print("电话号码验证:")
for phone in phones:
    result = validate_phone(phone)
    print(f"{phone:20s} -> {result if result else '无效格式'}")

# 提取文本中的所有电话号码
def extract_phones(text):
    """提取文本中的电话号码"""
    # 手机号
    mobiles = re.findall(r'1[3-9]\d{9}', text)

    # 固定电话
    landlines = re.findall(r'0\d{2,3}-?\d{7,8}', text)

    return {
        '手机号': mobiles,
        '固定电话': landlines
    }

text = """
联系方式：
手机：13812345678
座机：010-12345678
备用：13987654321
总机：021-87654321
"""

phones = extract_phones(text)
print("\n提取的电话号码:")
for phone_type, numbers in phones.items():
    print(f"{phone_type}: {numbers}")

# 格式化电话号码
def format_phone(phone):
    """格式化电话号码"""
    # 去除所有非数字字符
    digits = re.sub(r'\D', '', phone)

    # 手机号格式化为 xxx-xxxx-xxxx
    if len(digits) == 11 and digits[0] == '1':
        return f"{digits[0:3]}-{digits[3:7]}-{digits[7:11]}"

    # 固定电话格式化
    if len(digits) >= 10:
        if len(digits) == 10:
            return f"{digits[0:3]}-{digits[3:10]}"  # 区号3位
        else:
            return f"{digits[0:4]}-{digits[4:11]}"  # 区号4位

    return phone

phones = ['13812345678', '01012345678', '021-87654321']
print("\n格式化电话号码:")
for phone in phones:
    print(f"{phone:20s} -> {format_phone(phone)}")
```

### 13.8.2 匹配邮箱

```python
import re

def validate_email(email):
    """验证邮箱格式"""
    # 基本邮箱格式
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 测试
emails = [
    'user@example.com',
    'test.user@example.com',
    'user+tag@example.co.uk',
    'invalid@',
    '@example.com',
    'user@example',
    'user..name@example.com'
]

print("邮箱验证:")
for email in emails:
    result = validate_email(email)
    print(f"{email:30s} -> {'有效' if result else '无效'}")

# 提取邮箱的各个部分
def parse_email(email):
    """解析邮箱"""
    pattern = r'^(?P<username>[a-zA-Z0-9._%+-]+)@(?P<domain>[a-zA-Z0-9.-]+)\.(?P<tld>[a-zA-Z]{2,})$'
    result = re.match(pattern, email)

    if result:
        return result.groupdict()
    return None

email = 'user.name@example.com'
parts = parse_email(email)
print(f"\n邮箱 {email} 的组成:")
for key, value in parts.items():
    print(f"  {key}: {value}")

# 从文本中提取所有邮箱
def extract_emails(text):
    """提取文本中的邮箱地址"""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

text = """
请联系我们：
销售：sales@example.com
技术支持：support@example.com
或发送邮件到 info@company.co.uk
"""

emails = extract_emails(text)
print("\n提取的邮箱:")
for email in emails:
    print(f"  {email}")

# 隐藏邮箱（防爬虫）
def hide_email(email):
    """隐藏邮箱中间部分"""
    pattern = r'([a-zA-Z0-9._%+-]{1,3})([a-zA-Z0-9._%+-]*)(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

    def replace(match):
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        hidden = '*' * len(middle) if middle else ''
        return f"{prefix}{hidden}{suffix}"

    return re.sub(pattern, replace, email)

emails = ['user@example.com', 'test.name@example.com']
print("\n隐藏邮箱:")
for email in emails:
    print(f"{email:30s} -> {hide_email(email)}")
```

### 13.8.3 从 python-2.56 中提取 2 和 56 的数字

```python
import re

# 方法1：使用 findall
text = "python-2.56"
numbers = re.findall(r'\d+', text)
print(f"提取的数字: {numbers}")  # ['2', '56']

# 方法2：使用分组
result = re.search(r'python-(\d+)\.(\d+)', text)
if result:
    major = result.group(1)
    minor = result.group(2)
    print(f"主版本号: {major}, 次版本号: {minor}")

# 方法3：使用命名分组
result = re.search(r'python-(?P<major>\d+)\.(?P<minor>\d+)', text)
if result:
    print(f"版本信息: {result.groupdict()}")

# 扩展：解析各种版本号格式
def parse_version(version_str):
    """解析版本号"""
    # 匹配 x.y.z 或 x.y 格式
    pattern = r'(?P<software>[\w-]+)-(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<patch>\d+))?'
    result = re.search(pattern, version_str)

    if result:
        return result.groupdict()
    return None

versions = [
    'python-2.56',
    'python-3.9.7',
    'numpy-1.21.0',
    'django-4.0'
]

print("\n版本号解析:")
for version in versions:
    info = parse_version(version)
    if info:
        software = info['software']
        major = info['major']
        minor = info['minor']
        patch = info.get('patch', 'N/A')
        print(f"{version:20s} -> {software} {major}.{minor}.{patch}")

# 版本号比较
def compare_version(v1, v2):
    """比较两个版本号"""
    # 提取数字
    nums1 = list(map(int, re.findall(r'\d+', v1)))
    nums2 = list(map(int, re.findall(r'\d+', v2)))

    # 补齐长度
    max_len = max(len(nums1), len(nums2))
    nums1.extend([0] * (max_len - len(nums1)))
    nums2.extend([0] * (max_len - len(nums2)))

    # 比较
    if nums1 > nums2:
        return 1
    elif nums1 < nums2:
        return -1
    else:
        return 0

print("\n版本号比较:")
pairs = [
    ('python-2.56', 'python-3.9'),
    ('django-3.2.0', 'django-3.2.1'),
    ('flask-2.0', 'flask-2.0.0')
]

for v1, v2 in pairs:
    result = compare_version(v1, v2)
    if result > 0:
        print(f"{v1} > {v2}")
    elif result < 0:
        print(f"{v1} < {v2}")
    else:
        print(f"{v1} = {v2}")
```

### 13.8.4 从检索中获取网址

```python
import re

def extract_urls(text):
    """从文本中提取 URL"""
    # URL 正则表达式
    pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

    urls = re.findall(pattern, text)
    return urls

text = """
访问我们的网站：
主站：https://www.example.com
API：https://api.example.com/v1/users
文档：http://docs.example.com/guide
GitHub：https://github.com/user/repo
"""

urls = extract_urls(text)
print("提取的 URL:")
for url in urls:
    print(f"  {url}")

# 解析 URL 各部分
def parse_url(url):
    """解析 URL"""
    pattern = r'''
        (?P<protocol>https?)://           # 协议
        (?:www\.)?                        # www（可选）
        (?P<domain>[-a-zA-Z0-9@:%._\+~#=]{1,256})  # 域名
        (?:\.(?P<tld>[a-zA-Z0-9()]{1,6}))          # 顶级域名
        (?P<path>/[-a-zA-Z0-9()@:%_\+.~#?&/=]*)?   # 路径（可选）
    '''

    result = re.match(pattern, url, re.VERBOSE)
    if result:
        return result.groupdict()
    return None

urls = [
    'https://www.example.com',
    'https://api.example.com/v1/users',
    'http://docs.example.com/guide/index.html'
]

print("\nURL 解析:")
for url in urls:
    parts = parse_url(url)
    if parts:
        print(f"\n{url}")
        for key, value in parts.items():
            if value:
                print(f"  {key}: {value}")

# 验证 URL
def validate_url(url):
    """验证 URL 格式"""
    pattern = r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$'
    return re.match(pattern, url) is not None

urls = [
    'https://www.example.com',
    'http://example.com/path',
    'www.example.com',           # 无效（缺少协议）
    'https://example',           # 无效（缺少顶级域名）
]

print("\nURL 验证:")
for url in urls:
    result = validate_url(url)
    print(f"{url:40s} -> {'有效' if result else '无效'}")

# 提取特定域名的 URL
def extract_domain_urls(text, domain):
    """提取特定域名的 URL"""
    pattern = rf'https?://(?:[\w-]+\.)*{re.escape(domain)}(?:/[\w\-._~:/?#[\]@!$&\'()*+,;=]*)?'
    return re.findall(pattern, text)

text = """
参考链接：
https://github.com/python/cpython
https://docs.python.org/3/
https://www.python.org/downloads/
https://example.com
"""

github_urls = extract_domain_urls(text, 'github.com')
python_urls = extract_domain_urls(text, 'python.org')

print("\nGitHub URLs:", github_urls)
print("Python.org URLs:", python_urls)
```

### 13.8.5 替换文本中的所有数字为对应的词

```python
import re

# 数字到中文的映射
NUMBER_MAP = {
    '0': '零', '1': '一', '2': '二', '3': '三', '4': '四',
    '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'
}

def number_to_chinese(match):
    """将数字转换为中文"""
    number = match.group()
    return ''.join(NUMBER_MAP.get(digit, digit) for digit in number)

# 简单替换
text = "我有3个苹果和5个橙子"
new_text = re.sub(r'\d+', number_to_chinese, text)
print(f"原文: {text}")
print(f"替换后: {new_text}")

# 更复杂的转换
def number_to_chinese_advanced(num_str):
    """将数字转换为中文（支持大数）"""
    units = ['', '十', '百', '千', '万', '十万', '百万', '千万', '亿']
    digits = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']

    num = int(num_str)
    if num == 0:
        return '零'

    result = []
    unit_index = 0

    while num > 0:
        digit = num % 10
        if digit != 0:
            result.insert(0, digits[digit] + units[unit_index])
        elif result and result[0] != '零':
            result.insert(0, '零')

        num //= 10
        unit_index += 1

    return ''.join(result).rstrip('零')

def replace_number(match):
    """替换函数"""
    return number_to_chinese_advanced(match.group())

text = "今年是2024年，我25岁，有100元"
new_text = re.sub(r'\d+', replace_number, text)
print(f"\n原文: {text}")
print(f"替换后: {new_text}")

# 反向：中文数字转阿拉伯数字
CHINESE_MAP = {
    '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
    '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
    '十': 10, '百': 100, '千': 1000, '万': 10000
}

def chinese_to_number(chinese_num):
    """中文数字转阿拉伯数字（简化版）"""
    if chinese_num in CHINESE_MAP:
        return str(CHINESE_MAP[chinese_num])

    # 简单实现，只处理基本情况
    result = 0
    temp = 0

    for char in chinese_num:
        if char in ['十', '百', '千', '万']:
            if temp == 0:
                temp = 1
            result += temp * CHINESE_MAP[char]
            temp = 0
        else:
            temp = CHINESE_MAP.get(char, 0)

    result += temp
    return str(result)

text = "我有三个苹果和五个橙子，今年二十五岁"
# 匹配中文数字（简化版）
new_text = re.sub(r'[零一二三四五六七八九十百千万]+', lambda m: chinese_to_number(m.group()), text)
print(f"\n原文: {text}")
print(f"替换后: {new_text}")

# 其他替换示例
print("\n其他替换示例:")

# 1. 替换敏感词
def censor_text(text, sensitive_words):
    """替换敏感词"""
    pattern = '|'.join(re.escape(word) for word in sensitive_words)
    return re.sub(pattern, lambda m: '*' * len(m.group()), text)

text = "这是一个测试，包含敏感和违禁内容"
censored = censor_text(text, ['敏感', '违禁'])
print(f"审查后: {censored}")

# 2. 统一日期格式
text = "日期：2024/01/15 或 2024-01-15"
normalized = re.sub(r'(\d{4})[/-](\d{2})[/-](\d{2})', r'\1年\2月\3日', text)
print(f"统一格式: {normalized}")

# 3. 删除 HTML 标签
html = "<p>这是<strong>重要</strong>内容</p>"
plain_text = re.sub(r'<[^>]+>', '', html)
print(f"纯文本: {plain_text}")
```

## 本章小结

本章介绍了 Python 正则表达式的核心内容：

### 13.1 正则表达式基础
- **概念**：描述字符串模式的语言
- **作用**：匹配、搜索、替换、分割、验证
- **组成**：普通字符、元字符、字符类、量词、边界、分组

### 13.2 re 模块
- **search()**：在字符串中搜索第一个匹配
- **match()**：从字符串开头匹配
- **findall()**：查找所有匹配，返回列表
- **sub()**：替换匹配的内容
- **split()**：按模式分割字符串
- **compile()**：编译正则表达式，提高效率

### 13.3 表示字符
- **普通字符**：直接匹配
- **元字符**：`.` `^` `$` `*` `+` `?` `\` `|` `[]` `()`
- **预定义字符类**：`\d` `\w` `\s` 及其反义 `\D` `\W` `\S`
- **字符类**：`[abc]` `[a-z]` `[^abc]`

### 13.4 表示数量
- **基本量词**：`*` `+` `?` `{n}` `{n,}` `{n,m}`
- **应用**：匹配手机号、邮编、IP 地址等

### 13.5 表示边界
- **边界符**：`^` `$` `\b` `\B` `\A` `\Z`
- **零宽断言**：`(?=...)` `(?!...)` `(?<=...)` `(?<!...)`
- **应用**：验证输入、匹配完整单词

### 13.6 匹配分组
- **基本分组**：`()`
- **命名分组**：`(?P<name>...)`
- **非捕获分组**：`(?:...)`
- **反向引用**：`\1` `\2`

### 13.7 贪婪与非贪婪
- **贪婪模式**：默认，匹配尽可能多
- **非贪婪模式**：在量词后加 `?`，匹配尽可能少
- **应用**：提取 HTML 标签、引号内容

### 13.8 实战案例
- 匹配电话号码（手机号、固定电话、400/800）
- 匹配邮箱地址
- 提取版本号
- 提取 URL
- 文本替换

### 最佳实践

1. **使用原始字符串**：`r'pattern'` 避免转义问题
2. **编译重复使用的模式**：提高性能
3. **使用非贪婪模式**：避免过度匹配
4. **合理使用分组**：提取需要的部分
5. **添加注释**：使用 `re.VERBOSE` 提高可读性
6. **测试边界情况**：确保模式正确
7. **安全考虑**：避免正则表达式注入攻击

### 常见正则表达式

```python
# 手机号
r'^1[3-9]\d{9}$'

# 邮箱
r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 身份证号
r'^\d{17}[\dXx]$'

# IP 地址
r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

# URL
r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b'

# 日期 (YYYY-MM-DD)
r'^\d{4}-\d{2}-\d{2}$'

# 中文字符
r'[\u4e00-\u9fa5]+'
```

## 练习题

1. **基础练习**
   - 编写正则表达式匹配中国大陆身份证号
   - 验证密码强度（8-16位，包含大小写字母和数字）
   - 提取文本中的所有 IP 地址

2. **进阶练习**
   - 实现简单的 Markdown 解析器（提取标题、链接、代码块）
   - 编写日志分析工具，提取时间、级别、消息
   - 实现敏感信息脱敏（手机号、邮箱、身份证）

3. **综合项目**
   - 开发网页爬虫，提取页面中的链接和图片
   - 实现表单验证工具（验证各种输入格式）
   - 编写文本处理工具，支持搜索、替换、格式化
