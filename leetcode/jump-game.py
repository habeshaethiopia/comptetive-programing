class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=nums[0]
        jump=0
        n=len(nums)
        for i in range(n):
            if i > jump:
                return False
            jump=max(jump,i+nums[i])
            if jump>=n-1:
                return True
        return True