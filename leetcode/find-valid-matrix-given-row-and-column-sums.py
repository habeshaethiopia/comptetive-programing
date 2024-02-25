class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mtx=[[0]*len(colSum) for _ in rowSum]
        print(mtx)
        n=len(mtx)
        m=len(mtx[0])
        for i in range(len(mtx)):
            for j in range(len(mtx[0])):
                x=min(rowSum[i], colSum[j])
                mtx[i][j]=x
                rowSum[i]-=x
                colSum[j]-=x
        return mtx
