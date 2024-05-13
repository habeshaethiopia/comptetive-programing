# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        @cache
        def dp(c):
            if c==0:
                return 0
            if c<0:
                return float('inf')
            ans=float('inf')
            for i in range(len(coins)):
                take=dp(c-coins[i])+1
                ans=min(ans, take)
            return ans 
        ret=dp(amount)
        return  ret if ret!=float('inf') else -1
            
        
