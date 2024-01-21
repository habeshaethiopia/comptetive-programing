class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[(abs(x[0]**2)+abs(x[1]**2), i) for i,x in enumerate(points)]
        distance.sort()
        ans=[]
        print(distance)
        for i in range(k):
            ans.append(points[distance[i][1]])
        return ans