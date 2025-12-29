# 第 12 章 网络编程

网络编程是现代应用程序的核心技能之一。本章将介绍 Python 网络编程的基础知识，包括网络协议、Socket 编程、UDP/TCP 通信以及 HTTP 请求处理。

## 12.1 网络

### 12.1.1 网络编程三要素

网络编程的三要素是实现网络通信的基础：

1. **IP 地址**
   - 用于唯一标识网络中的设备
   - 类似于现实中的地址，确定通信的目标位置

2. **端口号**
   - 标识设备上的具体应用程序
   - 一个 IP 地址可以有多个端口，每个端口对应一个应用程序

3. **传输协议**
   - 定义数据传输的规则
   - 常见协议：TCP、UDP、HTTP 等

```python
# 网络通信示例概念
"""
客户端 (192.168.1.100:5000)
    ↓
    通过 TCP 协议
    ↓
服务器 (192.168.1.200:8080)
"""
```

### 12.1.2 TCP/IP 协议族

TCP/IP 协议族是互联网的基础协议集，采用四层模型：

| 层次 | 名称 | 主要协议 | 功能 |
|------|------|----------|------|
| 应用层 | Application Layer | HTTP, FTP, SMTP, DNS | 为应用程序提供网络服务 |
| 传输层 | Transport Layer | TCP, UDP | 提供端到端的数据传输 |
| 网络层 | Internet Layer | IP, ICMP, ARP | 处理数据包的路由和转发 |
| 网络接口层 | Link Layer | Ethernet, Wi-Fi | 处理硬件层面的数据传输 |

**协议族特点**：

- **分层设计**：每层独立，互不干扰
- **协议无关**：上层协议不依赖下层具体实现
- **可扩展性**：易于添加新协议

```python
# TCP/IP 协议栈数据封装示例
"""
应用层：HTTP 请求数据
    ↓ 添加 TCP 头部
传输层：TCP 段
    ↓ 添加 IP 头部
网络层：IP 数据包
    ↓ 添加以太网帧头
网络接口层：以太网帧
"""
```

## 12.2 IP

### 12.2.1 什么是 IP

IP（Internet Protocol，互联网协议）地址是网络设备的唯一标识符。

**IPv4 地址格式**：
- 由 4 个字节（32 位）组成
- 每个字节范围：0-255
- 用点分十进制表示：`192.168.1.1`

```python
import socket

# 获取本机 IP 地址
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"主机名: {hostname}")
print(f"IP 地址: {ip_address}")

# 获取域名对应的 IP 地址
domain = "www.python.org"
ip = socket.gethostbyname(domain)
print(f"{domain} 的 IP 地址: {ip}")

# 获取所有 IP 地址（某些域名有多个 IP）
ip_list = socket.getaddrinfo(domain, None)
print(f"{domain} 的所有 IP 地址:")
for info in ip_list:
    print(f"  {info[4][0]}")
```

### 12.2.2 子网掩码

子网掩码用于划分网络地址和主机地址。

**基本概念**：
- 与 IP 地址配合使用
- 确定 IP 地址的网络部分和主机部分
- 常见格式：`255.255.255.0` 或 `/24`

```python
import ipaddress

# 使用 ipaddress 模块处理 IP 和子网
network = ipaddress.IPv4Network('192.168.1.0/24')

print(f"网络地址: {network.network_address}")
print(f"广播地址: {network.broadcast_address}")
print(f"子网掩码: {network.netmask}")
print(f"主机数量: {network.num_addresses}")

# 判断 IP 是否在子网内
ip = ipaddress.IPv4Address('192.168.1.100')
print(f"{ip} 在网络中: {ip in network}")

# 遍历子网中的所有主机
print("\n前 5 个可用主机 IP:")
for i, host in enumerate(network.hosts()):
    if i >= 5:
        break
    print(f"  {host}")
```

### 12.2.3 IPv4 地址的分类

IPv4 地址分为 A、B、C、D、E 五类：

| 类别 | 范围 | 默认子网掩码 | 网络数 | 主机数 | 用途 |
|------|------|--------------|--------|--------|------|
| A 类 | 1.0.0.0 - 126.255.255.255 | 255.0.0.0 | 126 | 16,777,214 | 大型网络 |
| B 类 | 128.0.0.0 - 191.255.255.255 | 255.255.0.0 | 16,384 | 65,534 | 中型网络 |
| C 类 | 192.0.0.0 - 223.255.255.255 | 255.255.255.0 | 2,097,152 | 254 | 小型网络 |
| D 类 | 224.0.0.0 - 239.255.255.255 | - | - | - | 组播 |
| E 类 | 240.0.0.0 - 255.255.255.255 | - | - | - | 实验保留 |

```python
import ipaddress

def classify_ipv4(ip_str):
    """判断 IPv4 地址的类别"""
    ip = ipaddress.IPv4Address(ip_str)
    first_octet = int(str(ip).split('.')[0])

    if 1 <= first_octet <= 126:
        return 'A 类地址', '255.0.0.0'
    elif 128 <= first_octet <= 191:
        return 'B 类地址', '255.255.0.0'
    elif 192 <= first_octet <= 223:
        return 'C 类地址', '255.255.255.0'
    elif 224 <= first_octet <= 239:
        return 'D 类地址（组播）', 'N/A'
    elif 240 <= first_octet <= 255:
        return 'E 类地址（保留）', 'N/A'
    else:
        return '特殊地址', 'N/A'

# 测试不同类别的 IP
test_ips = ['10.0.0.1', '172.16.0.1', '192.168.1.1', '224.0.0.1']
for ip in test_ips:
    category, mask = classify_ipv4(ip)
    print(f"{ip:15s} -> {category:20s} (默认子网掩码: {mask})")
```

