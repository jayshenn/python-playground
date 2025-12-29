"""
参数传递

对应文档: 06-object-oriented-programming.md § 6.5.2
"""

# __init__ 方法可以接收参数，使得每个对象在创建时可以有不同的初始数据

class Student:
    def __init__(self, name, age, score):
        # 将接收到的参数绑定到 self（即当前对象实例）上
        self.name = name
        self.age = age
        self.score = score
    
    def info(self):
        print(f"学生: {self.name}, 年龄: {self.age}, 成绩: {self.score}")

if __name__ == '__main__':
    # 实例化时传入对应的参数（注意：self 不需要手动传参）
    stu1 = Student("张三", 18, 95)
    stu2 = Student("李四", 19, 88)
    
    stu1.info()
    stu2.info()
