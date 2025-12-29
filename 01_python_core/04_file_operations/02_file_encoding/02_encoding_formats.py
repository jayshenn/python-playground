"""
常见编码格式

对应文档: 05-file-operations.md § 5.3.2
"""

# 1. ASCII
# 最早的字符编码标准，只支持英文字符、数字和符号。
text = 'Hello'
ascii_bytes = text.encode('ascii')
print(f"ASCII bytes for '{text}': {ascii_bytes}")
print(f"Length: {len(ascii_bytes)} bytes")

# 2. GBK / GB2312
# 中国国家标准编码。
text_cn = '你好'
try:
    gbk_bytes = text_cn.encode('gbk')
    print(f"GBK bytes for '{text_cn}': {gbk_bytes}")
    print(f"Length: {len(gbk_bytes)} bytes")
except LookupError:
    print("GBK encoding not supported on this system")

# 3. UTF-8（推荐）
# Unicode 的一种实现方式，支持全世界所有语言。Python 3 默认编码。
text_utf8 = '你好World'
utf8_bytes = text_utf8.encode('utf-8')
print(f"UTF-8 bytes for '{text_utf8}': {utf8_bytes}")
print(f"Length: {len(utf8_bytes)} bytes")

# 解码
decoded = utf8_bytes.decode('utf-8')
print(f"Decoded: {decoded}")

# 4. Unicode 码点
print(f"ord('A'): {ord('A')}")
print(f"ord('你'): {ord('你')}")
print(f"chr(65): {chr(65)}")
print(f"chr(20320): {chr(20320)}")
