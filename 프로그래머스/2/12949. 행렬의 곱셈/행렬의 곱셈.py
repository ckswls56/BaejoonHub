import numpy as np

def solution(arr1, arr2):
    # NumPy 배열로 변환
    arr1_np = np.array(arr1)
    arr2_np = np.array(arr2)

    # 행렬 곱셈 수행
    result_np = np.dot(arr1_np, arr2_np)

    return result_np.tolist()
