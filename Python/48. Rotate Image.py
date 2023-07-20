class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        t = 0
        b = len(matrix) - 1

        while t < b:
            matrix[t], matrix[b] = matrix[b], matrix[t]
            t += 1
            b -= 1

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
