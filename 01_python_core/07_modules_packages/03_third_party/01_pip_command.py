"""
pip 命令方式

对应文档: 09-modules-and-packages.md § 9.9.1
"""

# pip 是 Python 的包管理工具，用于安装和管理第三方库

def main():
    print("--- 常用 pip 命令总结 ---")
    
    # 1. 安装包
    # pip install package_name
    
    # 2. 安装指定版本的包
    # pip install package_name==1.2.3
    
    # 3. 卸载包
    # pip uninstall package_name
    
    # 4. 列出已安装的包
    # pip list
    
    # 5. 查看包的详细信息
    # pip show package_name
    
    # 6. 国内镜像安装 (以清华为例)
    # pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple
    
    # 7. 导出依赖到文件
    # pip freeze > requirements.txt
    
    # 8. 从文件批量安装
    # pip install -r requirements.txt

if __name__ == '__main__':
    main()
