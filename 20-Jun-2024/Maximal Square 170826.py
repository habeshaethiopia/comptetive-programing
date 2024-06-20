# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        pre=[0]*(m+1)
        curr=[0]*(m+1)
        mx=0
        for i in range(n):
            curr=[0]*(m+1)
            for j in range(m-1,-1,-1):
                if matrix[i][j]=='1':
                    curr[j]=min(curr[j+1],pre[j+1],pre[j])+1
                    mx=max(curr[j],mx)
            print(curr)
            pre=curr
        return mx**2
        
                