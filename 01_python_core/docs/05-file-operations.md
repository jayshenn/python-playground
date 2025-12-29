# 第 5 章 文件操作

## 5.1 文件的基本概念

文件是存储在外部介质（如硬盘）上的数据集合。在 Python 中，文件操作是程序与外部数据交互的重要方式。

**为什么需要文件操作？**
- **数据持久化**：程序结束后数据仍然保存
- **数据共享**：不同程序之间可以通过文件交换数据
- **大数据处理**：处理无法完全加载到内存的大量数据
- **日志记录**：记录程序运行状态和错误信息

**文件操作的基本步骤**：
1. **打开文件**：使用 `open()` 函数
2. **读写数据**：执行读取或写入操作
3. **关闭文件**：使用 `close()` 方法释放资源

```python
# 文件操作的基本流程
file = open('example.txt', 'r')  # 打开文件
content = file.read()             # 读取内容
file.close()                      # 关闭文件
```

---

## 5.2 文件的分类

### 5.2.1 按内容分类

#### 1. 文本文件（Text File）

文本文件以字符形式存储数据，人类可读。

**特点**：
- 存储的是字符数据
- 可以用文本编辑器直接打开查看
- 占用空间相对较大
- 跨平台兼容性好

**常见文本文件**：
- `.txt` - 纯文本文件
- `.py` - Python 源代码
- `.md` - Markdown 文档
- `.json` - JSON 数据
- `.csv` - 逗号分隔值文件
- `.xml` - XML 文档
- `.html` - HTML 网页

```python
# 文本文件示例
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('这是一个文本文件')
```

#### 2. 二进制文件（Binary File）

二进制文件以字节形式存储数据，通常不可直接阅读。

**特点**：
- 存储的是二进制数据
- 需要专门的程序打开
- 占用空间小，效率高
- 可以存储任意类型的数据

**常见二进制文件**：
- 图像文件：`.jpg`、`.png`、`.gif`
- 音频文件：`.mp3`、`.wav`
- 视频文件：`.mp4`、`.avi`
- 压缩文件：`.zip`、`.rar`
- 可执行文件：`.exe`、`.dll`
- 数据库文件：`.db`、`.sqlite`

```python
# 二进制文件示例：复制图片
with open('source.jpg', 'rb') as source:
    with open('copy.jpg', 'wb') as target:
        target.write(source.read())
```

### 5.2.2 文本文件与二进制文件的区别

| 特性 | 文本文件 | 二进制文件 |
|------|---------|-----------|
| **存储方式** | 字符编码（如 UTF-8） | 原始字节 |
| **可读性** | 人类可读 | 人类不可读 |
| **打开方式** | `'r'`、`'w'` | `'rb'`、`'wb'` |
| **编码** | 需要指定编码 | 不涉及编码 |
| **换行符** | 自动转换 | 不转换 |
| **数据类型** | 字符串 | 字节 |
| **典型用途** | 配置文件、日志 | 图片、视频、压缩文件 |

```python
# 对比示例
# 文本模式
with open('text.txt', 'w') as f:
    f.write('Hello')  # 写入字符串

# 二进制模式
with open('binary.bin', 'wb') as f:
    f.write(b'Hello')  # 写入字节（注意 b 前缀）
```

---

## 5.3 文件的编码

### 5.3.1 什么是编码

编码是将字符转换为字节序列的规则。计算机只能处理二进制数据，所以需要将字符编码为字节。

**编码过程**：
```
字符 → (编码) → 字节 → 存储到文件
文件 → (解码) → 字节 → 字符
```

### 5.3.2 常见编码格式

#### 1. ASCII

- 最早的字符编码标准
- 只支持英文字符、数字和符号
- 每个字符占 1 字节（7 位）
- 只能表示 128 个字符

```python
# ASCII 编码示例
text = 'Hello'
bytes_data = text.encode('ascii')
print(bytes_data)  # b'Hello'
print(len(bytes_data))  # 5 字节
```

#### 2. GBK / GB2312

- 中国国家标准编码
- GB2312：简体中文
- GBK：扩展了 GB2312，包含繁体中文
- 英文字符占 1 字节，中文字符占 2 字节

