# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        new=list(zip(speed,efficiency))
        new.sort(key=lambda x:x[1],reverse=True)
        print(new)
        mheap=[]
        spd,res=0,0
        for s,e in new:
            if len(mheap)==k:
                spd-=heappop(mheap)
            heappush(mheap,s)
            spd+=s
            res=max(res,spd*e)
            # print(mheap)
        return res%(10**9+7)

