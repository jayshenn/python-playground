"""
特殊方法（魔法方法）

对应文档: 06-object-oriented-programming.md § 6.8.5
"""

# 特殊方法由 Python 自动调用，通常以 __ 开头和结尾

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # 控制 print(obj) 时的输出内容
    def __str__(self):
        return f"《{self.title}》- {self.author}"
    
    # 控制 len(obj) 时的返回结果
    def __len__(self):
        return self.pages
    
    # 控制对象销毁时的行为 (之前已介绍过)
    def __del__(self):
        # print(f"书籍 {self.title} 已从内存释放")
        pass

if __name__ == '__main__':
    my_book = Book("Python 进阶", "Guido", 350)
    
    # 调用 __str__
    print(my_book) 
    
    # 调用 __len__
    print(f"书的总页数: {len(my_book)}")
