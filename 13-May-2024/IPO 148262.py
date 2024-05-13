# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hea=[]
        heapify(hea)
        new=list(zip(profits,capital))
        new.sort(key=lambda x:x[1])
        last=0
        for i in range(k):
            while last< len(new) and w>=new[last][1]:
                heappush(hea, -new[last][0])
                last+=1
            if hea:
                w+=-heappop(hea)
        return w
