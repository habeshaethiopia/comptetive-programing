# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m=time//(n-1)
        if m%2:
            return n-time%(n-1)
        else:
           return  time%(n-1)+1