### 12.2.4 公网与私网

**公网 IP（Public IP）**：
- 在互联网上全球唯一
- 可以直接访问互联网
- 由 ISP（互联网服务提供商）分配

**私网 IP（Private IP）**：
- 仅在局域网内使用
- 不能直接访问互联网（需要 NAT）
- 可以重复使用

**私网 IP 地址范围**：
- A 类：`10.0.0.0` - `10.255.255.255` (10.0.0.0/8)
- B 类：`172.16.0.0` - `172.31.255.255` (172.16.0.0/12)
- C 类：`192.168.0.0` - `192.168.255.255` (192.168.0.0/16)

```python
import ipaddress

def is_private_ip(ip_str):
    """判断是否为私网 IP"""
    ip = ipaddress.IPv4Address(ip_str)
    return ip.is_private

# 测试公网和私网 IP
test_ips = [
    '192.168.1.1',    # 私网
    '10.0.0.1',       # 私网
    '172.16.0.1',     # 私网
    '8.8.8.8',        # 公网（Google DNS）
    '114.114.114.114' # 公网（国内 DNS）
]

for ip in test_ips:
    ip_type = "私网 IP" if is_private_ip(ip) else "公网 IP"
    print(f"{ip:15s} -> {ip_type}")

# 其他特殊 IP 判断
ip = ipaddress.IPv4Address('127.0.0.1')
print(f"\n127.0.0.1 是回环地址: {ip.is_loopback}")
print(f"127.0.0.1 是私网地址: {ip.is_private}")

ip = ipaddress.IPv4Address('169.254.1.1')
print(f"169.254.1.1 是链路本地地址: {ip.is_link_local}")
```

### 12.2.5 IPv4 与 IPv6

**IPv4 vs IPv6 对比**：

| 特性 | IPv4 | IPv6 |
|------|------|------|
| 地址长度 | 32 位 | 128 位 |
| 地址数量 | 约 43 亿 | 约 3.4×10³⁸ |
| 表示方法 | 点分十进制 (192.168.1.1) | 冒号分隔十六进制 (2001:db8::1) |
| 地址分配 | 即将耗尽 | 地址充足 |
| 配置 | 手动或 DHCP | 支持自动配置 |
| 安全性 | 可选 IPSec | 内置 IPSec |
| 报头大小 | 20-60 字节 | 40 字节（固定） |

```python
import ipaddress
import socket

# IPv4 地址处理
ipv4 = ipaddress.IPv4Address('192.168.1.1')
print(f"IPv4 地址: {ipv4}")
print(f"IPv4 整数表示: {int(ipv4)}")
print(f"IPv4 二进制: {bin(int(ipv4))}")

# IPv6 地址处理
ipv6 = ipaddress.IPv6Address('2001:db8::1')
print(f"\nIPv6 地址: {ipv6}")
print(f"IPv6 完整形式: {ipv6.exploded}")
print(f"IPv6 压缩形式: {ipv6.compressed}")

# IPv4 映射到 IPv6
ipv4_mapped = ipaddress.IPv6Address(f'::ffff:{ipv4}')
print(f"\nIPv4 映射的 IPv6: {ipv4_mapped}")

# 检查系统支持的地址族
print(f"\n系统支持 IPv4: {socket.has_ipv6 or True}")
print(f"系统支持 IPv6: {socket.has_ipv6}")

# 获取本机的 IPv6 地址
try:
    # 获取所有地址信息
    addr_info = socket.getaddrinfo(socket.gethostname(), None)
    print("\n本机所有 IP 地址:")
    for info in addr_info:
        family = "IPv4" if info[0] == socket.AF_INET else "IPv6"
        print(f"  {family}: {info[4][0]}")
except Exception as e:
    print(f"获取地址失败: {e}")
```

## 12.3 端口

### 12.3.1 什么是端口

端口（Port）是计算机与外界通信的出入口，用于区分不同的应用程序。

**端口特点**：
- 端口号范围：0-65535（16 位整数）
- 每个端口号对应一个应用程序
- 同一端口不能被多个程序同时占用

**端口的作用**：
```python
# 端口类比：IP 地址像小区地址，端口号像门牌号
"""
IP 地址: 192.168.1.100 (某台电脑)
    ↓
端口 80  -> Web 服务器
端口 22  -> SSH 服务
端口 3306 -> MySQL 数据库
端口 8080 -> 应用程序
"""
```

```python
import socket

def check_port(host, port):
    """检查端口是否开放"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        return False
    except socket.error:
        return False
    finally:
        sock.close()

# 检查常见端口
common_ports = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH',
    21: 'FTP',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    6379: 'Redis',
    27017: 'MongoDB'
}

print("检查本机常见端口状态:")
for port, service in common_ports.items():
    status = "开放" if check_port('localhost', port) else "关闭"
    print(f"端口 {port:5d} ({service:10s}): {status}")
```

### 12.3.2 端口号的分配

端口号分为三类：

