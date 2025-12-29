"""
复用父类方法

对应文档: 07-oop-features.md § 7.2.3
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} 正在努力工作中...")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # 使用 super() 调用父类的构造方法，复用赋值逻辑
        super().__init__(name, salary)
        self.bonus = bonus
        
    def work(self):
        # 先执行父类的 work 逻辑
        super().work()
        # 再增加子类特有的逻辑
        print(f"{self.name} 还在制定部门计划")

if __name__ == '__main__':
    m = Manager("老王", 20000, 5000)
    print(f"经理: {m.name}, 薪水: {m.salary}, 奖金: {m.bonus}")
    m.work()
