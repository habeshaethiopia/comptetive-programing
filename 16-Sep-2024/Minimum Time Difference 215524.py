# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s):
            hr,min=map(int,s.split(":"))
            return hr*60 + min
        timePoints.sort(key=lambda x:convert(x))
        ans=1440-abs(convert(timePoints[0])-convert(timePoints[-1]))
        for i in range(len(timePoints)-1):
            temp=abs(convert(timePoints[i])-convert(timePoints[i+1]))
            ans = min(ans,temp)
        
        return ans
