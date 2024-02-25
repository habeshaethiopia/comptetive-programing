class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=0
        curr=points[0][1]
        for i in points:
            if curr in range(i[0],i[1]+1):
                pass
            else:
                ans+=1
                curr=i[1]
        return ans+1 if ans else 1

            
