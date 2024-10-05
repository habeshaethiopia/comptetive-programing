# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(x):
            ans=0
            for i in str(x):
                ans+=int(i)

            return ans
        x=""
        for i in s:
            x+=str(ord(i)-ord('a')+1)
        for i in range(k):
            x=transform(int(x))
        return x