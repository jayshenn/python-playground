"""
自定义字段验证器

对应文档: 16-type-system-pydantic.md § 16.validation
"""

from pydantic import BaseModel, field_validator, ValidationError

class SignupForm(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v: str) -> str:
        """验证用户名只能是字母数字组合"""
        if not v.isalnum():
            raise ValueError('用户名必须是字母和数字')
        return v.lower() # 验证通过的同时还可以进行数据清洗 (转小写)

    @field_validator('password')
    @classmethod
    def password_complexity_check(cls, v: str) -> str:
        """验证密码复杂度"""
        if len(v) < 8:
            raise ValueError('密码至少 8 位')
        if not any(c.isupper() for c in v):
            raise ValueError('密码必须包含大写字母')
        if not any(c.isdigit() for c in v):
            raise ValueError('密码必须包含数字')
        return v

if __name__ == '__main__':
    try:
        # 故意传入非法数据
        SignupForm(username="alice!", password="123")
    except ValidationError as e:
        print(e)
        
    # 合法数据
    form = SignupForm(username="Alice2025", password="Password123")
    print(f"Validated form: {form}")
