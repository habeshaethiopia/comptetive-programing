# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        arr=[]
        def back(start):
            if start>=len(s):
                return len(arr)>=2
            for i in range(start,len(s)):
                m=int(s[start:i+1])
                if arr and arr[-1]-m!=1:
                    continue
                arr.append(m)
                # print(arr)
                if back(i+1):
                    return True
                arr.pop()
        return back(0)
                    

