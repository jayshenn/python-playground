"""
动态给类添加属性

对应文档: 06-object-oriented-programming.md § 6.9.2
"""

class Student:
    pass

if __name__ == '__main__':
    s1 = Student()
    s2 = Student()
    
    # 动态给类添加属性
    Student.school = "清华大学"
    
    # 所有实例都会获得该属性
    print(f"s1 的学校: {s1.school}")
    print(f"s2 的学校: {s2.school}")
