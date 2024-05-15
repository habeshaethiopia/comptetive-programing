# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coin: List[int]) -> int:
        @cache
        def dp(n,i):
            if n==0:
                return 1
            if n<0 or i==len(coin):
                return 0
            
            t=dp(n-coin[i],i)
            l=dp(n,i+1)
            
            return l+t
                
        ans=dp(amount, 0) 
        return ans if ans!=-float('inf') else 0
            
