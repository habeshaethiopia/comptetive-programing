class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        
        s=0
        m=float('inf')
        ans=0

        for i in range(len(nums)):
            s+=nums[i]
            
            while s>=target:
                m=min(m,i-left+1)
                s-=nums[left]
                left+=1
            
        return 0 if m==float('inf') else m
                