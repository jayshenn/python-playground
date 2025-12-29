# TCP (Transmission Control Protocol)

本章节介绍 TCP 协议的特点及其在 Python 中的编程实现。

## 核心知识点

1. **什么是 TCP**：面向连接、可靠的传输协议。传输前需三次握手，传输后需四次挥手。
2. **特点**：保证数据按序到达、不重不漏、支持流量控制和拥塞控制。
3. **TCP 编程流程**：
    - **客户端**：创建 Socket (`SOCK_STREAM`) -> `connect()` -> `send()` / `recv()` -> `close()`。
    - **服务端**：创建 Socket -> `bind()` -> `listen()` -> `accept()` -> `recv()` / `send()` -> `close()`。

## 文件列表

- `01_what_is_tcp.py`: 介绍 TCP 协议的特点和核心机制（如握手）。
- `02_tcp_programming.py`: 演示 TCP 客户端和服务端的基础交互逻辑。
