"""
最佳实践：处理异常

对应文档: 05-file-operations.md § 5.9.3
"""

def handle_file_exceptions(filename):
    print(f"\nTrying to read '{filename}'...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
            
    except FileNotFoundError:
        print("Error: File not found. Please checks the path.")
        
    except PermissionError:
        print("Error: Permission denied. Check file permissions.")
        
    except UnicodeDecodeError:
        print("Error: Encoding mismatch. Try a different encoding.")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == '__main__':
    # 1. 文件不存在
    handle_file_exceptions('non_existent.txt')
    
    # 2. 正常情况
    with open('exist.txt', 'w', encoding='utf-8') as f:
        f.write('Hello')
    handle_file_exceptions('exist.txt')
    
    # 清理
    import os
    if os.path.exists('exist.txt'):
        os.remove('exist.txt')