```python
# GBK 编码示例
text = '你好'
bytes_data = text.encode('gbk')
print(bytes_data)  # b'\xc4\xe3\xba\xc3'
print(len(bytes_data))  # 4 字节（每个汉字 2 字节）
```

#### 3. UTF-8（推荐）

- Unicode 的一种实现方式
- 支持全世界所有语言
- 变长编码：英文 1 字节，中文 3 字节
- 互联网最常用的编码
- **Python 3 默认编码**

```python
# UTF-8 编码示例
text = '你好World'
bytes_data = text.encode('utf-8')
print(bytes_data)  # b'\xe4\xbd\xa0\xe5\xa5\xbdWorld'
print(len(bytes_data))  # 11 字节（3+3+5）

# 解码
decoded = bytes_data.decode('utf-8')
print(decoded)  # 你好World
```

#### 4. Unicode

- 字符集标准，为每个字符分配唯一的编号（码点）
- 不是具体的编码方式，而是字符到编号的映射
- UTF-8、UTF-16、UTF-32 是 Unicode 的不同编码实现

```python
# Unicode 码点
print(ord('A'))  # 65
print(ord('你'))  # 20320
print(chr(65))   # 'A'
print(chr(20320))  # '你'
```

### 5.3.3 编码对比

| 编码 | 支持语言 | 英文占用 | 中文占用 | 优点 | 缺点 |
|------|---------|---------|---------|------|------|
| **ASCII** | 仅英文 | 1 字节 | 不支持 | 简单、高效 | 只支持英文 |
| **GBK** | 中文 | 1 字节 | 2 字节 | 节省空间 | 不支持其他语言 |
| **UTF-8** | 全球 | 1 字节 | 3 字节 | 兼容性好、支持所有语言 | 中文占用空间大 |
| **UTF-16** | 全球 | 2 字节 | 2 字节 | 定长、处理速度快 | 英文浪费空间 |

### 5.3.4 Python 中的编码处理

```python
# 1. 字符串编码为字节
text = "你好，世界！"
utf8_bytes = text.encode('utf-8')
gbk_bytes = text.encode('gbk')

print(utf8_bytes)  # b'\xe4\xbd\xa0\xe5\xa5\xbd...'
print(gbk_bytes)   # b'\xc4\xe3\xba\xc3...'

# 2. 字节解码为字符串
text1 = utf8_bytes.decode('utf-8')
text2 = gbk_bytes.decode('gbk')
print(text1)  # 你好，世界！
print(text2)  # 你好，世界！

# 3. 编码错误处理
try:
    # 用错误的编码解码
    utf8_bytes.decode('gbk')
except UnicodeDecodeError as e:
    print(f"解码错误: {e}")

# 4. 忽略错误
result = utf8_bytes.decode('gbk', errors='ignore')
print(result)  # 可能显示乱码或部分内容

# 5. 替换错误字符
result = utf8_bytes.decode('gbk', errors='replace')
print(result)  # 用 � 替换无法解码的字符
```

### 5.3.5 文件编码的最佳实践

```python
# 1. 始终显式指定编码
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('你好')

# 2. 读取时使用相同的编码
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. 处理未知编码的文件
def detect_encoding(file_path):
    """尝试不同编码读取文件"""
    encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    return None

# 4. 避免常见错误
# 错误：不指定编码（依赖系统默认编码）
# with open('file.txt', 'w') as f:  # 不推荐
#     f.write('你好')

# 正确：显式指定 UTF-8
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('你好')
```

---

## 5.4 文件打开与关闭

### 5.4.1 使用 open() 函数打开文件

**基本语法**：
```python
file_object = open(file_path, mode, encoding=None)
```

**参数说明**：
- `file_path`：文件路径（字符串）
- `mode`：打开模式（字符串）
- `encoding`：编码格式（文本模式下使用）

### 5.4.2 文件打开模式

