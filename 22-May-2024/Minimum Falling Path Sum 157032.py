# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, triangle: List[List[int]]) -> int:
        
        memo={}
        def dp(i,x):
            if (i,x) in memo:
                return memo[(i,x)]
            if i >= len(triangle) :
                return 0
            if  x<0 or x>=len(triangle[i]):
                return float('inf')
            
            ans = min(triangle[i][x]+dp(i+1,x+1), triangle[i][x]+dp(i+1,x),triangle[i][x]+dp(i+1,x-1))
            memo[(i,x)]=ans
            return ans
        ret=float('inf')
        for i in range(len(triangle)):
            ret=min(ret,dp(0,i))
        return ret