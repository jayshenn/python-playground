"""
批量验证

对应文档: 16-type-system-pydantic.md § 16.performance
"""

from pydantic import BaseModel, TypeAdapter
import time

class Item(BaseModel):
    id: int
    name: str

if __name__ == '__main__':
    # 准备 1000 条数据
    raw_items = [{"id": i, "name": f"Item {i}"} for i in range(1000)]
    
    # 1. 批量验证方案
    # 使用 TypeAdapter 一次性验证整个列表
    adapter = TypeAdapter(list[Item])
    
    start = time.time()
    items = adapter.validate_python(raw_items)
    end = time.time()
    
    print(f"Validated {len(items)} items in {end - start:.4f}s")
    
    # 对比：如果在循环中逐个调用 Item.model_validate()，速度通常会稍慢
    # 因为批量操作能更好地利用底层的 Rust 优化。