| 模式 | 说明 | 文件不存在 | 文件存在 | 指针位置 |
|------|------|-----------|---------|---------|
| **`'r'`** | 只读（文本） | 报错 | 读取 | 开头 |
| **`'w'`** | 只写（文本） | 创建 | 覆盖 | 开头 |
| **`'a'`** | 追加（文本） | 创建 | 追加到末尾 | 末尾 |
| **`'r+'`** | 读写（文本） | 报错 | 读写 | 开头 |
| **`'w+'`** | 读写（文本） | 创建 | 覆盖 | 开头 |
| **`'a+'`** | 读写（文本） | 创建 | 追加 | 末尾 |
| **`'rb'`** | 只读（二进制） | 报错 | 读取 | 开头 |
| **`'wb'`** | 只写（二进制） | 创建 | 覆盖 | 开头 |
| **`'ab'`** | 追加（二进制） | 创建 | 追加 | 末尾 |

```python
# 1. 'r' - 只读模式（默认）
file = open('data.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# 2. 'w' - 写入模式（覆盖）
file = open('output.txt', 'w', encoding='utf-8')
file.write('新内容')
file.close()

# 3. 'a' - 追加模式
file = open('log.txt', 'a', encoding='utf-8')
file.write('新日志\n')
file.close()

# 4. 'r+' - 读写模式
file = open('data.txt', 'r+', encoding='utf-8')
content = file.read()  # 先读取
file.write('追加内容')  # 再写入
file.close()

# 5. 'rb' - 二进制读取
with open('image.jpg', 'rb') as f:
    data = f.read()

# 6. 'wb' - 二进制写入
with open('output.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')
```

### 5.4.3 关闭文件

**为什么要关闭文件？**
- 释放系统资源
- 确保数据完整写入磁盘
- 避免文件被锁定

#### 方法 1：手动关闭

```python
# 基本方法
file = open('data.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()  # 确保文件被关闭

# 检查文件是否已关闭
print(file.closed)  # True
```

#### 方法 2：使用 with 语句（推荐）

```python
# with 语句自动关闭文件
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# 离开 with 块后，文件自动关闭

# 打开多个文件
with open('source.txt', 'r') as src, open('dest.txt', 'w') as dst:
    dst.write(src.read())
```

**with 语句的优点**：
- 自动关闭文件，即使发生异常
- 代码更简洁
- 不会忘记关闭文件

```python
# 对比：不使用 with
file = open('data.txt', 'r')
content = file.read()
file.close()  # 容易忘记

# 使用 with（推荐）
with open('data.txt', 'r') as file:
    content = file.read()
# 自动关闭，无需手动调用 close()
```

### 5.4.4 文件路径

#### 1. 相对路径

相对于当前工作目录的路径。

```python
# 相对路径示例
with open('data.txt', 'r') as f:  # 当前目录
    content = f.read()

with open('folder/data.txt', 'r') as f:  # 子目录
    content = f.read()

with open('../data.txt', 'r') as f:  # 父目录
    content = f.read()
```

#### 2. 绝对路径

从根目录开始的完整路径。

```python
# Windows 绝对路径
with open(r'C:\Users\username\data.txt', 'r') as f:
    content = f.read()

# macOS/Linux 绝对路径
with open('/home/username/data.txt', 'r') as f:
    content = f.read()

# 使用 pathlib（推荐）
from pathlib import Path

file_path = Path('/home/username/data.txt')
with open(file_path, 'r') as f:
    content = f.read()
```

#### 3. 跨平台路径处理

```python
import os
from pathlib import Path

# 方法 1：使用 os.path
file_path = os.path.join('folder', 'subfolder', 'data.txt')
with open(file_path, 'r') as f:
    content = f.read()

# 方法 2：使用 pathlib（推荐）
base_dir = Path(__file__).parent
file_path = base_dir / 'data' / 'file.txt'
with open(file_path, 'r') as f:
    content = f.read()

# 获取当前工作目录
print(os.getcwd())
print(Path.cwd())

# 检查文件是否存在
if os.path.exists('data.txt'):
    print("文件存在")

if Path('data.txt').exists():
    print("文件存在")
```

---

## 5.5 文件写操作

### 5.5.1 write() 方法

