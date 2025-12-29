"""NumPy 基础示例"""

import numpy as np


def main():
    print("=== NumPy 基础操作 ===\n")

    # 创建数组
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"一维数组: {arr1}")
    print(f"数组形状: {arr1.shape}")
    print(f"数组维度: {arr1.ndim}\n")

    # 创建二维数组
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"二维数组:\n{arr2}")
    print(f"数组形状: {arr2.shape}")
    print(f"数组维度: {arr2.ndim}\n")

    # 创建特殊数组
    zeros = np.zeros((3, 3))
    print(f"零矩阵:\n{zeros}\n")

    ones = np.ones((2, 4))
    print(f"全1矩阵:\n{ones}\n")

    # 数组运算
    arr = np.array([1, 2, 3, 4, 5])
    print(f"原数组: {arr}")
    print(f"数组 + 10: {arr + 10}")
    print(f"数组 * 2: {arr * 2}")
    print(f"数组平方: {arr ** 2}")
    print(f"数组均值: {arr.mean()}")
    print(f"数组总和: {arr.sum()}")


if __name__ == "__main__":
    main()
