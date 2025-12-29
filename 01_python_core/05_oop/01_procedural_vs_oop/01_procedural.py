"""
面向过程编程 (Procedural Programming)

对应文档: 06-object-oriented-programming.md § 6.1.1
"""

# 面向过程：以过程（函数）为中心，将问题分解为步骤

# 全局变量存储数据
students = []

def add_student(name, score):
    """添加学生"""
    students.append({'name': name, 'score': score})
    print(f"Added student: {name}, Score: {score}")

def get_average():
    """计算平均分"""
    if not students:
        return 0
    total = sum(s['score'] for s in students)
    return total / len(students)

def print_students():
    """打印所有学生"""
    print("\n--- Student List ---")
    for student in students:
        print(f"Name: {student['name']}, Score: {student['score']}")

def main():
    """主程序流程"""
    print("--- Procedural Programming Demo ---")
    
    # 1. 添加学生
    add_student('Alice', 85)
    add_student('Bob', 92)
    add_student('Charlie', 78)
    
    # 2. 打印列表
    print_students()
    
    # 3. 计算并打印平均分
    avg = get_average()
    print(f"\nClass Average: {avg:.2f}")

if __name__ == '__main__':
    main()
