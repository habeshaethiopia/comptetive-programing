# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i,con):
            if i==len(prices):
                return 0

            if con==1:
                return max(dp(i+1,2)-prices[i]-fee,dp(i+1,1))
            else:
                return max(prices[i]+dp(i+1,1),dp(i+1,2))
        return dp(0,1)