| 类别 | 端口范围 | 说明 | 示例 |
|------|----------|------|------|
| 知名端口 | 0-1023 | 系统保留，分配给标准服务 | HTTP(80), HTTPS(443), SSH(22) |
| 注册端口 | 1024-49151 | 注册给特定应用程序 | MySQL(3306), PostgreSQL(5432) |
| 动态端口 | 49152-65535 | 临时端口，供客户端动态使用 | 客户端随机分配 |

**常见知名端口**：

```python
# 常见端口号字典
WELL_KNOWN_PORTS = {
    20: 'FTP 数据传输',
    21: 'FTP 控制',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP (邮件发送)',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3 (邮件接收)',
    143: 'IMAP (邮件)',
    443: 'HTTPS',
    3389: 'Windows 远程桌面',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    6379: 'Redis',
    8080: 'HTTP 备用端口',
    27017: 'MongoDB'
}

def get_service_name(port):
    """根据端口号获取服务名称"""
    return WELL_KNOWN_PORTS.get(port, '未知服务')

# 查询端口对应的服务
ports_to_check = [80, 443, 3306, 8080, 12345]
for port in ports_to_check:
    service = get_service_name(port)
    print(f"端口 {port}: {service}")
```

## 12.4 socket 套接字

### 12.4.1 什么是 socket

Socket（套接字）是网络通信的端点，是应用程序与网络协议栈的接口。

**Socket 的概念**：
- 位于应用层和传输层之间
- 提供统一的编程接口
- 支持不同的协议（TCP、UDP 等）

**Socket 类型**：

| 类型 | 说明 | 特点 | 使用场景 |
|------|------|------|----------|
| SOCK_STREAM | 流式套接字 | 基于 TCP，可靠、有序、双向 | 文件传输、Web 服务 |
| SOCK_DGRAM | 数据报套接字 | 基于 UDP，不可靠、无序、快速 | 视频流、DNS 查询 |
| SOCK_RAW | 原始套接字 | 直接访问 IP 层 | 网络诊断工具 |

```python
import socket

# Socket 地址族
print("地址族:")
print(f"  AF_INET (IPv4): {socket.AF_INET}")
print(f"  AF_INET6 (IPv6): {socket.AF_INET6}")

# Socket 类型
print("\nSocket 类型:")
print(f"  SOCK_STREAM (TCP): {socket.SOCK_STREAM}")
print(f"  SOCK_DGRAM (UDP): {socket.SOCK_DGRAM}")

# 创建不同类型的 Socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"\nTCP Socket 创建成功: {tcp_socket}")
tcp_socket.close()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"UDP Socket 创建成功: {udp_socket}")
udp_socket.close()
```

### 12.4.2 socket 的使用

**Socket 编程基本流程**：

```python
"""
服务器端流程：
1. 创建 socket
2. 绑定地址和端口 (bind)
3. 监听连接 (listen)
4. 接受连接 (accept)
5. 发送/接收数据 (send/recv)
6. 关闭连接 (close)

客户端流程：
1. 创建 socket
2. 连接服务器 (connect)
3. 发送/接收数据 (send/recv)
4. 关闭连接 (close)
"""
```

**基本 Socket 方法**：

| 方法 | 说明 | 适用 |
|------|------|------|
| `socket()` | 创建套接字 | 服务器/客户端 |
| `bind(address)` | 绑定地址和端口 | 服务器 |
| `listen(backlog)` | 开始监听连接 | 服务器 |
| `accept()` | 接受客户端连接 | 服务器 |
| `connect(address)` | 连接到服务器 | 客户端 |
| `send(data)` | 发送数据 | 服务器/客户端 |
| `recv(bufsize)` | 接收数据 | 服务器/客户端 |
| `close()` | 关闭套接字 | 服务器/客户端 |

```python
import socket

# Socket 常用方法示例
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置 socket 选项
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 允许地址重用

# 设置超时
sock.settimeout(5.0)  # 5 秒超时

# 获取 socket 信息
print(f"Socket 家族: {sock.family}")
print(f"Socket 类型: {sock.type}")
print(f"Socket 超时: {sock.gettimeout()}")

# 获取主机名
hostname = socket.gethostname()
print(f"主机名: {hostname}")

# 关闭 socket
sock.close()

# 使用上下文管理器（推荐）
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket 在 with 块中自动管理")
    # s 会在退出 with 块时自动关闭
```

## 12.5 UDP

### 12.5.1 什么是 UDP

UDP（User Datagram Protocol，用户数据报协议）是一种无连接的传输层协议。

**UDP 特点**：

| 特点 | 说明 |
|------|------|
| 无连接 | 不需要建立连接，直接发送数据 |
| 不可靠 | 不保证数据到达，不保证顺序 |
| 快速 | 无握手过程，开销小 |
| 轻量 | 头部只有 8 字节 |
| 支持广播/组播 | 可以一对多传输 |

**UDP 优缺点**：

✅ **优点**：
- 速度快，实时性好
- 简单，开销小
- 支持一对多通信

❌ **缺点**：
- 不可靠，可能丢包
- 无流量控制
- 无拥塞控制

**适用场景**：
- 实时音视频传输
- DNS 查询
- 游戏数据传输
- 物联网设备通信

### 12.5.2 UDP 编程

**UDP 服务器**：

