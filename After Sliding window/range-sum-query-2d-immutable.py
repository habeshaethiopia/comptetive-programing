class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        self.primx=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.primx[i][j]=self.primx[i-1][j]+self.primx[i][j-1]\
                -self.primx[i-1][j-1]+self.matrix[i][j]
        

    def sumRegion(self, r1, c1, r2, c2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.primx[r2][c2]-self.primx[r2][c1-1]\
                -self.primx[r1-1][c2]+self.primx[r1-1][c1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)