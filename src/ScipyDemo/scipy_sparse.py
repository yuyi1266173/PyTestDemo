# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2023-7-5
# update date: 2023-7-5
# function: demo for study scipy.sparse


import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import connected_components


def demo_csr_matrix():
    # CSC - 压缩稀疏列（Compressed Sparse Column），按列压缩。
    # CSR - 压缩稀疏行（Compressed Sparse Row），按行压缩。
    arr_0 = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
    print(csr_matrix(arr_0))

    arr_1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
    mat = csr_matrix(arr_1)
    # 使用 data 属性查看存储的数据（不含 0 元素）
    print(mat.data)
    # 使用 count_nonzero() 方法计算非 0 元素的总数
    print(mat.count_nonzero())
    print(mat)

    # mat.eliminate_zeros()
    # print(mat)
    #
    # mat.sum_duplicates()
    # print(mat)

    print(csr_matrix(arr_1).tocsc())


def demo_connected_components():
    arr = np.array([
        [0, 1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])

    new_arr = csr_matrix(arr)
    print(connected_components(new_arr))


def demo_dijkstra():
    arr = np.array([
        [0, 1, 2],
        [1, 0, 0],
        [2, 0, 0]
    ])
    new_arr = csr_matrix(arr)
    print(dijkstra(new_arr, return_predecessors=True, indices=0))


if __name__ == "__main__":
    # demo_csr_matrix()
    # demo_connected_components()
    demo_dijkstra()