```python
import socket

def udp_server(host='127.0.0.1', port=9999):
    """UDP 服务器"""
    # 创建 UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定地址和端口
    server_socket.bind((host, port))
    print(f"UDP 服务器启动，监听 {host}:{port}")

    try:
        while True:
            # 接收数据（不需要 accept）
            data, client_address = server_socket.recvfrom(1024)
            print(f"收到来自 {client_address} 的数据: {data.decode('utf-8')}")

            # 发送响应
            response = f"服务器收到: {data.decode('utf-8')}"
            server_socket.sendto(response.encode('utf-8'), client_address)

    except KeyboardInterrupt:
        print("\n服务器关闭")
    finally:
        server_socket.close()

# 运行示例（注释掉，避免阻塞）
# udp_server()
```

**UDP 客户端**：

```python
import socket

def udp_client(host='127.0.0.1', port=9999):
    """UDP 客户端"""
    # 创建 UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 发送数据（不需要 connect）
        message = "你好，UDP 服务器！"
        client_socket.sendto(message.encode('utf-8'), (host, port))
        print(f"发送数据: {message}")

        # 接收响应
        client_socket.settimeout(5)  # 设置超时
        data, server_address = client_socket.recvfrom(1024)
        print(f"收到服务器响应: {data.decode('utf-8')}")

    except socket.timeout:
        print("接收超时")
    except Exception as e:
        print(f"错误: {e}")
    finally:
        client_socket.close()

# 运行示例（注释掉，避免阻塞）
# udp_client()
```

**UDP 广播示例**：

```python
import socket

def udp_broadcast_sender(port=9999):
    """UDP 广播发送端"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置广播选项
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    message = "广播消息"
    broadcast_address = ('255.255.255.255', port)

    sock.sendto(message.encode('utf-8'), broadcast_address)
    print(f"广播消息已发送: {message}")

    sock.close()

def udp_broadcast_receiver(port=9999):
    """UDP 广播接收端"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('', port))
    print(f"等待接收广播消息...")

    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f"收到来自 {address} 的广播: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("\n停止接收")
    finally:
        sock.close()

# 运行示例（注释掉，避免阻塞）
# udp_broadcast_sender()
# udp_broadcast_receiver()
```

## 12.6 TCP

### 12.6.1 什么是 TCP

TCP（Transmission Control Protocol，传输控制协议）是一种面向连接的、可靠的传输层协议。

**TCP 特点**：

| 特点 | 说明 |
|------|------|
| 面向连接 | 通信前需要建立连接（三次握手） |
| 可靠传输 | 保证数据完整、有序到达 |
| 流量控制 | 防止发送方发送过快 |
| 拥塞控制 | 防止网络拥塞 |
| 全双工通信 | 双方可同时发送和接收 |

**TCP 连接建立（三次握手）**：

```python
"""
客户端                    服务器
   |                         |
   |-------- SYN ----------->|  1. 客户端发送 SYN
   |                         |
   |<----- SYN + ACK --------|  2. 服务器回复 SYN + ACK
   |                         |
   |-------- ACK ----------->|  3. 客户端发送 ACK
   |                         |
   |   建立连接，开始通信      |
"""
```

**TCP 连接断开（四次挥手）**：

```python
"""
客户端                    服务器
   |                         |
   |-------- FIN ----------->|  1. 客户端发送 FIN
   |                         |
   |<------- ACK ------------|  2. 服务器回复 ACK
   |                         |
   |<------- FIN ------------|  3. 服务器发送 FIN
   |                         |
   |-------- ACK ----------->|  4. 客户端回复 ACK
   |                         |
   |      连接关闭            |
"""
```

**TCP vs UDP 对比**：

| 特性 | TCP | UDP |
|------|-----|-----|
| 连接 | 面向连接 | 无连接 |
| 可靠性 | 可靠（确认重传） | 不可靠 |
| 顺序 | 保证顺序 | 不保证顺序 |
| 速度 | 较慢 | 快速 |
| 开销 | 大（20 字节头部） | 小（8 字节头部） |
| 应用 | HTTP、FTP、邮件 | 视频、DNS、游戏 |

### 12.6.2 TCP 编程

**TCP 服务器**：

```python
import socket
import threading

def handle_client(client_socket, client_address):
    """处理客户端连接"""
    print(f"客户端 {client_address} 已连接")

    try:
        while True:
            # 接收数据
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"收到 {client_address} 的消息: {message}")

            # 发送响应
            response = f"服务器收到: {message}"
            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"处理客户端 {client_address} 时出错: {e}")
    finally:
        client_socket.close()
        print(f"客户端 {client_address} 已断开")

def tcp_server(host='127.0.0.1', port=8888):
    """TCP 服务器（支持多客户端）"""
    # 创建 TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口重用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定地址和端口
    server_socket.bind((host, port))

    # 开始监听（backlog=5 表示最多排队 5 个连接）
    server_socket.listen(5)
    print(f"TCP 服务器启动，监听 {host}:{port}")

    try:
        while True:
            # 接受客户端连接
            client_socket, client_address = server_socket.accept()

            # 为每个客户端创建新线程
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\n服务器关闭")
    finally:
        server_socket.close()

# 运行示例（注释掉，避免阻塞）
# tcp_server()
```

**TCP 客户端**：

