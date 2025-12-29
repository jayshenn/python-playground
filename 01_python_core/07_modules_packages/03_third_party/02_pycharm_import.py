"""
PyCharm 中导入

对应文档: 09-modules-and-packages.md § 9.9.2
"""

# 在 PyCharm 等现代 IDE 中，通常有更直观的方式管理库

def main():
    print("--- PyCharm 第三方库管理步骤 ---")
    print("1. 打开 Settings (macOS: Preferences)")
    print("2. 找到 Project: <你的项目名> -> Python Interpreter")
    print("3. 点击 '+' 号按钮搜索并安装库")
    print("4. 或者将鼠标悬停在未安装的 import 语句上，选择 'Install package'")
    
    print("\n提示：建议在虚拟环境 (venv) 中进行包安装，以保持全局 Python 环境的整洁。")

if __name__ == '__main__':
    main()
