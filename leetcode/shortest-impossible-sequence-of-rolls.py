class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        num=set()
        ans=0
        for i in range(len(rolls)):
            num.add(rolls[i])
            if len(num)==k:
                num.clear()
                ans+=1
        return ans+1
            