```python
import socket

def tcp_client(host='127.0.0.1', port=8888):
    """TCP 客户端"""
    # 创建 TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到服务器
        client_socket.connect((host, port))
        print(f"已连接到服务器 {host}:{port}")

        # 发送多条消息
        messages = ["你好", "这是第二条消息", "再见"]

        for msg in messages:
            # 发送数据
            client_socket.send(msg.encode('utf-8'))
            print(f"发送: {msg}")

            # 接收响应
            data = client_socket.recv(1024)
            print(f"收到: {data.decode('utf-8')}")

    except Exception as e:
        print(f"错误: {e}")
    finally:
        client_socket.close()
        print("连接已关闭")

# 运行示例（注释掉，避免阻塞）
# tcp_client()
```

**TCP 文件传输示例**：

```python
import socket
import os

def tcp_file_server(host='127.0.0.1', port=8888):
    """TCP 文件接收服务器"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"文件服务器启动，监听 {host}:{port}")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"客户端 {address} 已连接")

            # 接收文件名
            filename = client_socket.recv(1024).decode('utf-8')
            print(f"准备接收文件: {filename}")

            # 发送确认
            client_socket.send(b'OK')

            # 接收文件数据
            with open(f'received_{filename}', 'wb') as f:
                while True:
                    data = client_socket.recv(4096)
                    if not data:
                        break
                    f.write(data)

            print(f"文件 {filename} 接收完成")
            client_socket.close()

    except KeyboardInterrupt:
        print("\n服务器关闭")
    finally:
        server_socket.close()

def tcp_file_client(filename, host='127.0.0.1', port=8888):
    """TCP 文件发送客户端"""
    if not os.path.exists(filename):
        print(f"文件 {filename} 不存在")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"已连接到服务器 {host}:{port}")

        # 发送文件名
        client_socket.send(os.path.basename(filename).encode('utf-8'))

        # 等待确认
        client_socket.recv(1024)

        # 发送文件内容
        with open(filename, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client_socket.send(data)

        print(f"文件 {filename} 发送完成")

    except Exception as e:
        print(f"错误: {e}")
    finally:
        client_socket.close()

# 运行示例（注释掉，避免阻塞）
# tcp_file_server()
# tcp_file_client('test.txt')
```

## 12.7 HTTP

### 12.7.1 什么是 HTTP

HTTP（HyperText Transfer Protocol，超文本传输协议）是应用层协议，用于传输 Web 内容。

**HTTP 特点**：
- 基于 TCP/IP 协议
- 无状态协议（每次请求独立）
- 默认端口：80（HTTP）、443（HTTPS）
- 请求-响应模型

**HTTP 版本**：

| 版本 | 发布年份 | 主要特性 |
|------|----------|----------|
| HTTP/0.9 | 1991 | 只支持 GET 方法 |
| HTTP/1.0 | 1996 | 增加 POST、HEAD 等方法 |
| HTTP/1.1 | 1997 | 持久连接、管道化、缓存 |
| HTTP/2 | 2015 | 二进制分帧、多路复用、服务器推送 |
| HTTP/3 | 2022 | 基于 QUIC（UDP），更快速 |

### 12.7.2 HTTP 消息结构

**HTTP 请求格式**：

```
请求行
请求头
空行
请求体（可选）
```

**HTTP 请求示例**：

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive

```

**HTTP 响应格式**：

```
状态行
响应头
空行
响应体
```

**HTTP 响应示例**：

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Connection: keep-alive

<!DOCTYPE html>
<html>
...
</html>
```

```python
# 解析 HTTP 请求示例
def parse_http_request(request_text):
    """解析 HTTP 请求"""
    lines = request_text.split('\n')

    # 解析请求行
    request_line = lines[0].strip()
    method, path, version = request_line.split()

    # 解析请求头
    headers = {}
    i = 1
    while i < len(lines) and lines[i].strip():
        line = lines[i].strip()
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
        i += 1

    # 请求体
    body = '\n'.join(lines[i+1:]) if i+1 < len(lines) else ''

    return {
        'method': method,
        'path': path,
        'version': version,
        'headers': headers,
        'body': body
    }

# 示例请求
request = """GET /api/users HTTP/1.1
Host: api.example.com
User-Agent: Python Client
Accept: application/json

"""

parsed = parse_http_request(request)
print("请求方法:", parsed['method'])
print("请求路径:", parsed['path'])
print("HTTP 版本:", parsed['version'])
print("请求头:", parsed['headers'])
```

### 12.7.3 HTTP 请求方法

常见的 HTTP 请求方法：

| 方法 | 说明 | 特点 |
|------|------|------|
| GET | 获取资源 | 幂等、可缓存、参数在 URL 中 |
| POST | 提交数据 | 非幂等、不可缓存、参数在请求体 |
| PUT | 更新资源 | 幂等、完整更新 |
| PATCH | 部分更新 | 非幂等、部分更新 |
| DELETE | 删除资源 | 幂等 |
| HEAD | 获取响应头 | 类似 GET，但不返回响应体 |
| OPTIONS | 获取支持的方法 | 用于 CORS 预检 |

**幂等性**：多次执行相同操作，结果相同

```python
import urllib.request
import urllib.parse
import json

# GET 请求示例
def http_get(url):
    """发送 GET 请求"""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return data.decode('utf-8')
    except Exception as e:
        return f"错误: {e}"

# POST 请求示例
def http_post(url, data):
    """发送 POST 请求"""
    try:
        # 将数据编码
        data_encoded = urllib.parse.urlencode(data).encode('utf-8')

        # 创建请求
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')

        # 发送请求
        with urllib.request.urlopen(req) as response:
            result = response.read()
            return result.decode('utf-8')
    except Exception as e:
        return f"错误: {e}"

# 示例（注释掉，避免实际请求）
# result = http_get('https://api.github.com')
# print(result)

# post_data = {'name': 'John', 'age': 30}
# result = http_post('https://httpbin.org/post', post_data)
# print(result)
```

