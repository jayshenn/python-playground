"""
编码对比

对应文档: 05-file-operations.md § 5.3.3
"""

# | 编码 | 支持语言 | 英文占用 | 中文占用 | 优点 | 缺点 |
# |------|---------|---------|---------|------|------|
# | **ASCII** | 仅英文 | 1 字节 | 不支持 | 简单、高效 | 只支持英文 |
# | **GBK** | 中文 | 1 字节 | 2 字节 | 节省空间 | 不支持其他语言 |
# | **UTF-8** | 全球 | 1 字节 | 3 字节 | 兼容性好、支持所有语言 | 中文占用空间大 |
# | **UTF-16** | 全球 | 2 字节 | 2 字节 | 定长、处理速度快 | 英文浪费空间 |

text = "A中"

print(f"Text: {text}")

# UTF-8
utf8_bytes = text.encode('utf-8')
print(f"UTF-8: {utf8_bytes}, Length: {len(utf8_bytes)}")
# A (1 byte) + 中 (3 bytes) = 4 bytes

# GBK (might fail on some systems if not supported)
try:
    gbk_bytes = text.encode('gbk')
    print(f"GBK: {gbk_bytes}, Length: {len(gbk_bytes)}")
    # A (1 byte) + 中 (2 bytes) = 3 bytes
except LookupError:
    print("GBK encoding not available")
