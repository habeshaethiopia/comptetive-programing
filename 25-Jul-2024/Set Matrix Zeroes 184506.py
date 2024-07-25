# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        zerocol=set()
        zerorow=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zerocol.add(j)
                    zerorow.add(i)
        for i in range(n):
            for j in range(m):
                if i in  zerorow or j in zerocol:
                    matrix[i][j]=0
                