### 12.7.4 HTTP 状态码

HTTP 状态码表示请求的处理结果，分为 5 类：

| 类别 | 范围 | 含义 |
|------|------|------|
| 1xx | 100-199 | 信息性响应 |
| 2xx | 200-299 | 成功 |
| 3xx | 300-399 | 重定向 |
| 4xx | 400-499 | 客户端错误 |
| 5xx | 500-599 | 服务器错误 |

**常见状态码**：

| 状态码 | 说明 | 含义 |
|--------|------|------|
| 200 | OK | 请求成功 |
| 201 | Created | 资源已创建 |
| 204 | No Content | 成功但无返回内容 |
| 301 | Moved Permanently | 永久重定向 |
| 302 | Found | 临时重定向 |
| 304 | Not Modified | 资源未修改（缓存有效） |
| 400 | Bad Request | 请求错误 |
| 401 | Unauthorized | 未授权 |
| 403 | Forbidden | 禁止访问 |
| 404 | Not Found | 资源不存在 |
| 405 | Method Not Allowed | 方法不允许 |
| 500 | Internal Server Error | 服务器内部错误 |
| 502 | Bad Gateway | 网关错误 |
| 503 | Service Unavailable | 服务不可用 |

```python
# HTTP 状态码字典
HTTP_STATUS_CODES = {
    # 2xx 成功
    200: 'OK',
    201: 'Created',
    204: 'No Content',

    # 3xx 重定向
    301: 'Moved Permanently',
    302: 'Found',
    304: 'Not Modified',

    # 4xx 客户端错误
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',

    # 5xx 服务器错误
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable'
}

def get_status_message(code):
    """获取状态码说明"""
    return HTTP_STATUS_CODES.get(code, 'Unknown Status')

# 测试
for code in [200, 404, 500]:
    print(f"{code}: {get_status_message(code)}")

# 判断状态码类别
def get_status_category(code):
    """判断状态码类别"""
    if 100 <= code < 200:
        return "信息性响应"
    elif 200 <= code < 300:
        return "成功"
    elif 300 <= code < 400:
        return "重定向"
    elif 400 <= code < 500:
        return "客户端错误"
    elif 500 <= code < 600:
        return "服务器错误"
    else:
        return "未知"

print(f"\n404 属于: {get_status_category(404)}")
print(f"200 属于: {get_status_category(200)}")
```

## 12.8 案例：发送 HTTP 请求以及获取网站数据

本案例演示如何使用 Python 发送 HTTP 请求并获取网站数据。

### 使用 urllib

```python
import urllib.request
import urllib.parse
import json

def fetch_url(url):
    """获取 URL 内容"""
    try:
        # 创建请求
        req = urllib.request.Request(url)

        # 添加请求头（模拟浏览器）
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

        # 发送请求
        with urllib.request.urlopen(req, timeout=10) as response:
            # 获取响应信息
            status_code = response.status
            headers = dict(response.headers)
            content = response.read().decode('utf-8')

            return {
                'status': status_code,
                'headers': headers,
                'content': content
            }
    except urllib.error.HTTPError as e:
        return {'error': f'HTTP 错误: {e.code} {e.reason}'}
    except urllib.error.URLError as e:
        return {'error': f'URL 错误: {e.reason}'}
    except Exception as e:
        return {'error': f'其他错误: {e}'}

def fetch_json_api(url):
    """获取 JSON API 数据"""
    try:
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/json')

        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as e:
        return {'error': str(e)}

# 示例：获取 GitHub API 数据
# url = 'https://api.github.com/users/python'
# result = fetch_json_api(url)
# print(json.dumps(result, indent=2, ensure_ascii=False))
```

### 使用 requests 库（推荐）

```python
# 需要安装: pip install requests
try:
    import requests

    def get_request_example():
        """GET 请求示例"""
        url = 'https://api.github.com/users/python'

        # 发送 GET 请求
        response = requests.get(url)

        # 检查状态码
        if response.status_code == 200:
            data = response.json()
            print("用户名:", data.get('name'))
            print("关注者:", data.get('followers'))
            print("仓库数:", data.get('public_repos'))
        else:
            print(f"请求失败: {response.status_code}")

    def post_request_example():
        """POST 请求示例"""
        url = 'https://httpbin.org/post'

        # 请求数据
        data = {
            'name': 'Alice',
            'age': 25,
            'city': 'Beijing'
        }

        # 发送 POST 请求
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            print("服务器收到的数据:", result.get('json'))

    def advanced_request_example():
        """高级请求示例"""
        url = 'https://api.github.com/search/repositories'

        # 查询参数
        params = {
            'q': 'python',
            'sort': 'stars',
            'order': 'desc'
        }

        # 请求头
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Python Tutorial'
        }

        # 发送请求
        response = requests.get(url, params=params, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print(f"找到 {data['total_count']} 个仓库")

            # 显示前 5 个
            for item in data['items'][:5]:
                print(f"  - {item['name']}: ⭐ {item['stargazers_count']}")

    # 运行示例（注释掉，避免实际请求）
    # get_request_example()
    # post_request_example()
    # advanced_request_example()

except ImportError:
    print("requests 库未安装，请运行: pip install requests")
```

