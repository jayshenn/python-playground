"""
模型验证器 (跨字段验证)

对应文档: 16-type-system-pydantic.md § 16.validation
"""

from pydantic import BaseModel, model_validator, ValidationError

class Registration(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'Registration':
        """
        在所有单个字段验证完成后调用。
        此时可以访问 self.password 和 self.confirm_password。
        """
        if self.password != self.confirm_password:
            # 关联到具体字段的错误抛出方式 (可选)
            raise ValueError('两次输入的密码不一致')
        return self

if __name__ == '__main__':
    try:
        Registration(password="secret123", confirm_password="different")
    except ValidationError as e:
        print(f"Error: {e.errors()[0]['msg']}")
        
    # 成功示例
    reg = Registration(password="secret123", confirm_password="secret123")
    print("Registration successful!")
