class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[i+j].append(mat[i][j])
        rtn=[]
        rev=True
        for i in result.values():
            if rev:
                rtn+=(i[::-1])
                rev=False
            else:
                rtn+=(i)
                rev=True
        return rtn