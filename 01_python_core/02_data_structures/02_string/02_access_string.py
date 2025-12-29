"""
访问字符串

对应文档: 03-data-structures.md § 3.3.2
"""

text = "Python Programming"
print(f"Text: {text}")

# 索引访问
print(f"Index 0: {text[0]}")   # P
print(f"Index -1: {text[-1]}")  # g

# 切片
print(f"Slice [0:6]: {text[0:6]}")   # Python
print(f"Slice [7:]: {text[7:]}")    # Programming
print(f"Slice [:6]: {text[:6]}")    # Python
print(f"Slice [::2]: {text[::2]}")   # Pto rgamn（步长2）
print(f"Slice [::-1]: {text[::-1]}")  # gnimmargorP nohtyP（反转）

print("\n--- Traversing String ---")
# 遍历字符串
for char in "Hello":
    print(char, end=" ")
print()

print("\n--- Enumerate String ---")
# 遍历时获取索引
for i, char in enumerate("Hello"):
    print(f"{i}: {char}")
