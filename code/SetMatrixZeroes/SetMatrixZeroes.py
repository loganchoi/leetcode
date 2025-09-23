class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        row_i = set()
        col_i = set()
        for x in range(0,row):
            for y in range(0,col):
                if  matrix[x][y] == 0:
                    row_i.add(x)
                    col_i.add(y)

        for x in range(0,row):
            for y in range(0,col):
                if x in row_i or y in col_i:
                    matrix[x][y] = 0