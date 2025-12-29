"""
字符的编码和解码

对应文档: 01-python-basics.md § 1.4.6
"""

# 字符编码是将字符转换为字节序列的过程，解码是将字节序列转换回字符的过程。

# 编码（字符串 → 字节）
text = "Hello, 世界"
encoded = text.encode('utf-8')
print(f"Original text: {text}")
print(f"Encoded (utf-8): {encoded}")  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# 解码（字节 → 字符串）
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")

# 常见编码格式
utf8_bytes = text.encode('utf-8')
# gbk_bytes = text.encode('gbk') # 注意：在非中文环境下可能会报错，视系统支持情况而定

# 获取字符的 Unicode 码点
char_A = 'A'
char_Zhong = '中'
print(f"ord('{char_A}'): {ord(char_A)}")  # 65
print(f"ord('{char_Zhong}'): {ord(char_Zhong)}")  # 20013

# 根据码点获取字符
print(f"chr(65): {chr(65)}")  # A
print(f"chr(20013): {chr(20013)}")  # 中
