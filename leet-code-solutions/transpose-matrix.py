class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(len(matrix[0])):
            tmp=[]
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            result.append(tmp)
        return result

