# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mx=0
        mn=float('inf')
        for a in arrays :
            if mn>a[0] and mx<a[-1]:
                if  mn-a[0] > a[-1]-mx:

                    mn=min(mn,a[0])
                else:
                    mx=max(mx,a[-1])
                continue
            mx=max(mx,a[-1])
            mn=min(mn,a[0])
        arr=[]
        for i in  range(len(arrays)):
            arr.append((i,arrays[i][0]))
            if len(arrays[i])>1:
                arr.append((i,arrays[i][-1]))
        arr.sort(key=lambda x:x[1])
        print(arr[0][1], arr[-1][1])
        if arr[0][0]== arr[-1][0]:
            return max(abs(-arr[0][1]+arr[-2][1]), abs(arr[1][1]-arr[-1][1]))
        else:
            return abs(-arr[0][1]+ arr[-1][1])

       