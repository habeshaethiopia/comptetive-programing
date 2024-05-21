# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def coin(i):
            if i<0:
                return 0
            if i==0:
                return 1
            ans=0
            for x in range(1,n):
                ans=max(ans, coin(i-x)*x)

            return ans
        return coin(n)


            

