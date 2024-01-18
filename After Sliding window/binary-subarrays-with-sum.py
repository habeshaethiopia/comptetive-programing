class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pri=defaultdict(int)
        pri[0]=1
        c=0
        x=0
        for i in nums:
            x+=i
            if x-goal in pri:
                c+=pri[x-goal]
            pri[x]+=1
        return c
        