写入字符串到文件。

```python
# 基本写入
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('第一行\n')
    f.write('第二行\n')

# write() 返回写入的字符数
with open('output.txt', 'w', encoding='utf-8') as f:
    count = f.write('Hello, World!')
    print(f"写入了 {count} 个字符")  # 写入了 13 个字符

# 注意：write() 不会自动添加换行符
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('第一行')
    f.write('第二行')  # 结果：第一行第二行（没有换行）
```

### 5.5.2 writelines() 方法

写入字符串序列到文件。

```python
# 写入列表
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 注意：writelines() 不会自动添加换行符
lines = ['第一行', '第二行', '第三行']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)  # 结果：第一行第二行第三行

# 正确做法：手动添加换行符
lines = ['第一行', '第二行', '第三行']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(line + '\n' for line in lines)

# 或者使用 join
lines = ['第一行', '第二行', '第三行']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
```

### 5.5.3 写入不同类型的数据

```python
# 1. 写入字符串
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!')

# 2. 写入数字（需要转换为字符串）
with open('numbers.txt', 'w', encoding='utf-8') as f:
    numbers = [1, 2, 3, 4, 5]
    f.write(','.join(map(str, numbers)))

# 3. 写入字典（使用 JSON）
import json

data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 4. 写入二进制数据
data = bytes([0, 1, 2, 3, 4, 5])
with open('data.bin', 'wb') as f:
    f.write(data)
```

### 5.5.4 写入模式对比

```python
# 1. 'w' 模式：覆盖写入
with open('file.txt', 'w') as f:
    f.write('第一次写入\n')

with open('file.txt', 'w') as f:
    f.write('第二次写入\n')  # 覆盖了第一次的内容

# 2. 'a' 模式：追加写入
with open('file.txt', 'a') as f:
    f.write('第一次写入\n')

with open('file.txt', 'a') as f:
    f.write('第二次写入\n')  # 追加到文件末尾

# 3. 'x' 模式：独占创建（文件已存在会报错）
try:
    with open('new_file.txt', 'x') as f:
        f.write('只能创建新文件\n')
except FileExistsError:
    print("文件已存在")
```

### 5.5.5 缓冲和刷新

```python
# 1. 默认缓冲
with open('file.txt', 'w') as f:
    f.write('Hello')  # 数据在缓冲区
    # 离开 with 块时自动刷新

# 2. 手动刷新
with open('file.txt', 'w') as f:
    f.write('Hello')
    f.flush()  # 立即写入磁盘

# 3. 无缓冲（文本文件不支持，二进制文件可用）
with open('file.bin', 'wb', buffering=0) as f:
    f.write(b'Hello')  # 立即写入磁盘

# 4. 行缓冲
with open('file.txt', 'w', buffering=1) as f:
    f.write('Hello\n')  # 遇到换行符时刷新
```

---

## 5.6 文件读操作

### 5.6.1 read() 方法

读取整个文件内容。

```python
# 读取全部内容
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 读取指定字节数
with open('data.txt', 'r', encoding='utf-8') as f:
    chunk = f.read(10)  # 读取前 10 个字符
    print(chunk)

# 分块读取大文件
with open('large_file.txt', 'r', encoding='utf-8') as f:
    while True:
        chunk = f.read(1024)  # 每次读取 1024 字符
        if not chunk:
            break
        # 处理 chunk
        print(len(chunk))
```

### 5.6.2 readline() 方法

读取一行内容。

```python
# 读取单行
with open('data.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)  # 包含换行符 \n

# 读取多行
with open('data.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(line1, line2, line3)

# 读取所有行（使用循环）
with open('data.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:  # 文件结尾
            break
        print(line.rstrip())  # 去除末尾换行符
```

### 5.6.3 readlines() 方法

读取所有行，返回列表。

```python
# 读取所有行
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)  # ['第一行\n', '第二行\n', '第三行\n']

# 处理每一行
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # 去除两端空白

# 注意：readlines() 会将整个文件读入内存
# 对于大文件，不推荐使用
```

### 5.6.4 迭代文件对象（推荐）

