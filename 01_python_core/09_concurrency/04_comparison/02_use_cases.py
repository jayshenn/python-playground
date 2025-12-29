"""
使用场景

对应文档: 11-concurrency.md § 11.4.2
"""

def main():
    print("--- 选型建议 ---")
    
    print("\n1. 推荐使用 [多进程] 的场景 (CPU-Bound):")
    print("   - 科学计算、数据处理")
    print("   - 视频编码/解码、图片处理")
    print("   - 复杂的算法逻辑")
    
    print("\n2. 推荐使用 [多线程] 的场景 (IO-Bound):")
    print("   - 网络爬虫、Web 服务器")
    print("   - 文件读写密集型操作")
    print("   - 数据库查询、API 调用等待")

if __name__ == '__main__':
    main()
