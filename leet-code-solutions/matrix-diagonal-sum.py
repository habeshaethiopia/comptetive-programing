class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l=defaultdict(int)
        r=defaultdict(int)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                l[row+col]+=mat[row][col]
                r[row-col]+=mat[row][col]
        ret=r[0] + l[len(mat[0])-1]
        print(r,l)
        mid=floor(len(mat)/2)
        if len(mat[0])%2:
            ret=ret - mat[mid][mid]
        return ret