```python
# 方法 1：直接迭代文件对象（推荐）
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# 方法 2：enumerate 获取行号
with open('data.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"第 {i} 行: {line.strip()}")

# 优点：
# - 内存效率高（逐行读取）
# - 代码简洁
# - 适合处理大文件
```

### 5.6.5 读取方法对比

| 方法 | 返回值 | 适用场景 | 内存占用 |
|------|--------|---------|---------|
| **`read()`** | 字符串 | 小文件 | 高 |
| **`read(size)`** | 字符串 | 分块读取大文件 | 低 |
| **`readline()`** | 字符串 | 逐行处理 | 低 |
| **`readlines()`** | 列表 | 需要所有行列表 | 高 |
| **迭代文件对象** | 字符串（每行） | 逐行处理大文件 | 低（推荐） |

```python
# 对比示例
# 1. read() - 适合小文件
with open('small.txt', 'r') as f:
    content = f.read()
    print(content)

# 2. readlines() - 适合中等大小文件
with open('medium.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 3. 迭代 - 适合大文件（推荐）
with open('large.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### 5.6.6 文件指针操作

```python
# 1. tell() - 获取当前指针位置
with open('data.txt', 'r') as f:
    print(f.tell())  # 0（开头）
    f.read(5)
    print(f.tell())  # 5

# 2. seek() - 移动指针
with open('data.txt', 'r') as f:
    f.seek(10)  # 移动到第 10 个字节
    content = f.read()
    print(content)

# 3. seek() 的参数
# seek(offset, whence)
# whence: 0=开头, 1=当前位置, 2=结尾
with open('data.txt', 'rb') as f:
    f.seek(0, 0)   # 移动到开头
    f.seek(5, 1)   # 从当前位置向后移动 5 字节
    f.seek(-10, 2) # 从结尾向前移动 10 字节
```

---

## 5.7 常用函数和方法

### 5.7.1 文件对象方法

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    # 读取方法
    content = f.read()       # 读取全部
    line = f.readline()      # 读取一行
    lines = f.readlines()    # 读取所有行

    # 写入方法
    f.write('text')          # 写入字符串
    f.writelines(['a', 'b']) # 写入序列

    # 指针操作
    pos = f.tell()           # 获取指针位置
    f.seek(0)                # 移动指针

    # 其他方法
    f.flush()                # 刷新缓冲区
    f.close()                # 关闭文件
    f.closed                 # 是否已关闭
    f.name                   # 文件名
    f.mode                   # 打开模式
    f.encoding               # 编码格式
```

### 5.7.2 os 模块

```python
import os

# 文件操作
os.remove('file.txt')                    # 删除文件
os.rename('old.txt', 'new.txt')          # 重命名
os.path.exists('file.txt')               # 检查是否存在
os.path.isfile('file.txt')               # 是否是文件
os.path.isdir('folder')                  # 是否是目录
os.path.getsize('file.txt')              # 获取文件大小
os.path.getctime('file.txt')             # 创建时间
os.path.getmtime('file.txt')             # 修改时间

# 目录操作
os.getcwd()                              # 当前目录
os.chdir('/path/to/dir')                 # 切换目录
os.listdir('.')                          # 列出文件
os.mkdir('new_folder')                   # 创建目录
os.makedirs('path/to/folder')            # 创建多级目录
os.rmdir('folder')                       # 删除空目录

# 路径操作
os.path.join('folder', 'file.txt')       # 拼接路径
os.path.split('/path/to/file.txt')       # 分割路径
os.path.dirname('/path/to/file.txt')     # 目录名
os.path.basename('/path/to/file.txt')    # 文件名
os.path.splitext('file.txt')             # 分离扩展名
os.path.abspath('file.txt')              # 绝对路径
```

### 5.7.3 shutil 模块