### 网页爬取示例

```python
import urllib.request
import re

def simple_web_scraper(url):
    """简单的网页爬虫"""
    try:
        # 获取网页内容
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')

        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')

        # 提取标题
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1) if title_match else "未找到标题"

        # 提取所有链接
        links = re.findall(r'<a\s+href=["\'](.*?)["\']', html, re.IGNORECASE)

        # 提取图片
        images = re.findall(r'<img\s+[^>]*src=["\'](.*?)["\']', html, re.IGNORECASE)

        return {
            'title': title,
            'links_count': len(links),
            'images_count': len(images),
            'links': links[:10],  # 只返回前 10 个
            'images': images[:10]
        }
    except Exception as e:
        return {'error': str(e)}

# 示例（注释掉，避免实际请求）
# result = simple_web_scraper('https://www.python.org')
# print(f"标题: {result.get('title')}")
# print(f"链接数: {result.get('links_count')}")
# print(f"图片数: {result.get('images_count')}")
```

## 12.9 案例：通过 Starlette 构建 web 接口

Starlette 是一个轻量级的 ASGI Web 框架，适合构建高性能的 API 服务。

### 安装 Starlette

```bash
pip install starlette uvicorn
```

### 基础 Web 应用

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route
import uvicorn

# 定义路由处理函数
async def homepage(request):
    """首页"""
    return PlainTextResponse('欢迎使用 Starlette Web API')

async def get_user(request):
    """获取用户信息"""
    user_id = request.path_params.get('user_id')

    # 模拟用户数据
    user_data = {
        'id': user_id,
        'name': f'用户{user_id}',
        'email': f'user{user_id}@example.com'
    }

    return JSONResponse(user_data)

async def create_user(request):
    """创建用户"""
    # 获取 JSON 数据
    data = await request.json()

    # 模拟创建用户
    response_data = {
        'message': '用户创建成功',
        'user': data
    }

    return JSONResponse(response_data, status_code=201)

# 定义路由
routes = [
    Route('/', homepage),
    Route('/users/{user_id:int}', get_user),
    Route('/users', create_user, methods=['POST']),
]

# 创建应用
app = Starlette(debug=True, routes=routes)

# 运行应用（注释掉，避免阻塞）
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
```

### RESTful API 完整示例

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

# 模拟数据库
USERS_DB = {
    1: {'id': 1, 'name': '张三', 'age': 25},
    2: {'id': 2, 'name': '李四', 'age': 30},
}
next_id = 3

# API 处理函数
async def list_users(request):
    """获取所有用户 - GET /api/users"""
    return JSONResponse({'users': list(USERS_DB.values())})

async def get_user(request):
    """获取单个用户 - GET /api/users/{user_id}"""
    user_id = int(request.path_params['user_id'])

    if user_id in USERS_DB:
        return JSONResponse(USERS_DB[user_id])
    else:
        return JSONResponse({'error': '用户不存在'}, status_code=404)

async def create_user(request):
    """创建用户 - POST /api/users"""
    global next_id

    data = await request.json()

    # 验证数据
    if 'name' not in data or 'age' not in data:
        return JSONResponse(
            {'error': '缺少必需字段'},
            status_code=400
        )

    # 创建用户
    user = {
        'id': next_id,
        'name': data['name'],
        'age': data['age']
    }
    USERS_DB[next_id] = user
    next_id += 1

    return JSONResponse(user, status_code=201)

async def update_user(request):
    """更新用户 - PUT /api/users/{user_id}"""
    user_id = int(request.path_params['user_id'])

    if user_id not in USERS_DB:
        return JSONResponse({'error': '用户不存在'}, status_code=404)

    data = await request.json()

    # 更新用户
    USERS_DB[user_id].update(data)

    return JSONResponse(USERS_DB[user_id])

async def delete_user(request):
    """删除用户 - DELETE /api/users/{user_id}"""
    user_id = int(request.path_params['user_id'])

    if user_id not in USERS_DB:
        return JSONResponse({'error': '用户不存在'}, status_code=404)

    del USERS_DB[user_id]

    return JSONResponse({'message': '用户已删除'})

async def health_check(request):
    """健康检查 - GET /health"""
    return JSONResponse({'status': 'healthy'})

# 定义路由
routes = [
    Route('/health', health_check),
    Route('/api/users', list_users, methods=['GET']),
    Route('/api/users', create_user, methods=['POST']),
    Route('/api/users/{user_id:int}', get_user, methods=['GET']),
    Route('/api/users/{user_id:int}', update_user, methods=['PUT']),
    Route('/api/users/{user_id:int}', delete_user, methods=['DELETE']),
]

# 中间件配置
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*']
    )
]

# 创建应用
app = Starlette(debug=True, routes=routes, middleware=middleware)

# 运行应用
if __name__ == '__main__':
    print("启动 Starlette Web API 服务器...")
    print("访问 http://127.0.0.1:8000/health 检查服务状态")
    print("访问 http://127.0.0.1:8000/api/users 查看所有用户")
    # uvicorn.run(app, host='127.0.0.1', port=8000)
```

### 请求和响应示例

