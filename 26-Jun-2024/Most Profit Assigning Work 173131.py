# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], work: List[int]) -> int:
        p=[[difficulty[i], profit[i]] for i in range(len(profit))]
        p.sort(key=lambda x:x[0])
        maxwork=max(work)
        x=float('inf')
        for i in range(len(p)):
            if p[i][0]>maxwork:
                x=i
                break
        else:
            i=len(p)
        p=p[:i]
        work.sort()
        p.sort(key=lambda x:x[1])
        l=len(p)-1
        r=len(work)-1
        ans=0

        
        print(p,work)  
        while  l >= 0 and r >= 0:
            print(work[r],p[l][0])
            if work[r]>=p[l][0]:
                ans+=p[l][1]
                r-=1
            else:
                l-=1
        return ans