"""
求列表中某个元素的最大值、最小值、加和

对应文档: 03-data-structures.md § 3.2.9
"""

# 找出列表中所有偶数的最大值、最小值和总和
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# 过滤出偶数
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# 偶数的最大值、最小值、求和
print(f"Max even: {max(evens)}")
print(f"Min even: {min(evens)}")
print(f"Sum of evens: {sum(evens)}")

# 学生成绩统计
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 最高分学生
top_student = max(students, key=lambda s: s["score"])
print(f"Top student: {top_student['name']} - {top_student['score']}")

# 最低分
min_score = min(students, key=lambda s: s["score"])["score"]
print(f"Min score: {min_score}")

# 平均分
avg_score = sum(s["score"] for s in students) / len(students)
print(f"Average score: {avg_score:.2f}")
