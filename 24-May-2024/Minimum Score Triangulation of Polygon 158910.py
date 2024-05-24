# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo={}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            ans=float('inf')
            for k in range(i+1,j):
                ans=min(ans,values[i]*values[j]*values[k]+dp(i,k)+dp(k,j))
            if ans==float('inf'):
                return 0
            memo[(i,j)]=ans
            return ans
        return dp(0,len(values)-1)


