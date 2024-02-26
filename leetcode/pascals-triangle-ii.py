class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        pri=self.getRow(rowIndex-1)
        curr=[1]*(rowIndex+1)
        for i in range(1,rowIndex):
            curr[i]=pri[i-1]+pri[i]
        return curr
        