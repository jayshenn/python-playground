"""
导出为字典和 JSON

对应文档: 16-type-system-pydantic.md § 16.serialization
"""

from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    name: str
    start_time: datetime
    tags: list[str]

if __name__ == '__main__':
    event = Event(
        name="Tech Conference",
        start_time=datetime(2025, 5, 20, 9, 30),
        tags=["python", "ai"]
    )
    
    # 1. 导出为 Python 字典 (保持 datetime 对象)
    data_dict = event.model_dump()
    print(f"Dict type of start_time: {type(data_dict['start_time'])}")
    
    # 2. 导出为 JSON 字符串 (自动将 datetime 转为 ISO 格式字符串)
    json_str = event.model_dump_json()
    print(f"JSON string: {json_str}")
    
    # 3. 格式化 JSON 输出
    json_pretty = event.model_dump_json(indent=2)
    print(f"Pretty JSON:\n{json_pretty}")
