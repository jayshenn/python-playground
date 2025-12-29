"""
内置验证器类型

对应文档: 16-type-system-pydantic.md § 16.validation
"""

from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

# 注意：使用 EmailStr 可能需要安装 email-validator 库
# pip install "pydantic[email]"

class UserInfo(BaseModel):
    # 1. 专门的 Email 验证
    email: EmailStr
    
    # 2. 专门的 URL 验证 (会验证格式是否正确)
    website: HttpUrl | None = None

if __name__ == '__main__':
    try:
        # 尝试传入非法的 email 和 url
        UserInfo(email="invalid_mail", website="ftp://not_a_website")
    except ValidationError as e:
        print(f"Validation Errors:\n{e}")
        
    # 合法数据
    user = UserInfo(
        email="alice@example.com", 
        website="https://alice.dev"
    )
    print(f"Validated Email: {user.email}")
    # 注意：HttpUrl 对象在访问时是 Url 对象，可以获取其 scheme, host 等
    print(f"Website host: {user.website.host}")
