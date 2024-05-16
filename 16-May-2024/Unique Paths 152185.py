# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        # path = [(1, 0), (0, 1)]

        # def check(x, y):
        #     return x < n and y < m

        # @cache
        # def dp(x, y):
        #     # print(x,y)
        #     if x == n - 1 and y == m - 1:
        #         return 1
        #     ans = 0
        #     for i, j in [[1, 0], [0, 1]]:
        #         r, c = x + i, y + j
                
        #         if r < n and c < m:
        #             ans += dp(r, c)
        #     # print('ans',ans)
        #     return ans

        # return dp(0, 0)
        pre=[0]*n
        curr=[0]*n
        curr[0]=1
        for i in range(m):
            for j in range(1,n):
                curr[j]=curr[j-1]+pre[j]
            pre=curr
            curr=[1]+[0]*(n-1)
        return pre[-1]
