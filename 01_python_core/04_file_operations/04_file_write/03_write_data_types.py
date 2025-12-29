"""
写入不同类型的数据

对应文档: 05-file-operations.md § 5.5.3
"""

import os
import json

def write_string():
    """写入字符串"""
    print("\n--- Write String ---")
    filename = 'test_str.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Just a simple string.')
    
    print(f"Written string to {filename}")
    os.remove(filename)

def write_numbers():
    """写入数字"""
    print("\n--- Write Numbers ---")
    filename = 'test_num.txt'
    numbers = [1, 2, 3, 4, 5]
    
    with open(filename, 'w', encoding='utf-8') as f:
        # 必须先转换为字符串
        # f.write(123) # TypeError: write() argument must be str, not int
        f.write(','.join(map(str, numbers)))
        f.write('\n')
        
        # 逐个写入
        for num in numbers:
            f.write(f"{num} ")
    
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"Content: {f.read().strip()}")
    
    os.remove(filename)

def write_json():
    """写入 JSON 数据"""
    print("\n--- Write JSON ---")
    filename = 'test.json'
    data = {
        'name': 'Python',
        'age': 30,
        'features': ['Simple', 'Powerful']
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    with open(filename, 'r', encoding='utf-8') as f:
        print("JSON Content:")
        print(f.read())
    
    os.remove(filename)

def write_binary():
    """写入二进制数据"""
    print("\n--- Write Binary ---")
    filename = 'test.bin'
    # bytes 对象
    data = bytes([0, 10, 255, 65, 66]) # 0x00, 0x0A, 0xFF, 'A', 'B'
    
    with open(filename, 'wb') as f:
        f.write(data)
    
    with open(filename, 'rb') as f:
        print(f"Binary Content: {f.read()}")
    
    os.remove(filename)

if __name__ == '__main__':
    write_string()
    write_numbers()
    write_json()
    write_binary()