```python
import shutil

# 文件操作
shutil.copy('src.txt', 'dst.txt')        # 复制文件
shutil.copy2('src.txt', 'dst.txt')       # 复制文件（保留元数据）
shutil.move('src.txt', 'dst.txt')        # 移动文件
shutil.copyfile('src.txt', 'dst.txt')    # 复制文件内容

# 目录操作
shutil.copytree('src_dir', 'dst_dir')    # 复制目录树
shutil.rmtree('folder')                  # 删除目录树
shutil.make_archive('archive', 'zip', 'folder')  # 创建压缩包

# 磁盘使用情况
total, used, free = shutil.disk_usage('/')
print(f"总计: {total // (2**30)} GB")
print(f"已用: {used // (2**30)} GB")
print(f"空闲: {free // (2**30)} GB")
```

### 5.7.4 pathlib 模块（推荐）

```python
from pathlib import Path

# 创建路径对象
p = Path('data.txt')
p = Path('/usr/local/bin')
p = Path.home() / 'documents' / 'file.txt'

# 路径操作
print(p.name)           # 文件名
print(p.stem)           # 文件名（不含扩展名）
print(p.suffix)         # 扩展名
print(p.parent)         # 父目录
print(p.absolute())     # 绝对路径

# 文件判断
print(p.exists())       # 是否存在
print(p.is_file())      # 是否是文件
print(p.is_dir())       # 是否是目录

# 文件操作
p.unlink()              # 删除文件
p.rename('new.txt')     # 重命名
p.mkdir()               # 创建目录
p.rmdir()               # 删除目录

# 读写文件
content = p.read_text(encoding='utf-8')    # 读取文本
p.write_text('content', encoding='utf-8')  # 写入文本
data = p.read_bytes()                      # 读取二进制
p.write_bytes(data)                        # 写入二进制

# 遍历目录
for file in Path('.').glob('*.txt'):
    print(file)

for file in Path('.').rglob('*.py'):  # 递归查找
    print(file)
```

### 5.7.5 glob 模块

```python
import glob

# 查找文件
files = glob.glob('*.txt')                # 当前目录所有 .txt 文件
files = glob.glob('**/*.py', recursive=True)  # 递归查找所有 .py 文件
files = glob.glob('data/*.csv')           # data 目录的所有 .csv 文件

# 示例
for file in glob.glob('*.txt'):
    print(file)
```

---

## 5.8 案例：文件拷贝

### 5.8.1 基本文本文件拷贝

```python
def copy_text_file(source, destination):
    """
    拷贝文本文件

    参数:
        source: 源文件路径
        destination: 目标文件路径
    """
    try:
        with open(source, 'r', encoding='utf-8') as src:
            with open(destination, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
        print(f"文件拷贝成功: {source} -> {destination}")
    except FileNotFoundError:
        print(f"错误：源文件不存在 - {source}")
    except PermissionError:
        print(f"错误：没有权限访问文件")
    except Exception as e:
        print(f"错误：{e}")

# 使用示例
copy_text_file('source.txt', 'destination.txt')
```

### 5.8.2 二进制文件拷贝

```python
def copy_binary_file(source, destination):
    """
    拷贝二进制文件（适用于图片、视频等）

    参数:
        source: 源文件路径
        destination: 目标文件路径
    """
    try:
        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                dst.write(src.read())
        print(f"文件拷贝成功: {source} -> {destination}")
    except FileNotFoundError:
        print(f"错误：源文件不存在 - {source}")
    except Exception as e:
        print(f"错误：{e}")

# 使用示例
copy_binary_file('image.jpg', 'image_copy.jpg')
```

### 5.8.3 分块拷贝大文件

```python
def copy_large_file(source, destination, chunk_size=1024*1024):
    """
    分块拷贝大文件

    参数:
        source: 源文件路径
        destination: 目标文件路径
        chunk_size: 每次读取的字节数（默认 1MB）
    """
    try:
        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break
                    dst.write(chunk)
        print(f"大文件拷贝成功: {source} -> {destination}")
    except FileNotFoundError:
        print(f"错误：源文件不存在 - {source}")
    except Exception as e:
        print(f"错误：{e}")

# 使用示例
copy_large_file('large_video.mp4', 'large_video_copy.mp4')
```

### 5.8.4 带进度显示的文件拷贝

