from typing import List
import copy
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


class Solution:
    def rotate_for_myself(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        纯找规律找的，要用额外的空间来存储
        """
        n = len(matrix)
        matrix1 = [[0 for _ in range(n)] for _ in range(n)]
        sub_x = -( n + 1 )
        sub_num = 1
        i = 0
        j = 0
        # matrix_copy = copy.deepcopy(matrix)
        for i in range(n):
            start_x = sub_x + sub_num
            start_y = sub_x - start_x
            for j in range(n):
                # matrix_copy[i + n + start_x][j + n + start_y] = matrix[i][j]
                matrix1[i + n + start_x][j + n + start_y] = matrix[i][j]
                start_x = start_x + 1
                start_y = sub_x - start_x
            sub_x -= 2
            sub_num += 1
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix1[i][j]
        # print(f"rotate matrix:")
        # print_matrix(matrix)
        # print('-----------------')
    def rotate_for_offic(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        官方的解法，用的是转置加镜像的方法
        """
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i, n):  # j从i开始 避免重复交换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 镜像 也即行逆序
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
            # matrix[i].reverse() # 列表的逆序方法
            # matrix[i] = matrix[i][::-1] # 切片方法按行逆序
if __name__ == '__main__':
    matrix1 = [[1,2],[4,5]]
    matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
    print('original matrix:')
    print_matrix(matrix2)
    i = 0
    solution = Solution()
    solution.rotate(matrix2)
    print(f"rotate matrix:")
    print_matrix(matrix2)





