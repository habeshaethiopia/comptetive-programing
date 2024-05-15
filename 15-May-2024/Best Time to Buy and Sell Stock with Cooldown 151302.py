# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo={}
        def dp(i,c):

            if i==len(prices):
                return 0
            key=(i,c)
            if key in memo:
                return memo[key]
            if c==1:
                memo[key]=max(dp(i+1,2)-prices[i],dp(i+1,c))
                return memo[key]
            elif c==2:
                memo[key]=max(prices[i]+dp(i+1,3),dp(i+1,c))
                return memo[key] 
            else:
                memo[key]=dp(i+1,1)
                return memo[key] 
        return dp(0,1)
        
            
