"""
sub

对应文档: 13-regular-expressions.md § 13.2.4
"""

import re

# re.sub() 用于替换字符串中的匹配项

def main():
    text = "联系电话: 138-1234-5678"
    
    # 将所有的 - 替换为 空
    new_text = re.sub(r"-", "", text)
    print(f"替换后的结果: {new_text}")
    
    # 将数字替换为 * (脱敏处理)
    hidden_text = re.sub(r"\d", "*", text)
    print(f"脱敏后的结果: {hidden_text}")

if __name__ == '__main__':
    main()
