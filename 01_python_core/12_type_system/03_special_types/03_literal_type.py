"""
Literal 类型：字面值限定

对应文档: 14-type-system-basics.md § 14.special
"""

from typing import Literal

# 1. 字符串字面值限定
type LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    """只能接受预定义的四个级别字符串"""
    print(f"Log level set to {level}")

# 2. 数字字面值限定
def get_http_status_message(code: Literal[200, 404, 500]) -> str:
    """模拟 HTTP 状态码映射"""
    status_map = {
        200: "OK",
        404: "Not Found",
        500: "Internal Server Error"
    }
    return status_map.get(code, "Unknown")

# 3. 布尔字面值限定
def delete_database(confirm: Literal[True]) -> None:
    """强制要求传入 True，确保调用者明确风险"""
    print("Database deleted!")

if __name__ == '__main__':
    # 合法调用
    set_log_level("INFO")
    
    print(f"200 -> {get_http_status_message(200)}")
    
    delete_database(True)
    
    # 以下调用虽然运行时可能成功（Python 不强制检查），但类型检查器会报错：
    # set_log_level("TRACE")
    # get_http_status_message(403)
    # delete_database(False)
