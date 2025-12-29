"""
类型别名

对应文档: 14-type-system-basics.md § 14.basic
"""

# 如果一个类型很复杂，可以给它起一个别名

# 3.10 之前
# Vector = list[float]

# 3.10+ 推荐使用 TypeAlias (需从 typing 导入)
from typing import TypeAlias

# 定义别名
UserId: TypeAlias = int
Point2D: TypeAlias = tuple[float, float]

def get_distance(p1: Point2D, p2: Point2D) -> float:
    # 逻辑计算...
    return 0.0

if __name__ == '__main__':
    start: Point2D = (0.0, 0.0)
    end: Point2D = (3.0, 4.0)
    print(f"Distance: {get_distance(start, end)}")
