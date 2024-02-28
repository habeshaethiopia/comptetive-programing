class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        ans=0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]>nums[i]:
                k=ceil(nums[i-1]/nums[i])
                nums[i-1]=floor(nums[i-1]/(k))
                ans+=k-1
        return ans


