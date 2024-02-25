class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        i=0
        n=len(tickets)
        while tickets[k]:
            if tickets[i%n]>0:
                tickets[i%n]-=1
                ans+=1
            i+=1
        return ans

