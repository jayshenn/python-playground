"""
命名规范

对应文档: 06-object-oriented-programming.md § 6.3.2
"""

# Python 类的命名规范遵循 PEP 8
# 1. 使用大驼峰命名法 (PascalCase / UpperCamelCase)
# 2. 每个单词的首字母大写，不使用下划线
# 3. 命名应简洁且具有描述性

class MyFirstClass:
    pass

class UserProfileManager:
    pass

# 不推荐的写法 (虽然语法正确，但不符合规范)：
# class my_class: pass
# class myclass: pass

if __name__ == '__main__':
    print("类名应使用大驼峰命名法，例如: MyFirstClass")
    print(f"规范示例: {MyFirstClass.__name__}")
    print(f"规范示例: {UserProfileManager.__name__}")