```python
# 使用 requests 测试 API（需要先启动服务器）
try:
    import requests

    def test_api():
        """测试 RESTful API"""
        base_url = 'http://127.0.0.1:8000'

        # 1. 健康检查
        print("1. 健康检查")
        response = requests.get(f'{base_url}/health')
        print(f"   状态码: {response.status_code}")
        print(f"   响应: {response.json()}\n")

        # 2. 获取所有用户
        print("2. 获取所有用户")
        response = requests.get(f'{base_url}/api/users')
        print(f"   用户列表: {response.json()}\n")

        # 3. 创建新用户
        print("3. 创建新用户")
        new_user = {'name': '王五', 'age': 28}
        response = requests.post(f'{base_url}/api/users', json=new_user)
        print(f"   状态码: {response.status_code}")
        print(f"   新用户: {response.json()}\n")

        # 4. 获取单个用户
        print("4. 获取用户 ID=1")
        response = requests.get(f'{base_url}/api/users/1')
        print(f"   用户信息: {response.json()}\n")

        # 5. 更新用户
        print("5. 更新用户 ID=1")
        update_data = {'age': 26}
        response = requests.put(f'{base_url}/api/users/1', json=update_data)
        print(f"   更新后: {response.json()}\n")

        # 6. 删除用户
        print("6. 删除用户 ID=2")
        response = requests.delete(f'{base_url}/api/users/2')
        print(f"   响应: {response.json()}\n")

        # 7. 获取不存在的用户
        print("7. 获取不存在的用户 ID=999")
        response = requests.get(f'{base_url}/api/users/999')
        print(f"   状态码: {response.status_code}")
        print(f"   响应: {response.json()}\n")

    # 运行测试（需要先启动服务器）
    # test_api()

except ImportError:
    print("requests 库未安装")
```

## 本章小结

本章介绍了 Python 网络编程的核心内容：

### 12.1 网络基础
- **网络编程三要素**：IP 地址、端口号、传输协议
- **TCP/IP 协议族**：四层模型（应用层、传输层、网络层、网络接口层）

### 12.2 IP 地址
- **IP 概念**：网络设备的唯一标识符
- **子网掩码**：划分网络地址和主机地址
- **IPv4 分类**：A、B、C、D、E 五类地址
- **公网与私网**：公网 IP 全局唯一，私网 IP 局域网内使用
- **IPv4 vs IPv6**：地址长度、数量、安全性等方面的对比

### 12.3 端口
- **端口概念**：标识设备上的具体应用程序
- **端口分类**：知名端口（0-1023）、注册端口（1024-49151）、动态端口（49152-65535）

### 12.4 Socket 套接字
- **Socket 概念**：网络通信的端点，应用程序与协议栈的接口
- **Socket 类型**：SOCK_STREAM（TCP）、SOCK_DGRAM（UDP）
- **基本方法**：socket()、bind()、listen()、accept()、connect()、send()、recv()、close()

### 12.5 UDP 编程
- **UDP 特点**：无连接、不可靠、快速、轻量
- **适用场景**：实时音视频、DNS 查询、游戏
- **UDP 编程**：服务器和客户端实现、广播通信

### 12.6 TCP 编程
- **TCP 特点**：面向连接、可靠传输、流量控制、拥塞控制
- **三次握手**：建立连接的过程
- **四次挥手**：断开连接的过程
- **TCP 编程**：服务器和客户端实现、文件传输

### 12.7 HTTP 协议
- **HTTP 概念**：应用层协议，用于传输 Web 内容
- **消息结构**：请求行/状态行、头部、空行、消息体
- **请求方法**：GET、POST、PUT、DELETE 等
- **状态码**：2xx 成功、3xx 重定向、4xx 客户端错误、5xx 服务器错误

### 12.8 HTTP 请求实战
- **urllib 库**：Python 标准库，用于发送 HTTP 请求
- **requests 库**：第三方库，更简洁易用（推荐）
- **网页爬取**：获取网页内容并提取信息

### 12.9 Web 接口开发
- **Starlette 框架**：轻量级 ASGI Web 框架
- **RESTful API**：实现增删改查操作
- **路由和中间件**：组织 API 结构

### 最佳实践

1. **选择合适的协议**
   - 需要可靠传输：使用 TCP
   - 需要高速传输：使用 UDP
   - Web 应用：使用 HTTP/HTTPS

2. **异常处理**
   - 始终捕获网络异常
   - 设置超时时间
   - 优雅处理错误

3. **资源管理**
   - 使用 with 语句管理 socket
   - 及时关闭连接
   - 避免资源泄漏

4. **安全性**
   - 使用 HTTPS 加密传输
   - 验证用户输入
   - 防止 SQL 注入、XSS 等攻击

5. **性能优化**
   - 使用连接池
   - 启用持久连接
   - 合理使用缓存

## 练习题

1. **基础练习**
   - 编写一个 TCP 聊天程序，支持多客户端同时在线
   - 实现一个 UDP 广播程序，在局域网内发送消息
   - 使用 socket 实现简单的 HTTP 服务器

2. **进阶练习**
   - 实现一个文件传输工具，支持断点续传
   - 编写网络爬虫，爬取指定网站的数据
   - 使用 Starlette 构建完整的 RESTful API

3. **综合项目**
   - 实现一个简单的聊天室（支持群聊、私聊）
   - 开发一个 Web API 服务器（用户管理、数据存储）
   - 实现一个网络代理服务器
