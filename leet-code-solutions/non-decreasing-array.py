class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0
        min = nums[-1]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count +=1
                if i>0 and nums[i-1]> nums[i+1]:
                    nums[i+1]=nums[i]
        if count > 1:
            return False
        else:
            return True
            