```python
import os

def copy_file_with_progress(source, destination, chunk_size=1024*1024):
    """
    带进度显示的文件拷贝

    参数:
        source: 源文件路径
        destination: 目标文件路径
        chunk_size: 每次读取的字节数
    """
    try:
        # 获取文件大小
        file_size = os.path.getsize(source)
        copied_size = 0

        with open(source, 'rb') as src:
            with open(destination, 'wb') as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break

                    dst.write(chunk)
                    copied_size += len(chunk)

                    # 计算进度
                    progress = (copied_size / file_size) * 100
                    print(f"\r进度: {progress:.1f}%", end='')

        print(f"\n文件拷贝成功: {source} -> {destination}")

    except FileNotFoundError:
        print(f"\n错误：源文件不存在 - {source}")
    except Exception as e:
        print(f"\n错误：{e}")

# 使用示例
copy_file_with_progress('large_file.zip', 'large_file_copy.zip')
```

### 5.8.5 使用 shutil 模块拷贝

```python
import shutil
import os

def copy_file_shutil(source, destination):
    """
    使用 shutil 模块拷贝文件（推荐方法）

    参数:
        source: 源文件路径
        destination: 目标文件路径
    """
    try:
        # 方法 1：copy() - 拷贝文件
        shutil.copy(source, destination)

        # 方法 2：copy2() - 拷贝文件和元数据
        # shutil.copy2(source, destination)

        # 方法 3：copyfile() - 仅拷贝内容
        # shutil.copyfile(source, destination)

        print(f"文件拷贝成功: {source} -> {destination}")

    except FileNotFoundError:
        print(f"错误：源文件不存在 - {source}")
    except PermissionError:
        print(f"错误：没有权限访问文件")
    except Exception as e:
        print(f"错误：{e}")

# 使用示例
copy_file_shutil('source.txt', 'destination.txt')
```

### 5.8.6 批量拷贝文件

```python
import os
import shutil

def batch_copy_files(source_dir, dest_dir, extension='*.txt'):
    """
    批量拷贝指定类型的文件

    参数:
        source_dir: 源目录
        dest_dir: 目标目录
        extension: 文件扩展名（如 '*.txt'）
    """
    import glob

    # 创建目标目录
    os.makedirs(dest_dir, exist_ok=True)

    # 查找所有匹配的文件
    pattern = os.path.join(source_dir, extension)
    files = glob.glob(pattern)

    # 拷贝文件
    copied_count = 0
    for source_file in files:
        filename = os.path.basename(source_file)
        dest_file = os.path.join(dest_dir, filename)

        try:
            shutil.copy2(source_file, dest_file)
            print(f"已拷贝: {filename}")
            copied_count += 1
        except Exception as e:
            print(f"拷贝失败 {filename}: {e}")

    print(f"\n共拷贝 {copied_count} 个文件")

# 使用示例
batch_copy_files('source_folder', 'backup_folder', '*.txt')
```

### 5.8.7 完整的文件拷贝工具

```python
import os
import shutil
from pathlib import Path

def advanced_copy(source, destination, overwrite=False, preserve_metadata=True):
    """
    高级文件拷贝工具

    参数:
        source: 源文件或目录路径
        destination: 目标路径
        overwrite: 是否覆盖已存在的文件
        preserve_metadata: 是否保留元数据（修改时间等）

    返回:
        成功返回 True，失败返回 False
    """
    source_path = Path(source)
    dest_path = Path(destination)

    # 检查源是否存在
    if not source_path.exists():
        print(f"错误：源不存在 - {source}")
        return False

    # 检查目标是否已存在
    if dest_path.exists() and not overwrite:
        print(f"错误：目标已存在 - {destination}")
        print("提示：使用 overwrite=True 来覆盖")
        return False

    try:
        # 如果是文件
        if source_path.is_file():
            if preserve_metadata:
                shutil.copy2(source, destination)
            else:
                shutil.copy(source, destination)

            file_size = source_path.stat().st_size
            print(f"文件拷贝成功: {source} -> {destination}")
            print(f"大小: {file_size:,} 字节")

        # 如果是目录
        elif source_path.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=overwrite)

            file_count = sum(1 for _ in dest_path.rglob('*') if _.is_file())
            print(f"目录拷贝成功: {source} -> {destination}")
            print(f"包含 {file_count} 个文件")

        return True

    except PermissionError:
        print(f"错误：没有权限访问")
        return False
    except Exception as e:
        print(f"错误：{e}")
        return False

# 使用示例
advanced_copy('source.txt', 'backup.txt', overwrite=True)
advanced_copy('source_folder', 'backup_folder', overwrite=False)
```

