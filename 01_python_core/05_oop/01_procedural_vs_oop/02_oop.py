"""
面向对象编程 (Object Oriented Programming)

对应文档: 06-object-oriented-programming.md § 6.1.2
"""

# 面向对象：以对象为中心，数据和操作封装在一起

class Student:
    """学生类：封装学生的数据和行为"""
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def get_grade(self):
        """获取等级（行为）"""
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'F'
            
    def __str__(self):
        return f"{self.name}: {self.score} (Grade: {self.get_grade()})"

class StudentManager:
    """学生管理类：管理学生集合"""
    
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        """添加学生对象"""
        self.students.append(student)
        print(f"Added: {student.name}")
        
    def get_average(self):
        """计算平均分"""
        if not self.students:
            return 0
        total = sum(s.score for s in self.students)
        return total / len(self.students)
        
    def print_students(self):
        """打印所有学生"""
        print("\n--- Student List (OOP) ---")
        for student in self.students:
            print(student) # 自动调用 __str__

def main():
    print("--- Object Oriented Programming Demo ---")
    
    # 1. 创建管理对象
    manager = StudentManager()
    
    # 2. 创建并添加学生对象
    s1 = Student('Alice', 85)
    s2 = Student('Bob', 92)
    s3 = Student('Charlie', 78)
    
    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)
    
    # 3. 操作对象
    manager.print_students()
    
    print(f"\nClass Average: {manager.get_average():.2f}")

if __name__ == '__main__':
    main()
