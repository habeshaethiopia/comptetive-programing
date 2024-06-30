# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = 0
        # for i in triangle:
        #     ans += min(i)
        # return ans

        # dp = [0] * len(triangle)
        # for row in triangle:
        #     for i in triangle:
        #         dp[len(row) - 1] = min()
        @cache
        def dp(i,x):
            if i >= len(triangle):
                return 0
            ans = min(triangle[i][x]+dp(i+1,x+1), triangle[i][x]+dp(i+1,x))
            return ans
        return dp(0,0)
