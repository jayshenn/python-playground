"""
TypedDict 继承

对应文档: 15-type-system-stdlib.md § 15.typeddict
"""

from typing import TypedDict

class BaseResponse(TypedDict):
    status: int
    message: str

class UserResponse(BaseResponse):
    """继承 BaseResponse 并添加 data 字段"""
    data: dict[str, str | int]

class PaginatedResponse(UserResponse):
    """多层继承"""
    page: int
    total_pages: int

if __name__ == '__main__':
    # 必须包含继承自父类的所有必需键
    resp: PaginatedResponse = {
        "status": 200,
        "message": "Success",
        "data": {"id": 1, "name": "Alice"},
        "page": 1,
        "total_pages": 5
    }
    
    print(f"Response status: {resp['status']}")
    print(f"Page info: {resp['page']}/{resp['total_pages']}")
