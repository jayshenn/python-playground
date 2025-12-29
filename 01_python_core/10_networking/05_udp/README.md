# UDP (User Datagram Protocol)

本章节介绍 UDP 协议的特点及其在 Python 中的编程实现。

## 核心知识点

1. **什么是 UDP**：无连接、不可靠的传输协议。发送数据前不需要建立连接，速度快但可能丢包。
2. **适用场景**：实时性要求高（如视频会议、在线游戏）、允许少量数据丢失的业务。
3. **UDP 编程流程**：
    - 创建 Socket (`SOCK_DGRAM`)。
    - 使用 `sendto()` 发送数据。
    - 使用 `recvfrom()` 接收数据。

## 文件列表

- `01_what_is_udp.py`: 介绍 UDP 协议的特点和优缺点。
- `02_udp_programming.py`: 演示 UDP 发送者和接收者的基础代码。
