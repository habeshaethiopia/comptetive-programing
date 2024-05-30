# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n=len(stones)
        myset=set(stones)
        memo={}
        def dp(p,k):
            # print(p,k)
            if (p,k) in memo:
                return memo[(p,k)]
            if p not in myset or k<=0:
                return False
            if p==stones[-1]:
                return True
            memo[(p,k)]=dp(p+k-1,k-1) or dp(p+k+1,k+1) or  dp(p+k,k)
            return memo[(p,k)]
        return dp(1,1)