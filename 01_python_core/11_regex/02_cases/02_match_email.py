"""
匹配邮箱

对应文档: 13-regular-expressions.md § 13.8.2
"""

import re

# 简单邮箱正则：用户名@域名.后缀

def check_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    emails = ["test@example.com", "user.name@company.org", "invalid-email", "test@site"]
    for e in emails:
        print(f"{e} 是否合法: {check_email(e)}")
