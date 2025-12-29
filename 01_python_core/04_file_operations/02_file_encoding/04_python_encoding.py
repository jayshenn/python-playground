"""
Python 中的编码处理

对应文档: 05-file-operations.md § 5.3.4
"""

# 1. 字符串编码为字节
text = "你好，世界！"
utf8_bytes = text.encode('utf-8')
print(f"Encoded (utf-8): {utf8_bytes}")

try:
    gbk_bytes = text.encode('gbk')
    print(f"Encoded (gbk): {gbk_bytes}")
except LookupError:
    print("GBK encoding not available")
    gbk_bytes = None

# 2. 字节解码为字符串
text1 = utf8_bytes.decode('utf-8')
print(f"Decoded (utf-8): {text1}")

if gbk_bytes:
    text2 = gbk_bytes.decode('gbk')
    print(f"Decoded (gbk): {text2}")

# 3. 编码错误处理
print("\n--- Error Handling ---")
try:
    # 用错误的编码解码
    # gbk 字节用 utf-8 解码通常会失败
    if gbk_bytes:
        gbk_bytes.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"Decode error: {e}")

# 4. 忽略错误
if gbk_bytes:
    result_ignore = gbk_bytes.decode('utf-8', errors='ignore')
    print(f"Ignore errors: '{result_ignore}'")

# 5. 替换错误字符
if gbk_bytes:
    result_replace = gbk_bytes.decode('utf-8', errors='replace')
    print(f"Replace errors: '{result_replace}'")
