"""
条件验证

对应文档: 16-type-system-pydantic.md § 16.validation
"""

from pydantic import BaseModel, model_validator, ValidationError
from typing import Literal

class Payment(BaseModel):
    """
    支付模型：根据支付方式(method)验证不同的必需字段。
    """
    method: Literal["credit_card", "paypal"]
    amount: float
    
    # 信用卡相关
    card_number: str | None = None
    cvv: str | None = None
    
    # PayPal 相关
    paypal_email: str | None = None

    @model_validator(mode='after')
    def validate_payment_details(self) -> 'Payment':
        if self.method == "credit_card":
            if not self.card_number or not self.cvv:
                raise ValueError("信用卡支付需要提供卡号和 CVV")
        elif self.method == "paypal":
            if not self.paypal_email:
                raise ValueError("PayPal 支付需要提供邮箱地址")
        return self

if __name__ == '__main__':
    # 1. 信用卡支付，但缺少信息
    try:
        Payment(method="credit_card", amount=100.0)
    except ValidationError as e:
        print(f"Credit Card Error: {e.errors()[0]['msg']}")
        
    # 2. 合法支付
    p1 = Payment(method="paypal", amount=50.0, paypal_email="alice@pay.com")
    print(f"PayPal payment validated: {p1.paypal_email}")
    
    p2 = Payment(method="credit_card", amount=200.0, card_number="1234", cvv="999")
    print(f"Credit Card payment validated: {p2.card_number}")
