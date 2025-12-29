"""
类属性 vs 实例属性

对应文档: 06-object-oriented-programming.md § 6.7.3
"""

class Game:
    top_score = 100  # 类属性

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0  # 实例属性

if __name__ == '__main__':
    p1 = Game("小明")
    
    # 1. 实例可以访问类属性
    print(f"当前最高分 (通过实例访问): {p1.top_score}")
    
    # 2. 如果通过实例修改类属性名，实际上是创建了一个同名的“实例属性”
    p1.top_score = 999  # 这不会修改 Game.top_score，而是给 p1 增加了一个 top_score 属性
    
    print(f"p1 的 top_score: {p1.top_score}")        # 999 (访问实例属性)
    print(f"Game 的 top_score: {Game.top_score}")    # 100 (类属性未变)
    
    # 3. 查找顺序：对象属性 -> 类属性
    p2 = Game("小红")
    print(f"p2 的 top_score: {p2.top_score}")        # 100 (p2 没有实例属性，向上找类属性)
