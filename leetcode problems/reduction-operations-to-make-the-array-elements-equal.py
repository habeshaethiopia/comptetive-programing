class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        ans=0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c+=1
            ans+=c
        return ans
    