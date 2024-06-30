# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter([_ for _ in s])
        t=Counter([_ for _ in t])
        for i in t:
            if s[i]!=t[i]:
                return i
        