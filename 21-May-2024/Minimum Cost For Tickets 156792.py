# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = {0: 1, 1: 7, 2: 30}
        # @cache
        # def dp(i, dy):
        #     if i >= len(days):
        #         return 0
        #     if days[i] <= dy:
        #         return dp(i + 1, dy)
        #     ans = float("inf")
        #     for x in range(3):
        #         ans = min(ans, dp(i + 1, dy + d[x]) + costs[x])
        #         print(ans)
        #     print(ans, (i , dy))
        #     return ans
        # return dp(0,days[0]-1)


        dp = [0]*(days[-1]+1)

        def get(i):
            if i >= len(dp):
                return 0
            return dp[i]

        curr_day = len(days)-1
        for i in range(len(dp)-1, -1, -1):
            ans = float('inf')
            if curr_day >= 0 and days[curr_day] == i:
                curr_day -= 1
                for x in range(3):
                    
                    ans = min(ans, costs[x] + get(i + d[x]))
                    # print(ans, x, costs[x])
                dp[i] = ans
            else:
                dp[i] = get(i+1)
            # print(dp)
            
            
        
        return dp[0]