"""
最佳实践：始终使用 with 语句

对应文档: 05-file-operations.md § 5.9.1
"""

import os

FILENAME = 'practice_with.txt'

def bad_practice():
    """反例：不使用 with 语句"""
    print("\n--- Bad Practice ---")
    
    try:
        f = open(FILENAME, 'w', encoding='utf-8')
        f.write('Some content')
        # 如果这里发生异常，close() 可能不会被执行
        # f.close()  <-- 容易忘记
        print("File opened without 'with'. Closed? ", f.closed)
        f.close()
        print("File closed manually. Closed? ", f.closed)
    except Exception as e:
        print(f"Error: {e}")

def good_practice():
    """正例：使用 with 语句"""
    print("\n--- Good Practice ---")
    
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write('Better content')
        print("Inside 'with'. Closed? ", f.closed)
    
    # 离开代码块自动关闭
    print("Outside 'with'. Closed? ", f.closed)

if __name__ == '__main__':
    bad_practice()
    good_practice()
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
