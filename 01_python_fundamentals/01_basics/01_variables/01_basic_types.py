"""Python 基本数据类型示例"""


def main():
    # 整数 (int)
    age = 25
    print(f"年龄: {age}, 类型: {type(age)}")

    # 浮点数 (float)
    height = 1.75
    print(f"身高: {height}, 类型: {type(height)}")

    # 字符串 (str)
    name = "张三"
    print(f"姓名: {name}, 类型: {type(name)}")

    # 布尔值 (bool)
    is_student = True
    print(f"是学生: {is_student}, 类型: {type(is_student)}")

    # 列表 (list)
    fruits = ["苹果", "香蕉", "橙子"]
    print(f"水果列表: {fruits}, 类型: {type(fruits)}")

    # 元组 (tuple)
    coordinates = (10, 20)
    print(f"坐标: {coordinates}, 类型: {type(coordinates)}")

    # 字典 (dict)
    person = {"name": "李四", "age": 30, "city": "北京"}
    print(f"人员信息: {person}, 类型: {type(person)}")

    # 集合 (set)
    numbers = {1, 2, 3, 4, 5}
    print(f"数字集合: {numbers}, 类型: {type(numbers)}")


if __name__ == "__main__":
    main()