---

## 5.9 文件操作的最佳实践

### 5.9.1 始终使用 with 语句

```python
# 不推荐
file = open('data.txt', 'r')
content = file.read()
file.close()

# 推荐
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
```

### 5.9.2 显式指定编码

```python
# 不推荐
with open('data.txt', 'r') as f:
    content = f.read()

# 推荐
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### 5.9.3 处理异常

```python
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有权限访问文件")
except UnicodeDecodeError:
    print("编码错误")
except Exception as e:
    print(f"发生错误: {e}")
```

### 5.9.4 使用 pathlib 处理路径

```python
from pathlib import Path

# 推荐
file_path = Path('data') / 'file.txt'
if file_path.exists():
    content = file_path.read_text(encoding='utf-8')
```

### 5.9.5 逐行处理大文件

```python
# 不推荐（大文件会占用大量内存）
with open('large_file.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        process(line)

# 推荐
with open('large_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        process(line)
```

---

## 综合示例

### 示例 1：日志文件分析

```python
from pathlib import Path
from collections import Counter

def analyze_log_file(log_path):
    """分析日志文件，统计错误类型"""
    error_counter = Counter()

    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'ERROR' in line:
                # 提取错误类型
                parts = line.split()
                if len(parts) > 2:
                    error_type = parts[2]
                    error_counter[error_type] += 1

    # 打印统计结果
    print("错误统计:")
    for error_type, count in error_counter.most_common():
        print(f"{error_type}: {count} 次")

# 使用示例
# analyze_log_file('app.log')
```

### 示例 2：CSV 文件处理

```python
def process_csv(input_file, output_file):
    """处理 CSV 文件，过滤和转换数据"""
    import csv

    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

            writer.writeheader()
            for row in reader:
                # 过滤：只保留分数大于 60 的记录
                if int(row['score']) > 60:
                    writer.writerow(row)

# 使用示例
# process_csv('students.csv', 'passed_students.csv')
```

### 示例 3：配置文件读写

```python
import json

def save_config(config_dict, config_file='config.json'):
    """保存配置到 JSON 文件"""
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config_dict, f, ensure_ascii=False, indent=2)

def load_config(config_file='config.json'):
    """从 JSON 文件加载配置"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 使用示例
config = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'settings': {
        'debug': True,
        'language': 'zh-CN'
    }
}

save_config(config)
loaded_config = load_config()
print(loaded_config)
```

---

## 总结

本章介绍了 Python 文件操作的核心概念：

1. **文件基本概念**：文件的作用和操作流程
2. **文件分类**：文本文件和二进制文件的区别
3. **文件编码**：ASCII、GBK、UTF-8 等编码格式
4. **文件打开与关闭**：open() 函数和 with 语句
5. **文件写操作**：write()、writelines() 方法
6. **文件读操作**：read()、readline()、readlines() 和文件迭代
7. **常用函数**：os、shutil、pathlib 模块
8. **实战案例**：文件拷贝的多种实现方式

掌握文件操作是 Python 编程的重要技能，能够让程序与外部数据进行有效交互。

---

## 练习题

1. 编写程序，读取文本文件并统计单词出现次数
2. 实现一个简单的日志记录器，将日志写入文件
3. 编写程序，将多个文本文件合并为一个文件
4. 实现文件加密和解密功能（简单的字符替换）
5. 编写程序，统计代码文件的行数、空行数和注释行数
6. 实现一个文件搜索工具，在目录中查找包含特定文本的文件
7. 编写程序，将 CSV 文件转换为 JSON 格式
8. 实现一个文件备份工具，自动备份指定目录的文件
